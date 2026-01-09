code = """import json, re, pandas as pd

# load reviews
path_rev = var_call_NOfxB2jBeKOX9PcUPoblRljt
with open(path_rev,'r') as f:
    reviews = json.load(f)
rev = pd.DataFrame(reviews)
rev['rating'] = pd.to_numeric(rev['rating'], errors='coerce')
rev = rev.dropna(subset=['purchase_id','rating'])

# load book details rows
path_books = var_call_MhfIbf4ZMkdgtOTrr3gRlShs
with open(path_books,'r') as f:
    books = json.load(f)
bk = pd.DataFrame(books)

# extract 4-digit year from details (prefer publication date / released on)
year_pat = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(text):
    if not isinstance(text,str):
        return None
    # prioritize phrases
    candidates = []
    for m in re.finditer(r'(?:Publication date|Published|released on|Release date|published on|first edition on)\D{0,40}?(18\d{2}|19\d{2}|20\d{2})', text, flags=re.IGNORECASE):
        candidates.append(int(m.group(1)))
    if candidates:
        return candidates[0]
    m = year_pat.search(text)
    return int(m.group(1)) if m else None

bk['year'] = bk['details'].map(extract_year)
bk = bk.dropna(subset=['book_id','year'])
bk['year'] = bk['year'].astype(int)
# restrict plausible publication years
bk = bk[(bk['year']>=1800) & (bk['year']<=2026)]

# map purchase_id_* to bookid_* by numeric suffix
suffix_pat = re.compile(r'_(\d+)$')

def suffix_num(s):
    if not isinstance(s,str):
        return None
    m = suffix_pat.search(s)
    return int(m.group(1)) if m else None

rev['num'] = rev['purchase_id'].map(suffix_num)
bk['num'] = bk['book_id'].map(suffix_num)

merged = rev.merge(bk[['num','year']], on='num', how='inner')
merged['decade_start'] = (merged['year']//10)*10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

# decade must have at least 10 distinct books (num) with at least one rating
books_per_decade = merged.groupby('decade')['num'].nunique().rename('distinct_books')
avg_rating = merged.groupby('decade')['rating'].mean().rename('avg_rating')
summary = pd.concat([books_per_decade, avg_rating], axis=1).reset_index()
summary = summary[summary['distinct_books']>=10]
summary = summary.sort_values(['avg_rating','distinct_books'], ascending=[False,False])

top_decade = summary.iloc[0]['decade'] if len(summary)>0 else None
print('__RESULT__:')
print(json.dumps({'decade': top_decade}))"""

env_args = {'var_call_MhfIbf4ZMkdgtOTrr3gRlShs': 'file_storage/call_MhfIbf4ZMkdgtOTrr3gRlShs.json', 'var_call_t5OJYjkabLo4LcXA7qV6qG6q': ['review'], 'var_call_NOfxB2jBeKOX9PcUPoblRljt': 'file_storage/call_NOfxB2jBeKOX9PcUPoblRljt.json'}

exec(code, env_args)
