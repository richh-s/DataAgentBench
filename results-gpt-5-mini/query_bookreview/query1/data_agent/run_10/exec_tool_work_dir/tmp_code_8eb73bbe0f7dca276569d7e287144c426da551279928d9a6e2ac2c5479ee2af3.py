code = """import pandas as pd
import json
import re

# Load data from storage file paths
books_path = var_call_s9HLnt8Vua54xCtuk2Vh9yHN
reviews_path = var_call_pyZ0e0oVsTrh2hmUHZN1DdIF

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# normalize column names
# extract numeric id suffix from book_id and purchase_id
def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r"(\d+)$", str(s))
    return int(m.group(1)) if m else None

books_df['num_id'] = books_df['book_id'].apply(extract_num)
reviews_df['num_id'] = reviews_df['purchase_id'].apply(extract_num)

# extract year from details using 4-digit numbers between 1500 and 2023
def extract_year(s):
    if pd.isna(s):
        return None
    years = re.findall(r"(1[5-9]\d{2}|20\d{2}|19\d{2})", str(s))
    if not years:
        return None
    # choose first plausible year
    for y in years:
        yi = int(y)
        if 1500 <= yi <= 2023:
            return yi
    return None

books_df['year'] = books_df['details'].apply(extract_year)

# drop books without num_id or year
books_df = books_df.dropna(subset=['num_id', 'year'])
books_df['num_id'] = books_df['num_id'].astype(int)
books_df['year'] = books_df['year'].astype(int)
books_df['decade'] = (books_df['year'] // 10 * 10).astype(int).astype(str) + 's'

# clean reviews ratings and num_id
reviews_df = reviews_df.dropna(subset=['num_id', 'rating'])
reviews_df['num_id'] = reviews_df['num_id'].astype(int)
# ratings may be strings; convert to float
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')
reviews_df = reviews_df.dropna(subset=['rating'])

# Join reviews to books on num_id
merged = pd.merge(reviews_df, books_df[['num_id','book_id','year','decade']], on='num_id', how='inner')

# compute per-book average rating
per_book = merged.groupby('book_id').agg({'rating':'mean', 'num_id':'first', 'decade':'first', 'year':'first'}).reset_index()
per_book.rename(columns={'rating':'avg_rating'}, inplace=True)

# For each decade, count distinct books that have been rated and compute average of per-book averages
decade_stats = per_book.groupby('decade').agg(num_books=('book_id','nunique'), avg_of_books=('avg_rating','mean')).reset_index()

# filter decades with at least 10 distinct books
valid = decade_stats[decade_stats['num_books']>=10]

if valid.empty:
    result = None
else:
    # find the decade with highest average; if tie, pick the one with most books then earliest decade
    best_row = valid.sort_values(['avg_of_books','num_books','decade'], ascending=[False,False,True]).iloc[0]
    result = best_row['decade']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rwu5eKjngAgDFN6drKfghk74': ['review'], 'var_call_8ZEs9XtFSqBH34cyVzfpvda5': ['books_info'], 'var_call_s9HLnt8Vua54xCtuk2Vh9yHN': 'file_storage/call_s9HLnt8Vua54xCtuk2Vh9yHN.json', 'var_call_kKTnzWWPWceIks63FwRuGYtH': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_169'}, {'purchase_id': 'purchaseid_145'}, {'purchase_id': 'purchaseid_194'}, {'purchase_id': 'purchaseid_81'}, {'purchase_id': 'purchaseid_199'}, {'purchase_id': 'purchaseid_96'}, {'purchase_id': 'purchaseid_148'}, {'purchase_id': 'purchaseid_200'}, {'purchase_id': 'purchaseid_20'}, {'purchase_id': 'purchaseid_52'}, {'purchase_id': 'purchaseid_159'}, {'purchase_id': 'purchaseid_83'}, {'purchase_id': 'purchaseid_67'}, {'purchase_id': 'purchaseid_58'}, {'purchase_id': 'purchaseid_95'}, {'purchase_id': 'purchaseid_62'}, {'purchase_id': 'purchaseid_136'}, {'purchase_id': 'purchaseid_10'}, {'purchase_id': 'purchaseid_46'}, {'purchase_id': 'purchaseid_38'}, {'purchase_id': 'purchaseid_31'}, {'purchase_id': 'purchaseid_7'}, {'purchase_id': 'purchaseid_4'}, {'purchase_id': 'purchaseid_104'}, {'purchase_id': 'purchaseid_162'}, {'purchase_id': 'purchaseid_5'}, {'purchase_id': 'purchaseid_158'}, {'purchase_id': 'purchaseid_165'}, {'purchase_id': 'purchaseid_6'}, {'purchase_id': 'purchaseid_86'}, {'purchase_id': 'purchaseid_174'}, {'purchase_id': 'purchaseid_177'}, {'purchase_id': 'purchaseid_187'}, {'purchase_id': 'purchaseid_63'}, {'purchase_id': 'purchaseid_33'}], 'var_call_pyZ0e0oVsTrh2hmUHZN1DdIF': 'file_storage/call_pyZ0e0oVsTrh2hmUHZN1DdIF.json'}

exec(code, env_args)
