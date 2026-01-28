code = """import json
import pandas as pd
# load review aggregation
rl = var_call_jlG5CwF37zAI4YYMAQcbO7Ss
df_reviews = pd.DataFrame(rl)
# convert numeric fields
df_reviews['avg_rating'] = pd.to_numeric(df_reviews['avg_rating'], errors='coerce')
df_reviews['review_count'] = pd.to_numeric(df_reviews['review_count'], errors='coerce')
# map purchase_id to book_id
df_reviews['book_id'] = df_reviews['purchase_id'].str.replace('purchaseid_','bookid_')

# load books data from file path
books_path = var_call_puamCRi612M8a4Sp5y5oOlyo
with open(books_path, 'r') as f:
    books = json.load(f)
df_books = pd.DataFrame(books)

# ensure categories is string
df_books['categories'] = df_books['categories'].astype(str)
# filter for Children's Books in categories
mask = df_books['categories'].str.contains("Children's Books", na=False)
df_children = df_books[mask].copy()

# merge
df_merged = pd.merge(df_children, df_reviews, on='book_id', how='inner')
# filter avg_rating >= 4.5
df_result = df_merged[df_merged['avg_rating'] >= 4.5].copy()
# prepare output
out = []
for _, row in df_result.iterrows():
    out.append({
        'book_id': row['book_id'],
        'title': row.get('title'),
        'avg_rating': float(row['avg_rating']) if pd.notnull(row['avg_rating']) else None,
        'review_count': int(row['review_count']) if pd.notnull(row['review_count']) else None,
        'categories': row.get('categories')
    })

result_json = json.dumps(out)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_kAcwLQaKKmRCGAaiYlkvdW0v': ['review'], 'var_call_DZTAPIFU5Ms0JTKSu7JTGPXw': ['books_info'], 'var_call_jlG5CwF37zAI4YYMAQcbO7Ss': [{'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_107', 'avg_rating': '4.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_109', 'avg_rating': '1.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_11', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'review_count': '8'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'review_count': '13'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_137', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_140', 'avg_rating': '4.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_145', 'avg_rating': '4.0', 'review_count': '5'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'review_count': '10'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_155', 'avg_rating': '1.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'review_count': '24'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_167', 'avg_rating': '4.0', 'review_count': '12'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'review_count': '49'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_189', 'avg_rating': '2.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_193', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_20', 'avg_rating': '3.875', 'review_count': '16'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_25', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_31', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_32', 'avg_rating': '3.5714285714285716', 'review_count': '7'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_45', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_5', 'avg_rating': '3.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_62', 'avg_rating': '4.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_67', 'avg_rating': '3.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'review_count': '31'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_85', 'avg_rating': '3.8333333333333335', 'review_count': '12'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_93', 'avg_rating': '3.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_99', 'avg_rating': '4.4', 'review_count': '5'}], 'var_call_puamCRi612M8a4Sp5y5oOlyo': 'file_storage/call_puamCRi612M8a4Sp5y5oOlyo.json'}

exec(code, env_args)
