code = """import json, re, pandas as pd
from pathlib import Path

rev_src = var_call_4G0r7EM9AcmxIQ4hlN37g4cI
if isinstance(rev_src, str) and Path(rev_src).exists():
    reviews = json.load(open(rev_src, 'r'))
else:
    reviews = rev_src

df_rev = pd.DataFrame(reviews)
df_rev['rating'] = pd.to_numeric(df_rev.get('rating'), errors='coerce')

books = var_call_9a2pBMBAONc2bNSkXMrci6k9

def extract_year(details):
    if details is None:
        return None
    m = re.search(r'\b(19\d{2}|20\d{2})\b', str(details))
    return int(m.group(1)) if m else None

rows = []
for r in books:
    bid = r.get('book_id')
    year = extract_year(r.get('details'))
    if bid is not None and year is not None:
        rows.append({'book_id': bid, 'year': year})

df_books = pd.DataFrame(rows)

if df_books.empty:
    out = None
else:
    def extract_num(x):
        m = re.search(r'(\d+)$', str(x))
        return m.group(1) if m else None

    df_rev['num'] = df_rev['purchase_id'].map(extract_num)
    df_books['num'] = df_books['book_id'].map(extract_num)

    df = df_rev.merge(df_books[['num','book_id','year']], on='num', how='inner')
    df = df.dropna(subset=['rating','year'])
    df['decade_start'] = (df['year']//10)*10

    agg = df.groupby('decade_start').agg(
        avg_rating=('rating','mean'),
        distinct_books=('book_id','nunique')
    ).reset_index()

    agg = agg[agg['distinct_books']>=10]
    if agg.empty:
        out = None
    else:
        best = agg.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
        out = f"{int(best['decade_start'])}s"

print('__RESULT__:')
print(json.dumps({'decade': out}))"""

env_args = {'var_call_9a2pBMBAONc2bNSkXMrci6k9': [{'book_id': 'bookid_47', 'details': 'The book was published on January 1, 1986, by an unspecified publisher and is written in English.'}, {'book_id': 'bookid_53', 'details': 'This book, published by Frank Amato Publications on January 1, 1997, is written in English and features a spiral binding with a total of 31 pages. It has an ISBN-10 number of 1571880879 and an ISBN-13 number of 978-1571880871. The item weighs 3.2 ounces and has dimensions of 5.5 x 0.25 x 8.75 inches.'}, {'book_id': 'bookid_54', 'details': 'This book, published by Dover Publications on August 1, 2006, is written in English and is suitable for readers aged 8 to 9 years. It has an ISBN-10 of 0486457117 and an ISBN-13 of 978-0486457116. The book weighs 1.01 pounds and has dimensions of 5.25 x 1.5 x 8.5 inches.'}, {'book_id': 'bookid_86', 'details': 'The book, published by William Stout Publishers in its first edition on January 1, 2007, is available in English and features a hardcover format with a total of 262 pages. It has an ISBN-10 of 0974621439 and an ISBN-13 of 978-0974621432. The item weighs 5.35 pounds.'}, {'book_id': 'bookid_95', 'details': 'This book is published by Tyndale House Publishers in its 14th printing edition, released on January 1, 1985. It is written in English and comes in a paperback format, comprising 240 pages. The book has an ISBN-10 of 084236661X and an ISBN-13 of 978-0842366618. Weighing 10.4 ounces, its dimensions are 5.5 inches in width, 0.75 inches in thickness, and 8.5 inches in height.'}, {'book_id': 'bookid_123', 'details': 'The book, published by Aspen Publishers on July 27, 2010, is written in English and is available in paperback format, comprising 1,232 pages. It has an ISBN-10 number of 0735590591 and an ISBN-13 number of 978-0735590595. The item weighs 3.1 pounds and has dimensions of 7 x 1.25 x 10 inches.'}, {'book_id': 'bookid_160', 'details': 'This book, published by Scala Publishers on July 12, 2006, is available in English and spans 112 pages. It has an ISBN-10 of 1857592379 and an ISBN-13 of 978-1857592375. The item weighs 1.05 pounds and its dimensions are 8.74 x 0.41 x 8.68 inches.'}, {'book_id': 'bookid_168', 'details': 'The book, published by Harcourt School Publishers in its first edition on January 1, 2008, is available in English and consists of 179 pages. It has an ISBN-10 of 015343631X and an ISBN-13 of 978-0153436314. The item weighs 13.5 ounces.'}], 'var_call_60uZGIeorU02f963etPN1axz': ['review'], 'var_call_4G0r7EM9AcmxIQ4hlN37g4cI': 'file_storage/call_4G0r7EM9AcmxIQ4hlN37g4cI.json'}

exec(code, env_args)
