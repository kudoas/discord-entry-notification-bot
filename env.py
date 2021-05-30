import os

from dotenv import load_dotenv


def get_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return {
        "SERVER_ID": int(os.environ.get('SERVER_ID')),
        "DISCORD_TOKEN": os.environ.get('DISCORD_TOKEN'),
        'WEB_HOOK_URL': os.environ.get("WEB_HOOK_URL")
    }
