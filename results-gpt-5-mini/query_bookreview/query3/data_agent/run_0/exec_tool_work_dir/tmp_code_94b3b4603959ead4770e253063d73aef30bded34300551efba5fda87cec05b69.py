code = """import json
import pandas as pd

# Load data from the stored JSON files produced by previous queries
with open(var_call_AuX1aFHkD4dCkYT9y6BYWVV8, 'r') as f:
    reviews = json.load(f)
with open(var_call_Pgy9mOhaUH9JF6OLM4DeGk22, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Normalize and filter reviews from 2020 onwards
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
df_rev['review_time'] = pd.to_datetime(df_rev['review_time'], errors='coerce')
filtered = df_rev[df_rev['review_time'] >= pd.to_datetime('2020-01-01')]

# Group by purchase_id and compute average rating and count
grp = (
    filtered.groupby('purchase_id', dropna=False)
    .agg(avg_rating=('rating', 'mean'), review_count=('rating', 'count'))
    .reset_index()
)

# Map purchase_id -> book_id by replacing prefix
grp['book_id'] = grp['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Filter books that are in "Children's Books" category
# categories field is a string representation of a list; check for substring
children_books = df_books[df_books['categories'].str.contains("Children's Books", na=False)]

# Merge grouped review stats with children books
merged = grp.merge(children_books, on='book_id', how='inner')

# Filter for average rating >= 4.5
merged = merged[merged['avg_rating'] >= 4.5]

# Prepare result list sorted by avg_rating desc and review_count desc
merged['avg_rating'] = merged['avg_rating'].round(3)
merged = merged.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False])

result_list = []
for _, row in merged.iterrows():
    result_list.append({
        'book_id': row['book_id'],
        'title': row.get('title', None),
        'avg_rating': float(row['avg_rating']) if pd.notna(row['avg_rating']) else None,
        'review_count': int(row['review_count'])
    })

# Print result in the required format as a JSON string
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_FXoCbIUbjnpNQlzdGLH7WpO2': ['review'], 'var_call_AuX1aFHkD4dCkYT9y6BYWVV8': 'file_storage/call_AuX1aFHkD4dCkYT9y6BYWVV8.json', 'var_call_5hwb6Bq10ZWyxBYEoch6hjy5': ['books_info'], 'var_call_Pgy9mOhaUH9JF6OLM4DeGk22': 'file_storage/call_Pgy9mOhaUH9JF6OLM4DeGk22.json'}

exec(code, env_args)
