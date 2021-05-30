import requests
import json
import discord

from env import get_env

client = discord.Client()


class Reporter:
    def __init__(self):
        self.__web_hook_url = get_env()['WEB_HOOK_URL']

    def report(self, message):
        requests.post(
            url=self.__web_hook_url,
            data=json.dumps({
                "text": message
            }),
        )


@client.event
async def on_voice_state_update(member, before, after):
    rep = Reporter()
    if member.guild.id == get_env()["SERVER_ID"]:
        if before.channel is None:
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            rep.report(msg)
        if after.channel is None:
            msg = f'{member.name} が {before.channel.name} から退出しました。'
            rep.report(msg)

client.run(get_env()["DISCORD_TOKEN"])
