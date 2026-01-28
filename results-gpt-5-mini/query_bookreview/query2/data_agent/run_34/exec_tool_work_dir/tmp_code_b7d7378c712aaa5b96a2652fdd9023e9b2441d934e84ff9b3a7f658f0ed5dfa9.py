code = """import json
import pandas as pd
import re

# Load tool results from storage
avg5 = var_call_7jItzTmYZCeCq5qFHc5kZ7Qr  # list of dicts with purchase_id

# Load large JSON results from file paths
with open(var_call_jMckq1d3SCR09bLz1k6OZ4pU, 'r') as f:
    reviews = json.load(f)
with open(var_call_2OazurDIeZD2sxHQurszGgTe, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_avg5 = pd.DataFrame(avg5)
df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Normalize helper
def normalize(s):
    if s is None:
        return ""
    s = str(s).lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Build a map of purchase_id -> representative title (most common)
rep_titles = {}
for pid, group in df_reviews.groupby('purchase_id'):
    titles = group['title'].dropna().astype(str).tolist()
    if not titles:
        rep_titles[pid] = ""
    else:
        rep = pd.Series(titles).mode()
        rep_titles[pid] = rep.iloc[0] if not rep.empty else titles[0]

# Filter to only purchase_ids with avg_rating == 5.0
pids_5 = set(df_avg5['purchase_id'].tolist())
# prepare normalized title map for those
pid_title_norm = {pid: normalize(rep_titles.get(pid, '')) for pid in pids_5}

# Work on df_books: normalize titles and ensure string fields
if df_books.empty:
    result = []
else:
    df_books['title_norm'] = df_books['title'].apply(lambda x: normalize(x if pd.notna(x) else ''))
    df_books['details_str'] = df_books['details'].fillna('').astype(str)
    df_books['description_str'] = df_books.get('description','').fillna('').astype(str)
    df_books['categories_str'] = df_books['categories'].fillna('').astype(str)

    # Filter books to English-language if possible (check details or description or categories)
    def is_english(row):
        det = str(row.get('details','') ).lower()
        desc = str(row.get('description','') ).lower()
        cats = str(row.get('categories','') ).lower()
        return ('english' in det) or ('english' in desc) or ('english' in cats)

    df_books = df_books[df_books.apply(is_english, axis=1)].copy()

    # Matching: try exact normalized match, substring, or Jaccard token overlap
    def jaccard(a, b):
        sa = set(a.split())
        sb = set(b.split())
        if not sa or not sb:
            return 0.0
        return len(sa & sb) / len(sa | sb)

    matches = []
    for pid, tnorm in pid_title_norm.items():
        if not tnorm:
            continue
        best = None
        best_score = 0.0
        for _, brow in df_books.iterrows():
            bnorm = brow['title_norm']
            score = 0.0
            if tnorm == bnorm and tnorm != "":
                score = 1.0
            elif tnorm in bnorm or bnorm in tnorm:
                score = 0.9
            else:
                score = jaccard(tnorm, bnorm)
            if score > best_score:
                best_score = score
                best = brow
        # accept matches with score >= 0.5
        if best is not None and best_score >= 0.5:
            matches.append({
                'purchase_id': pid,
                'review_title': rep_titles.get(pid,''),
                'book_id': best['book_id'],
                'book_title': best['title'],
                'author': best.get('author',''),
                'categories': best.get('categories',''),
                'details': best.get('details',''),
                'match_score': round(float(best_score),3)
            })

    # Remove duplicates by book_id
    seen = set()
    unique_matches = []
    for m in matches:
        if m['book_id'] not in seen:
            seen.add(m['book_id'])
            unique_matches.append(m)

    # Sort results by match_score desc
    result = sorted(unique_matches, key=lambda x: -x['match_score'])

# Print final result as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QjWhfWqE1Q0o99yzH3ao0gAh': ['review'], 'var_call_7jItzTmYZCeCq5qFHc5kZ7Qr': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'review_count': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'review_count': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'review_count': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'review_count': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'review_count': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'review_count': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'review_count': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'review_count': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'review_count': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'review_count': '1'}], 'var_call_MEHfOifs72m6vA1jTfgIOT56': ['books_info'], 'var_call_X46ZZJy3bNyTpZJ6H2UcCpMb': [], 'var_call_5tvFAT8mlpUuOtFWGU0QwpMh': [], 'var_call_jMckq1d3SCR09bLz1k6OZ4pU': 'file_storage/call_jMckq1d3SCR09bLz1k6OZ4pU.json', 'var_call_2OazurDIeZD2sxHQurszGgTe': 'file_storage/call_2OazurDIeZD2sxHQurszGgTe.json'}

exec(code, env_args)
