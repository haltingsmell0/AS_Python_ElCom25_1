# Практикум по программированию · ЭлКом25-1

Это репозиторий **для форка**. Свой код пишите в форке, ветка `master`.
**В этот родительский репозиторий pull request отправлять не нужно**.

Задания, лекции и БРС — в базовом курсе: https://github.com/hilleri123/AS_Python

- Лаб. 1: https://github.com/hilleri123/AS_Python/blob/master/1lab/task.md
- Лаб. 2: https://github.com/hilleri123/AS_Python/blob/master/2lab/task.md
- Лаб. 3: https://github.com/hilleri123/AS_Python/blob/master/3lab/task.md
- Лаб. 4: https://github.com/hilleri123/AS_Python/blob/master/4lab/task.md
- БРС: https://github.com/hilleri123/AS_Python/blob/master/BRS.md
- Как устроена сдача: https://github.com/hilleri123/AS_Python/blob/master/ORGANIZATION.md

# Инструкция по сдаче

1. Создайте форк этого репозитория. Как нажать Fork и не спутать свой репо с чужим: https://github.com/hilleri123/AS_Python/blob/master/GIT.md

2. Заполните `student.json`:

```json
{
    "name_f": "Иванов",
    "name_i": "Иван",
    "name_o": "Иванович",
    "group": "ЭлКом25-1",
    "id": 222222,
    "variant": 1
}
```

`id` — номер зачётной книжки (целое число, без кавычек). Вариант: `(id % 4) + 1`, тоже число. Группа в файле — `ЭлКом25-1`.

3. Пишите код в `1lab/`, `2lab/`, `3lab/`, `4lab/`. Точка входа — `main.py`.
4. Запуск **из корня** репозитория:

```bash
python3 1lab/main.py
python3 2lab/main.py
python3 3lab/main.py
python3 4lab/main.py
```

5. Зависимости укажите в `requirements.txt`.

## Важно

- Если в git есть файл `.env`, работа **не смотрится**. Это ломает скрипты проверки. Удалите `.env` из репозитория (он уже в `.gitignore`).
- Проверяется взаимный плагиат. Больше 70% — работа не принимается.
- Больше 95% — работа аннулируется и больше не принимается; баллы только после дополнительного задания.
- Если списано у нескольких — баллы никому или только автору более раннего коммита.
- Не запускается командой из пункта 4 — не принимается.
- Не работает на другой ОС: **-50%**.
- Больше 10 нарушений PEP 8: **-10%**.
- Падение программы: **-30%** за сценарий.
- Ввод, от которого программа падает: **-20%**.

Работу выполняйте самостоятельно.
