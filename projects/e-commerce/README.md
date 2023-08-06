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
python projects/e-commerce/fraud_detector_service.py
python projects/e-commerce/email_service.py
python projects/e-commerce/log_service.py
```

Now, keep your eyes on application console because everything will be logged 😉

## Related Links

- [Kafka Python - Docs](https://kafka-python.readthedocs.io/en/master/index.html)
- [Medium - Kafka-Python explained in 10 lines of code](https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1)
