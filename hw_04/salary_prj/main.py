#!/usr/bin/python
# -*- coding: utf-8 -*-

from calculation import total_salary


def main():
    file_path = "salary_statement.txt"
    result = total_salary(file_path)
    print(f"Загальна сума: {result[0]}, Середня зарплата: {result[1]}")


if __name__ == "__main__":
    main()
