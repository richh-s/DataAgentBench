code = """import json
import pandas as pd
import ast

# Load the query results from storage files
with open(var_call_bHBrjS8YJsf514lKhSkkuRqq, 'r') as f:
    reviews = json.load(f)
with open(var_call_5holZWswYIxifNcIIiVoGuuJ, 'r') as f:
    books = json.load(f)

# Create DataFrames
rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

# Clean reviews: ensure rating numeric and filter review_time already >=2020 from query
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
# Map purchase_id -> book_id by replacing prefix
rev_df['book_id'] = rev_df['purchase_id'].str.replace('purchaseid_', 'bookid_', regex=False)

# Aggregate average rating and count per book_id
agg = rev_df.groupby('book_id').agg(average_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()

# Clean books categories: parse string representation into actual list when possible
def parse_categories(cat_str):
    if not cat_str:
        return []
    try:
        parsed = ast.literal_eval(cat_str)
        if isinstance(parsed, list):
            return parsed
        else:
            return []
    except Exception:
        # fallback: treat as raw string and check
        return [cat_str]

books_df['categories_parsed'] = books_df['categories'].apply(parse_categories)

# Filter books that have "Children's Books" in categories
books_df['is_children'] = books_df['categories_parsed'].apply(lambda lst: "Children's Books" in lst)
children_books = books_df[books_df['is_children']]

# Join aggregated ratings with children books
merged = pd.merge(children_books, agg, on='book_id', how='inner')

# Filter average_rating >= 4.5
result_df = merged[merged['average_rating'] >= 4.5].copy()

# Prepare output records
result_df['average_rating'] = result_df['average_rating'].round(3)
output = []
for _, row in result_df.sort_values(['average_rating', 'review_count'], ascending=[False, False]).iterrows():
    output.append({
        'book_id': row['book_id'],
        'title': row['title'],
        'average_rating': float(row['average_rating']),
        'review_count': int(row['review_count']),
        'categories': row['categories_parsed']
    })

# Print according to required format as JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_OvMrDQsQdqzWJeaRFfXYthdn': ['review'], 'var_call_q3YsWqSLv4a88dUK8Jv3Rc6J': ['books_info'], 'var_call_bHBrjS8YJsf514lKhSkkuRqq': 'file_storage/call_bHBrjS8YJsf514lKhSkkuRqq.json', 'var_call_5holZWswYIxifNcIIiVoGuuJ': 'file_storage/call_5holZWswYIxifNcIIiVoGuuJ.json'}

exec(code, env_args)
