import chess
from chess import Board, Move

from src.chess_util import is_piece_hanging, is_saving_hanging_piece


def test_is_piece_hanging():
    board = Board("2kr1bn1/pb1qp3/npP4r/5Pp1/8/5N2/PP3PPP/RNBQKB1R w KQ g6 0 12")
    assert is_piece_hanging(board, chess.G5)
    assert not is_piece_hanging(board, chess.H2)


def test_is_saving_hanging_piece():
    board = Board("2kr1bn1/pb1qp3/npP4r/5Pp1/8/5NP1/PP3P1P/RNBQKB1R b KQ - 0 12")
    assert is_saving_hanging_piece(board, Move.from_uci('g5g4'))
    assert is_saving_hanging_piece(board, Move.from_uci('h6h5'))
