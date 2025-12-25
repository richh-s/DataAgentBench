code = """import json
import pandas as pd
import re

# Load books data
with open(locals()['var_function-call-9691461039886443860'], 'r') as f:
    books_data = json.load(f)

# Load reviews data
with open(locals()['var_function-call-11309326900241549733'], 'r') as f:
    reviews_data = json.load(f)

df_books = pd.DataFrame(books_data)
df_reviews = pd.DataFrame(reviews_data)

# Filter books
def is_lit_fiction(cats_str):
    try:
        cats = json.loads(cats_str)
        if isinstance(cats, list):
            return "Literature & Fiction" in cats
        return False
    except:
        return False

def is_english(details_str):
    if not isinstance(details_str, str):
        return False
    # Check for "English" in details. 
    # Usually "written in English" or "available in English".
    # Being safe, just checking if "English" word is present might be enough given the preview, 
    # but let's be slightly more specific if possible or just check "English".
    # Preview: "is written in English", "available in English"
    return "English" in details_str

df_books['is_target_cat'] = df_books['categories'].apply(is_lit_fiction)
df_books['is_english'] = df_books['details'].apply(is_english)

filtered_books = df_books[df_books['is_target_cat'] & df_books['is_english']].copy()

# Extract numeric ID from book_id
# Format: bookid_123
def extract_id(s):
    if pd.isna(s): return None
    match = re.search(r'(\d+)$', s)
    if match:
        return int(match.group(1))
    return None

filtered_books['id_num'] = filtered_books['book_id'].apply(extract_id)

# Process reviews
# Convert rating to float
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Extract numeric ID from purchase_id
df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_id)

# Calculate average rating
avg_ratings = df_reviews.groupby('id_num')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Filter for perfect 5.0 rating
perfect_ratings = avg_ratings[avg_ratings['avg_rating'] == 5.0]

# Join
result_df = pd.merge(filtered_books, perfect_ratings, on='id_num', how='inner')

# Get titles
matching_titles = result_df['title'].tolist()

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-11363522286454655722': ['books_info'], 'var_function-call-17654425553148879647': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.'}], 'var_function-call-12769311707369777128': ['review'], 'var_function-call-8143159411005836352': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}], 'var_function-call-8580599794465530696': [{'count': '200'}], 'var_function-call-3150087587708573177': [{'count(*)': '1833'}], 'var_function-call-9691461039886443860': 'file_storage/function-call-9691461039886443860.json', 'var_function-call-11309326900241549733': 'file_storage/function-call-11309326900241549733.json'}

exec(code, env_args)
