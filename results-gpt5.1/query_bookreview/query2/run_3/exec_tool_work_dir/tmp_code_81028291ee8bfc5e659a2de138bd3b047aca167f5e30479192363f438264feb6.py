code = """import json, pandas as pd
from pathlib import Path

# Load large books details and categories
with open(var_call_MBMqf8gIK837HXUFN7ZUYyzK, 'r') as f:
    details_data = json.load(f)
with open(var_call_slbvgyxKBmTnRleDZj0IARA9, 'r') as f:
    categories_data = json.load(f)

reviews = pd.DataFrame(var_call_2p873NoAT7fl9C6gukl7J8vB)
books_details = pd.DataFrame(details_data)
books_categories = pd.DataFrame(categories_data)

# Filter English-language books using 'details' column (contains 'English')
books_details['is_english'] = books_details['details'].str.contains('English', case=False, na=False)
english_books = books_details[books_details['is_english']]

# Filter Literature & Fiction using categories containing 'Literature & Fiction'
books_categories['is_lit_fic'] = books_categories['categories'].str.contains('Literature & Fiction', na=False)
lit_fic_books = books_categories[books_categories['is_lit_fic']]

# Join to get English Literature & Fiction books
eng_lit_fic = pd.merge(english_books[['book_id']], lit_fic_books[['book_id']], on='book_id', how='inner').drop_duplicates()

# Fuzzy join: purchase_id in reviews to book_id in books
# Here, IDs seem aligned like 'purchaseid_12' vs 'bookid_12' (same numeric suffix). Map by numeric part.
reviews['num'] = reviews['purchase_id'].str.extract('(\d+)$').astype(int)
eng_lit_fic['num'] = eng_lit_fic['book_id'].str.extract('(\d+)$').astype(int)

matched = pd.merge(reviews, eng_lit_fic, on='num', how='inner')

# Load full books_info to get titles/authors
books_info = pd.read_json(var_call_slbvgyxKBmTnRleDZj0IARA9)
# books_info file actually only has book_id and categories; need to reconstruct minimal info by joining back to details
books_full = pd.merge(books_details, books_categories, on='book_id', how='left')

result = pd.merge(matched, books_full, on='book_id', how='left')

# Select and deduplicate relevant columns
out_cols = ['book_id', 'purchase_id', 'title', 'author', 'categories', 'details', 'avg_rating', 'num_reviews']
# title/author may not exist in books_full; handle safely
for c in ['title','author']:
    if c not in result.columns:
        result[c] = None

final = result[out_cols].drop_duplicates(subset=['book_id']).sort_values('book_id')

answer = final.to_dict(orient='records')

s = json.dumps(answer)
print("__RESULT__:")
print(s)"""

env_args = {'var_call_FbJG9QuDfag9VtMMukPDomxC': [], 'var_call_MBMqf8gIK837HXUFN7ZUYyzK': 'file_storage/call_MBMqf8gIK837HXUFN7ZUYyzK.json', 'var_call_slbvgyxKBmTnRleDZj0IARA9': 'file_storage/call_slbvgyxKBmTnRleDZj0IARA9.json', 'var_call_7EOOa4jyxJdwpp0uxUjUFIct': ['review'], 'var_call_2p873NoAT7fl9C6gukl7J8vB': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'num_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'num_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'num_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'num_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'num_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'num_reviews': '1'}]}

exec(code, env_args)
