from chess import Board, Move

from src.habits1 import sort_moves, get_priority_map, get_priority, search


def test_search():
    board = Board("2kr1bn1/pb1qp3/npP4r/5Pp1/8/5N2/PP3PPP/RNBQKB1R w KQ g6 0 12")
    move = search(board)


def test_sort_moves():
    board = Board("2kr1bn1/pb1qp3/npP4r/5Pp1/8/5N2/PP3PPP/RNBQKB1R w KQ g6 0 12")
    moves = sort_moves(board)
    print(moves)
    priority_map = get_priority_map(board)
    print(priority_map)


def test_get_priority():
    board = Board("2kr1bn1/pb1qp3/npP4r/5Pp1/8/5N2/PP3PPP/RNBQKB1R w KQ g6 0 12")
    expected_to_moves = {
        0: 'f3g5',
        0: 'c1g5',
        1: 'f1a6',
        1: 'd1d7',
        1: 'f5g6',
        2: 'd1d3',
        3: 'a2a3'
    }
    for expected_priority, move in expected_to_moves.items():
        assert expected_priority == get_priority(board, Move.from_uci(move))
