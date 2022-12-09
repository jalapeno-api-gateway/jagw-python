JAGW_PROTO_DIR ?= $(JAGW_DIR)/proto
JAGW_PYTHON_PB2_DIR = ./

.PHONY: help

help:
	@echo "Env Variables:"
	@echo "	JAGW_DIR: $(JAGW_DIR)"
	@echo "	JAGW_PROTO_DIR: $(JAGW_PROTO_DIR)"	
	@echo ""
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  	help: Show this help"
	@echo "  	proto-gen: Generate proto files"

proto-gen:
	mkdir -p $(JAGW_PYTHON_PB2_DIR)/core && touch $(JAGW_PYTHON_PB2_DIR)/core/__init__.py
	mkdir -p $(JAGW_PYTHON_PB2_DIR)/requestservice && touch $(JAGW_PYTHON_PB2_DIR)/requestservice/__init__.py
	mkdir -p $(JAGW_PYTHON_PB2_DIR)/subscriptionservice && touch $(JAGW_PYTHON_PB2_DIR)/subscriptionservice/__init__.py
	python3 -m grpc_tools.protoc --proto_path=$(JAGW_PROTO_DIR) \
	--python_out=$(JAGW_PYTHON_PB2_DIR) \
	--pyi_out=$(JAGW_PYTHON_PB2_DIR) \
	--grpc_python_out=${JAGW_PYTHON_PB2_DIR} \
	$(JAGW_PROTO_DIR)/**/*.proto