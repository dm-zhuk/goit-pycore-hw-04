#!/usr/bin/python
# -*- coding: utf-8 -*-

from analyse import get_cats_info


def main():
    file_path = "cats_db.txt"
    result = get_cats_info(file_path)
    for cat in result:
        print(f"id: {cat['id']}, name: {cat['name']}, age: {cat['age']}")


if __name__ == "__main__":
    main()
