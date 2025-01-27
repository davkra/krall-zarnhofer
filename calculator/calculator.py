import sys
import json


def hello():
    return "Hello world!"


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def calculate(num1, num2, operation):
    if operation == "add":
        return addition(num1, num2)
    elif operation == "subtract":
        return subtraction(num1, num2)


def main():
    print(hello())


if __name__ == "__main__":
    try:
        data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        data = None

    if not data:
        main()
    else:
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        operation = data["operation"]
        result = calculate(num1, num2, operation)
        print(json.dumps({"result": result}))
