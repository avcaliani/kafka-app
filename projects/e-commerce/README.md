# 🛒 e-commerce

![#](https://img.shields.io/badge/python-3.10.x-yellow.svg)

## Quick Start

To start coding, create your own virtual environment.

```bash
cd projects/e-commerce \
    && python3 -m venv .venv \
    && source .venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && cd -
```

Here it is our producer.

```bash
python projects/e-commerce/new_order_service.py
```

In another terminal we can execute the consumers.
> 💡 Don't forget to activate python venv before running ;)

```bash
# Log Service
python projects/e-commerce/consumer_service.py \
    -n "📚 log service" \
    -g "log-service" \
    -p "ECOMMERCE*"

# Fraud Detector Service
python projects/e-commerce/consumer_service.py \
    -n "🕵️ fraud detector service" \
    -g "fraud-detector-service" \
    -t "ECOMMERCE_NEW_ORDER"

# e-Mail Service
python projects/e-commerce/consumer_service.py \
    -n "📧 e-mail service" \
    -g "email-service" \
    -t "ECOMMERCE_NEW_EMAIL"
```

Now, keep your eyes on application console because everything will be logged 😉

## Related Links

- [Kafka Python - Docs](https://kafka-python.readthedocs.io/en/master/index.html)
- [Medium - Kafka-Python explained in 10 lines of code](https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1)
