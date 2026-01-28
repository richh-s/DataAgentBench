code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

books = load_records(var_call_TwTbYNooHxpb1PFzg2Mfua20)

year_re = re.compile(r"\b(19\d{2}|20\d{2})\b")

cnt_year_found = 0
sample=[]
for r in books[:200]:
    d=r.get('details','')
    ys=year_re.findall(d)
    if ys:
        cnt_year_found += 1
        if len(sample)<5:
            sample.append({'details': d, 'ys': ys})

print('__RESULT__:')
print(json.dumps({'n': len(books[:200]), 'with_year': cnt_year_found, 'sample': sample}))"""

env_args = {'var_call_jMkFlOuc59m05cKrFcBdHNzh': 'file_storage/call_jMkFlOuc59m05cKrFcBdHNzh.json', 'var_call_bI9Q294bak9ak7apqvZONiKS': 'file_storage/call_bI9Q294bak9ak7apqvZONiKS.json', 'var_call_3DuR13sc2CwOcoAXrRhoqU4p': ['review'], 'var_call_e9DyEWiH6hw0IEZyWFFYVICh': 'file_storage/call_e9DyEWiH6hw0IEZyWFFYVICh.json', 'var_call_LqFZLY7jnubHTpUQ2uTB5OQt': {'decade': None, 'error': 'No publication years parsed from books details.'}, 'var_call_TwTbYNooHxpb1PFzg2Mfua20': 'file_storage/call_TwTbYNooHxpb1PFzg2Mfua20.json', 'var_call_95nEpNhKu65G97VKOKdm8WZn': {'decade': None, 'error': 'No publication years parsed from books details (full set).'}, 'var_call_25Pg2cBnkDZ8up4wRgPx2sFB': {'books_total_preview': 200, 'details_none': 0, 'details_with_year': 0, 'sample': []}, 'var_call_xGeKUcq1jkl0i3bFnAiOmlla': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_call_QNg6HkOhsIoWY4wnjlefExZx': {'found': []}, 'var_call_2GEuSZOxw2oxLkHIBVFPcAnK': {'m1': ['2004'], 'm2': ['2004'], 'ord': [74, 97, 110, 117, 97, 114, 121, 32, 49, 44, 32, 50, 48, 48, 52]}, 'var_call_mFwrsDxmT1d4ZbKBSRzuiSNg': {'findall': ['2004'], 'pat': '\\b(19\\d{2}|20\\d{2})\\b'}}

exec(code, env_args)
