import main


def empty_board():
    horizontals = [[False] * 4 for _ in range(5)]
    verticals = [[False] * 5 for _ in range(4)]
    boxes = [[None] * 4 for _ in range(4)]
    return horizontals, verticals, boxes


def test_move_check_horizontal():
    assert main.move_check("A1-A2") == (0, 0, 0, 1)


def test_move_check_vertical():
    assert main.move_check("A1-B1") == (0, 0, 1, 0)


def test_move_check_reverse_direction():
    assert main.move_check("B3-A3") == (1, 2, 0, 2)


def test_move_check_wrong_format():
    assert main.move_check("A1B1") is False


def test_move_check_diagonal():
    assert main.move_check("A1-B2") is False


def test_is_box_false_on_empty_board():
    horizontals, verticals, _ = empty_board()
    assert main.is_box(horizontals, verticals, 0, 0) is False


def test_is_box_true_when_all_four_edges_exist():
    horizontals, verticals, _ = empty_board()

    horizontals[0][0] = True
    horizontals[1][0] = True
    verticals[0][0] = True
    verticals[0][1] = True

    assert main.is_box(horizontals, verticals, 0, 0) is True


def test_check_boxes_closes_one_box():
    horizontals, verticals, boxes = empty_board()

    # Три стороны левого верхнего квадрата уже стоят.
    horizontals[0][0] = True
    verticals[0][0] = True
    verticals[0][1] = True

    # Игрок ставит нижнюю горизонтальную сторону.
    horizontals[1][0] = True

    new_boxes = main.check_boxes(
        horizontals, verticals, boxes,
        "h", 1, 0, "X"
    )

    assert new_boxes == 1
    assert boxes[0][0] == "X"


def test_check_boxes_can_close_two_boxes_at_once():
    horizontals, verticals, boxes = empty_board()

    # Квадрат сверху от будущего общего ребра.
    horizontals[0][0] = True
    verticals[0][0] = True
    verticals[0][1] = True

    # Квадрат снизу от будущего общего ребра.
    horizontals[2][0] = True
    verticals[1][0] = True
    verticals[1][1] = True

    # Общее горизонтальное ребро между ними.
    horizontals[1][0] = True

    new_boxes = main.check_boxes(
        horizontals, verticals, boxes,
        "h", 1, 0, "O"
    )

    assert new_boxes == 2
    assert boxes[0][0] == "O"
    assert boxes[1][0] == "O"


def test_check_boxes_does_not_count_box_twice():
    horizontals, verticals, boxes = empty_board()

    horizontals[0][0] = True
    horizontals[1][0] = True
    verticals[0][0] = True
    verticals[0][1] = True
    boxes[0][0] = "X"

    new_boxes = main.check_boxes(
        horizontals, verticals, boxes,
        "h", 0, 0, "O"
    )

    assert new_boxes == 0
    assert boxes[0][0] == "X"


def test_game_continues_on_empty_board():
    horizontals, verticals, _ = empty_board()
    assert main.game_continues(horizontals, verticals) is True


def test_game_stops_when_all_edges_are_filled():
    horizontals = [[True] * 4 for _ in range(5)]
    verticals = [[True] * 5 for _ in range(4)]

    assert main.game_continues(horizontals, verticals) is False
