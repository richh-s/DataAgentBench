code = """import json
import pandas as pd

books_path = var_call_pRLFf1uGnd9sIAK58vrpRrTd
reviews_path = var_call_bWD8aiXmknR4yB0zMqClK4JE
with open(books_path, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# show first 10 book records keys and sample
a = books[:10]
b = reviews[:10]

out = {'first_10_books': a, 'first_10_reviews': b, 'books_keys': list(books[0].keys()), 'reviews_keys': list(reviews[0].keys())}
print('__RESULT__:')
import json
print(json.dumps(out))"""

env_args = {'var_call_HjCwp3kP57Wi9qGfmIhDYN3p': ['books_info'], 'var_call_pRLFf1uGnd9sIAK58vrpRrTd': 'file_storage/call_pRLFf1uGnd9sIAK58vrpRrTd.json', 'var_call_6OqtxT8HeK3FLZ5u4gMbPLp4': ['review'], 'var_call_bWD8aiXmknR4yB0zMqClK4JE': 'file_storage/call_bWD8aiXmknR4yB0zMqClK4JE.json', 'var_call_4rVGdv08NLfl4bToC7WwgqbT': {'decade': None, 'avg_rating': None, 'book_count': 0}, 'var_call_2VUlZqlAGCWekiBjZqCGkLA7': {'total_books_in_books_db': 200, 'books_with_extracted_year': 0, 'decade_counts_in_books_with_year': {}, 'unique_books_in_reviews_joined_with_books': 0, 'unique_books_per_decade_in_merged': {}, 'sample_books_with_no_year': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}]}}

exec(code, env_args)
