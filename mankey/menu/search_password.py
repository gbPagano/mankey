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
from mankey.utils.sync_data import save_new_pwd, search_pwd



def search_pwd_menu():
    console = Console()
    console.set_alt_screen()
    
    keyword = Prompt.ask("Where is the password from?")
    search_pwd(keyword)
    input()
