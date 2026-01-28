code = """import json
import pandas as pd
import os

# Load the full books data from the file
books_file = var_functions.query_db:12
df_books = pd.read_json(books_file)

print("Books loaded:", len(df_books))

# Find books in Literature & Fiction category
def is_literature_fiction(categories_str):
    if pd.isna(categories_str):
        return False
    try:
        # Parse the string representation of list
        categories_list = eval(categories_str)
        return "Literature & Fiction" in categories_list
    except:
        return False

# Apply filter
lit_fiction_books = df_books[df_books['categories'].apply(is_literature_fiction)]
print("Literature & Fiction books:", len(lit_fiction_books))

# Get their book_ids
lit_fiction_book_ids = lit_fiction_books['book_id'].tolist()
print("First 10 book IDs:", lit_fiction_book_ids[:10])

# Create a mapping of book_id to title for later
book_id_to_title = dict(zip(lit_fiction_books['book_id'], lit_fiction_books['title']))

# Print results in required format
result = {
    'lit_fiction_book_ids': lit_fiction_book_ids,
    'book_id_to_title': book_id_to_title
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': [{'title': 'Chaucer', 'book_id': 'bookid_1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'rating_number': '29'}, {'title': 'Notes from a Kidwatcher', 'book_id': 'bookid_2', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'rating_number': '1'}, {'title': 'Service: A Navy SEAL at War', 'book_id': 'bookid_3', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'rating_number': '3421'}, {'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'book_id': 'bookid_4', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'rating_number': '40'}, {'title': 'Parker & Knight', 'book_id': 'bookid_5', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'rating_number': '381'}, {'title': 'Writings from a Black Woman Living in the Land of the "Free": Strength, Power, Resilience', 'book_id': 'bookid_6', 'categories': '["Books", "Arts & Photography", "History & Criticism"]', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.', 'rating_number': '5'}, {'title': "Child Development: A Practitioner's Guide:2nd (Second) edition", 'book_id': 'bookid_7', 'categories': '["Books", "Parenting & Relationships", "Parenting"]', 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.', 'rating_number': '2'}, {'title': 'Make: Electronics: Learning Through Discovery', 'book_id': 'bookid_8', 'categories': '["Books", "Engineering & Transportation", "Engineering"]', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.', 'rating_number': '1366'}, {'title': 'Reunion: The Children of Lauderdale Park', 'book_id': 'bookid_9', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.', 'rating_number': '12'}, {'title': 'Four Centuries of American Education', 'book_id': 'bookid_10', 'categories': '["Books", "Education & Teaching", "Schools & Teaching"]', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.', 'rating_number': '133'}], 'var_functions.query_db:10': [{'categories': '["Books", "Literature & Fiction", "Dramas & Plays"]'}, {'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]'}, {'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'categories': '["Books", "Literature & Fiction", "Classics"]'}, {'categories': '["Books", "Literature & Fiction"]'}, {'categories': '["Books", "Literature & Fiction", "Contemporary"]'}, {'categories': '["Books", "Literature & Fiction", "Mythology & Folk Tales"]'}, {'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'categories': '["Books", "Children\'s Books", "Literature & Fiction"]'}, {'categories': '["Books", "Literature & Fiction", "United States"]'}, {'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'categories': '["Books", "Christian Books & Bibles", "Literature & Fiction"]'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
