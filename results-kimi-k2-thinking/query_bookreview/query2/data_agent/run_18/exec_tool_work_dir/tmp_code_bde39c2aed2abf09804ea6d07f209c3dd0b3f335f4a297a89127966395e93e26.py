code = """import json
import pandas as pd

books_file = locals()['var_functions.query_db:20']
with open(books_file, 'r') as f:
    books_lit_fiction = json.load(f)

reviews_file = locals()['var_functions.query_db:6']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

books_df = pd.DataFrame(books_lit_fiction)
reviews_df = pd.DataFrame(reviews_data)

print('English Literature & Fiction books count:', len(books_df))

reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
avg_ratings = reviews_df.groupby('purchase_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['purchase_id', 'avg_rating', 'review_count']

perfect_ratings = avg_ratings[avg_ratings['avg_rating'] == 5.0]
print('Perfect rating books count:', len(perfect_ratings))
print('Sample perfect rating IDs:', perfect_ratings['purchase_id'].head(5).tolist())
print('Sample literature fiction book IDs:', books_df['book_id'].head(5).tolist())

# Check if there's any overlap in the numeric parts
perfect_numbers = [pid.replace('purchaseid_', '') for pid in perfect_ratings['purchase_id']]
book_numbers = [bid.replace('bookid_', '') for bid in books_df['book_id']]

common_numbers = set(perfect_numbers) & set(book_numbers)
print('Common numeric IDs found:', len(common_numbers))

# Get the actual matching books
matching_book_ids = ['bookid_' + num for num in common_numbers]
result_books = books_df[books_df['book_id'].isin(matching_book_ids)]

print('Final matching books:', len(result_books))

output = []
for _, row in result_books.iterrows():
    # Parse author info
    author_str = row['author'] if row['author'] else 'Unknown'
    author_name = 'Unknown'
    if author_str != 'None' and author_str:
        try:
            import ast
            author_dict = ast.literal_eval(author_str)
            if isinstance(author_dict, dict) and 'name' in author_dict:
                author_name = author_dict['name']
        except:
            author_name = str(author_str).split(' (')[0]
    
    output.append({
        'title': row['title'],
        'author': author_name,
        'subtitle': row.get('subtitle', ''),
        'book_id': row['book_id']
    })

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': [], 'var_functions.query_db:18': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_44', 'title': 'Reptilian', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
