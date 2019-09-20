PROJECT_NAME ?= nk
.PHONY: game run-game run start
game run-game run start:
	@echo
	cd $(PROJECT_NAME) && make run
	@echo
	@echo "- DONE: $@"
