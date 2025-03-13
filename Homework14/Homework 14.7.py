import yaml

# Чтение YAML и добавление новых книг
def add_book_to_yaml(yaml_file, new_book):
    with open(yaml_file, 'r') as f:
        books = yaml.load(f, Loader=yaml.FullLoader)
    books.append(new_book)
    with open(yaml_file, 'w') as f:
        yaml.dump(books, f)

new_book = {
    'title': 'Новая книга',
    'author': 'Новый автор',
    'year': 2025
}

add_book_to_yaml('books.yaml', new_book)
print("Книга добавлена!")
