code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
books_path = var_call_Ski2B0XLoAMqJtiOKqJe6MaV
reviews_path = var_call_mbaQejlQ1FbFTwXBbHhBwzfu

with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Normalize IDs: extract numeric part and form bookid_x
books_df['id_num'] = books_df['book_id'].str.extract(r'(\d+)')
books_df['book_id_norm'] = 'bookid_' + books_df['id_num'].astype(str)

# For reviews, convert purchaseid to bookid
reviews_df['id_num'] = reviews_df['purchase_id'].str.extract(r'(\d+)')
reviews_df['book_id_norm'] = 'bookid_' + reviews_df['id_num'].astype(str)

# Convert rating to numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Aggregate per-book average rating
book_avg = reviews_df.groupby('book_id_norm', dropna=True)['rating'].mean().reset_index().rename(columns={'rating':'book_avg_rating'})

# Extract publication year from details (first 4-digit year 1000-2099)
def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", text)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

books_df['pub_year'] = books_df['details'].apply(extract_year)

# Merge books with book_avg on normalized id
merged = pd.merge(book_avg, books_df, left_on='book_id_norm', right_on='book_id_norm', how='left')

# Keep entries with a publication year
merged = merged[merged['pub_year'].notna()].copy()
merged['pub_year'] = merged['pub_year'].astype(int)
merged['decade_start'] = (merged['pub_year'] // 10) * 10
merged['decade'] = merged['decade_start'].astype(str) + 's'

# Compute per-decade stats: count of distinct books and mean of book averages
decade_stats = merged.groupby('decade').agg(book_count=('book_id_norm','nunique'), decade_avg_rating=('book_avg_rating','mean')).reset_index()

# Filter decades with at least 10 distinct books
eligible = decade_stats[decade_stats['book_count'] >= 10].copy()

if eligible.empty:
    result = {'decade': None, 'average': None, 'book_count': 0}
else:
    # Choose decade with highest average; if tie, pick the earliest decade
    eligible = eligible.sort_values(['decade_avg_rating','decade'], ascending=[False, True])
    top = eligible.iloc[0]
    result = {'decade': top['decade'], 'average': round(float(top['decade_avg_rating']), 4), 'book_count': int(top['book_count'])}

import sys
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bMMqeR45aFoJadN71Hovrr6o': ['review'], 'var_call_oehPK5UAD3eNQTBmjYZOm2ct': ['books_info'], 'var_call_N2q1Cmba11qdKyioRjamiHZv': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_169'}, {'purchase_id': 'purchaseid_145'}, {'purchase_id': 'purchaseid_194'}, {'purchase_id': 'purchaseid_81'}, {'purchase_id': 'purchaseid_199'}, {'purchase_id': 'purchaseid_96'}, {'purchase_id': 'purchaseid_148'}, {'purchase_id': 'purchaseid_200'}, {'purchase_id': 'purchaseid_20'}, {'purchase_id': 'purchaseid_52'}, {'purchase_id': 'purchaseid_159'}, {'purchase_id': 'purchaseid_83'}, {'purchase_id': 'purchaseid_67'}, {'purchase_id': 'purchaseid_58'}, {'purchase_id': 'purchaseid_95'}, {'purchase_id': 'purchaseid_62'}, {'purchase_id': 'purchaseid_136'}, {'purchase_id': 'purchaseid_10'}, {'purchase_id': 'purchaseid_46'}, {'purchase_id': 'purchaseid_38'}, {'purchase_id': 'purchaseid_31'}, {'purchase_id': 'purchaseid_7'}, {'purchase_id': 'purchaseid_4'}, {'purchase_id': 'purchaseid_104'}, {'purchase_id': 'purchaseid_162'}, {'purchase_id': 'purchaseid_5'}, {'purchase_id': 'purchaseid_158'}, {'purchase_id': 'purchaseid_165'}, {'purchase_id': 'purchaseid_6'}, {'purchase_id': 'purchaseid_86'}, {'purchase_id': 'purchaseid_174'}, {'purchase_id': 'purchaseid_177'}, {'purchase_id': 'purchaseid_187'}, {'purchase_id': 'purchaseid_63'}, {'purchase_id': 'purchaseid_33'}], 'var_call_3V18kyeWoJSQZNvKE5Dw0jVJ': [{'book_id': 'bookid_78'}, {'book_id': 'bookid_107'}, {'book_id': 'bookid_53'}, {'book_id': 'bookid_7'}, {'book_id': 'bookid_25'}, {'book_id': 'bookid_180'}, {'book_id': 'bookid_122'}, {'book_id': 'bookid_47'}, {'book_id': 'bookid_153'}, {'book_id': 'bookid_67'}, {'book_id': 'bookid_64'}, {'book_id': 'bookid_19'}, {'book_id': 'bookid_106'}, {'book_id': 'bookid_61'}, {'book_id': 'bookid_43'}, {'book_id': 'bookid_52'}, {'book_id': 'bookid_193'}, {'book_id': 'bookid_148'}, {'book_id': 'bookid_129'}, {'book_id': 'bookid_87'}, {'book_id': 'bookid_117'}, {'book_id': 'bookid_51'}, {'book_id': 'bookid_175'}, {'book_id': 'bookid_27'}, {'book_id': 'bookid_2'}, {'book_id': 'bookid_152'}, {'book_id': 'bookid_198'}, {'book_id': 'bookid_128'}, {'book_id': 'bookid_130'}, {'book_id': 'bookid_142'}, {'book_id': 'bookid_65'}, {'book_id': 'bookid_140'}, {'book_id': 'bookid_179'}, {'book_id': 'bookid_81'}, {'book_id': 'bookid_54'}, {'book_id': 'bookid_94'}, {'book_id': 'bookid_82'}, {'book_id': 'bookid_90'}, {'book_id': 'bookid_55'}, {'book_id': 'bookid_161'}, {'book_id': 'bookid_37'}, {'book_id': 'bookid_89'}, {'book_id': 'bookid_66'}, {'book_id': 'bookid_155'}, {'book_id': 'bookid_191'}, {'book_id': 'bookid_69'}, {'book_id': 'bookid_126'}, {'book_id': 'bookid_184'}, {'book_id': 'bookid_113'}, {'book_id': 'bookid_28'}, {'book_id': 'bookid_33'}, {'book_id': 'bookid_119'}, {'book_id': 'bookid_98'}, {'book_id': 'bookid_32'}, {'book_id': 'bookid_22'}, {'book_id': 'bookid_99'}, {'book_id': 'bookid_13'}, {'book_id': 'bookid_158'}, {'book_id': 'bookid_199'}, {'book_id': 'bookid_109'}, {'book_id': 'bookid_103'}, {'book_id': 'bookid_29'}, {'book_id': 'bookid_26'}, {'book_id': 'bookid_194'}, {'book_id': 'bookid_163'}, {'book_id': 'bookid_86'}, {'book_id': 'bookid_127'}, {'book_id': 'bookid_3'}, {'book_id': 'bookid_143'}, {'book_id': 'bookid_125'}, {'book_id': 'bookid_93'}, {'book_id': 'bookid_124'}, {'book_id': 'bookid_149'}, {'book_id': 'bookid_131'}, {'book_id': 'bookid_75'}, {'book_id': 'bookid_132'}, {'book_id': 'bookid_108'}, {'book_id': 'bookid_139'}, {'book_id': 'bookid_36'}, {'book_id': 'bookid_17'}, {'book_id': 'bookid_171'}, {'book_id': 'bookid_58'}, {'book_id': 'bookid_100'}, {'book_id': 'bookid_187'}, {'book_id': 'bookid_137'}, {'book_id': 'bookid_73'}, {'book_id': 'bookid_68'}, {'book_id': 'bookid_16'}, {'book_id': 'bookid_72'}, {'book_id': 'bookid_70'}, {'book_id': 'bookid_44'}, {'book_id': 'bookid_136'}, {'book_id': 'bookid_6'}, {'book_id': 'bookid_150'}, {'book_id': 'bookid_197'}, {'book_id': 'bookid_146'}, {'book_id': 'bookid_186'}, {'book_id': 'bookid_121'}, {'book_id': 'bookid_63'}, {'book_id': 'bookid_40'}], 'var_call_Ski2B0XLoAMqJtiOKqJe6MaV': 'file_storage/call_Ski2B0XLoAMqJtiOKqJe6MaV.json', 'var_call_mbaQejlQ1FbFTwXBbHhBwzfu': 'file_storage/call_mbaQejlQ1FbFTwXBbHhBwzfu.json'}

exec(code, env_args)
