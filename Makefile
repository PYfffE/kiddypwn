BYPASS_SECUTIRY_FLAGS=-fno-stack-protector -z execstack -D_FORTIFY_SOURCE=0 -Wno-implicit-function-declaration
BUILD_DIR=./build/
SRC_DIR=./src

default:
	mkdir -p ./build/
	gcc $(BYPASS_SECUTIRY_FLAGS) -o ./build/vuln $(SRC_DIR)/main.c
