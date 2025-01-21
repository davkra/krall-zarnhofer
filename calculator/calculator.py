import sys
import json


def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2


def hello():
    return "Hello world!"


def hello_world():
    return "Hello, World!"


def main():
    print(hello())


if __name__ == "__main__":
    data = json.loads(sys.stdin.read())
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    operation = data["operation"]
    result = calculate(num1, num2, operation)
    print(json.dumps({"result": result}))
