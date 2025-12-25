code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-4026345379581364922'], 'r') as f:
    books_data = json.load(f)

books_df = pd.DataFrame(books_data)

print("__RESULT__:")
sample = books_df['details'].head(5).tolist()
matches = []
for s in sample:
    m = re.findall(r'\b(19\d{2}|20\d{2})\b', str(s))
    matches.append((s, m))

print(json.dumps(matches))"""

env_args = {'var_function-call-12529152152854367773': ['books_info'], 'var_function-call-12529152152854365124': ['review'], 'var_function-call-6311656691598576275': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'title': 'Chaucer'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'title': 'Notes from a Kidwatcher'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'title': 'Service: A Navy SEAL at War'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'title': 'Parker & Knight'}], 'var_function-call-6311656691598576288': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-10657165289891689323': [{'cnt': '200'}], 'var_function-call-10657165289891691338': [{'cnt': '1833'}], 'var_function-call-4026345379581364922': 'file_storage/function-call-4026345379581364922.json', 'var_function-call-4026345379581363023': 'file_storage/function-call-4026345379581363023.json', 'var_function-call-6368653580204674794': 'No decade meets the criteria', 'var_function-call-2092849460664914225': {'total_books': 200, 'books_with_year': 0, 'years_sample': [], 'decade_counts_books': {}, 'total_reviews': 1833, 'reviews_matched': 1833, 'merged_rows': 0}}

exec(code, env_args)
