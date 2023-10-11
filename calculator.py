 class Calculator: #Calculator


@statucmethod
def add(x, y):  
    return x + y
    
@statucmethod  
def subtract(x, y):
    return x - y

@statucmethod   
def multiply(x, y):
    return x * y

@statucmethod
def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다."
    return x / y

def main():
    x = float(input("첫 번째 숫자를 입력하세요: "))
    y = float(input("두 번째 숫자를 입력하세요: "))
    operation = input("연산을 선택하세요 (+, -, *, /): ")

    if operation == "+":
        print(f"{x} + {y} = {add(x, y)}")
    elif operation == "-":
        print(f"{x} - {y} = {subtract(x, y)}")
    elif operation == "*":
        print(f"{x} * {y} = {multiply(x, y)}")
    elif operation == "/":
        print(f"{x} / {y} = {divide(x, y)}")
    else:
        print("올바른 연산자를 선택하세요.")

if __name__ == "__main__":
    main()
