code = """import json
import pandas as pd

books_file = locals()['var_functions.query_db:2']
with open(books_file, 'r') as f:
    books_data = json.load(f)

reviews_file = locals()['var_functions.query_db:6']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

print('Books shape:', books_df.shape)
print('Reviews shape:', reviews_df.shape)
print('Books columns:', list(books_df.columns))
print('Reviews columns:', list(reviews_df.columns))

sample_cat = books_df['categories'].iloc[0]
print('Categories sample type:', type(sample_cat))
print('Categories sample value:', str(sample_cat)[:200])

# Now find Literature & Fiction books in English
lit_fiction_books = []
for _, row in books_df.iterrows():
    categories_str = str(row['categories'])
    details_str = str(row['details'])
    if 'Literature & Fiction' in categories_str and 'English' in details_str:
        lit_fiction_books.append(row['book_id'])

print('Found Literature & Fiction books in English:', len(lit_fiction_books))
print('Sample book IDs:', lit_fiction_books[:10])

# Calculate average ratings for these books
reviews_df['rating'] = reviews_df['rating'].astype(float)
avg_ratings = reviews_df.groupby('purchase_id')['rating'].mean().reset_index()
perfect_books = avg_ratings[avg_ratings['rating'] == 5.0]
print('Books with perfect 5.0 ratings:', len(perfect_books))

# Now we need to match book_id with purchase_id
# Based on the hint, these should refer to same books but different naming
# Let's check if IDs match pattern
print('Sample book IDs format:', lit_fiction_books[:5])
print('Sample purchase IDs format:', reviews_df['purchase_id'].unique()[:5])

result = []
for book_id in lit_fiction_books:
    # Try to match book_id with purchase_id
    purchase_id = None
    if book_id.startswith('bookid_'):
        num = book_id.replace('bookid_', '')
        purchase_id = f'purchaseid_{num}'
    
    if purchase_id in perfect_books['purchase_id'].values:
        # Find the book details
        book_info = books_df[books_df['book_id'] == book_id]
        if not book_info.empty:
            result.append({
                'title': book_info.iloc[0]['title'],
                'subtitle': book_info.iloc[0]['subtitle'],
                'author': book_info.iloc[0]['author'],
                'book_id': book_id,
                'average_rating': 5.0
            })

print('Final matching books:', len(result))
for book in result:
    print(book)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
