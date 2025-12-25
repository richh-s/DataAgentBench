code = """import json, pandas as pd

books_file = var_call_VDTddWxCKeLtlMTu2Uzrn7nF
reviews_file = var_call_kuRlHoxuw3XhG6Mps4h2ytF5

with open(books_file, 'r') as f:
    books = json.load(f)
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)[['book_id','details']]
reviews_df = pd.DataFrame(reviews)[['purchase_id','rating']]

# Extract year from details text
import re

def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'(19|20)\d{2}', text)
    return int(m.group(0)) if m else None

books_df['year'] = books_df['details'].apply(extract_year)

# merge on purchase_id == book_id
merged = reviews_df.merge(books_df, left_on='purchase_id', right_on='book_id', how='left')

merged = merged.dropna(subset=['year'])
merged['rating'] = pd.to_numeric(merged['rating'], errors='coerce')
merged = merged.dropna(subset=['rating'])

# compute per-book average rating
book_avg = merged.groupby(['book_id','year'])['rating'].mean().reset_index()

# decade
book_avg['decade'] = (book_avg['year']//10)*10

# count distinct books per decade
decade_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='book_count')
valid_decades = decade_counts[decade_counts['book_count']>=10]['decade']

valid_book_avg = book_avg[book_avg['decade'].isin(valid_decades)]

decade_avg = valid_book_avg.groupby('decade')['rating'].mean().reset_index()

best = decade_avg.sort_values(['rating','decade'], ascending=[False,True]).head(1)

if best.empty:
    result = None
else:
    decade = int(best.iloc[0]['decade'])
    result = f"{decade}s"

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VDTddWxCKeLtlMTu2Uzrn7nF': 'file_storage/call_VDTddWxCKeLtlMTu2Uzrn7nF.json', 'var_call_rGmPMyjf6LxjRBdmMgRFbumf': ['books_info'], 'var_call_EpQBcK5uPUwJISAl8qXXfsTr': ['review'], 'var_call_kuRlHoxuw3XhG6Mps4h2ytF5': 'file_storage/call_kuRlHoxuw3XhG6Mps4h2ytF5.json'}

exec(code, env_args)
