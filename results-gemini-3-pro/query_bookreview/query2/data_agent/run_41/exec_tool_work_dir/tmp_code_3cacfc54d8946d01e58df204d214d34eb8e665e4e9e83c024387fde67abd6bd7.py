code = """import json
import pandas as pd

# Load purchase_ids with perfect ratings
# Variable name for purchase_ids result: var_function-call-4677829308773681684
purchase_ids_data = locals()['var_function-call-4677829308773681684']
# Extract the list of IDs and normalize to match book_id format
# purchaseid_X -> bookid_X
perfect_book_ids = set()
for record in purchase_ids_data:
    pid = record['purchase_id']
    if pid.startswith('purchaseid_'):
        bid = pid.replace('purchaseid_', 'bookid_')
        perfect_book_ids.add(bid)

# Load candidate books
# Variable name for books file path: var_function-call-17913364839849121521
books_file_path = locals()['var_function-call-17913364839849121521']
with open(books_file_path, 'r') as f:
    books_data = json.load(f)

# Filter books
final_books = []
for book in books_data:
    if book['book_id'] in perfect_book_ids:
        # Check Language again just to be sure (though SQL handled it)
        details = book.get('details', '')
        if 'English' in details:
            final_books.append(book)

# Prepare result
# Return all matching books. The user asked for "Which English-language books... Return all matching books."
# Returning the list of dicts is appropriate.
print("__RESULT__:")
print(json.dumps(final_books))"""

env_args = {'var_function-call-3698189048801328799': ['books_info'], 'var_function-call-4692194811702381297': [{'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'book_id': 'bookid_1'}, {'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'book_id': 'bookid_2'}, {'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'book_id': 'bookid_3'}, {'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'book_id': 'bookid_4'}, {'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'book_id': 'bookid_5'}], 'var_function-call-2242958500640357391': ['review'], 'var_function-call-4677829308773681684': [{'purchase_id': 'purchaseid_101'}, {'purchase_id': 'purchaseid_105'}, {'purchase_id': 'purchaseid_108'}, {'purchase_id': 'purchaseid_110'}, {'purchase_id': 'purchaseid_114'}, {'purchase_id': 'purchaseid_116'}, {'purchase_id': 'purchaseid_117'}, {'purchase_id': 'purchaseid_118'}, {'purchase_id': 'purchaseid_12'}, {'purchase_id': 'purchaseid_121'}, {'purchase_id': 'purchaseid_122'}, {'purchase_id': 'purchaseid_123'}, {'purchase_id': 'purchaseid_124'}, {'purchase_id': 'purchaseid_126'}, {'purchase_id': 'purchaseid_127'}, {'purchase_id': 'purchaseid_128'}, {'purchase_id': 'purchaseid_130'}, {'purchase_id': 'purchaseid_132'}, {'purchase_id': 'purchaseid_133'}, {'purchase_id': 'purchaseid_134'}, {'purchase_id': 'purchaseid_14'}, {'purchase_id': 'purchaseid_143'}, {'purchase_id': 'purchaseid_144'}, {'purchase_id': 'purchaseid_146'}, {'purchase_id': 'purchaseid_150'}, {'purchase_id': 'purchaseid_151'}, {'purchase_id': 'purchaseid_152'}, {'purchase_id': 'purchaseid_153'}, {'purchase_id': 'purchaseid_156'}, {'purchase_id': 'purchaseid_16'}, {'purchase_id': 'purchaseid_160'}, {'purchase_id': 'purchaseid_163'}, {'purchase_id': 'purchaseid_166'}, {'purchase_id': 'purchaseid_168'}, {'purchase_id': 'purchaseid_170'}, {'purchase_id': 'purchaseid_171'}, {'purchase_id': 'purchaseid_172'}, {'purchase_id': 'purchaseid_174'}, {'purchase_id': 'purchaseid_177'}, {'purchase_id': 'purchaseid_180'}, {'purchase_id': 'purchaseid_181'}, {'purchase_id': 'purchaseid_182'}, {'purchase_id': 'purchaseid_184'}, {'purchase_id': 'purchaseid_192'}, {'purchase_id': 'purchaseid_195'}, {'purchase_id': 'purchaseid_197'}, {'purchase_id': 'purchaseid_2'}, {'purchase_id': 'purchaseid_21'}, {'purchase_id': 'purchaseid_24'}, {'purchase_id': 'purchaseid_26'}, {'purchase_id': 'purchaseid_28'}, {'purchase_id': 'purchaseid_29'}, {'purchase_id': 'purchaseid_33'}, {'purchase_id': 'purchaseid_34'}, {'purchase_id': 'purchaseid_38'}, {'purchase_id': 'purchaseid_39'}, {'purchase_id': 'purchaseid_40'}, {'purchase_id': 'purchaseid_41'}, {'purchase_id': 'purchaseid_42'}, {'purchase_id': 'purchaseid_47'}, {'purchase_id': 'purchaseid_54'}, {'purchase_id': 'purchaseid_56'}, {'purchase_id': 'purchaseid_57'}, {'purchase_id': 'purchaseid_59'}, {'purchase_id': 'purchaseid_6'}, {'purchase_id': 'purchaseid_60'}, {'purchase_id': 'purchaseid_64'}, {'purchase_id': 'purchaseid_7'}, {'purchase_id': 'purchaseid_71'}, {'purchase_id': 'purchaseid_73'}, {'purchase_id': 'purchaseid_74'}, {'purchase_id': 'purchaseid_75'}, {'purchase_id': 'purchaseid_79'}, {'purchase_id': 'purchaseid_80'}, {'purchase_id': 'purchaseid_82'}, {'purchase_id': 'purchaseid_83'}, {'purchase_id': 'purchaseid_84'}, {'purchase_id': 'purchaseid_88'}, {'purchase_id': 'purchaseid_9'}, {'purchase_id': 'purchaseid_90'}, {'purchase_id': 'purchaseid_91'}, {'purchase_id': 'purchaseid_97'}, {'purchase_id': 'purchaseid_98'}], 'var_function-call-17913364839849121521': 'file_storage/function-call-17913364839849121521.json'}

exec(code, env_args)
