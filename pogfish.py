from stockfish import Stockfish
import pyautogui
import os
import chess
import time, random
STOCK_FISH_PATH = "F:\\pogfish\\stockfish_20011801_x64_modern.exe"

board = chess.Board()

stockfish = Stockfish(STOCK_FISH_PATH, parameters={
    "Write Debug Log": "false",
    "Contempt": 3,
    "Min Split Depth": 20,
    "Threads": 6,
    "Ponder": "false",
    "Hash": 16,
    "MultiPV": 1,
    "Skill Level": 40,
    "Move Overhead": 30,
    "Minimum Thinking Time": 15,
    "Slow Mover": 80,
    "UCI_Chess960": "false",
})
orig_pos = pyautogui.position()
is_white = True
print("[W]hite or [B]lack?")
ans = input("> ")
if ans.lower() == "b":
    is_white = False
else:
    is_white = True
if not is_white:
    for k, v in PIECE_POS.items():
        v.reverse()
print("Enter White Opening Move:")
wom = input("> ")
board.push_san(wom.strip())
print("Enter Black Opening Move:")
bom = input("> ")
board.push_san(bom.strip())
if not is_white:
    print("Enter White's Second Move:")
    wsm = input("> ")
    board.push_san(wsm)
stockfish.set_fen_position(board.fen())
best_move = stockfish.get_best_move()
print("Your Best Move:", best_move)
while True:
    while True:
        try:
            print("Enter Your Move or Nothing If You Chose Best Move:")
            mov = input("> ")
            if mov.lower() == None or mov.lower() == "":
                board.push_uci(best_move)
            else:
                board.push_san(mov.strip())
            break
        except ValueError:
            print("Try Again!")
    while True:
        try:
            print("Enter Opponent's Move:")
            omov = input("> ")
            board.push_san(omov)
            break
        except ValueError:
            print("Try Again")
    stockfish.set_fen_position(board.fen())
    best_move = stockfish.get_best_move()
    os.system("clear")
    print(board)
    print("Your Best Move:", best_move)