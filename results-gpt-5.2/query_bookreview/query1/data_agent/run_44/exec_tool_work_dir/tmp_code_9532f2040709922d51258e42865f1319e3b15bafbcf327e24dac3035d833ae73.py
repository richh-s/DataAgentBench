code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_Tn6sOjSIuNuAoIUPUdbx0UfD)
reviews = load_records(var_call_UMyZY4nMqBS4EtIh23S7iB3Z)

books_df = pd.DataFrame(books)
rev_df = pd.DataFrame(reviews)

# extract publication year from details
pat_year = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    # prioritize near keywords
    kws = ['published', 'publication', 'release', 'released', 'first edition', 'edition']
    s_low = s.lower()
    idxs = [s_low.find(k) for k in kws if s_low.find(k) != -1]
    if idxs:
        start = max(min(idxs)-50, 0)
        end = min(min(idxs)+150, len(s))
        sub = s[start:end]
        m = pat_year.search(sub)
        if m:
            return int(m.group(1))
    m = pat_year.search(s)
    return int(m.group(1)) if m else None

books_df['year'] = books_df['details'].map(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year']//10)*10

# reviews: coerce rating to float
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['rating','purchase_id'])

# fuzzy join: normalize ids by extracting numeric suffix
id_num = re.compile(r'(\d+)')
books_df['id_num'] = books_df['book_id'].astype(str).str.extract(id_num, expand=False)
rev_df['id_num'] = rev_df['purchase_id'].astype(str).str.extract(id_num, expand=False)

joined = rev_df.merge(books_df[['book_id','decade','id_num']], on='id_num', how='inner')
# distinct books that have been rated per decade
rated_books = joined.drop_duplicates(subset=['decade','book_id'])
counts = rated_books.groupby('decade')['book_id'].nunique().rename('n_books')
# average rating per decade across all reviews
avg = joined.groupby('decade')['rating'].mean().rename('avg_rating')
summary = pd.concat([counts, avg], axis=1).dropna()
summary = summary[summary['n_books']>=10]
if summary.empty:
    result = {'decade': None}
else:
    best_decade = summary.sort_values(['avg_rating','n_books'], ascending=[False, False]).index[0]
    result = {'decade': f"{int(best_decade)}s"}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Tn6sOjSIuNuAoIUPUdbx0UfD': 'file_storage/call_Tn6sOjSIuNuAoIUPUdbx0UfD.json', 'var_call_byjZYqedbL1LCsUpBXYp6MC8': ['review'], 'var_call_UMyZY4nMqBS4EtIh23S7iB3Z': 'file_storage/call_UMyZY4nMqBS4EtIh23S7iB3Z.json'}

exec(code, env_args)
