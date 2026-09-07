def acquaintance():
    print("Точки и квадраты.")
    print("Введите имя Первого игрока")
    player1 = str(input()).capitalize()
    print("Введите имя Второго игрока")
    player2 = str(input()).capitalize()
    return player1, player2


def print_board(horizontals, verticals, boxes):
    print("    1   2   3   4   5")
    for r in range(5):
        print(chr(ord("A") + r), end="   ")
        for c in range(5):
            print("●", end="")
            if c < 4:
                if horizontals[r][c]:
                    print("---", end='')
                else:
                    print("   ", end='')
        print()
        if r < 4:
            print("    ", end='')
            for c in range(5):
                if verticals[r][c]:
                    print("|", end='')
                else:
                    print(' ', end='')
                if c < 4:
                    owner = boxes[r][c]
                    if owner is None:
                        print("   ", end='')
                    else:
                        print(f" {owner} ", end='')
            print()


def move_check(move_text):
    if not(
            len(move_text) == 5
            and move_text[0] in "ABCDE"
            and move_text[1] in "12345"
            and move_text[2] == "-"
            and move_text[3] in "ABCDE"
            and move_text[4] in "12345"
        ):
            print("Неправильный формат. Пример хода: A1-A2")
    else:
        r1 = ord(move_text[0]) - ord("A")
        c1 = int(move_text[1]) - 1
        r2 = ord(move_text[3]) - ord("A")
        c2 = int(move_text[4]) - 1
        if not abs(r1-r2) + abs(c1-c2) == 1:
            print("Неправильный ход. Пример хода: A1-A2")
        else:
            return r1, c1, r2, c2
    return False


def parse_edge(player_name, n_move):
    print(f"Ход {n_move}. {player_name}, твоя очередь")
    move_coo = False
    while not move_coo:
        move_coo = move_check(input().upper())
    r1, c1, r2, c2 = move_coo
    if r1 == r2:
        edge = "h"
    else:
        edge = "v"
    return edge, min(r1, r2), min(c1, c2)


def is_box(horizontals, verticals, r, c):
    return (
        horizontals[r][c]
        and horizontals[r + 1][c]
        and verticals[r][c]
        and verticals[r][c + 1]
    )


def check_boxes(horizontals, verticals, boxes, edge, r, c, player):
    new_boxes = 0
    if edge == "h":
        if r > 0:
            if (boxes[r - 1][c] is None 
                and is_box(horizontals, verticals, r - 1, c)):
                boxes[r - 1][c] = player
                new_boxes += 1
        if r < 4:
            if (boxes[r][c] is None 
                and is_box(horizontals, verticals, r, c)):
                boxes[r][c] = player
                new_boxes += 1
    elif edge == "v":
        if c > 0:
            if (boxes[r][c - 1] is None 
                and is_box(horizontals, verticals, r, c - 1)):
                boxes[r][c - 1] = player
                new_boxes += 1
        if c < 4:
            if (boxes[r][c] is None 
                and is_box(horizontals, verticals, r, c)):
                boxes[r][c] = player
                new_boxes += 1
    return new_boxes


def game_continues(horizontals, verticals):
    for r in horizontals:
        if False in r:
            return True
    for v in verticals:
        if False in v:
            return True
    return False

    
def main():
    horizontals = [[False]*4 for _ in range(5)]
    verticals = [[False]*5 for _ in range(4)]
    boxes = [[None]*4 for _ in range(4)]
    names = acquaintance()
    score = [0,0]
    print_board(horizontals, verticals, boxes)
    n_move, order, symbols = 1, 0, ("X", "O")
    while game_continues(horizontals, verticals):
        print(
        f"{names[0]}: {score[0]} | "
        f"{names[1]}: {score[1]}"
    )
        edge, r, c = parse_edge(names[order], n_move)
        if edge == "h":
            if horizontals[r][c]:
                print("Это ребро уже занято!")
                continue
            horizontals[r][c] = True
        elif edge == "v":
            if verticals[r][c]:
                print("Это ребро уже занято!")
                continue
            verticals[r][c] = True
        new_boxes = check_boxes(horizontals, verticals, boxes, edge, r, c, symbols[order])
        score[order] += new_boxes
        print_board(horizontals, verticals, boxes)
        if new_boxes == 0:
            order = (order+1)%2
        n_move += 1
    if score[0] > score[1]:
        print(f"Игра окончена! Победил {names[0]} "
              f"со счётом {score[0]}:{score[1]}!")
    elif score[1] > score[0]:
        print(f"Игра окончена! Победил {names[1]} "
              f"со счётом {score[1]}:{score[0]}!")
    else:
        print(f"Игра окончена! Ничья — {score[0]}:{score[1]}.")

        
if __name__ == "__main__":
    main()
