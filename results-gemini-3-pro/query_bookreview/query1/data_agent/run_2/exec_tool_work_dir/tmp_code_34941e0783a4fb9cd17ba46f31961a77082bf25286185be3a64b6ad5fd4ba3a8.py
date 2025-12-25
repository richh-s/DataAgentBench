code = """import json
import re
import pandas as pd

file_path_books = locals()['var_function-call-5762601890028283317']
file_path_reviews = locals()['var_function-call-5861420824831990695']

with open(file_path_books, 'r') as f:
    books_data = json.load(f)
with open(file_path_reviews, 'r') as f:
    reviews_data = json.load(f)

df_books = pd.DataFrame(books_data)
df_reviews = pd.DataFrame(reviews_data)

def extract_id(s):
    if not s: return None
    parts = s.split('_')
    if len(parts) > 1:
        return parts[-1]
    return s

df_books['id_num'] = df_books['book_id'].apply(extract_id)
df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_id)

def extract_year(text):
    if not isinstance(text, str): return None
    pub_match = re.search(r'(?:published|released).*?(\b19\d{2}|20\d{2}\b)', text, re.IGNORECASE)
    if pub_match: return int(pub_match.group(1))
    ed_match = re.search(r'edition.*?\b(19\d{2}|20\d{2})\b', text, re.IGNORECASE)
    if ed_match: return int(ed_match.group(1))
    candidates = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    if candidates: return int(candidates[0])
    return None

df_books['year'] = df_books['details'].apply(extract_year)
df_books_valid = df_books.dropna(subset=['year'])

print("__RESULT__:")
debug_info = {
    "total_books": len(df_books),
    "books_with_valid_year": len(df_books_valid),
    "sample_years": df_books_valid['year'].head(10).tolist(),
    "books_per_decade": df_books_valid['year'].apply(lambda y: int(y//10*10)).value_counts().to_dict(),
    "total_reviews": len(df_reviews),
    "sample_book_ids": df_books['id_num'].head(5).tolist(),
    "sample_review_ids": df_reviews['id_num'].head(5).tolist(),
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4991624145889692617': ['books_info'], 'var_function-call-17824524347429052940': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-6644222601643079336': [{'count': '200'}], 'var_function-call-10449438570185145554': ['review'], 'var_function-call-2425197519240266821': [{'COUNT(*)': '1833'}], 'var_function-call-5762601890028283317': 'file_storage/function-call-5762601890028283317.json', 'var_function-call-5861420824831990695': 'file_storage/function-call-5861420824831990695.json', 'var_function-call-18194477350139040333': 'No decade meets criteria'}

exec(code, env_args)
