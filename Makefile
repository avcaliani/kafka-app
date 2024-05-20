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

init-env:
	docker-compose down
	docker-compose up -d

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

.PHONY: services init-env email-service fraud-service log-service order-service user-service
