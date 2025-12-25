code = """import json
import pandas as pd
import re

# Load data
with open(var_function_call_5580944683610533376, 'r') as f:
    books_data = json.load(f)

with open(var_function_call_5580944683610532767, 'r') as f:
    reviews_data = json.load(f)

df_books = pd.DataFrame(books_data)
df_reviews = pd.DataFrame(reviews_data)

# Extract numeric id from book_id and purchase_id
# Assuming book_id is like 'bookid_1' and purchase_id is like 'purchaseid_1'
def extract_id(s):
    if not s: return None
    m = re.search(r'_(\d+)$', s)
    if m:
        return int(m.group(1))
    return None

df_books['id_num'] = df_books['book_id'].apply(extract_id)
df_reviews['id_num'] = df_reviews['purchase_id'].apply(extract_id)

# Parse year from details
def extract_year(details):
    if not details:
        return None
    # Pattern: Look for 4 digits starting with 19 or 20
    # Prefer years after 'published' or 'released'
    # Simple approach first: find all years
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
    
    # Refined approach: look for year associated with date patterns or "published"
    # Regex to find "published ... YYYY" or "released ... YYYY"
    # Limiting the distance to avoid picking up ISBNs if they happen to start with 19/20 (less likely for ISBN-13 usually 978)
    
    # Let's try to find a year that is part of a date string or near 'published'
    # "January 1, 2004"
    # "May 20, 1996"
    # "released on ... 2004"
    
    # Search for year in the whole string. If multiple, we need logic.
    # Usually the publication year is the one mentioned in "published on ..."
    
    match = re.search(r'(?:published|released).*?(\d{4})', details, re.IGNORECASE)
    if match:
        y = int(match.group(1))
        if 1900 <= y <= 2025:
            return y
    
    # Fallback: Just find any valid year
    for y_str in years:
        y = int(y_str)
        if 1900 <= y <= 2025:
            return y
            
    return None

df_books['year'] = df_books['details'].apply(extract_year)

# Drop books without year or id
df_books = df_books.dropna(subset=['year', 'id_num'])

# Join reviews
# Ensure rating is numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
df_reviews = df_reviews.dropna(subset=['id_num', 'rating'])

# Merge
merged = pd.merge(df_reviews, df_books, on='id_num', how='inner')

# Calculate decade
merged['decade'] = (merged['year'] // 10) * 10
merged['decade_str'] = merged['decade'].astype(int).astype(str) + "s"

# Group by decade
# We need:
# 1. Number of distinct books rated.
# 2. Average rating.

decade_stats = merged.groupby('decade_str').agg(
    distinct_books=('id_num', 'nunique'),
    avg_rating=('rating', 'mean')
).reset_index()

# Filter decades with >= 10 distinct books
valid_decades = decade_stats[decade_stats['distinct_books'] >= 10]

# Find max avg rating
if not valid_decades.empty:
    best_decade = valid_decades.loc[valid_decades['avg_rating'].idxmax()]
    result = best_decade['decade_str']
else:
    result = "No decade meets criteria"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7970652068856732905': ['books_info'], 'var_function-call-7970652068856733106': ['review'], 'var_function-call-10927987280028368897': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'description': '[]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'description': '["About the Author", "SANDRA WILDE, Ph.D., is widely recognized for her expertise in developmental spelling and her advocacy of holistic approaches to spelling and phonics. She is Professor of Curriculum and Instruction at Portland State University in Oregon. She is best known for her work in invented spelling, phonics and miscue analysis. She specializes in showing teachers how kids\' invented spellings and miscues can help us work with them in more sophisticated and learner-centered ways. Looking at what kids do as they read and write is at the heart of Sandra\'s presentations and workshops. She can do lively keynote presentations that highlight the interesting things that we can learn by paying close attention to students\' invented spellings and miscues, as well as workshops of varying lengths that focus on student-centered teaching of spelling and phonics. She has recently begun offering workshops that focus on understanding students\' miscues as a guide to appropriate instruction, p"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'description': '["Review", "Praise for SERVICE\\"An action-packed...reflective saga of contemporary military service.\\"―", "Kirkus Reviews", "\\"Marcus Luttrell, with James D. Hornfischer, has written another emotional story that the reader will not want to put down.\\"―", "American Thinker", "About the Author", "Marcus Luttrell", "became a combat-trained Navy SEAL in 2002 and served in many dangerous Special Operations assignments around the world. He is the author of the", "New York Times", "bestseller", "Lone Survivor", ", and is a popular corporate and organizational speaker. He lives near Houston, Texas.\xa0James D. Hornfischer\xa0is the author of four bestselling books on the U.S. Navy in World War II,", "The Fleet at Flood", "Tide", ",", "Neptune\'s", "Inferno, Ship of Ghosts,", "and", "The Last Stand of the Tin Can Sailors,", "winner of the Samuel Eliot Morison Award. He lives in Austin, Texas."]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'description': '[]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'description': '[]'}], 'var_function-call-8909836039816690815': [{'count': '200'}], 'var_function-call-8909836039816688776': [{'COUNT(*)': '1833'}], 'var_function-call-5580944683610533376': 'file_storage/function-call-5580944683610533376.json', 'var_function-call-5580944683610532767': 'file_storage/function-call-5580944683610532767.json'}

exec(code, env_args)
