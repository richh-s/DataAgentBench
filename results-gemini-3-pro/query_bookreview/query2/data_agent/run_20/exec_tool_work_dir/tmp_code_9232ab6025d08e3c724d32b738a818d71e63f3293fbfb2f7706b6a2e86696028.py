code = """import pandas as pd
import json
import re

# Load books data
with open(locals()['var_function-call-16170260137062075368'], 'r') as f:
    books_data = json.load(f)

# Load reviews data
with open(locals()['var_function-call-17100740750032186423'], 'r') as f:
    reviews_data = json.load(f)

# Process books
filtered_books = []
for book in books_data:
    cats = book.get('categories', '')
    details = book.get('details', '')
    
    # Check category
    # The category is a string representation of a list, e.g., '["Books", "Literature & Fiction", ...]'
    # We can check if "Literature & Fiction" is in the string.
    if "Literature & Fiction" not in cats:
        continue
        
    # Check language
    # Look for "English" in details.
    if "English" not in details:
        continue
        
    # Extract numeric ID
    # book_id format: "bookid_123"
    match = re.search(r'bookid_(\d+)', book['book_id'])
    if match:
        book_num_id = match.group(1)
        filtered_books.append({
            'id': book_num_id,
            'title': book['title'],
            'full_book': book
        })

# Process reviews
df_reviews = pd.DataFrame(reviews_data)
# Convert rating to float
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Extract numeric ID from purchase_id
# purchase_id format: "purchaseid_123"
def extract_id(pid):
    match = re.search(r'purchaseid_(\d+)', pid)
    return match.group(1) if match else None

df_reviews['id'] = df_reviews['purchase_id'].apply(extract_id)
df_reviews = df_reviews.dropna(subset=['id'])

# Calculate average rating
avg_ratings = df_reviews.groupby('id')['rating'].mean().reset_index()

# Filter for perfect 5.0
perfect_ratings = avg_ratings[avg_ratings['rating'] == 5.0]

# Join
# We want books that are in filtered_books and have id in perfect_ratings
perfect_ids = set(perfect_ratings['id'])
result_books = [b for b in filtered_books if b['id'] in perfect_ids]

# Prepare result
# User asked for "matching books". I will return a list of titles or book info.
# Titles seem most appropriate for "Which books...".
result_titles = [b['title'] for b in result_books]

print("__RESULT__:")
print(json.dumps(result_titles))"""

env_args = {'var_function-call-10173418647085641424': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-3578514819117847668': ['review'], 'var_function-call-4992182490688654217': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-3957210483370643278': [{'count': '200'}], 'var_function-call-15728570595496227198': [{'COUNT(*)': '1833'}], 'var_function-call-16170260137062075368': 'file_storage/function-call-16170260137062075368.json', 'var_function-call-17100740750032186423': 'file_storage/function-call-17100740750032186423.json'}

exec(code, env_args)
