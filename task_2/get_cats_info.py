def get_cats_info(path: str) -> list[dict]:
    cats_info = []
    try:
        with open(path, encoding='utf-8') as file:
            for el in file.readlines():
                [id, name, age] = el.split(',')
                cats_info.append({
                        'id': id,
                        'name': name,
                        'age': age.strip()
                    })
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

    return cats_info
