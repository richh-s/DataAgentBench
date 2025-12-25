code = """import json
import pandas as pd

# Load books info
books_file = locals()['var_function-call-11329988777974949992']
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Load reviews info
reviews_data = locals()['var_function-call-4812081073815958732']

# Process Books
books_processed = []
for b in books_data:
    # Check categories
    try:
        cats = json.loads(b['categories'])
        if "Literature & Fiction" not in cats:
            continue
    except:
        continue

    # Check language
    # Simplest check: "English" in details text.
    # Note: "English" is capitalized.
    if "English" not in b['details']:
        continue
        
    # Extract ID
    # book_id format: "bookid_X"
    bid = b['book_id']
    if bid.startswith("bookid_"):
        id_suffix = bid.split("_")[1]
        books_processed.append({
            "id_suffix": id_suffix,
            "title": b['title']
        })

# Process Reviews
reviews_ids = set()
for r in reviews_data:
    pid = r['purchase_id']
    if pid.startswith("purchaseid_"):
        id_suffix = pid.split("_")[1]
        reviews_ids.add(id_suffix)

# Join
final_titles = []
for b in books_processed:
    if b['id_suffix'] in reviews_ids:
        final_titles.append(b['title'])

print("__RESULT__:")
print(json.dumps(final_titles))"""

env_args = {'var_function-call-2373740321481844783': ['books_info'], 'var_function-call-7951502031637460914': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-11329988777974949992': 'file_storage/function-call-11329988777974949992.json', 'var_function-call-347824687725619848': ['review'], 'var_function-call-4812081073815958732': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0'}]}

exec(code, env_args)
