code = """import json

# Load the full result from the previous query using the storage key
result_file = locals()['var_functions.query_db:5']
with open(result_file, 'r') as f:
    books_data = json.load(f)

# Get basic info
print('Number of books in Literature & Fiction:', len(books_data))

# Extract book_ids for querying the review database
book_ids = [book['book_id'] for book in books_data]
print('Total book_ids extracted:', len(book_ids))
print('First few book_ids:', book_ids[:5])"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
