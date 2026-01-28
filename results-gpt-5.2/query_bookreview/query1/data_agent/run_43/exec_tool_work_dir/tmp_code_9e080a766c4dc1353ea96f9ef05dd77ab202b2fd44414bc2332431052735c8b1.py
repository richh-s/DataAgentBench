code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_TwTbYNooHxpb1PFzg2Mfua20)
reviews = load_records(var_call_e9DyEWiH6hw0IEZyWFFYVICh)

year_re = re.compile(r"\\b(19\\d{2}|20\\d{2})\\b")

def extract_year(details):
    if not details:
        return None
    ys = year_re.findall(details)
    if not ys:
        return None
    return int(ys[-1])

book_year = []
for r in books:
    bid = r.get('book_id')
    if not bid:
        continue
    y = extract_year(r.get('details'))
    if y is not None:
        book_year.append({'purchase_id': bid, 'year': y})

bdf = pd.DataFrame(book_year)

rdf = pd.DataFrame(reviews)
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf = rdf.dropna(subset=['purchase_id','rating'])

if bdf.empty:
    out = {'decade': None, 'error':'No publication years parsed from books details.'}
else:
    bdf = bdf.dropna(subset=['purchase_id','year'])
    bdf = bdf[(bdf['year']>=1500) & (bdf['year']<=2026)].drop_duplicates('purchase_id')
    merged = rdf.merge(bdf, on='purchase_id', how='inner')
    merged['decade_start'] = (merged['year'].astype(int)//10)*10
    merged['decade'] = merged['decade_start'].astype(int).astype(str) + 's'
    agg_all = merged.groupby('decade').agg(avg_rating=('rating','mean'), distinct_books=('purchase_id','nunique')).reset_index()
    agg = agg_all[agg_all['distinct_books']>=10]
    if agg.empty:
        out = {'decade': None, 'error':'No decades with >=10 distinct rated books after join.', 'top_by_books': agg_all.sort_values('distinct_books', ascending=False).head(20).to_dict(orient='records')}
    else:
        best_row = agg.sort_values(['avg_rating','distinct_books'], ascending=[False, False]).iloc[0]
        out = {'decade': best_row['decade'], 'avg_rating': float(best_row['avg_rating']), 'distinct_books': int(best_row['distinct_books'])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jMkFlOuc59m05cKrFcBdHNzh': 'file_storage/call_jMkFlOuc59m05cKrFcBdHNzh.json', 'var_call_bI9Q294bak9ak7apqvZONiKS': 'file_storage/call_bI9Q294bak9ak7apqvZONiKS.json', 'var_call_3DuR13sc2CwOcoAXrRhoqU4p': ['review'], 'var_call_e9DyEWiH6hw0IEZyWFFYVICh': 'file_storage/call_e9DyEWiH6hw0IEZyWFFYVICh.json', 'var_call_LqFZLY7jnubHTpUQ2uTB5OQt': {'decade': None, 'error': 'No publication years parsed from books details.'}, 'var_call_TwTbYNooHxpb1PFzg2Mfua20': 'file_storage/call_TwTbYNooHxpb1PFzg2Mfua20.json', 'var_call_95nEpNhKu65G97VKOKdm8WZn': {'decade': None, 'error': 'No publication years parsed from books details (full set).'}, 'var_call_25Pg2cBnkDZ8up4wRgPx2sFB': {'books_total_preview': 200, 'details_none': 0, 'details_with_year': 0, 'sample': []}, 'var_call_xGeKUcq1jkl0i3bFnAiOmlla': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_call_QNg6HkOhsIoWY4wnjlefExZx': {'found': []}, 'var_call_2GEuSZOxw2oxLkHIBVFPcAnK': {'m1': ['2004'], 'm2': ['2004'], 'ord': [74, 97, 110, 117, 97, 114, 121, 32, 49, 44, 32, 50, 48, 48, 52]}, 'var_call_mFwrsDxmT1d4ZbKBSRzuiSNg': {'findall': ['2004'], 'pat': '\\b(19\\d{2}|20\\d{2})\\b'}, 'var_call_w5J7afpSGbZ2RRZy6KAJq6pE': {'n': 200, 'with_year': 0, 'sample': []}, 'var_call_NGiNs7mxxd1MjIaU5EjypQpF': {'len': 313, 'tail': '-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'repr_tail': "'-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'"}, 'var_call_LF8vVTJLG1PKekz2EchISC1j': {'years': [], 'repr': "'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English a'"}, 'var_call_m0UYqjzqBciXqS0okv1yPL9f': {'idx': 88, 'segment': 'anuary 1, 2004. It i', 'ords': [97, 110, 117, 97, 114, 121, 32, 49, 44, 32, 50, 48, 48, 52, 46, 32, 73, 116, 32, 105]}, 'var_call_FuAUAC9yjLhvRsZ1k9RmHMCQ': {'all_4digit': ['2004', '0701', '1698', '0701', '1698'], 'isbn10': []}, 'var_call_wLmAAl3iNXkEqCnY5ZwzVRh7': {'re_search': True, 're_findall': ['2004']}, 'var_call_ILZwnbd2Ry3qPC4nBHV47ODd': {'decade': None, 'error': 'No publication years parsed from books details.'}, 'var_call_4znJ7e1tJFaKg0oS81luItRq': {'with_year_in_first10': 0}, 'var_call_kunxZUgUUzwEk3b4Y4wjA4P2': {'book_id': 'bookid_1', 'years': [], 'snippet': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in'}, 'var_call_ZIs8gWzwpO77cjFYh9UXwQWT': {'pat_findall': ['2004'], 'pat2_findall': [], 'pat': '\\b(19\\d{2}|20\\d{2})\\b', 'pat2': '\x08(19\\d{2}|20\\d{2})\x08'}}

exec(code, env_args)
