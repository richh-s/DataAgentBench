code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

reviews = load_records(var_call_TXYMBMUeBXaGZnz9cFpzW5Vj)
books_details = load_records(var_call_90Jin4oEqKhCARnyLR9BtOus)

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['purchase_id','rating'])

bd_df = pd.DataFrame(books_details)

# Extract year from details text
pattern = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(txt):
    if txt is None:
        return None
    m = pattern.findall(str(txt))
    if not m:
        return None
    # use earliest plausible publication year (min)
    years = [int(y) for y in m]
    # filter to 1450-2026 sanity
    years = [y for y in years if 1450 <= y <= 2026]
    return min(years) if years else None

bd_df['pub_year'] = bd_df['details'].map(extract_year)
bd_df = bd_df.dropna(subset=['book_id','pub_year'])
bd_df['pub_year'] = bd_df['pub_year'].astype(int)

# Fuzzy join: purchaseid_XXX -> bookid_XXX (based on numeric suffix)
rev_df['suffix'] = rev_df['purchase_id'].astype(str).str.extract(r'(\d+)$')[0]
bd_df['suffix'] = bd_df['book_id'].astype(str).str.extract(r'(\d+)$')[0]
rev_df = rev_df.dropna(subset=['suffix'])
bd_df = bd_df.dropna(subset=['suffix'])

merged = rev_df.merge(bd_df[['suffix','pub_year']], on='suffix', how='inner')
merged['decade_start'] = (merged['pub_year']//10)*10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# Count distinct books rated per decade
books_per_decade = merged.groupby('decade')['suffix'].nunique().rename('distinct_books')
avg_rating = merged.groupby('decade')['rating'].mean().rename('avg_rating')
summary = pd.concat([books_per_decade, avg_rating], axis=1).reset_index()
summary = summary[summary['distinct_books']>=10]
summary = summary.sort_values(['avg_rating','distinct_books'], ascending=[False, False])

best_decade = None
if len(summary):
    best_decade = summary.iloc[0]['decade']

print('__RESULT__:')
print(json.dumps({'best_decade': best_decade}))"""

env_args = {'var_call_90Jin4oEqKhCARnyLR9BtOus': 'file_storage/call_90Jin4oEqKhCARnyLR9BtOus.json', 'var_call_X7Z1jaIy8eSEmP6vvYzxzCO5': 'file_storage/call_X7Z1jaIy8eSEmP6vvYzxzCO5.json', 'var_call_sOIMCXdumtYDMoAZymq3AyYJ': ['review'], 'var_call_TXYMBMUeBXaGZnz9cFpzW5Vj': 'file_storage/call_TXYMBMUeBXaGZnz9cFpzW5Vj.json'}

exec(code, env_args)
