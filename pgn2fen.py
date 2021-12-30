import chess.pgn
import sys
from datetime import datetime
import glob

if __name__ == "__main__":
    x_output_name = datetime.now().strftime("output/x_%Y-%m-%d-%H-%M-%S")
    y_output_name = datetime.now().strftime("output/y_%Y-%m-%d-%H-%M-%S")

    with open(x_output_name, "w") as x_file, open(y_output_name, "w") as y_file:
        for f in glob.glob("./data/*.pgn"):
            with open(f) as pgn_file:
                print(f'Parsing file: {f}')
                game = chess.pgn.read_game(pgn_file)
                while game is not None:
                    if game.headers['Result'] == '1-0':
                        result = '255.0'
                    elif game.headers['Result'] == '0-1':
                        result = '-255.0'
                    else:
                        result = '0.0'
                    board = game.board()

                    i = 0
                    for move in game.mainline_moves():
                        board.push(move)
                        if i % 2 != 0:
                            i = i + 1
                            continue
                        else:
                            i = i + 1
                        x_file.write(f'{board.fen()}\n')
                        y_file.write(f'{result}\n')
                    game = chess.pgn.read_game(pgn_file)
