code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

books = load_json_maybe(var_call_jayhWvOp75lyEhzbaPCcOpa5)
reviews = load_json_maybe(var_call_0tRRXp3IBCXrw9TVYTtuT6ED)

books_df = pd.DataFrame(books)
rev_df = pd.DataFrame(reviews)

# parse year
pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')
books_df['year'] = books_df['details'].map(lambda s: int(min([int(m.group(1)) for m in pat.finditer(s)]) ) if isinstance(s,str) and pat.search(s) else None)
books_df = books_df.dropna(subset=['year'])

# direct join on id string (purchase_id == book_id)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
merged = rev_df.dropna(subset=['rating']).merge(books_df[['book_id','year']], left_on='purchase_id', right_on='book_id', how='inner')

merged['decade'] = ((merged['year']//10)*10).astype(int).astype(str) + 's'
agg = merged.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('book_id','nunique'))
agg10 = agg[agg['distinct_books']>=10].sort_values('avg_rating', ascending=False)

print('__RESULT__:')
print(json.dumps({'n_joined': int(len(merged)), 'n_books_joined': int(merged['book_id'].nunique()) if len(merged) else 0, 'agg10_rows': int(len(agg10))}))"""

env_args = {'var_call_lVdbHjDu4Q5P2EL8WqXV2oI8': 'file_storage/call_lVdbHjDu4Q5P2EL8WqXV2oI8.json', 'var_call_7qqPYSGJHmSMyCRr2XWCce4R': ['review'], 'var_call_0tRRXp3IBCXrw9TVYTtuT6ED': 'file_storage/call_0tRRXp3IBCXrw9TVYTtuT6ED.json', 'var_call_6ZdhwmT3hWz1qLaCV5BPzyvD': {'decade': None}, 'var_call_jayhWvOp75lyEhzbaPCcOpa5': 'file_storage/call_jayhWvOp75lyEhzbaPCcOpa5.json', 'var_call_Zy2yKWdQEm5pQt2pQYd8zI2o': {'decade': None}}

exec(code, env_args)
