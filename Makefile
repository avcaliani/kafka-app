.DEFAULT_GOAL := services

services:
	@echo "⭐ Choose a project to exectute..."
	@echo "  » email-service 📧"
	@echo "  » fraud-service 🕵️‍♂️"
	@echo "  » log-service 📖"
	@echo "  » order-service 📦"
	@echo "  » user-service ☃️"
	@echo ""
	@echo "⏰ $(shell date)"

# 👇 This command is used to wait kafka to be up and running.
delayed-start:
	sleep 30

email-service:
	python -m email_service.main

fraud-service:
	python -m fraud_service.main

log-service:
	python -m log_service.main

order-service:
	uvicorn order_service.main:app --host 0.0.0.0 --port 8000

user-service:
	python -m user_service.main

.PHONY: services delayed-start email-service fraud-service log-service order-service user-service
