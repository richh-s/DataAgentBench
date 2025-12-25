code = """import json
import pandas as pd
import re

# Load books data
# var_function-call-2984293492520454682 contains file path
with open(locals()['var_function-call-2984293492520454682'], 'r') as f:
    books_data = json.load(f)

# Load ratings data
# var_function-call-13536745062166533250 is a list of dicts directly (it was small enough)
ratings_data = locals()['var_function-call-13536745062166533250']

# Process ratings
perfect_rating_ids = set()
for r in ratings_data:
    pid = r['purchase_id']
    # extract number
    match = re.search(r'purchaseid_(\d+)', pid)
    if match:
        perfect_rating_ids.add(int(match.group(1)))

# Process books and filter
result_titles = []

for book in books_data:
    # 1. Check ID match first (fastest)
    bid_str = book['book_id']
    match = re.search(r'bookid_(\d+)', bid_str)
    if not match:
        continue
    bid = int(match.group(1))
    
    if bid not in perfect_rating_ids:
        continue
        
    # 2. Check Category
    cats_str = book['categories']
    try:
        cats = json.loads(cats_str)
    except:
        cats = []
    
    if "Literature & Fiction" not in cats:
        continue
        
    # 3. Check Language
    details = book.get('details', '')
    if 'English' not in details:
        continue
        
    result_titles.append(book['title'])

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-8183950526751016887': [{'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'book_id': 'bookid_1'}, {'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'book_id': 'bookid_2'}, {'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'book_id': 'bookid_3'}, {'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'book_id': 'bookid_4'}, {'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'book_id': 'bookid_5'}], 'var_function-call-13285630706825325697': ['review'], 'var_function-call-10829167773397983789': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-2984293492520454682': 'file_storage/function-call-2984293492520454682.json', 'var_function-call-13536745062166533250': [{'purchase_id': 'purchaseid_101'}, {'purchase_id': 'purchaseid_105'}, {'purchase_id': 'purchaseid_108'}, {'purchase_id': 'purchaseid_110'}, {'purchase_id': 'purchaseid_114'}, {'purchase_id': 'purchaseid_116'}, {'purchase_id': 'purchaseid_117'}, {'purchase_id': 'purchaseid_118'}, {'purchase_id': 'purchaseid_12'}, {'purchase_id': 'purchaseid_121'}, {'purchase_id': 'purchaseid_122'}, {'purchase_id': 'purchaseid_123'}, {'purchase_id': 'purchaseid_124'}, {'purchase_id': 'purchaseid_126'}, {'purchase_id': 'purchaseid_127'}, {'purchase_id': 'purchaseid_128'}, {'purchase_id': 'purchaseid_130'}, {'purchase_id': 'purchaseid_132'}, {'purchase_id': 'purchaseid_133'}, {'purchase_id': 'purchaseid_134'}, {'purchase_id': 'purchaseid_14'}, {'purchase_id': 'purchaseid_143'}, {'purchase_id': 'purchaseid_144'}, {'purchase_id': 'purchaseid_146'}, {'purchase_id': 'purchaseid_150'}, {'purchase_id': 'purchaseid_151'}, {'purchase_id': 'purchaseid_152'}, {'purchase_id': 'purchaseid_153'}, {'purchase_id': 'purchaseid_156'}, {'purchase_id': 'purchaseid_16'}, {'purchase_id': 'purchaseid_160'}, {'purchase_id': 'purchaseid_163'}, {'purchase_id': 'purchaseid_166'}, {'purchase_id': 'purchaseid_168'}, {'purchase_id': 'purchaseid_170'}, {'purchase_id': 'purchaseid_171'}, {'purchase_id': 'purchaseid_172'}, {'purchase_id': 'purchaseid_174'}, {'purchase_id': 'purchaseid_177'}, {'purchase_id': 'purchaseid_180'}, {'purchase_id': 'purchaseid_181'}, {'purchase_id': 'purchaseid_182'}, {'purchase_id': 'purchaseid_184'}, {'purchase_id': 'purchaseid_192'}, {'purchase_id': 'purchaseid_195'}, {'purchase_id': 'purchaseid_197'}, {'purchase_id': 'purchaseid_2'}, {'purchase_id': 'purchaseid_21'}, {'purchase_id': 'purchaseid_24'}, {'purchase_id': 'purchaseid_26'}, {'purchase_id': 'purchaseid_28'}, {'purchase_id': 'purchaseid_29'}, {'purchase_id': 'purchaseid_33'}, {'purchase_id': 'purchaseid_34'}, {'purchase_id': 'purchaseid_38'}, {'purchase_id': 'purchaseid_39'}, {'purchase_id': 'purchaseid_40'}, {'purchase_id': 'purchaseid_41'}, {'purchase_id': 'purchaseid_42'}, {'purchase_id': 'purchaseid_47'}, {'purchase_id': 'purchaseid_54'}, {'purchase_id': 'purchaseid_56'}, {'purchase_id': 'purchaseid_57'}, {'purchase_id': 'purchaseid_59'}, {'purchase_id': 'purchaseid_6'}, {'purchase_id': 'purchaseid_60'}, {'purchase_id': 'purchaseid_64'}, {'purchase_id': 'purchaseid_7'}, {'purchase_id': 'purchaseid_71'}, {'purchase_id': 'purchaseid_73'}, {'purchase_id': 'purchaseid_74'}, {'purchase_id': 'purchaseid_75'}, {'purchase_id': 'purchaseid_79'}, {'purchase_id': 'purchaseid_80'}, {'purchase_id': 'purchaseid_82'}, {'purchase_id': 'purchaseid_83'}, {'purchase_id': 'purchaseid_84'}, {'purchase_id': 'purchaseid_88'}, {'purchase_id': 'purchaseid_9'}, {'purchase_id': 'purchaseid_90'}, {'purchase_id': 'purchaseid_91'}, {'purchase_id': 'purchaseid_97'}, {'purchase_id': 'purchaseid_98'}]}

exec(code, env_args)
