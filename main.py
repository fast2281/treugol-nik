def определить_тип_по_сторонам(a, b, c):
    if a == b == c:
        return "Равносторонний треугольник"
    elif a == b or b == c or a == c:
        return "Равнобедренный треугольник"
    else:
        return "Разносторонний треугольник"

def определить_тип_по_углам(a, b, c):
    стороны = sorted([a, b, c])  # Сортируем: a ≤ b ≤ c
    a, b, c = стороны[0], стороны[1], стороны[2]

    a2_b2 = a**2 + b**2
    c2 = c**2

    if abs(a2_b2 - c2) < 1e-6:
        return "Прямоугольный треугольник"
    elif a2_b2 > c2:
        return "Остроугольный треугольник"
    else:
        return "Тупоугольный треугольник"

def ввести_сторону(название):
    значение = input(f"Введите сторону {название}: ")
    try:
        число = float(значение)
        if число <= 0:
            print(f"Ошибка: сторона {название} должна быть положительным числом.")
            return None
        return число
    except ValueError:
        print(f"Ошибка: сторона {название} должна быть числом.")
        return None

def треугольник_калькулятор():
    print("Определение типа треугольника по длинам сторон.")

    a = ввести_сторону('a')
    if a is None: return

    b = ввести_сторону('b')
    if b is None: return

    c = ввести_сторону('c')
    if c is None: return

    if a + b <= c or a + c <= b or b + c <= a:
        print("Ошибка: треугольник с такими сторонами не существует.")
        return

    тип_сторон = определить_тип_по_сторонам(a, b, c)
    тип_углов = определить_тип_по_углам(a, b, c)

    print(f"Результат: {тип_сторон}, {тип_углов}")

# Запуск
треугольник_калькулятор()
