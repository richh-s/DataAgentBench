code = """import json
import pandas as pd
import re

# Load results from storage variables
books_path = var_call_bjVMycRx8S0UvdzItFh2FwCe  # path to JSON file
reviews = var_call_uCaUWC353HOluUt58Qk418MJ

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Clean reviews: cast rating to float
df_reviews = df_reviews[df_reviews['rating'].notnull()].copy()
# Some ratings may be strings
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
# Drop rows with invalid ratings
df_reviews = df_reviews[df_reviews['rating'].notnull()].copy()

# Map purchase_id to book_id by replacing 'purchaseid_' with 'bookid_'
def map_purchase_to_book(pid):
    if pd.isna(pid):
        return None
    s = str(pid)
    if s.startswith('bookid_'):
        return s
    if s.startswith('purchaseid_'):
        return 'bookid_' + s.split('_', 1)[1]
    # fallback: extract trailing digits
    m = re.search(r'(\d+)$', s)
    if m:
        return 'bookid_' + m.group(1)
    return s

df_reviews['book_id'] = df_reviews['purchase_id'].apply(map_purchase_to_book)

# Extract publication year from details in books

def extract_year(details):
    if not isinstance(details, str):
        return None
    # find all 4-digit numbers
    matches = re.findall(r"(1[5-9]\d{2}|20\d{2}|21\d{2})", details)
    # filter reasonable years 1500-2025
    for m in matches:
        y = int(m)
        if 1500 <= y <= 2025:
            return y
    return None

if 'details' not in df_books.columns:
    df_books['details'] = None

# Apply extraction
df_books['year'] = df_books['details'].apply(extract_year)
# Create decade string like '2010s'
def year_to_decade(y):
    if pd.isna(y):
        return None
    y = int(y)
    decade = (y // 10) * 10
    return f"{decade}s"

df_books['decade'] = df_books['year'].apply(year_to_decade)

# Merge reviews aggregated per book with books
# Compute per-book average rating
book_avg = df_reviews.groupby('book_id', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
# Count number of reviews per book optional
book_avg_counts = df_reviews.groupby('book_id')['rating'].count().reset_index().rename(columns={'rating':'num_reviews'})
book_avg = book_avg.merge(book_avg_counts, on='book_id')

# Merge with books to get decade
merged = book_avg.merge(df_books[['book_id','title','decade','year']], on='book_id', how='left')

# Consider only books with a valid decade
merged = merged[merged['decade'].notnull()].copy()

# For each decade, we need number of distinct books that have been rated
decade_book_counts = merged.groupby('decade')['book_id'].nunique().reset_index().rename(columns={'book_id':'num_books'})
# Compute average of book avg ratings per decade
decade_avg = merged.groupby('decade')['avg_rating'].mean().reset_index().rename(columns={'avg_rating':'decade_avg_rating'})

decade_stats = decade_book_counts.merge(decade_avg, on='decade')

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['num_books'] >= 10].copy()

if eligible.empty:
    result = json.dumps("No decade has at least 10 distinct rated books in the available data.")
else:
    # Find decade with highest average rating
    eligible = eligible.sort_values(['decade_avg_rating','decade'], ascending=[False, True])
    top = eligible.iloc[0]
    result = json.dumps(top['decade'])

print("__RESULT__:")
print(result)"""

