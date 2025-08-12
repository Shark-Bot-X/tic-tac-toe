# Tic Tac Toe vs Sneh's AI

A web-based Tic Tac Toe game where you play against an AI powered by Q-Learning reinforcement learning.

Live on -> https://tic-tac-toe-1-jyux.onrender.com/

## 🎮 How to Play

- You are **X** (red), AI is **O** (teal)
- Click any empty cell to make your move
- Try to get three in a row (horizontally, vertically, or diagonally)
- The AI will respond automatically after your move

## 🛠️ Local Development

1. **Clone the repository**:
   ```bash
   git clone (https://github.com/Shark-Bot-X/tic-tac-toe)
   cd tic-tac-toe-ai
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the Q-table**:
   ```bash
   python create_basic_qtable.py
   ```

5. **Run the app**:
   ```bash
   python app.py
   ```

6. **Open browser** to `http://localhost:5000`

## 🤖 About the AI

The AI uses Q-Learning, a reinforcement learning algorithm that learns optimal moves through trial and error. The `qtable_O.pkl` file contains the AI's learned strategy, including:

- Strategic opening moves (center and corners)
- Defensive blocks to prevent player wins  
- Offensive moves to secure victories
- Fallback random moves for unexplored game states

## 🔧 Customization

### Modify AI Behavior
Edit `create_basic_qtable.py` to change the AI's strategy, then regenerate the Q-table.

### Update Styling
Modify the CSS in `templates/index.html` to change the game's appearance.

### Add Features
Extend `app.py` to add new game modes, difficulty levels, or statistics tracking.

## 📊 Deployment Requirements

- **Python**: 3.8+
- **Memory**: ~100MB
- **Storage**: ~10MB
- **Platform**: Any Python-compatible hosting (Render, Heroku, Railway, etc.)

## 🐛 Troubleshooting

**Q-table not found error**: Make sure to run `create_basic_qtable.py` and commit the generated `qtable_O.pkl` file.

**Connection errors**: Check that your deployment platform allows outbound HTTP requests.

**Game not loading**: Verify all template files are in the `templates/` directory.

## 📜 License

This project is open source and available under the MIT License.
