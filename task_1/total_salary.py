import re


def get_salaries(path: str) -> list[int]:
    with open(path, encoding='utf-8') as file:
        salaries_list = []
        for el in file.readlines():
            match = re.search(r'\d+', el)
            if match:
                salaries_list.append(int(match.group()))
        # salaries_list = [int(re.search(r'\d+', el).group()) for el in file.readlines()]
        return salaries_list


def total_salary(path: str) -> int:
    salaries_list = get_salaries(path)
    total = sum(salaries_list)
    average = int(total / len(salaries_list))
    return total, average 


