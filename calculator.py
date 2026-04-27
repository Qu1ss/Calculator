# calculator.py

def add(a, b):
    """Сложение двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b


def multiply(a, b):
    """Умножение двух чисел."""
    return a * b


def divide(a, b):
    """Деление двух чисел."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


if __name__ == "__main__":
    print("Калькулятор")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"3 * 5 = {multiply(3, 5)}")
print(f"15 / 3 = {divide(15, 3)}")