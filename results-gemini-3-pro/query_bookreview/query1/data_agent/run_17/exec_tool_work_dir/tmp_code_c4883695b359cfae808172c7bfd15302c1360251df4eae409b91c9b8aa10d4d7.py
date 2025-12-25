code = """import pandas as pd
import json
import re

debug_info = []

try:
    books_path = locals()['var_function-call-2854040385375366253']
    reviews_path = locals()['var_function-call-8076026722880818786']
    
    with open(books_path, 'r') as f:
        books_data = json.load(f)
    debug_info.append("Books loaded: " + str(len(books_data)))
    if books_data:
        debug_info.append("Sample book: " + str(books_data[0]))

    with open(reviews_path, 'r') as f:
        reviews_data = json.load(f)
    debug_info.append("Reviews loaded: " + str(len(reviews_data)))
    if reviews_data:
        debug_info.append("Sample review: " + str(reviews_data[0]))

    book_rows = []
    for b in books_data:
        b_id_str = b.get('book_id', '')
        m_id = re.search(r'bookid_(\d+)', b_id_str)
        if m_id:
            b_id = int(m_id.group(1))
            details = b.get('details', '')
            # Regex for year
            matches = re.findall(r'\b(19\d{2}|20[0-2]\d)\b', details)
            if matches:
                year = int(matches[0])
                book_rows.append({'id': b_id, 'year': year})
    
    debug_info.append("Book rows extracted: " + str(len(book_rows)))
    if book_rows:
        debug_info.append("Sample extracted book: " + str(book_rows[0]))

    review_rows = []
    for r in reviews_data:
        p_id_str = r.get('purchase_id', '')
        m_id = re.search(r'purchaseid_(\d+)', p_id_str)
        if m_id:
            p_id = int(m_id.group(1))
            rating = r.get('rating')
            if rating is not None:
                review_rows.append({'id': p_id, 'rating': float(rating)})
    
    debug_info.append("Review rows extracted: " + str(len(review_rows)))
    if review_rows:
        debug_info.append("Sample extracted review: " + str(review_rows[0]))

    books_df = pd.DataFrame(book_rows)
    reviews_df = pd.DataFrame(review_rows)
    
    merged = pd.merge(reviews_df, books_df, on='id', how='inner')
    debug_info.append("Merged rows: " + str(len(merged)))
    
    if not merged.empty:
        merged['decade'] = (merged['year'] // 10) * 10
        merged['decade_str'] = merged['decade'].astype(str) + 's'
        decade_stats = merged.groupby('decade_str').agg(
            avg_rating=('rating', 'mean'),
            distinct_books=('id', 'nunique')
        ).reset_index()
        debug_info.append("Decade stats:\n" + decade_stats.to_string())
        
        filtered = decade_stats[decade_stats['distinct_books'] >= 10].sort_values('avg_rating', ascending=False)
        debug_info.append("Filtered stats:\n" + filtered.to_string())
        
        if not filtered.empty:
            result = filtered.iloc[0]['decade_str']
        else:
            result = "No decade"
    else:
        result = "Merged empty"

except Exception as e:
    debug_info.append("Error: " + str(e))
    result = "Error"

print('__RESULT__:')
print(json.dumps({"result": result, "debug": debug_info}))"""

env_args = {'var_function-call-18285819101688998563': ['books_info'], 'var_function-call-5145458456639782822': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'title': 'Chaucer'}, {'book_id': 'bookid_2', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'title': 'Notes from a Kidwatcher'}, {'book_id': 'bookid_3', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'title': 'Service: A Navy SEAL at War'}, {'book_id': 'bookid_4', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_5', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'title': 'Parker & Knight'}], 'var_function-call-17929056958116322902': ['review'], 'var_function-call-17752187517382031100': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-16756112236562577240': [{'count': '200'}], 'var_function-call-11434732551085023285': [{'count(*)': '1833'}], 'var_function-call-2854040385375366253': 'file_storage/function-call-2854040385375366253.json', 'var_function-call-8076026722880818786': 'file_storage/function-call-8076026722880818786.json', 'var_function-call-12568867168959983259': 'debug'}

exec(code, env_args)
