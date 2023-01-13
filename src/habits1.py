import random
from typing import List, Dict

import chess
from chess import Board, Move, PAWN, KNIGHT, BISHOP, ROOK, QUEEN


def search(board: Board) -> Move:
    sorted_moves = sort_moves(board)
    return sorted_moves[0]


def sort_moves(board: Board) -> List[Move]:
    """
    Priority is:
    1. Take free pieces
    2. Take equal trades
    3. Control the center
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
    random.shuffle(moves)  # Helps to add variety to moves
    for move in moves:
        moves_to_priorities[move] = get_priority(board, move)
    return moves_to_priorities


def get_priority(board: Board, move: Move) -> int:
    if is_free_capture(board, move):
        return 0
    elif is_equal_trade(board, move):
        return 1
    elif is_move_towards_center(board, move):
        return 2
    else:
        return 3


def is_free_capture(board: Board, move: Move) -> bool:
    # TODO: Should only consider pieces, not pawns?
    # Is capture and no defenders
    return board.is_capture(move) and not board.is_attacked_by(not board.turn, move.to_square)


def is_equal_trade(board: Board, move: Move) -> bool:
    piece_types_to_values = {PAWN: 1, KNIGHT: 3, BISHOP: 3, ROOK: 5, QUEEN: 9}
    return board.is_en_passant(move) or (board.is_capture(move) and
                                         (piece_types_to_values[board.piece_type_at(move.from_square)] ==
                                          piece_types_to_values[board.piece_type_at(move.to_square)]))


def is_move_towards_center(board: Board, move: Move) -> bool:
    center = {chess.C3, chess.C4, chess.C5, chess.C6,
              chess.D3, chess.D4, chess.D5, chess.D6,
              chess.E3, chess.E4, chess.E5, chess.E6,
              chess.F3, chess.F4, chess.F5, chess.F6}
    return move.from_square not in center and move.to_square in center \
        and board.piece_type_at(move.from_square) != chess.KING
