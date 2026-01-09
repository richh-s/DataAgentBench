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

year_pat = re.compile(r'\b(1[5-9]\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    ys = [int(m.group(1)) for m in year_pat.finditer(s)]
    if not ys:
        return None
    cand = [yy for yy in ys if 1800 <= yy <= 2029]
    if not cand:
        return None
    return min(cand)

books_df['year'] = books_df['details'].map(extract_year)
books_df = books_df.dropna(subset=['year','book_id'])

suffix_pat = re.compile(r'_(\d+)\b')

def suffix_num(x):
    if not isinstance(x, str):
        return None
    m = suffix_pat.search(x)
    return int(m.group(1)) if m else None

books_df['sid'] = books_df['book_id'].map(suffix_num)
rev_df['sid'] = rev_df['purchase_id'].map(suffix_num)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

merged = rev_df.dropna(subset=['sid','rating']).merge(books_df.dropna(subset=['sid'])[['sid','year']], on='sid', how='inner')
merged['decade_start'] = (merged['year'].astype(int)//10)*10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

agg = merged.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('sid','nunique'))
agg10 = agg[agg['distinct_books']>=10].sort_values(['avg_rating','distinct_books'], ascending=[False, False])

decade = None
if len(agg10):
    decade = agg10.index[0]

print('__RESULT__:')
print(json.dumps({'decade': decade}))"""

env_args = {'var_call_lVdbHjDu4Q5P2EL8WqXV2oI8': 'file_storage/call_lVdbHjDu4Q5P2EL8WqXV2oI8.json', 'var_call_7qqPYSGJHmSMyCRr2XWCce4R': ['review'], 'var_call_0tRRXp3IBCXrw9TVYTtuT6ED': 'file_storage/call_0tRRXp3IBCXrw9TVYTtuT6ED.json', 'var_call_6ZdhwmT3hWz1qLaCV5BPzyvD': {'decade': None}, 'var_call_jayhWvOp75lyEhzbaPCcOpa5': 'file_storage/call_jayhWvOp75lyEhzbaPCcOpa5.json'}

exec(code, env_args)
