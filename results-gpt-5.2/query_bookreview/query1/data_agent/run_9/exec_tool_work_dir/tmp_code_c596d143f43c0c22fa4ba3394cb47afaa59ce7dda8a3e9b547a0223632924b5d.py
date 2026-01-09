code = """import json, pandas as pd, re

def load(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

reviews = load(var_call_jhGuny2dK3ig7QI5RN3UwoXH)
books = load(var_call_C8GPXR8kk4qdfTdYDuKfP6TM)

df_r = pd.DataFrame(reviews)
df_r['purchase_id_num'] = df_r['purchase_id'].str.extract(r'(\d+)').astype(int)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# parse publication year from details text
pat_year = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')

def extract_year(txt):
    if not isinstance(txt, str):
        return None
    # prefer years near keywords
    lower = txt.lower()
    # find all year occurrences
    years = [int(y) for y in pat_year.findall(txt)]
    if not years:
        return None
    # if contains 'published' or 'released' or 'publication'
    keys = ['published', 'released', 'publication', 'first edition', 'edition']
    best = None
    best_score = -1
    for m in pat_year.finditer(txt):
        y = int(m.group(0))
        start = max(0, m.start()-40)
        end = min(len(txt), m.end()+40)
        window = lower[start:end]
        score = sum(k in window for k in keys)
        if score > best_score:
            best_score = score
            best = y
    return best if best is not None else years[0]

b = pd.DataFrame(books)
b['book_id_num'] = b['book_id'].str.extract(r'(\d+)').astype(int)
b['pub_year'] = b['details'].apply(extract_year)

# fuzzy join via numeric suffix mapping purchaseid_n -> bookid_n
merged = df_r.merge(b[['book_id_num','pub_year']], left_on='purchase_id_num', right_on='book_id_num', how='inner')
merged = merged.dropna(subset=['pub_year','rating'])
merged['decade_start'] = (merged['pub_year']//10)*10
merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'

# at least 10 distinct books that have been rated in that decade
# distinct books: book_id_num
by = merged.groupby('decade').agg(
    avg_rating=('rating','mean'),
    distinct_books=('book_id_num','nunique')
).reset_index()
by = by[by['distinct_books']>=10]
by = by.sort_values(['avg_rating','distinct_books'], ascending=[False, False])
result = None
if len(by):
    result = by.iloc[0]['decade']

print('__RESULT__:')
print(json.dumps({'decade': result}))"""

env_args = {'var_call_C8GPXR8kk4qdfTdYDuKfP6TM': 'file_storage/call_C8GPXR8kk4qdfTdYDuKfP6TM.json', 'var_call_BfoAqBQyU3hHpZa2BroDXZFO': 'file_storage/call_BfoAqBQyU3hHpZa2BroDXZFO.json', 'var_call_dpjgng3eO3nO329gmIFjQHnq': [{'book_id': 'bookid_47', 'details': 'The book was published on January 1, 1986, by an unspecified publisher and is written in English.'}, {'book_id': 'bookid_86', 'details': 'The book, published by William Stout Publishers in its first edition on January 1, 2007, is available in English and features a hardcover format with a total of 262 pages. It has an ISBN-10 of 0974621439 and an ISBN-13 of 978-0974621432. The item weighs 5.35 pounds.'}, {'book_id': 'bookid_95', 'details': 'This book is published by Tyndale House Publishers in its 14th printing edition, released on January 1, 1985. It is written in English and comes in a paperback format, comprising 240 pages. The book has an ISBN-10 of 084236661X and an ISBN-13 of 978-0842366618. Weighing 10.4 ounces, its dimensions are 5.5 inches in width, 0.75 inches in thickness, and 8.5 inches in height.'}, {'book_id': 'bookid_127', 'details': 'This book is published by Bonanza Books in a reprint edition dated January 1, 1930. It is written in English and is available in hardcover with a total of 204 pages. The ISBN-10 for the book is 0517202484, while its ISBN-13 is 978-0517202487. The item weighs 1.95 pounds.'}, {'book_id': 'bookid_123', 'details': 'The book, published by Aspen Publishers on July 27, 2010, is written in English and is available in paperback format, comprising 1,232 pages. It has an ISBN-10 number of 0735590591 and an ISBN-13 number of 978-0735590595. The item weighs 3.1 pounds and has dimensions of 7 x 1.25 x 10 inches.'}, {'book_id': 'bookid_136', 'details': 'The book "Cooking for the Rushed; Revised and Updated Edition," published on December 1, 2010, is available in English and features a paperback format consisting of 192 pages. It has an ISBN-10 of 0968522637 and an ISBN-13 of 978-0968522639. The item weighs 1.65 pounds and its dimensions are 5.11 x 1.11 x 8.11 inches.'}, {'book_id': 'bookid_144', 'details': 'The book is published by Baen in a reissue edition dated September 25, 2018. It is written in English and is available as a mass market paperback, consisting of 528 pages. The ISBN-10 for this edition is 1481483536, while the ISBN-13 is 978-1481483537. The item weighs 8.8 ounces and has dimensions of 4.13 x 1.3 x 6.75 inches.'}, {'book_id': 'bookid_160', 'details': 'This book, published by Scala Publishers on July 12, 2006, is available in English and spans 112 pages. It has an ISBN-10 of 1857592379 and an ISBN-13 of 978-1857592375. The item weighs 1.05 pounds and its dimensions are 8.74 x 0.41 x 8.68 inches.'}, {'book_id': 'bookid_168', 'details': 'The book, published by Harcourt School Publishers in its first edition on January 1, 2008, is available in English and consists of 179 pages. It has an ISBN-10 of 015343631X and an ISBN-13 of 978-0153436314. The item weighs 13.5 ounces.'}], 'var_call_i51Ocq0fCMW2Dy7uYbW2J3Z2': ['review'], 'var_call_jhGuny2dK3ig7QI5RN3UwoXH': 'file_storage/call_jhGuny2dK3ig7QI5RN3UwoXH.json'}

exec(code, env_args)
