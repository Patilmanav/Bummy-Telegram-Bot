# Telegram Bot with Multiple Buttons

This is a simple Telegram bot built using Python and the `python-telegram-bot` library. The bot provides multiple interactive buttons for user interaction and fetches data from an external API.

## Features

- `/start` command to initiate the bot and display multiple buttons.
- Buttons:
  - `Interact`: Responds with a simple message.
  - `Employee List`: Fetches and displays a list of employees from an external API.
- `/employee <id>` command to fetch and display details of a specific employee by ID.

## Requirements

- Python 3.8+
- `python-telegram-bot` library
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/patilmanav/telegram-bot-multiple-buttons.git
    cd telegram-bot-multiple-buttons
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `keys.py` file and add your Telegram bot token:
    ```python
    token = 'YOUR_TELEGRAM_BOT_TOKEN'
    ```

## Running the Bot Locally

1. Run the bot:
    ```bash
    python bot.py
    ```

2. Interact with your bot on Telegram by searching for your bot's username and sending the `/start` command.

## Deployment on Heroku

1. Ensure you have the `Heroku CLI` installed and are logged in:
    ```bash
    heroku login
    ```

2. Create a new Heroku app:
    ```bash
    heroku create your-app-name
    ```

3. Set your Telegram bot token as a config variable:
    ```bash
    heroku config:set TELEGRAM_BOT_TOKEN='YOUR_TELEGRAM_BOT_TOKEN'
    ```

4. Push your code to Heroku:
    ```bash
    git add .
    git commit -m "Deploy to Heroku"
    git push heroku master
    ```

5. Scale the bot to run a worker:
    ```bash
    heroku ps:scale worker=1
    ```

6. Check the logs to ensure the bot is running:
    ```bash
    heroku logs --tail
    ```

## File Structure

```plaintext
.
├── bot.py                # Main bot script
├── keys.py               # File to store bot token
├── requirements.txt      # Dependencies
├── Procfile              # Heroku process file
├── runtime.txt           # Specifies the Python version (optional)
└── README.md             # This file
