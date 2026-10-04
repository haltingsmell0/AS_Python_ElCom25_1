TEXT2NUM = {
    "ноль": 0,
    "один": 1,
    "одна": 1,
    "два": 2,
    "две": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
    "сто": 100,
    "двести": 200,
    "триста": 300,
    "четыреста": 400,
    "пятьсот": 500,
    "шестьсот": 600,
    "семьсот": 700,
    "восемьсот": 800,
    "девятьсот": 900,
}

NUM2TEXT = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
    40: "сорок",
    50: "пятьдесят",
    60: "шестьдесят",
    70: "семьдесят",
    80: "восемьдесят",
    90: "девяносто",
    100: "сто",
    200: "двести",
    300: "триста",
    400: "четыреста",
    500: "пятьсот",
    600: "шестьсот",
    700: "семьсот",
    800: "восемьсот",
    900: "девятьсот",
}

NUM2TEXT_R = NUM2TEXT.copy()
NUM2TEXT_K = NUM2TEXT.copy()
NUM2TEXT_K.update({1: "одна", 2: "две"})

THOUSAND_FORMS = ("тысяча", "тысячи", "тысяч")
RUBLE_FORMS = ["рубль", "рубля", "рублей"]
KOPEK_FORMS = ["копейка", "копейки", "копеек"]

def tokenize(text: str) -> list[str]:
    return text.lower().split()

def separation(tokens: list[str]) -> list[list[str] | str]:
    parts = [[]]
    for token in tokens:
        if token in ("плюс", "минус"):
            parts.extend([token, []])
        else:
            parts[-1].append(token)
    if len(parts) == 1:
        raise ValueError("Введите хотя бы одну опреацию: «плюс» или «минус»")
    if not parts[-1]:
        raise ValueError("Выражение имеет опертор на конце без суммы")
    return parts

def subwords_to_number(words: list[str]) -> int:
    number = 0
    for word in words:
        if word not in TEXT2NUM:
            raise ValueError(f"Неизвестное слово: {word}")
        number += TEXT2NUM[word]
    return number

def words_to_number(words: list[str]) -> int:
    if not words:
        raise ValueError("Не указано число")

    thousand_index = next((i for i, word in enumerate(words) if word in THOUSAND_FORMS), None)
    if thousand_index is None:
        return  subwords_to_number(words)
    return (
        (subwords_to_number(words[:thousand_index]) if words[:thousand_index] else 1) * 1000 
        + subwords_to_number(words[thousand_index + 1:])
    )

def parse_money(money: list[str]) -> int:
    ruble_indexes = [i for i, word in enumerate(money) if word in RUBLE_FORMS]
    kopek_indexes = [i for i, word in enumerate(money) if word in KOPEK_FORMS]
    if len(ruble_indexes) > 1 or len(kopek_indexes) > 1:
        raise ValueError("В сумме повторяется название денежной единицы")

    r_index = ruble_indexes[0] if ruble_indexes else None
    k_index = kopek_indexes[0] if kopek_indexes else None
    if r_index is None and k_index is None:
        raise ValueError("Укажи рубли или копейки")
    if r_index is not None and k_index is not None and r_index > k_index:
        raise ValueError("Сначала укажи рубли, затем копейки")

    last_unit_index = k_index if k_index is not None else r_index
    if last_unit_index != len(money) - 1:
        raise ValueError("После суммы остались лишние слова")

    rubles, kopeks = 0, 0
    if r_index is not None:
        rubles = words_to_number(money[:r_index])
        if rubles > 999999:
            raise ValueError("Сумма должна быть до миллиона")
    if k_index is not None:
        kopeks_start = r_index + 1 if r_index is not None else 0
        kopeks = words_to_number(money[kopeks_start:k_index])
        if kopeks > 99:
            raise ValueError("Копейки должны быть от 0 до 99")
    return rubles*100 + kopeks

def parse_expression(parts: list[list[str] | str], total: int | None = None) -> int:
    if not parts:
        if total is None:
            raise ValueError("Пустое выражение")
        return total
    if total is None:
        total = parse_money(parts[0])
        parts = parts[1:]
    if not parts:
        return(total)

    if parts[0] == "минус":
        total -= parse_money(parts[1])
    elif parts[0] == "плюс":
        total += parse_money(parts[1])
    else:
        raise ValueError("Неизвестная операция")
    return parse_expression(parts[2:], total)



def number_to_words(number: int, d: dict) -> str:
    digits = []
    digits.append(number // 100 * 100)
    words = []
    if number % 100 > 20:
        digits.append(number % 100 // 10 * 10)
        digits.append(number % 10)
    else:
        digits.append(number % 100)
    for dig in digits:
        if dig:
            words.append(d[dig])
    if not words:
        return "ноль"
    return " ".join(words)

def ending(number: int, lst: list) -> str:
    n_end = number % 100
    if n_end > 20:
        n_end %= 10
    if n_end == 1:
        return lst[0]
    elif n_end in [2,3,4]:
        return lst[1]
    else:
        return lst[2]

def money_to_words(total: int) -> str:
    r_num = total // 100
    thousands = r_num // 1000
    remains = r_num % 1000
    parts = []
    if thousands:
        parts.append(number_to_words(thousands, NUM2TEXT_K))
        parts.append(ending(thousands, THOUSAND_FORMS))
    if remains:
        parts.append(number_to_words(remains, NUM2TEXT_R))
    parts.append(ending(remains, RUBLE_FORMS))
    r_text = " ".join(parts)
    k_num = total % 100
    k_text = number_to_words(k_num, NUM2TEXT_K) + " " + ending(k_num, KOPEK_FORMS)
    if r_num == 0:
        if k_num == 0:
            return "ноль рублей"
        return k_text
    if k_num == 0:
        return r_text
    return r_text + " " + k_text

def calc(text: str) -> str:
    tokens = tokenize(text)
    parts = separation(tokens)
    total = parse_expression(parts)
    if total < 0:
        raise ValueError("Результат не может быть отрицательным")
    if total >= 100000000:
        raise ValueError("Результат не может быть больше миллиона")
    return money_to_words(total)

def main():
    print("Введи суммы в рублях и/или копейках, с операциями «плюс» или «минус».")
    try:
        print(calc(input()))
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
