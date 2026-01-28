code = """import json

# Get the file path
file_path = locals()['var_functions.query_db:4']

# Read the full result from the file
with open(file_path, 'r') as f:
    literature_books = json.load(f)

print("Found " + str(len(literature_books)) + " books in Literature & Fiction category")
print("Sample books:")
for i, book in enumerate(literature_books[:3]):
    title = book['title']
    book_id = book['book_id']
    print("  " + str(i+1) + ". " + title + " (book_id: " + book_id + ")")

# Create a list of book_ids to query reviews
book_ids = [book['book_id'] for book in literature_books]
print("\nTotal book_ids to check: " + str(len(book_ids)))
print("Sample book_ids: " + str(book_ids[:5]))

# Output the data for next step
result = {"book_ids": book_ids, "literature_books_count": len(literature_books)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
