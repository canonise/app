from __future__ import annotations

from discord import Intents
from discord.ext.commands import Bot
from aiohttp import ClientSession


class App(Bot):
    def __init__(self: App):
        super().__init__(
            command_prefix = "...",
            case_insensetive = True,
            intents = Intents.all()
        )
        self.token = "..."
        self.http: ClientSession
        self.__cogs__ = {
            "cogs.information"
        }
        

    async def setup_hook(self: App) -> None:
        await self.walk_commands()
        await self.tree.sync()


    async def walk_commands(self: App) -> None:
        for ext in self.__cogs__:
            try:
                await self.load_extension(ext)
                print(f"Loaded {ext}")
                
            except Exception as e:
                print(str(e))


    def run(self: App) -> None:
        super().run(self.token, reconnect=True)