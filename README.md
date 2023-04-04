# Discord Bot User Presence Tracker

This is a Python script for a Discord bot that tracks the presence of a specific user in a guild and logs the time they spend online. The script utilizes the Discord API and the `discord.py` library.

## Requirements

- Python 3.x
- `discord.py` library
- Discord bot token
- Discord guild and user ID

## Setup

1. Clone or download the repository to your local machine.
2. Install the `discord.py` library using pip: `pip install discord.py`.
3. In the `config.py` file, replace the `TOKEN`, `GUILD_ID`, and `USER_ID` values with your own Discord bot token and the guild and user IDs you want to track.
4. Run the `bot.py` script using `python bot.py`.
5. In Discord, type the command `!s` in any channel that the bot has access to. The bot will then start tracking the user's presence and logging their online time.

## How it works

The bot continuously checks the user's status in the guild and logs the time they spend online. If the user is offline, the bot will wait for 60 seconds before checking their status again. If the user goes offline after being online, the bot will log the time they spent online.

The bot can be stopped by pressing `CTRL + C` in the command line or by shutting down the script.

## Commands

- `!s`: Starts tracking the user's presence and logging their online time.
