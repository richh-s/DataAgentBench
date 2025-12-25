code = """import json
import re
import pandas as pd

books_path = locals()['var_function-call-6325774532205901436']
with open(books_path, 'r') as f: books_data = json.load(f)
books_df = pd.DataFrame(books_data)

month_pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)'
date_pattern = re.compile(month_pattern + r'[\s,]+(?:(?:\d{1,2})[\s,]+)?(\d{4})', re.IGNORECASE)

def extract_year(details):
    if not isinstance(details, str): return None
    match = date_pattern.search(details)
    return int(match.group(1)) if match else None

books_df['year'] = books_df['details'].apply(extract_year)
missing_year = books_df[books_df['year'].isna()]['details'].head(10).tolist()

print("__RESULT__:")
print(json.dumps(missing_year))"""

env_args = {'var_function-call-13006791733557201821': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-15627107773603411334': ['review'], 'var_function-call-8627314569768500697': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-6325774532205901436': 'file_storage/function-call-6325774532205901436.json', 'var_function-call-9221213419928042691': 'file_storage/function-call-9221213419928042691.json', 'var_function-call-128572507644170288': {'decade': '2020s', 'avg_rating': 4.663636363636364, 'distinct_books': 21}, 'var_function-call-9595701592515954116': [{'decade_str': '1930s', 'distinct_books': 2, 'avg_rating': 5.0}, {'decade_str': '1940s', 'distinct_books': 1, 'avg_rating': 5.0}, {'decade_str': '2020s', 'distinct_books': 21, 'avg_rating': 4.663636363636364}, {'decade_str': '2010s', 'distinct_books': 88, 'avg_rating': 4.608591885441528}, {'decade_str': '1970s', 'distinct_books': 2, 'avg_rating': 4.285714285714286}, {'decade_str': '2000s', 'distinct_books': 47, 'avg_rating': 4.276223776223776}, {'decade_str': '1880s', 'distinct_books': 1, 'avg_rating': 4.25}, {'decade_str': '1980s', 'distinct_books': 11, 'avg_rating': 4.208333333333333}, {'decade_str': '1990s', 'distinct_books': 16, 'avg_rating': 3.8208955223880596}]}

exec(code, env_args)
