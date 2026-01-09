code = """import json, re, pandas as pd

def load_json(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

books_details = load_json(var_call_nvaDshaicaOfIFWDNZmwWAUP)
reviews = load_json(var_call_TRwC4U8JAOWpknTbtmNakY08)

bd = pd.DataFrame(books_details)
rv = pd.DataFrame(reviews)

rv['rating'] = pd.to_numeric(rv['rating'], errors='coerce')
rv = rv.dropna(subset=['rating','purchase_id'])

# Map purchaseid_### -> bookid_### (fuzzy join per hint)
rv['book_id'] = rv['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# extract publication year from details
pat = re.compile(r'\b(1[5-9]\d{2}|20\d{2})\b')

def extract_year(s):
    if s is None:
        return None
    s = str(s)
    # prefer years near keywords
    m = re.search(r'(?i)(published|publication date|publisher|first edition|reprint edition|edition)\D{0,40}?(1[5-9]\d{2}|20\d{2})', s)
    if m:
        return int(m.group(2))
    # else any year
    m2 = pat.search(s)
    if m2:
        return int(m2.group(1))
    return None

bd['pub_year'] = bd['details'].apply(extract_year)
bd = bd.dropna(subset=['pub_year'])
bd['decade_start'] = (bd['pub_year']//10)*10
bd['decade'] = bd['decade_start'].astype(int).astype(str) + 's'

# join
j = rv.merge(bd[['book_id','decade']], on='book_id', how='inner')

# restrict to decades with at least 10 distinct books rated
agg = j.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id', pd.Series.nunique),
    n_ratings=('rating','size')
).reset_index()

eligible = agg[agg['distinct_books'] >= 10]
if eligible.empty:
    result = None
else:
    best = eligible.sort_values(['avg_rating','distinct_books','n_ratings'], ascending=[False,False,False]).iloc[0]
    result = {'decade': str(best['decade']), 'avg_rating': float(best['avg_rating']), 'distinct_books': int(best['distinct_books'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_HeJHZ90rebESmWG0Wbw0lR9M': 'file_storage/call_HeJHZ90rebESmWG0Wbw0lR9M.json', 'var_call_ob6DCRkCNsJKPRK3kKIfHTKI': 'file_storage/call_ob6DCRkCNsJKPRK3kKIfHTKI.json', 'var_call_HJIceP1Wxrj5kWhIv0eJqdzD': [{'book_id': 'bookid_53', 'details': 'This book, published by Frank Amato Publications on January 1, 1997, is written in English and features a spiral binding with a total of 31 pages. It has an ISBN-10 number of 1571880879 and an ISBN-13 number of 978-1571880871. The item weighs 3.2 ounces and has dimensions of 5.5 x 0.25 x 8.75 inches.'}, {'book_id': 'bookid_54', 'details': 'This book, published by Dover Publications on August 1, 2006, is written in English and is suitable for readers aged 8 to 9 years. It has an ISBN-10 of 0486457117 and an ISBN-13 of 978-0486457116. The book weighs 1.01 pounds and has dimensions of 5.25 x 1.5 x 8.5 inches.'}, {'book_id': 'bookid_127', 'details': 'This book is published by Bonanza Books in a reprint edition dated January 1, 1930. It is written in English and is available in hardcover with a total of 204 pages. The ISBN-10 for the book is 0517202484, while its ISBN-13 is 978-0517202487. The item weighs 1.95 pounds.'}, {'book_id': 'bookid_136', 'details': 'The book "Cooking for the Rushed; Revised and Updated Edition," published on December 1, 2010, is available in English and features a paperback format consisting of 192 pages. It has an ISBN-10 of 0968522637 and an ISBN-13 of 978-0968522639. The item weighs 1.65 pounds and its dimensions are 5.11 x 1.11 x 8.11 inches.'}, {'book_id': 'bookid_144', 'details': 'The book is published by Baen in a reissue edition dated September 25, 2018. It is written in English and is available as a mass market paperback, consisting of 528 pages. The ISBN-10 for this edition is 1481483536, while the ISBN-13 is 978-1481483537. The item weighs 8.8 ounces and has dimensions of 4.13 x 1.3 x 6.75 inches.'}], 'var_call_nvaDshaicaOfIFWDNZmwWAUP': 'file_storage/call_nvaDshaicaOfIFWDNZmwWAUP.json', 'var_call_nSHwMQmkypF2pNi08mYmR49E': ['review'], 'var_call_TRwC4U8JAOWpknTbtmNakY08': 'file_storage/call_TRwC4U8JAOWpknTbtmNakY08.json'}

exec(code, env_args)
