import chess.pgn
import sys
from datetime import datetime

if __name__ == "__main__":
    output_name = datetime.now().strftime("output/%Y-%m-%d-%H-%M-%S.csv")
    with open(sys.argv[1]) as pgn_file, open(output_name, "w") as fen_file:
        game = chess.pgn.read_game(pgn_file)
        for _ in range(4000):
            if game.headers['Result'] == '1-0':
                result = '1.0'
            elif game.headers['Result'] == '0-1':
                result = '0.0'
            else:
                result = '0.5'
            board = game.board()

            for move in game.mainline_moves():
                board.push(move)
                fen_file.write(f'{board.fen()},{result}\n')
            game = chess.pgn.read_game(pgn_file)
