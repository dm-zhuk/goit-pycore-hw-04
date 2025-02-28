def get_cats_info(path: str) -> list[dict]:
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as fc:
            for line in fc:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Помилка в рядку '{line}': wrong format")
                    continue

        return cats

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        return []
