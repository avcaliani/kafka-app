from functools import reduce

from fastapi import FastAPI, status
from kafka_core.producer import get_instance, show_sent_message
from order_service.models import Order

app = FastAPI()
kafka = get_instance()


def _calc_total(order: Order) -> Order:
    total = reduce(
        lambda x, y: x + y,
        map(lambda item: item.get("price") * item.get("amount"), order.items),
    )
    order.total = total
    return order


def _get_email_msg(order: Order) -> dict:
    return {
        "customer_email": order.customer_email,
        "email_template": "template__new_order",
    }


@app.post("/order", status_code=status.HTTP_201_CREATED)
async def new_order(order: Order):
    customer_email = bytes(order.customer_email, "utf-8")
    updated_order = _calc_total(order)
    show_sent_message(
        kafka.send(
            topic="ECOMMERCE_NEW_ORDER",
            key=customer_email,
            value=updated_order.model_dump(mode="json"),
        )
    )
    show_sent_message(
        kafka.send(
            topic="ECOMMERCE_NEW_EMAIL",
            key=customer_email,
            value=_get_email_msg(updated_order),
        )
    )
    return updated_order
