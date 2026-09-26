import discord
from discord import ui
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


class CustomTicketView(ui.LayoutView):

  def __init__(self):
    super().__init__(timeout=None)

    container = ui.Container(
        ui.TextDisplay("# ````BOT × Designer \\ KAKTUSIK PL```"),
        ui.Separator(spacing=1),
        ui.TextDisplay(
            ":index_pointing_at_the_viewer_tone5: · __Kup se bota__ pozdrawiam"
        ),
        ui.TextDisplay(
            ":mag_right: · **Kaktusik PL** // __quejxgg__"
        ),
        ui.TextDisplay(
            ":zany_face: · nie wiedzialem co tam __dac__ xd"
        ),
        ui.Separator(spacing=1),
    )
    
    btn_first = ui.Button(
        label=" **kup se cos xd**",
        style=discord.ButtonStyle.secondary,
        custom_id="przycisk_1",
        emoji=":money_with_wings:",
    )

    btn_second = ui.Button(
        label=" nie kupuj se czegos",
        style=discord.ButtonStyledanger,
        custom_id="przycisk_2",
        emoji=":clown:",
    )

    action_row = ui.ActionRow(btn_first, btn_second)

    self.add_item(container)
    self.add_item(action_row)

    self.add_item(ui.TextDisplay("![Baner dolny](https://cdn.discordapp.com/attachments/1522165650464702536/1553326543210807336/baner.webp?ex=6ab8d793&is=6ab78613&hm=2af030471ad733302938f2e95c840fac2538ed29bf7fdd6b0b957387f172c53f&)"))

    self.add_item(ui.TextDisplay("-# lubie jesc © 2026 × Kaktusik"))


@bot.event
async def on_ready():
  print(f"Zalogowano jako {bot.user}")


@bot.command()
@commands.has_permissions(administrator=True)
async def ticket(ctx):
  view = CustomTicketView()
  await ctx.send(view=view)
  await ctx.message.delete()


bot.run("MTU1MzMxODQ4NzQ2Njg0MDE2Ng.GC4vK2.9QeWlEfjeJGapttSM3rR3hCds4MawAb4Iejimk")
