code = """import json
import pandas as pd
import re
import ast

# Load storage variables
reviews = var_call_nC5DfcA3KTJeIcgIIBRjeC5T
books_file_path = var_call_TQEJqJJ7UgfazlLOSLDrs1Yl

# Load books JSON
with open(books_file_path, "r", encoding="utf-8") as f:
    books = json.load(f)

# Reviews DataFrame
df_rev = pd.DataFrame(reviews)
# Convert types
df_rev["avg_rating"] = df_rev["avg_rating"].astype(float)
try:
    df_rev["review_count"] = df_rev["review_count"].astype(int)
except Exception:
    df_rev["review_count"] = df_rev["review_count"].apply(lambda x: int(x) if x not in (None, "") else 0)

# Map purchase_id to book_id by extracting digits
def map_bookid(pid):
    if pid is None:
        return None
    s = "".join(ch for ch in str(pid) if ch.isdigit())
    if s == "":
        return None
    return "bookid_" + s

df_rev["book_id"] = df_rev["purchase_id"].apply(map_bookid)

# Books DataFrame
df_books = pd.DataFrame(books)

# Parse categories field into list and check for Children
import json as _json

def parse_categories(cat_field):
    if cat_field is None:
        return []
    if isinstance(cat_field, list):
        return cat_field
    s = str(cat_field).strip()
    if s in ("", "[]"):
        return []
    # try json
    try:
        parsed = _json.loads(s)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass
    # try ast
    try:
        parsed = ast.literal_eval(s)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass
    # fallback: return as single-element list
    return [s]

df_books["categories_list"] = df_books["categories"].apply(parse_categories)

# Merge on book_id
df_merged = pd.merge(df_rev, df_books, on="book_id", how="left")

# Check if categories contain Children substring
def categories_has_children(cat_list):
    if not isinstance(cat_list, list):
        return False
    for it in cat_list:
        try:
            if "Children" in str(it):
                return True
        except Exception:
            continue
    return False

mask = df_merged["avg_rating"] >= 4.5
mask = mask & df_merged["categories_list"].apply(categories_has_children)
filtered = df_merged[mask].copy()

# Build output
results = []
for _, r in filtered.iterrows():
    results.append({
        "book_id": r.get("book_id"),
        "title": r.get("title"),
        "avg_rating": float(r.get("avg_rating") if r.get("avg_rating") is not None else 0.0),
        "review_count": int(r.get("review_count") if r.get("review_count") is not None else 0),
        "categories_list": r.get("categories_list")
    })

titles = [x["title"] for x in results if x.get("title")]
if not titles:
    plain = "No Children Books have avg rating >= 4.5 from 2020 onwards in the data."
else:
    lines = ["- " + t for t in titles]
    plain = "Books (Children Books) with avg rating >= 4.5 from 2020 onwards:\n" + "\n".join(lines)

out = {"results": results, "plain_text": plain}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_8sjVu1btoN6NrvyoeUOWqkvO': ['review'], 'var_call_iR312fU5tdUT9Rq8lzzg4jah': ['books_info'], 'var_call_nC5DfcA3KTJeIcgIIBRjeC5T': [{'purchase_id': 'purchaseid_96', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_94', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_66', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_55', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_46', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_4', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_37', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_3', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_22', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_200', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_198', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_196', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_187', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_185', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_169', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_154', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_129', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_10', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_13', 'avg_rating': '4.923076923076923', 'review_count': '13'}, {'purchase_id': 'purchaseid_149', 'avg_rating': '4.9', 'review_count': '10'}, {'purchase_id': 'purchaseid_178', 'avg_rating': '4.795918367346939', 'review_count': '49'}, {'purchase_id': 'purchaseid_76', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_48', 'avg_rating': '4.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_115', 'avg_rating': '4.75', 'review_count': '8'}, {'purchase_id': 'purchaseid_8', 'avg_rating': '4.709677419354839', 'review_count': '31'}, {'purchase_id': 'purchaseid_158', 'avg_rating': '4.708333333333333', 'review_count': '24'}, {'purchase_id': 'purchaseid_72', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_50', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_23', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_161', 'avg_rating': '4.5', 'review_count': '2'}, {'purchase_id': 'purchaseid_99', 'avg_rating': '4.4', 'review_count': '5'}, {'purchase_id': 'purchaseid_62', 'avg_rating': '4.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_45', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_31', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_25', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_193', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_167', 'avg_rating': '4.0', 'review_count': '12'}, {'purchase_id': 'purchaseid_145', 'avg_rating': '4.0', 'review_count': '5'}, {'purchase_id': 'purchaseid_140', 'avg_rating': '4.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_137', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_11', 'avg_rating': '4.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_107', 'avg_rating': '4.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_20', 'avg_rating': '3.875', 'review_count': '16'}, {'purchase_id': 'purchaseid_85', 'avg_rating': '3.8333333333333335', 'review_count': '12'}, {'purchase_id': 'purchaseid_5', 'avg_rating': '3.75', 'review_count': '4'}, {'purchase_id': 'purchaseid_32', 'avg_rating': '3.5714285714285716', 'review_count': '7'}, {'purchase_id': 'purchaseid_93', 'avg_rating': '3.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_67', 'avg_rating': '3.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_189', 'avg_rating': '2.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_155', 'avg_rating': '1.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_109', 'avg_rating': '1.0', 'review_count': '2'}], 'var_call_TQEJqJJ7UgfazlLOSLDrs1Yl': 'file_storage/call_TQEJqJJ7UgfazlLOSLDrs1Yl.json', 'var_call_XQaqicjdfgWYq18k9Cvfc0uu': {'reviews_count': 80, 'books_file_path': 'file_storage/call_TQEJqJJ7UgfazlLOSLDrs1Yl.json'}}

exec(code, env_args)
