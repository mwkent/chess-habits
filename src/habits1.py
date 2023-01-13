from typing import List, Dict

from chess import Board, Move, PAWN, KNIGHT, BISHOP, ROOK, QUEEN


def search(board: Board) -> Move:
    sorted_moves = sort_moves(board)
    return sorted_moves[0]


def sort_moves(board: Board) -> List[Move]:
    """
    Priority is:
    1. Take free pieces
    2. Take equal trades
    """
    moves_to_priorities = get_priority_map(board)

    def priority_getter(value):
        return moves_to_priorities.get(value)

    return sorted(moves_to_priorities, key=priority_getter)


def get_priority_map(board: Board) -> Dict[Move, int]:
    """
    Maps moves to their priority.
    """
    moves_to_priorities = {}
    moves = list(board.legal_moves)
    for move in moves:
        moves_to_priorities[move] = get_priority(board, move)
    return moves_to_priorities


def get_priority(board: Board, move: Move) -> int:
    if is_free_capture(board, move):
        return 0
    elif is_equal_trade(board, move):
        return 1
    else:
        return 2


def is_free_capture(board: Board, move: Move) -> bool:
    # TODO: Should only consider pieces, not pawns?
    # Is capture and no defenders
    return board.is_capture(move) and not board.is_attacked_by(not board.turn, move.to_square)


def is_equal_trade(board: Board, move: Move) -> bool:
    piece_types_to_values = {PAWN: 1, KNIGHT: 3, BISHOP: 3, ROOK: 5, QUEEN: 9}
    return board.is_en_passant(move) or (board.is_capture(move) and
                                         (piece_types_to_values[board.piece_type_at(move.from_square)] ==
                                          piece_types_to_values[board.piece_type_at(move.to_square)]))
