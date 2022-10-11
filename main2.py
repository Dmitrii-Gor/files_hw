def number_of_line(*files):
    lines = {}
    for file in files:
        with open(file, encoding='utf-8') as file_obj:
            lines.update({file: file_obj.readlines()})
    lines_sort = {}
    for i in sorted(lines, key=lines.get, reverse=True):
        lines_sort[i] = lines[i]
    return lines_sort

result = number_of_line('1', '2', '3')

print(result)
for key, value in result.items():
        with open('key', encoding='utf-8') as f:
            with open('resf', 'a', encoding='Utf-8') as f:
                f.writelines(f'Название файла - {key}\n')
                f.writelines(f'Количество строк в файле - {len(value)}\n')
                f.writelines(value)
                f.writelines('\n')