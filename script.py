#!/usr/bin/python3

from curses.ascii import isdigit
from enum import Enum
from pathlib import Path
from sys import argv
from typing import List
import os


class CommandType(Enum):
    CREATE = "create"


def main():
    if len(argv) < 2:
        help()
        exit(-1)

    if argv[1] == CommandType.CREATE.value:
        createProblem(argv)
        exit(0)

    help()
    exit(0)


def help():
    print("""
  To create folder for problem: use `create folder/problem-name`, example Codility/problem-1
        """)


def createProblem(argv: List[str]):
    if len(argv) < 3:
        print("Please provide name and parent folder")

    arg = argv[2]

    path = list(filter(lambda x: x != "", arg.split("/")))

    path = walkFolder(path)

    createFile(path, "solution.py", SOLUTION)
    createFile(path, "README.md", README)


def walkFolder(path: List[str]):
    basePath = Path(".")
    curPath = basePath

    for idx, name in enumerate(path):
        curPath = Path(curPath, name)

        if idx == len(path) - 1 and curPath.is_dir():
            print("The problem already exist at " +
                  str(curPath.relative_to(basePath)))
            exit(-1)

        if not curPath.is_dir():
            os.mkdir(curPath)

    return curPath


def createFile(path: Path, fileName: str, content: str):
    with open(Path(path, fileName), "w") as file:
        file.write(content)

    return True


README = """# <Problem name>

# Problem Overview

# Solution Strategy

"""
SOLUTION = """def solution():
  # write solution here
  pass

"""

if __name__ == "__main__":
    main()
