import discord
import json
from discord.ext import commands
from discord.ext.commands.context import Context

# 데이터 베이스 참조하기
def 도서관_정보_가져오기():
    with open('data/library.json', encoding='utf-8') as fp:
        도서관_정보 = json.load(fp)
    return 도서관_정보

async def facilities(ctx  : Context):
    정보 = 도서관_정보_가져오기()
    string = ""    
    for facil in 정보["시설"]:
        string += facil["이름"]
        string += " : "
        string += facil["설명"]
        string += "\n"

    string += "\n이런 시설들이 있어요!"
    await ctx.send(f"{string}")
    return

async def operating_hours(ctx : Context):
    정보 = 도서관_정보_가져오기()
    open = 정보["운영시간"]["open"]
    closed = 정보["운영시간"]["closed"]
    await ctx.send(f"도서관은 {open}부터 {closed}까지 운영해요!")
    return

@commands.command()
async def 도서관(ctx : Context, menu : str= None):
    """
        menu에는 운영시간, 시설이 들어와야 한다.
    """
    
    if menu == None:
        await ctx.send(f"도서관에 대해 알고 싶으면\n!도서관 운영시간, !도서관 시설 라고 보내주세요!")
    
    if menu == "운영시간":
        return await operating_hours(ctx)
    
    if menu == "시설":
        return await facilities(ctx)