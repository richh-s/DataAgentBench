code = """import json
import pandas as pd

# Load query results from files
with open(var_call_Vpat9FV8YBoIyNF4NRCsYd9h, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_fDeT3L4axcQOaQI7MryLaf3g, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Clean and prepare reviews
# Convert rating to float
df_reviews['rating'] = df_reviews['rating'].astype(float)
# Map purchase_id to book_id by replacing prefix
df_reviews['book_id'] = df_reviews['purchase_id'].str.replace('purchaseid_', 'bookid_')

# Aggregate average rating and count per book_id
agg = df_reviews.groupby('book_id').agg(avg_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()

# Prepare books categories: parse stringified list
def parse_categories(cat_str):
    try:
        return json.loads(cat_str)
    except Exception:
        return []

df_books['categories_parsed'] = df_books['categories'].apply(parse_categories)

# Merge
merged = agg.merge(df_books, on='book_id', how='left')

# Filter for Children's Books in categories and avg_rating >= 4.5
def has_childrens(categories):
    if not categories:
        return False
    return any((c.strip() == "Children's Books") for c in categories)

merged['is_childrens'] = merged['categories_parsed'].apply(has_childrens)
filtered = merged[(merged['is_childrens']) & (merged['avg_rating'] >= 4.5)].copy()

# Prepare output
output = []
for _, row in filtered.sort_values(by=['avg_rating','review_count'], ascending=[False, False]).iterrows():
    output.append({
        'book_id': row['book_id'],
        'title': row.get('title'),
        'categories': row['categories_parsed'],
        'avg_rating': round(float(row['avg_rating']), 3),
        'review_count': int(row['review_count'])
    })

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_GwxX3oQPWrS3exZ85hLEAXnn': ['review'], 'var_call_oWbNdZk36K6fLi0SPBLXw0IP': ['books_info'], 'var_call_Vpat9FV8YBoIyNF4NRCsYd9h': 'file_storage/call_Vpat9FV8YBoIyNF4NRCsYd9h.json', 'var_call_fDeT3L4axcQOaQI7MryLaf3g': 'file_storage/call_fDeT3L4axcQOaQI7MryLaf3g.json'}

exec(code, env_args)
