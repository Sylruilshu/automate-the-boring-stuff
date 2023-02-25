# chess_board = {'a1': ' ', 'b1': ' ', 'c1': ' ', 'd1': ' ', 'e1': ' ', 'f1': ' ', 'g1': ' ', 'h1': ' ',
#                'a2': ' ', 'b2': ' ', 'c2': ' ', 'd2': ' ', 'e2': ' ', 'f2': ' ', 'g2': ' ', 'h2': ' ',
#                'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
#                'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
#                'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
#                'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
#                'a7': ' ', 'b7': ' ', 'c7': ' ', 'd7': ' ', 'e7': ' ', 'f7': ' ', 'g7': ' ', 'h7': ' ',
#                'a8': ' ', 'b8': ' ', 'c8': ' ', 'd8': ' ', 'e8': ' ', 'f8': ' ', 'g8': ' ', 'h8': ' '}

# Rules:
# 1 king for each colour
# no more than 8 pawns per each colour
# no more than 16 pieces per each colour
# pieces must be on valid spaces from a1 - h8
# piece names begin with either W (white) or B (black)

valid_chess_board = {
    "h1": "Bking",
    "c6": "Wqueen",
    "g2": "Bbishop",
    "h5": "Bqueen",
    "e3": "Wking",
}

invalid_kings = {
    "e8": "Bking",
    "d1": "Wqueen",
    "f8": "Bbishop",
    "e1": "Wking",
    "e3": "Wking",
}

invalid_pawns = {
    "a7": "Bpawn",
    "b7": "Bpawn",
    "c7": "Bpawn",
    "d7": "Bpawn",
    "e7": "Bpawn",
    "f7": "Bpawn",
    "g7": "Bpawn",
    "h7": "Bpawn",
    "h6": "Bpawn",
}

invalid_num_pieces = {
    "a2": "Wpawn",
    "b2": "Wpawn",
    "c2": "Wpawn",
    "d2": "Wpawn",
    "e2": "Wpawn",
    "f2": "Wpawn",
    "g2": "Wpawn",
    "h2": "Wpawn",
    "a1": "Wrook",
    "b1": "Wknight",
    "c1": "Wbishop",
    "d1": "Wqueen",
    "e1": "Wking",
    "f1": "Wbishop",
    "g1": "Wknight",
    "h1": "Wrook",
    "a3": "Wrook",
}

invalid_chess_coordinates = {"z9": "Bqueen"}

invalid_piece_colours = {
    "h1": "king",
    "c6": "queen",
    "g2": "bishop",
    "h5": "queen",
    "e3": "king",
}


def has_one_king_for_each_colour(chess_board: dict) -> bool:
    white_kings = 0
    black_kings = 0

    for piece in chess_board.values():
        colour_of_piece = piece[0]
        type_of_piece = piece[1:]
        if type_of_piece == "king" and colour_of_piece == "W":
            white_kings += 1
        if type_of_piece == "king" and colour_of_piece == "B":
            black_kings += 1

    return white_kings == 1 and black_kings == 1


def has_valid_num_of_pawns(chess_board: dict) -> bool:
    white_pawns = 0
    black_pawns = 0

    for piece in chess_board.values():
        colour_of_piece = piece[0]
        type_of_piece = piece[1:]
        if type_of_piece == "pawn" and colour_of_piece == "W":
            white_pawns += 1
        if type_of_piece == "pawn" and colour_of_piece == "B":
            black_pawns += 1

    return white_pawns <= 8 and black_pawns <= 8


def has_valid_num_of_pieces(chess_board: dict) -> bool:
    white_pieces = 0
    black_pieces = 0

    for piece in chess_board.values():
        colour_of_piece = piece[0]

        if colour_of_piece == "W":
            white_pieces += 1
        if colour_of_piece == "B":
            black_pieces += 1

    return white_pieces <= 16 and black_pieces <= 16


def is_valid_square(chess_board: dict) -> bool:
    valid_squares = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for square in chess_board.keys():
        square_coordinate = square[0]
        num_coordinate = int(square[1])

        if square_coordinate not in valid_squares:
            return False

        if num_coordinate < 1 or num_coordinate > 8:
            return False

    return True


def has_valid_piece_colour(chess_board: dict) -> bool:
    for piece in chess_board.values():
        colour_of_piece = piece[0]
        if colour_of_piece not in ["W", "B"]:
            return False

    return True


def validate_chess_board(chess_board: dict) -> bool:
    if not has_one_king_for_each_colour(chess_board):
        return False
    if not has_valid_num_of_pawns(chess_board):
        return False
    if not has_valid_num_of_pawns(chess_board):
        return False
    if not is_valid_square(chess_board):
        return False
    if not has_valid_piece_colour(chess_board):
        return False
    return True


assert validate_chess_board(valid_chess_board), "Valid chess board evaluated to false"
assert validate_chess_board(invalid_kings) == False, "Invalid kings evaluated to true"
assert validate_chess_board(invalid_pawns) == False, "Invalid pawns evaluated to true"
assert (
    validate_chess_board(invalid_piece_colours) == False
), "Invalid piece colour evaluated to true"
assert (
    validate_chess_board(invalid_chess_coordinates) == False
), "Invalid chess coordinates evaluated to true"

print("All assertions passed!")
