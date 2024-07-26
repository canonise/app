from __future__ import annotations

from discord.ext.commands import Cog
from discord.app_commands import allowed_installs, allowed_contexts

from ext.tree import App
from ext.interaction import Interaction

from discord import Message, Embed, Interaction as Default, User


bot = App()


class Information(Cog):
    def __init__(self: Information, bot: App, /) -> None:
        self.bot = bot


    @bot.tree.command(
        name = "avatar",
        description = "View an avatar",
        extras = {
            "usage": "<member>",
            "example": "route"
        }
    )
    @allowed_installs(
        guilds=True, 
        users=True
    )
    @allowed_contexts(
        guilds=True, 
        dms=True, 
        private_channels=True
    )
    async def avatar(
        self: Information,
        default: Default,
        user: User = None
        
    ) -> Message:
        
        ctx = Interaction(default)
        user = user or ctx.author
        
        return await ctx.send(
            b = Embed(
                title = user.name
            ).set_image(
                url = user.avatar.url
            )
        )


async def setup(bot: App):
    return await bot.add_cog(Information(bot))
