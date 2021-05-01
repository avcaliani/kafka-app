from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_timestamp, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
# https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html


def spark_session() -> SparkSession:
    return SparkSession \
        .builder \
        .appName('spark-app') \
        .getOrCreate()


def sales_schema():
    return StructType([
        StructField('user', StringType()),
        StructField('product', StructType([
            StructField('name', StringType()),
            StructField('price', DoubleType()),
        ])),
        StructField('quantity', IntegerType()),
        StructField('total', DoubleType()),
        StructField('created_at', StringType()),
    ])


#docker-compose exec spark-app /app/run.sh
# add props in dockerfile
if __name__ == '__main__':
    spark = spark_session()
    print(f'Spark Version: {spark.version}')
    try:
        df = spark.readStream \
            .format('kafka') \
            .option('kafka.bootstrap.servers', 'kafka:29092') \
            .option('subscribe', 'sales-topic') \
            .option('maxOffsetsPerTrigger', 20) \
            .load()

        # Parsing JSON message
        df = df.withColumn('data', from_json(col('value').cast('string'), sales_schema())).select('data.*')

        # Processing
        users = spark.read.option('header', True).csv('/datalake/trusted/users')
        df = df.filter(col('user') != '#fake_user') \
            .withColumn('created_at', to_timestamp(col('created_at'), 'yyyy-MM-dd HH:mm:SS')) \
            .withColumn('processed_at', current_timestamp()) \
            .join(users, 'user', 'left')

        df.printSchema()
        df.writeStream \
            .format('console') \
            .option('truncate', False) \
            .option('checkpointLocation', '/datalake/checkpoint/spark-app/sales-topic') \
            .trigger(processingTime='5 seconds') \
            .start()
            
        spark.streams.awaitAnyTermination()
    except Exception as ex:
        print(f'Unexpected Error! {ex}')
    finally:
        spark.stop()