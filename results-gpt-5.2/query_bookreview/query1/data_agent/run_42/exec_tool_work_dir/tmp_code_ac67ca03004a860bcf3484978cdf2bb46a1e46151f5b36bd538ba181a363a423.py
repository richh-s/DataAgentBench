code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

books = load(var_call_TUqUb5kfiIbZ4bLNj4K0vPMp)
revs = load(var_call_3wQsLj7zi5L6Eu8eJG9vyEgs)

books_df = pd.DataFrame(books)
revs_df = pd.DataFrame(revs)

# parse year from details text
pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(s):
    if not isinstance(s, str):
        return None
    # prioritize phrases like 'on <Month> <day>, <year>' and 'released on' etc by taking last year in string
    yrs = [int(m.group(1)) for m in pat.finditer(s)]
    if not yrs:
        return None
    # choose last plausible year between 1800 and 2026
    for y in reversed(yrs):
        if 1800 <= y <= 2026:
            return y
    return None

books_df['year'] = books_df['details'].map(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10) * 10

# normalize ids for fuzzy join by extracting trailing digits
id_pat = re.compile(r'(\d+)')

def norm_id(x):
    if x is None:
        return None
    m = id_pat.findall(str(x))
    return m[-1] if m else None

books_df['norm'] = books_df['book_id'].map(norm_id)
revs_df['norm'] = revs_df['purchase_id'].map(norm_id)

# ratings to float
revs_df['rating'] = pd.to_numeric(revs_df['rating'], errors='coerce')
revs_df = revs_df.dropna(subset=['rating','norm'])

merged = revs_df.merge(books_df[['norm','decade']], on='norm', how='inner')

# count distinct books with at least one rating per decade
books_per_decade = merged.groupby('decade')['norm'].nunique().rename('distinct_books')
avg_rating = merged.groupby('decade')['rating'].mean().rename('avg_rating')
summary = pd.concat([books_per_decade, avg_rating], axis=1).dropna().reset_index()
summary = summary[summary['distinct_books'] >= 10]

if summary.empty:
    ans = None
else:
    best = summary.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
    ans = f"{int(best['decade'])}s"

print('__RESULT__:')
print(json.dumps({'decade': ans}))"""

env_args = {'var_call_TUqUb5kfiIbZ4bLNj4K0vPMp': 'file_storage/call_TUqUb5kfiIbZ4bLNj4K0vPMp.json', 'var_call_CCm9IHh5WGNl49rFSAinmGgH': ['review'], 'var_call_3wQsLj7zi5L6Eu8eJG9vyEgs': 'file_storage/call_3wQsLj7zi5L6Eu8eJG9vyEgs.json'}

exec(code, env_args)
