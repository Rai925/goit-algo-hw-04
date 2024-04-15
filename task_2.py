def get_cats_info(path):
    cat_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_info = {
                        'id': cat_data[0],
                        'name': cat_data[1],
                        'age': cat_data[2]
                    }
                    cat_list.append(cat_info)
                else:
                    print(f"Помилка у форматі рядка: {line}")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")

    return cat_list

cats_info = get_cats_info("cats_data.txt")

for cat in cats_info:
    print(cat)
