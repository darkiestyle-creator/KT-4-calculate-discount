print(
    f"""Добро пожаловать!
Уже скоро наступает ЧЁРНАЯ ПЯТНИЦА!
Готовы принимать приятные скидки?)
"""
)

def good_price():
  while True:
    price_input = input("Введите цену: ")

    if not price_input.isdigit():
      print("Ошибка: нужно ввести только цифры")
      continue

    return int(price_input)

price = good_price()

while price <= 0:
  print("Цена должна быть больше нуля. Попробуйте еще раз")
  price = good_price()

def calculate(price, system):
  if system == "fix":
    if price > 10000:
      return price - 2000
    else:
      return price
  elif system == "procent":
    return price * 0.85

  elif system == "student":
    discount = price * 0.25
    if discount > 4000:
      discount = 4000
    return price - discount
  else:
    return price

print(
    f"""
Результаты для цены {price} рублей:
- Фиксированная: {calculate(price, "fix")}
- Процентная: {calculate(price, "procent")}
- Студенческая: {calculate(price, "student")}
"""
)