code = """import json, re, pandas as pd

# Load data from stored JSON files
with open(var_call_5dwCE4tu8xQa66eB3wyRTBzu, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_V2MudqENPjmroLDcBNOyV1cj, 'r', encoding='utf-8') as f:
    avgs = json.load(f)

# DataFrames
df_books = pd.DataFrame(books)
df_avgs = pd.DataFrame(avgs)

# helper to extract numeric id
def extract_num_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(\d+)", s)
    return int(m.group(1)) if m else None

# extract year from details
def extract_year(s):
    if not isinstance(s, str):
        return None
    # search for 4-digit year between 1000 and 2099
    m = re.search(r"\b(19|20)\d{2}\b", s)
    if m:
        return int(m.group(0))
    return None

# apply
df_books['num_id'] = df_books['book_id'].apply(extract_num_id)
df_books['year'] = df_books['details'].apply(extract_year)
# derive decade
df_books['decade'] = df_books['year'].apply(lambda y: f"{(y//10)*10}s" if pd.notnull(y) else None)

# avgs numeric id and float avg
df_avgs['num_id'] = df_avgs['purchase_id'].apply(extract_num_id)
# convert avg_rating to float
df_avgs['avg_rating'] = pd.to_numeric(df_avgs['avg_rating'], errors='coerce')

# merge on num_id
df_merged = pd.merge(df_books, df_avgs, on='num_id', how='inner', suffixes=('_book','_avg'))

# keep relevant columns
df_merged = df_merged[['book_id','purchase_id','num_id','year','decade','avg_rating']]
# drop rows without decade or avg_rating
df_merged = df_merged[df_merged['decade'].notnull() & df_merged['avg_rating'].notnull()]

# group by decade: count distinct books and mean of avg_rating
grp = df_merged.groupby('decade').agg(book_count=('num_id', lambda x: x.nunique()),
                                       mean_avg_rating=('avg_rating', 'mean')).reset_index()

# filter decades with at least 10 distinct books
grp_filtered = grp[grp['book_count'] >= 10]

if grp_filtered.empty:
    result = None
else:
    # find decade with highest mean_avg_rating
    top = grp_filtered.sort_values(['mean_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {'decade': top['decade'], 'average_rating': round(float(top['mean_avg_rating']),4), 'book_count': int(top['book_count'])}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8TbuovrDdOB1xBpUtttDEP9A': ['review'], 'var_call_14ux0gRqZwo7087az28Kt6PP': ['books_info'], 'var_call_5dwCE4tu8xQa66eB3wyRTBzu': 'file_storage/call_5dwCE4tu8xQa66eB3wyRTBzu.json', 'var_call_V2MudqENPjmroLDcBNOyV1cj': 'file_storage/call_V2MudqENPjmroLDcBNOyV1cj.json'}

exec(code, env_args)
