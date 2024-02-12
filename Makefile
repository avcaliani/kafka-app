.DEFAULT_GOAL := services

services:
	@echo "⭐ Choose a project to exectute..."
	@echo "  » email-service 📧"
	@echo "  » fraud-service 🕵️‍♂️"
	@echo "  » log-service 📖"
	@echo "  » order-service 📦"
	@echo ""
	@echo "⏰ $(shell date)"

init-env:
	docker-compose up -d

email-service: init-env
	python -m email_service.main

fraud-service: init-env
	python -m fraud_service.main

log-service: init-env
	python -m log_service.main

order-service: init-env
	python -m order_service.main

.PHONY: services init-env email-service fraud-service log-service order-service
