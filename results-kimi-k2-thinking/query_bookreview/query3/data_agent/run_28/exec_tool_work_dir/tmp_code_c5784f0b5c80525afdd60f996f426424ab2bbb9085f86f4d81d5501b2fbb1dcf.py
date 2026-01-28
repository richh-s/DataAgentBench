code = """import json
import pandas as pd
import ast

# Load the books data
books_file = var_functions.query_db:0
books_data = json.loads(open(books_file).read())
books_df = pd.DataFrame(books_data)

# Check the structure
print("Books columns:", books_df.columns.tolist())
print("\nFirst few rows:")
print(books_df[['title', 'book_id', 'categories']].head())

# Look for Children's Books in categories
children_books = []
for idx, row in books_df.iterrows():
    try:
        categories = ast.literal_eval(row['categories'])
        if any("Children" in str(cat) for cat in categories):
            children_books.append({
                'book_id': row['book_id'],
                'title': row['title'],
                'categories': categories
            })
    except:
        continue

print(f"\nFound {len(children_books)} children's books")
print("\nSample children's books:")
for b in children_books[:10]:
    print(f"- {b['title']} ({b['book_id']})")
    print(f"  Categories: {b['categories']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
