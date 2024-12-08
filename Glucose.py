def glucose(quantity: float):
    if 4.1 <= quantity <= 6.0:
        print("Глюкоза в норме")
    elif quantity > 6.0:
        print("Глюкоза повышена!")
    elif quantity < 4.1:
        print("Глюкоза понижена!")
try:
    glucose(float(input("Введите ваш уровень глюкозы: ")))
except ValueError:
    print("Неверный ввод!")