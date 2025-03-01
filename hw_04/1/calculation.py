def total_salary(path: str) -> tuple[int, float]:
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as fc:
            for line in fc:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка в рядку '{line}': wrong format || salary not int")
                    continue

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return (0, 0)
