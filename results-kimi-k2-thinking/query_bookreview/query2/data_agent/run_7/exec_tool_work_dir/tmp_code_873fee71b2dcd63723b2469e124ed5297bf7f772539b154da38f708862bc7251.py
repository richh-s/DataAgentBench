code = """import json

# Get the file path from storage
books_file_path = locals()['var_functions.query_db:2']

# Read the books data
with open(books_file_path, 'r') as f:
    books_data = json.load(f)

# Filter for Literature & Fiction category and extract book_ids
lit_fiction_book_ids = []
for book in books_data:
    categories_str = book.get('categories', '')
    if 'Literature & Fiction' in categories_str:
        lit_fiction_book_ids.append(book['book_id'])

print('__RESULT__:')
print(json.dumps({
    'count': len(lit_fiction_book_ids),
    'book_ids': lit_fiction_book_ids
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
