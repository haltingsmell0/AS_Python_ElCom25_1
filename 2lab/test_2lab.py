"""Проверки лабораторной 2, вариант «Деньги»."""

import pytest
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("lab2_main", Path(__file__).with_name("main.py"))
assert _spec is not None and _spec.loader is not None
_lab2 = module_from_spec(_spec)
_spec.loader.exec_module(_lab2)
calc = _lab2.calc
main = _lab2.main


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("один рубль плюс два рубля", "три рубля"),
        ("пять рублей минус два рубля", "три рубля"),
        ("сто три рубля плюс сто рублей", "двести три рубля"),
        ("сто двадцать три рубля плюс сто рублей", "двести двадцать три рубля"),
        ("сто одиннадцать рублей плюс сто рублей", "двести одиннадцать рублей"),
        ("двадцать одна копейка плюс две копейки", "двадцать три копейки"),
        ("один рубль плюс пятьдесят копеек", "один рубль пятьдесят копеек"),
        ("одна копейка плюс две копейки", "три копейки"),
        ("два рубля пять копеек минус один рубль", "один рубль пять копеек"),
        ("один рубль минус один рубль", "ноль рублей"),
        ("одна тысяча рублей плюс два рубля", "одна тысяча два рубля"),
        ("тысяча двести рублей плюс одна копейка", "одна тысяча двести рублей одна копейка"),
        ("одна тысяча один рубль плюс один рубль", "одна тысяча два рубля"),
        ("десять рублей плюс два рубля минус три рубля", "девять рублей"),
        ("десять рублей минус два рубля плюс три рубля", "одиннадцать рублей"),
    ],
)
def test_calc_returns_amount_in_words(expression: str, expected: str) -> None:
    assert calc(expression) == expected


@pytest.mark.parametrize(
    "expression",
    [
        "",
        "один рубль",
        "один рубль плюс",
        "один рубль минус два рубля",
        "один доллар плюс два рубля",
        "один рубль два рубля плюс три рубля",
        "один рубль копейка плюс два рубля",
        "сто копеек плюс один рубль",
        "один рубль неизвестно плюс два рубля",
    ],
)
def test_calc_rejects_invalid_expression(expression: str) -> None:
    with pytest.raises(ValueError):
        calc(expression)


def test_main_prints_result(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr("builtins.input", lambda: "два рубля плюс три рубля")

    main()

    assert "пять рублей" in capsys.readouterr().out


def test_main_prints_error_instead_of_traceback(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("builtins.input", lambda: "один рубль минус два рубля")

    main()

    output = capsys.readouterr().out
    assert "Ошибка:" in output
    assert "отрицательным" in output
    assert "Traceback" not in output
