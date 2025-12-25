code = """import json, pandas as pd

books_path = var_call_VNy7hyXHHbjqJtgMRFPWj5Gl
with open(books_path, 'r') as f:
    books = json.load(f)
reviews_path = var_call_p4rv91vENer3wyFVMKHGwZPu
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

reviews_df['rating'] = reviews_df['rating'].astype(float)

import re

def extract_year(details):
    if not isinstance(details, str):
        return None
    m = re.search(r"(19|20)\d{2}", details)
    return int(m.group(0)) if m else None

books_df['year'] = books_df['details'].apply(extract_year)
books_df = books_df.dropna(subset=['year'])
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10) * 10

merged = reviews_df.merge(books_df[['book_id','decade']], left_on='purchase_id', right_on='book_id', how='inner')

agg = merged.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('book_id','nunique')).reset_index()
agg = agg[agg['distinct_books'] >= 10]

if agg.empty:
    result = None
else:
    best = agg.sort_values('avg_rating', ascending=False).iloc[0]
    result = {'decade': int(best['decade']), 'average_rating': float(best['avg_rating']), 'distinct_books': int(best['distinct_books'])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VNy7hyXHHbjqJtgMRFPWj5Gl': 'file_storage/call_VNy7hyXHHbjqJtgMRFPWj5Gl.json', 'var_call_GOAIcHsGqfMJFyuFsfcaZkTh': ['books_info'], 'var_call_XQKg6kynY7hlZ8CITmOdcqlw': ['review'], 'var_call_p4rv91vENer3wyFVMKHGwZPu': 'file_storage/call_p4rv91vENer3wyFVMKHGwZPu.json'}

exec(code, env_args)
