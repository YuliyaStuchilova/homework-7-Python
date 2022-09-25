from book import book


info = book()


def export_file():
    with open('export.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{info[0]} {info[1]} {info[2]} - {info[3]}\n')
