#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from colorama import init, Fore

init()


def dir_tree(path, prefix=""):
    if not path.exists() or not path.is_dir():
        print(
            Fore.RED
            + "Error: The specified path does not exist or is not a directory."
            + Fore.RESET
        )
        return

    for item in path.iterdir():
        if item.is_dir():
            print(Fore.CYAN + prefix + item.name + Fore.RESET)
            dir_tree(item, prefix + "    ")  # Recur with increased prefix
        else:
            print(Fore.GREEN + prefix + item.name + Fore.RESET)
