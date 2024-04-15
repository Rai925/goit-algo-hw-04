def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    salary = int(parts[1])
                    total_salary += salary
                    num_developers += 1
                else:
                    print(f"Skipping invalid line: {line}")

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    if num_developers == 0:
        print("No valid data found in the file.")
        return None

    average_salary = total_salary / num_developers

    return total_salary, average_salary

file_path = "list.txt"
result = total_salary(file_path)

if result is not None:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
