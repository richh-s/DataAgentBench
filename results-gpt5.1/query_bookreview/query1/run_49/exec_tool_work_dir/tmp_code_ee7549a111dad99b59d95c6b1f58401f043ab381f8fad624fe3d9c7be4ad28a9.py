code = """import json, re, pandas as pd

with open(var_call_bSPqq6wJ4Cavp1Y3brdNCRhh, 'r') as f:
    books = json.load(f)

reviews = var_call_gb2F2vsaEGOWSWXzLtRvzPrv

# Ensure reviews is a list of dicts
if isinstance(reviews, dict):
    reviews = [reviews]

year_pattern = re.compile(r'(19\d{2}|20\d{2})')

book_years = {}
for row in books:
    details = row.get('details') or ''
    years = [int(y) for y in year_pattern.findall(details)]
    year = min(years) if years else None
    if year:
        decade = int(year // 10 * 10)
        book_years[row['book_id']] = decade

rev_df = pd.DataFrame(list(reviews))
rev_df['rating'] = rev_df['rating'].astype(float)
rev_df['decade'] = rev_df['purchase_id'].map(book_years)
rev_df = rev_df.dropna(subset=['decade'])

book_avg = rev_df.groupby(['purchase_id','decade'])['rating'].mean().reset_index()

decade_stats = book_avg.groupby('decade').agg(
    distinct_books=('purchase_id','nunique'),
    avg_rating=('rating','mean')
).reset_index()

eligible = decade_stats[decade_stats['distinct_books'] >= 10]

if eligible.empty:
    result = None
else:
    best = eligible.sort_values(['avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {
        'decade': int(best['decade']),
        'average_rating': float(best['avg_rating']),
        'distinct_books': int(best['distinct_books'])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_bSPqq6wJ4Cavp1Y3brdNCRhh': 'file_storage/call_bSPqq6wJ4Cavp1Y3brdNCRhh.json', 'var_call_VqPFUDO7mxMhfHDB3mtnrEZR': ['books_info'], 'var_call_fnlaCJJsfM9DgceTkvaytbNx': ['review'], 'var_call_gb2F2vsaEGOWSWXzLtRvzPrv': 'file_storage/call_gb2F2vsaEGOWSWXzLtRvzPrv.json'}

exec(code, env_args)
