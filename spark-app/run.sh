#!/bin/bash -xe

spark-submit --master local \
    --packages "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1" \
    /app/main.py

exit 0