env_args = {'var_call_xbHmbRwaGSy9GuPgNPHtNYbk': ['review'], 'var_call_jPGH9HC2B4ZI3MnacHwuILXc': ['books_info'], 'var_call_bjVMycRx8S0UvdzItFh2FwCe': 'file_storage/call_bjVMycRx8S0UvdzItFh2FwCe.json', 'var_call_uCaUWC353HOluUt58Qk418MJ': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}, {'purchase_id': 'purchaseid_188', 'rating': '1'}, {'purchase_id': 'purchaseid_23', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '3'}, {'purchase_id': 'purchaseid_99', 'rating': '2'}, {'purchase_id': 'purchaseid_190', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_169', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_194', 'rating': '4'}, {'purchase_id': 'purchaseid_81', 'rating': '5'}, {'purchase_id': 'purchaseid_199', 'rating': '1'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_96', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '4'}, {'purchase_id': 'purchaseid_148', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_200', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '1'}, {'purchase_id': 'purchaseid_20', 'rating': '5'}, {'purchase_id': 'purchaseid_52', 'rating': '5'}, {'purchase_id': 'purchaseid_159', 'rating': '2'}, {'purchase_id': 'purchaseid_83', 'rating': '5'}, {'purchase_id': 'purchaseid_67', 'rating': '3'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_58', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '4'}, {'purchase_id': 'purchaseid_95', 'rating': '5'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '3'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_136', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_46', 'rating': '5'}, {'purchase_id': 'purchaseid_38', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_31', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_7', 'rating': '5'}, {'purchase_id': 'purchaseid_4', 'rating': '5'}, {'purchase_id': 'purchaseid_104', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_162', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '3'}, {'purchase_id': 'purchaseid_158', 'rating': '3'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_165', 'rating': '3'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_6', 'rating': '5'}, {'purchase_id': 'purchaseid_158', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_46', 'rating': '5'}, {'purchase_id': 'purchaseid_83', 'rating': '5'}, {'purchase_id': 'purchaseid_86', 'rating': '5'}, {'purchase_id': 'purchaseid_174', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_177', 'rating': '5'}, {'purchase_id': 'purchaseid_187', 'rating': '5'}, {'purchase_id': 'purchaseid_188', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_63', 'rating': '2'}, {'purchase_id': 'purchaseid_33', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '2'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_62', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_32', 'rating': '4'}, {'purchase_id': 'purchaseid_157', 'rating': '5'}, {'purchase_id': 'purchaseid_193', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_185', 'rating': '4'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_187', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_13', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_72', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '3'}, {'purchase_id': 'purchaseid_42', 'rating': '5'}, {'purchase_id': 'purchaseid_96', 'rating': '5'}, {'purchase_id': 'purchaseid_73', 'rating': '5'}, {'purchase_id': 'purchaseid_188', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '4'}, {'purchase_id': 'purchaseid_97', 'rating': '5'}, {'purchase_id': 'purchaseid_59', 'rating': '5'}, {'purchase_id': 'purchaseid_192', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_193', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '2'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_109', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_99', 'rating': '5'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '4'}, {'purchase_id': 'purchaseid_148', 'rating': '4'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_163', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_52', 'rating': '5'}, {'purchase_id': 'purchaseid_109', 'rating': '4'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_106', 'rating': '5'}, {'purchase_id': 'purchaseid_130', 'rating': '5'}, {'purchase_id': 'purchaseid_118', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_103', 'rating': '1'}, {'purchase_id': 'purchaseid_8', 'rating': '4'}, {'purchase_id': 'purchaseid_5', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_103', 'rating': '4'}, {'purchase_id': 'purchaseid_5', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '4'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '2'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '5'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_154', 'rating': '2'}, {'purchase_id': 'purchaseid_32', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '5'}, {'purchase_id': 'purchaseid_161', 'rating': '4'}, {'purchase_id': 'purchaseid_41', 'rating': '5'}, {'purchase_id': 'purchaseid_36', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_145', 'rating': '5'}, {'purchase_id': 'purchaseid_20', 'rating': '4'}, {'purchase_id': 'purchaseid_124', 'rating': '5'}, {'purchase_id': 'purchaseid_48', 'rating': '5'}, {'purchase_id': 'purchaseid_32', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_3', 'rating': '5'}, {'purchase_id': 'purchaseid_148', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '3'}, {'purchase_id': 'purchaseid_197', 'rating': '5'}, {'purchase_id': 'purchaseid_196', 'rating': '5'}, {'purchase_id': 'purchaseid_41', 'rating': '5'}]}

exec(code, env_args)
