from flask import Flask, render_template, request, jsonify
import pickle, os, random

# ===== Game Logic =====
def check_winner(board):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in win_states:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]
    if " " not in board:
        return "Draw"
    return None

def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]

def board_to_string(board):
    return "".join(board)

class QLearningAgent:
    def __init__(self, player):
        self.player = player
        self.q_table = {}
        self.epsilon = 0  # no randomness in play

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, board):
        state = board_to_string(board)
        moves = available_moves(board)
        q_values = [self.get_q(state, a) for a in moves]
        max_q = max(q_values)
        best_moves = [a for a, q in zip(moves, q_values) if q == max_q]
        return random.choice(best_moves)

# ===== Load AI =====
app = Flask(__name__)

agent_O = QLearningAgent("O")
if os.path.exists("qtable_O.pkl"):
    with open("qtable_O.pkl", "rb") as f:
        agent_O.q_table = pickle.load(f)
else:
    raise FileNotFoundError("qtable_O.pkl not found. Train the AI first.")

# ===== Routes =====
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    board = data["board"]
    ai_move = agent_O.choose_action(board)
    board[ai_move] = "O"

    winner = check_winner(board)
    return jsonify({"board": board, "winner": winner})

if __name__ == "__main__":
    app.run(debug=True)
