# 📦 Order Service

## How to Run ther API?

```bash
# Dev Mode 🍻
fastapi dev order_service/main.py

# Production Mode 🚀
fastapi run order_service/main.py
```

### Payload Example

```json
// URL: http://localhost:8000/order"
{
  "customer_email": "anthony@github.com",
  "items": [
    { "item_id": "xyz", "amount":  1, "price": 10.99 },
    { "item_id": "xpto", "amount":  2,  "price": 5.99 }
  ]
}   
```
