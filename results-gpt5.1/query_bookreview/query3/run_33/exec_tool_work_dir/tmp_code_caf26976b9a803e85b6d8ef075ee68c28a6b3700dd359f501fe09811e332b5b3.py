code = """import json, pandas as pd
# Load full books_info and review data from files
with open(var_call_f047np2BRirc2ypKPuuY4Cn4, 'r') as f:
    books = json.load(f)
with open(var_call_lkKOZTECyWFLL4QdZeTk3Ler, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Filter to Children's Books via substring in categories string
child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Aggregate reviews by purchase_id
reviews_df['rating'] = reviews_df['rating'].astype(float)
agg = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})

# Fuzzy join on id pattern: map purchaseid_X to bookid_X based on shared suffix after underscore
def purchase_to_book(pid):
    if isinstance(pid, str) and '_' in pid:
        suffix = pid.split('_', 1)[1]
        return 'bookid_' + suffix
    return None

agg['book_id'] = agg['purchase_id'].map(purchase_to_book)

# Join with children's books
merged = pd.merge(child_books, agg, on='book_id', how='inner')

# Filter avg_rating >= 4.5
result_df = merged[merged['avg_rating'] >= 4.5][['book_id', 'title', 'avg_rating']].drop_duplicates().sort_values('avg_rating', ascending=False)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_f047np2BRirc2ypKPuuY4Cn4': 'file_storage/call_f047np2BRirc2ypKPuuY4Cn4.json', 'var_call_xpMddGwcd0wBoTgbZEk7IZEA': ['review'], 'var_call_lkKOZTECyWFLL4QdZeTk3Ler': 'file_storage/call_lkKOZTECyWFLL4QdZeTk3Ler.json'}

exec(code, env_args)
