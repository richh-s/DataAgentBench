code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-9228085530283185054'], 'r') as f:
    books_data = json.load(f)

with open(locals()['var_function-call-1997033837490250050'], 'r') as f:
    reviews_data = json.load(f)

# Process Books
book_decades = {}
# Improved regex: Month (Day,)? Year
date_pattern = re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(?:\d{1,2},?\s+)?(\d{4})', re.IGNORECASE)

for book in books_data:
    b_id_str = book['book_id']
    match = re.search(r'bookid_(\d+)', b_id_str)
    if match:
        b_id = int(match.group(1))
        
        details = book.get('details', '')
        # Search for first date
        date_match = date_pattern.search(details)
        if date_match:
            year = int(date_match.group(2))
            decade_val = (year // 10) * 10
            decade_str = f"{decade_val}s"
            book_decades[b_id] = decade_str

# Process Reviews
book_ratings_list = {} # book_id -> list of ratings

for review in reviews_data:
    p_id_str = review['purchase_id']
    rating = float(review['rating'])
    
    match = re.search(r'purchaseid_(\d+)', p_id_str)
    if match:
        p_id = int(match.group(1))
        
        if p_id in book_decades:
            if p_id not in book_ratings_list:
                book_ratings_list[p_id] = []
            book_ratings_list[p_id].append(rating)

# Aggregate
decade_metrics = {}

for b_id, ratings in book_ratings_list.items():
    decade = book_decades[b_id]
    
    if decade not in decade_metrics:
        decade_metrics[decade] = {
            'all_ratings': [],
            'book_averages': []
        }
    
    decade_metrics[decade]['all_ratings'].extend(ratings)
    decade_metrics[decade]['book_averages'].append(sum(ratings)/len(ratings))

results = []
for decade, metrics in decade_metrics.items():
    num_books = len(metrics['book_averages'])
    if num_books >= 10:
        avg_rating_all = sum(metrics['all_ratings']) / len(metrics['all_ratings'])
        avg_rating_books = sum(metrics['book_averages']) / len(metrics['book_averages'])
        results.append({
            'decade': decade,
            'average_rating_all': avg_rating_all,
            'average_rating_books': avg_rating_books,
            'num_books': num_books
        })

results.sort(key=lambda x: x['average_rating_all'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17856659061725383219': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-11151910933134896868': [{'count': '200'}], 'var_function-call-12221250218822420543': ['review'], 'var_function-call-4201403886222267313': [{'COUNT(*)': '1833'}], 'var_function-call-9228085530283185054': 'file_storage/function-call-9228085530283185054.json', 'var_function-call-1997033837490250050': 'file_storage/function-call-1997033837490250050.json', 'var_function-call-11410058371541896141': [{'decade': '2020s', 'average_rating': 4.663636363636364, 'num_books': 21}, {'decade': '2010s', 'average_rating': 4.608591885441528, 'num_books': 88}, {'decade': '2000s', 'average_rating': 4.273684210526316, 'num_books': 46}, {'decade': '1980s', 'average_rating': 4.208333333333333, 'num_books': 11}, {'decade': '1990s', 'average_rating': 3.838235294117647, 'num_books': 17}]}

exec(code, env_args)
