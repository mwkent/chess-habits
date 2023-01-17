import chess
from chess import Board, Move, Square, PAWN, KNIGHT, BISHOP, ROOK, QUEEN


def is_free_capture(board: Board, move: Move) -> bool:
    # TODO: Should only consider pieces, not pawns?
    # Is capture and no defenders
    return board.is_capture(move) and not board.is_attacked_by(not board.turn, move.to_square)


def is_saving_hanging_piece(board: Board, move: Move) -> bool:
    piece_color = board.color_at(move.from_square)
    for piece_type in range(1, 6):  # All piece types except king
        for piece in board.pieces(piece_type, piece_color):
            if is_piece_hanging(board, piece):
                board.push(move)
                try:
                    if (piece == move.from_square and not is_piece_hanging(board, move.to_square)) or \
                            (piece != move.from_square and not is_piece_hanging(board, piece)):
                        return True
                finally:
                    board.pop()
    return False


def is_piece_hanging(board: Board, piece: Square) -> bool:
    piece_color = board.color_at(piece)
    return board.is_attacked_by(not piece_color, piece) and not board.is_attacked_by(piece_color, piece)


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
