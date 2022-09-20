from time import sleep

import click
from rich.align import Align
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.rule import Rule
from rich.text import Text

from mankey.data.master import master_encrypted
from mankey.utils import choice_option
from mankey.utils.crypto import decrypt
from mankey.utils.sync_data import save_new_pwd


def new_pwd() -> int:
    console = Console()
    console.set_alt_screen()
    console.print(Rule("STORE NEW PASSWORD", style="cyan"))

    name = Prompt.ask("Where is the password from?")
    url = Prompt.ask("\nEnter the url")
    user = Prompt.ask("\nWhat is your user?")
    pwd = Prompt.ask("\nWhat is your password?", password=True)


    console.print(f"\nIt's from [green]{name}[/]")
    console.print(f"The url is [yellow]{url}[/]")
    console.print(f"Your user is [cyan]{user}[/]")
    if Confirm.ask("Want to confirm your password?", default=False):
        console.print(f"Your password is [red]{pwd}[/]")


    save_new_pwd(name, url, user, pwd)
    click.getchar()
    return
