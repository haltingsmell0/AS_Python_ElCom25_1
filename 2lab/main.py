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
}
RUBLE_FORMS = ["рубль", "рубля", "рублей"]
KOPEK_FORMS = ["копейка", "копейки", "копеек"]

def tokenize(text: str) -> list[str]:
    return text.lower().split()

def words_to_number(words: str) -> int:
    s = 0
    for word in words:
        s += TEXT2NUM[word]
    return s

def parse_money(tokens: list[str]) -> int:
    r_index = next((i for i, word in enumerate(tokens) if word in RUBLE_FORMS), None)
    k_index = next((i for i, word in enumerate(tokens) if word in KOPEK_FORMS), None)
    rubles, kopeks = 0, 0
    if r_index:
        rubles = words_to_number(tokens[:r_index])
    if k_index:
        kopeks_start = r_index + 1 if r_index is not None else 0
        kopeks = words_to_number(tokens[kopeks_start:k_index])
    return rubles*100 + kopeks

def parse_expression(tokens: list[str]) -> int:
    if "плюс" in tokens:
        index = tokens.index("плюс")
        operator = "плюс"
    elif "минус" in tokens:
        index = tokens.index("минус")
        operator = "минус"
    left_tokens = tokens[:index]
    right_tokens = tokens[index+1:]
    left = parse_money(left_tokens)
    right = parse_money(right_tokens)

def calc(text: str) -> str:
    tokens = tokenize(text)


def main():
    raise NotImplementedError(
        "Реализуйте лабораторную 2 своего варианта (поле variant в student.json)"
    )


if __name__ == "__main__":
    main()
