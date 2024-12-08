def converter(value, from_unit, to_unit):
    conversion_factors = {
        ('мг', 'г'): 0.001,
        ('г', 'мг'): 1000,
        ('мл', 'л'): 0.001,
        ('л', 'мл'): 1000
    }
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if (from_unit, to_unit) in conversion_factors:
        factor = conversion_factors[(from_unit, to_unit)]
        print(f"Перевод: {value * factor}")
    else:
        print(f"Ошибка: Не умею конвертировать из '{from_unit}' в '{to_unit}'.")
print(f'Конвертер единиц измерения дозировки лекарственных средств. Я умею переводить мг в г, мл в л и наоборот')
value = float(input("Количество:"))
from_unit = input("Из единицы:")
to_unit = input("В единицы:")
converter(value, from_unit, to_unit)