code = """import json

# Read the full result from the file
file_path = var_functions.query_db:4
with open(file_path, 'r') as f:
    literature_books = json.load(f)

print(f"Found {len(literature_books)} books in Literature & Fiction category")
print("Sample books:")
for i, book in enumerate(literature_books[:3]):
    print(f"  {i+1}. {book['title']} (book_id: {book['book_id']})")

print(f"\nFirst book structure:")
print(json.dumps(literature_books[0], indent=2)[:2000] + "...")

# Create a list of book_ids to query reviews
book_ids = [book['book_id'] for book in literature_books]
print(f"\nTotal book_ids to check: {len(book_ids)}")
print(f"Sample book_ids: {book_ids[:5]}")

# Output the data for next step
print("__RESULT__:")
print(json.dumps({"book_ids": book_ids, "literature_books": literature_books}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
