code = """import json

# Load the full result from the previous query
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    books_data = json.load(f)

# Print the first few entries to understand the structure
print('Number of books in Literature & Fiction:', len(books_data))
print('\nFirst book entry:')
print(json.dumps(books_data[0], indent=2))

# Extract book_ids for querying the review database
book_ids = [book['book_id'] for book in books_data]
print(f'\nTotal book_ids extracted: {len(book_ids)}')"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
