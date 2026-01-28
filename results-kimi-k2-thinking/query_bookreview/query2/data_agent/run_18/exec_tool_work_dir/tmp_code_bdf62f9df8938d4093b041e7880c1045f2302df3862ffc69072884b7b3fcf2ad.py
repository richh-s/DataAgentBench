code = """import json
import pandas as pd

# Load literature & fiction books in English
books_file = locals()['var_functions.query_db:32']
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Load all reviews
reviews_file = locals()['var_functions.query_db:6']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Create DataFrames
books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

print('Total English Literature & Fiction books:', len(books_df))
print('Total reviews:', len(reviews_df))

# Convert rating to numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Calculate average rating for each purchase_id
avg_ratings = reviews_df.groupby('purchase_id')['rating'].mean().reset_index()
avg_ratings.columns = ['purchase_id', 'avg_rating']

# Get books with perfect 5.0 rating
perfect_ratings = avg_ratings[avg_ratings['avg_rating'] == 5.0]
print('Books with perfect 5.0 rating:', len(perfect_ratings))

# Create mapping: bookid_X -> purchaseid_X
books_df['purchase_id'] = books_df['book_id'].str.replace('bookid_', 'purchaseid_')

# Merge books with their average ratings
merged = pd.merge(books_df, perfect_ratings, on='purchase_id', how='inner')
print('Matching books after merge:', len(merged))

# Format results
results = []
for _, row in merged.iterrows():
    # Parse author from JSON string
    author_info = row['author']
    author_name = 'Unknown'
    if pd.notna(author_info) and author_info != 'None':
        try:
            import ast
            author_dict = ast.literal_eval(author_info)
            if isinstance(author_dict, dict) and 'name' in author_dict:
                author_name = author_dict['name']
        except:
            author_name = str(author_info)
    
    results.append({
        'title': row['title'],
        'author': author_name,
        'subtitle': row.get('subtitle', ''),
        'book_id': row['book_id'],
        'categories': row['categories'],
        'average_rating': 5.0
    })

print('Final results:', len(results))
for book in results:
    print(f"Title: {book['title']} | Author: {book['author']}")

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': [], 'var_functions.query_db:18': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_44', 'title': 'Reptilian', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
