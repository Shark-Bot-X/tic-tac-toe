# Tic Tac Toe vs AI

A web-based Tic Tac Toe game where you play against an AI powered by Q-Learning reinforcement learning.

## 🚀 Quick Deploy to Render

1. **Fork/Clone this repository** to your GitHub account

2. **Create the Q-table** (run locally first):
   ```bash
   python create_basic_qtable.py
   ```
   This creates `qtable_O.pkl` file needed by the AI.

3. **Commit and push** the qtable_O.pkl file to your repository:
   ```bash
   git add qtable_O.pkl
   git commit -m "Add AI Q-table"
   git push
   ```

4. **Deploy on Render**:
   - Go to [Render.com](https://render.com) and create account
   - Connect your GitHub account
   - Create new "Web Service"
   - Select this repository
   - Render will automatically detect the `render.yaml` configuration
   - Click "Deploy"

## 🎮 How to Play

- You are **X** (red), AI is **O** (teal)
- Click any empty cell to make your move
- Try to get three in a row (horizontally, vertically, or diagonally)
- The AI will respond automatically after your move

## 📁 Project Structure

```
tic-tac-toe-ai/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment config
├── create_basic_qtable.py # Script to create AI Q-table
├── qtable_O.pkl          # AI's trained Q-table (generated)
├── templates/
│   └── index.html        # Game interface
└── README.md            # This file
```

## 🛠️ Local Development

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
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