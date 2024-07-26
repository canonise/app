from __future__ import annotations

from discord import Interaction as BaseInteraction, Embed, Message
from typing import Any


class M():
    a = "..."       # Tick emoji
    b = "..."       # Fail emoji
    
    ab = "..."      # Green color
    bb = "..."      # Red color


class Interaction():
    def __init__(
        self: Interaction, 
        interaction: BaseInteraction, 
        /
    ) -> None:
        self.i = interaction
        self.u = interaction.user
        self.g = interaction.guild
        self.c = interaction.channel
        self.m = interaction.message


    @property
    def author(self: Interaction):
        return self.u


    async def send(
        self: Interaction,
        a: str = None,       # Message
        b: Embed = None,     # Embed
        d: bool = None,      # Ephemeral
        **kwargs: Any
    ) -> Message:
        
        await self.i.response.send_message(
            content = a,
            Embed = b,
            ephemeral = d,
            **kwargs
        )


    async def followup(
        self: Interaction,
        a: str = None,       # Message
        b: Embed = None,     # Embed
        d: bool = None,      # Ephemeral
        **kwargs: Any
    ) -> Message:
        
        await self.i.followup.send(
            content = a,
            Embed = b,
            ephemeral = d,
            **kwargs
        )


    async def approve(
        self: Interaction,
        a: str = None,      # Message
        b: bool = False,    # Followup
        c: bool = True      # Ephemeral
    ) -> Message:
        
        if a:
            Embed = Embed(
                description = f"{M.a} {self.author.mention} {a}",
                color = M.ab
            )
            if b:
                return await self.followup(
                    a=None, 
                    b=Embed, 
                    d=c
                )
            else:
                return await self.send(
                    a=None, 
                    b=Embed, 
                    d=c
                )


    async def deny(
        self: Interaction,
        a: str = None,      # Message
        b: bool = False,    # Followup
        c: bool = True      # Ephemeral
    ) -> Message:
        
        if a:
            Embed = Embed(
                description = f"{M.b} {self.author.mention} {a}",
                color = M.bb
            )
            if b:
                return await self.followup(
                    a=None, 
                    b=Embed, 
                    d=c
                )
            else:
                return await self.send(
                    a=None, 
                    b=Embed, 
                    d=c
                )