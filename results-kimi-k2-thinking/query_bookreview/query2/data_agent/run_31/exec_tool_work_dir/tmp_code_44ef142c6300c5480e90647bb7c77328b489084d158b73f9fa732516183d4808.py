code = """import json

# Get the file path from the local variables
file_path = locals()['var_functions.query_db:4']

# Read the full result from the file
with open(file_path, 'r') as f:
    literature_books = json.load(f)

# Count the books
book_count = len(literature_books)
print('Found ' + str(book_count) + ' books in Literature & Fiction category')

# Show sample books
print('Sample books:')
for i in range(min(3, book_count)):
    book = literature_books[i]
    print('  ' + str(i+1) + '. ' + book['title'] + ' (book_id: ' + book['book_id'] + ')')

# Create a list of book_ids to query reviews
book_ids = [book['book_id'] for book in literature_books]
print('\nTotal book_ids to check: ' + str(len(book_ids)))
print('Sample book_ids: ' + str(book_ids[:5]))

# Output the data
result = {'book_ids': book_ids}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
