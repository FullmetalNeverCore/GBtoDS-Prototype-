
import random
import asyncio
import schedule
import os, sys, time, datetime
import datetime
import json
import discord
from discord.ext import commands, tasks
from discord.utils import get
import control 

client = commands.Bot(command_prefix="!")

@client.event
async def on_message(msg):
    MOVES_SET = ['up','down','right','left','a','b']
    control.Control().move(str(msg.content)) if str(msg.content) in MOVES_SET else print("pass")


client.run("")