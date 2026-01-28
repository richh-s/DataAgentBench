code = """import json
import pandas as pd
import numpy as np

# Get all Literature & Fiction books (without English filter for completeness)
books_result = locals().get('var_functions.query_db:22')
if isinstance(books_result, str):
    with open(books_result, 'r') as f:
        books_result = json.load(f)

# Get all reviews
reviews_result = locals().get('var_functions.query_db:14')
if isinstance(reviews_result, str):
    with open(reviews_result, 'r') as f:
        reviews_result = json.load(f)

# Create DataFrames
books_df = pd.DataFrame(books_result)
reviews_df = pd.DataFrame(reviews_result)

# Convert rating to numeric
reviews_df['rating_numeric'] = pd.to_numeric(reviews_df['rating'])

# Transform purchase_id to book_id (purchaseid_X -> bookid_X)
reviews_df['book_id'] = reviews_df['purchase_id'].str.replace('purchaseid_', 'bookid_')

# Calculate average rating and review count for each book
book_stats = reviews_df.groupby('book_id').agg(
    avg_rating=('rating_numeric', 'mean'),
    review_count=('rating_numeric', 'count')
).reset_index()

# Round avg_rating to 1 decimal to handle floating point precision
book_stats['avg_rating_rounded'] = book_stats['avg_rating'].round(1)

# Find books with perfect 5.0 rating
perfect_books = book_stats[book_stats['avg_rating_rounded'] == 5.0]

# Merge with books data
perfect_books_with_details = pd.merge(
    perfect_books, 
    books_df, 
    on='book_id', 
    how='inner'
)

# Filter for English-language books (check details for 'English')
english_perfect_books = perfect_books_with_details[
    perfect_books_with_details['details'].str.contains('English', case=False, na=False)
]

# Extract English language info more reliably
english_perfect_books = english_perfect_books.copy()
english_perfect_books['language'] = 'English'

# Sort by review count descending, then by title
english_perfect_books = english_perfect_books.sort_values(
    ['review_count', 'title'], 
    ascending=[False, True]
)

# Select relevant columns
result_df = english_perfect_books[[
    'book_id', 
    'title', 
    'avg_rating', 
    'review_count',
    'categories',
    'details'
]]

# Convert to list of dictionaries
result_list = result_df.to_dict('records')

# Create final response
final_output = {
    "total_books_found": len(result_list),
    "books": result_list
}

print("__RESULT__:")
print(json.dumps(final_output, indent=2))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'text': "I loved this book all the way until the end. I have recently discovered that the author is intending to release another book, and from what I understand it will continue where this one left off. I am thankful for this, as the way this book ended was definitely a negative for me. I wanted to know more! What happened to the author, did she learn what she came to learn? Did she get the job she was hoping for? So many questions.<br /><br />From the beginning of Linda's book, it is easy to love her. She is open, honest and definitely has the type of personality you want your heroine to have, whether the book is fiction or reality. I couldn't help but root for Linda throughout her trials with her host family, even when I thought she acted as a bit of a brat herself. Listening to her internal thoughts about what she went through and her desire to achieve her goals made this book feel close to my heart.<br /><br />I applaud the adventurous spirit of the author and her decision to keep journal entries from that chapter of her life. What great material to have later to inspire a book! While I enjoyed the entire memoir, my favourite part of this book would have to be the author's descriptions of the many places she visited and the people she met along the way. While I think she could definitely have made a better impression on the family she worked for if she had been honest about her lack of French language skills from the beginning, she is a pioneer. Her drive and desire to learn the language from those in the actual country was inspiring. Not many people would have been gutsy enough to do what Linda did.<br /><br />I also particularly enjoyed the relationship between Linda and Antoine. The Kind heart of the author was apparent in her actions toward the children, even when she struggled with them.<br /><br />There is some romance, and I appreciated the way the author handled it. While sex scenes are not necessarily automatically offensive, there is something about memoirs that makes me uncomfortable if they are filled with them. This author manages to hint at her experiences without going into too much detail, leaving the reader to decide exactly what happened. Great writing.<br /><br />When you step into reading this book, you learn a lot about French customs, French cuisine and wine. You also get the opportunity to brush up on your French skills a bit and get to step outside yourself and live an adventure through the eyes of the author. I read this book in one sitting with very few breaks in between and found myself enthralled in the sights, sounds and atmosphere of this memoir.<br /><br />In the end, I was disappointed that the book ended. I could have kept reading about Linda's experiences without stopping anytime in the foreseeable future. The end of the book leaves many unanswered questions, that I am assuming the author will be answering in her next book. Were this a standalone, I would be very disappointed with the way the book ended, but with the knowledge that she is writing another book to continue with her story, I can't fault this one. One thing is for sure, if you read this book, you will be anxiously awaiting the next.<br /><br />I would recommend this to anyone who likes books about travel, memoirs or just a good story that came from the recollections and heart of the author. Read it, you will be glad you did. Overall, this was a VERY enjoyable read that gave me many reasons to wish I could drop everything and head off to France!", 'review_time': '2013-05-05 10:47:00', 'helpful_vote': '1', 'verified_purchase': '0', 'purchase_id': 'purchaseid_190'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'text': "Looked online for years for something like this.  It's the best I've seen.", 'review_time': '2020-08-12 11:06:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_8'}, {'rating': '4', 'title': 'Referance Guide', 'text': 'Good reference guide for the basics', 'review_time': '2014-11-13 18:55:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_178'}], 'var_functions.execute_python:12': {'lit_fiction_book_ids': ['bookid_1', 'bookid_9', 'bookid_13', 'bookid_30', 'bookid_36', 'bookid_37', 'bookid_38', 'bookid_39', 'bookid_44', 'bookid_49', 'bookid_55', 'bookid_69', 'bookid_70', 'bookid_74', 'bookid_77', 'bookid_82', 'bookid_84', 'bookid_89', 'bookid_92', 'bookid_93', 'bookid_98', 'bookid_99', 'bookid_101', 'bookid_106', 'bookid_109', 'bookid_111', 'bookid_122', 'bookid_137', 'bookid_142', 'bookid_144', 'bookid_161', 'bookid_167', 'bookid_171', 'bookid_177', 'bookid_179', 'bookid_180', 'bookid_182', 'bookid_187', 'bookid_188', 'bookid_195'], 'count': 40}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'perfect_rating_books': [{'book_id': 'bookid_74', 'title': 'Child Of The King A Journey of Hope Book 1: Earthly Story With A Heavenly Message', 'avg_rating': 5.0, 'review_count': 8, 'categories': '["Books", "Literature & Fiction"]', 'details': 'This book, published by Self Publishing on December 1, 2022, is written in English and comprises 192 pages. It has an ISBN 13 of 979-8887592497 and weighs 8.8 ounces. The dimensions of the book are 5.5 by 0.48 by 8.5 inches.'}, {'book_id': 'bookid_144', 'title': 'Forged in Blood (Freehold)', 'avg_rating': 5.0, 'review_count': 6, 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]', 'details': 'The book is published by Baen in a reissue edition dated September 25, 2018. It is written in English and is available as a mass market paperback, consisting of 528 pages. The ISBN-10 for this edition is 1481483536, while the ISBN-13 is 978-1481483537. The item weighs 8.8 ounces and has dimensions of 4.13 x 1.3 x 6.75 inches.'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'avg_rating': 5.0, 'review_count': 4, 'categories': '["Books", "Literature & Fiction", "Poetry"]', 'details': 'The book, published by Suzeteo Enterprises on February 14, 2019, is available in English and consists of 48 pages. It has an ISBN-10 of 1947844938 and an ISBN-13 of 978-1947844933. The Lexile measure for this book is 990L. Weighing 2.08 ounces, its dimensions are 5 inches in width, 0.1 inches in thickness, and 8 inches in height.'}, {'book_id': 'bookid_171', 'title': 'Exits, Desires, & Slow Fires', 'avg_rating': 5.0, 'review_count': 3, 'categories': '["Books", "Literature & Fiction", "Poetry"]', 'details': 'The book, published by CreateSpace Independent Publishing Platform in its first edition on September 20, 2017, is written in English and consists of 83 pages. It has an ISBN 10 of 154710435X and an ISBN 13 of 978-1547104352. The item weighs 3.2 ounces and has dimensions of 5 x 0.21 x 8 inches.'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'avg_rating': 5.0, 'review_count': 3, 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.'}, {'book_id': 'bookid_195', 'title': 'Something That Feels Like Truth (Switchgrass Books)', 'avg_rating': 5.0, 'review_count': 2, 'categories': '["Books", "Literature & Fiction", "Short Stories & Anthologies"]', 'details': 'This book, published by Northern Illinois University Press in its first edition on September 1, 2013, is available in English and is presented in paperback format with a total of 290 pages. It has an ISBN-10 of 9780875806938 and an ISBN-13 of 978-0875806938. Suitable for readers aged 18 years and older, the book weighs 11.7 ounces and its dimensions are 5 x 0.9 x 8 inches.'}, {'book_id': 'bookid_101', 'title': 'Knowing When To Die: Uncollected Stories', 'avg_rating': 5.0, 'review_count': 2, 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'details': 'This book, published by Independent Legions Publishing in its first edition on June 19, 2018, is written in English and spans 216 pages. It is available in paperback and has an ISBN-10 of 8831959018 and an ISBN-13 of 978-8831959018. The item weighs 9.9 ounces and has dimensions of 5.5 x 0.54 x 8.5 inches.'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'avg_rating': 5.0, 'review_count': 2, 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]', 'details': 'This book, published independently on February 19, 2023, is written in English and spans 257 pages in paperback format. It has an ISBN 13 of 979-8378201969 and weighs 14.1 ounces. The dimensions of the book are 5.5 x 0.65 x 8.5 inches.'}, {'book_id': 'bookid_82', 'title': 'Fire Cracker', 'avg_rating': 5.0, 'review_count': 2, 'categories': '["Books", "Literature & Fiction", "United States"]', 'details': 'This book, published by Kensington on July 1, 1997, is available in English and features a paperback format with a total of 312 pages. It has an ISBN-10 of 1575661810 and an ISBN-13 of 978-1575661810. The item weighs 1.3 pounds and its dimensions are 6.25 inches in width, 1.25 inches in thickness, and 9.5 inches in height.'}, {'book_id': 'bookid_84', 'title': 'Local Honey', 'avg_rating': 5.0, 'review_count': 2, 'categories': '["Books", "Literature & Fiction"]', 'details': 'This book, published by Xlibris on June 26, 2015, is written in English and spans 166 pages in paperback format. It has an ISBN 10 of 1503581098 and an ISBN 13 of 978-1503581098. The item weighs 8.8 ounces and has dimensions of 6 x 0.42 x 9 inches.'}, {'book_id': 'bookid_122', 'title': 'Childe Harold of Dysna', 'avg_rating': 5.0, 'review_count': 1, 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'The book, published by Naydus Press on July 27, 2021, is written in English and features a paperback format consisting of 80 pages. It has an ISBN 10 of 1734193603 and an ISBN 13 of 978-1734193602. Weighing 4 ounces, the book measures 4.9 by 0.3 by 7.8 inches.'}, {'book_id': 'bookid_182', 'title': 'Liza of Lambeth', 'avg_rating': 5.0, 'review_count': 1, 'categories': '["Books", "Literature & Fiction", "Classics"]', 'details': 'This book, published independently on June 1, 2020, is available in English and comprises 125 pages in paperback format. It has an ISBN 13 of 979-8650407126 and weighs 6.9 ounces. The dimensions of the book are 6 x 0.32 x 9 inches.'}, {'book_id': 'bookid_180', 'title': 'The Sludge', 'avg_rating': 5.0, 'review_count': 1, 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'details': 'The book, published by Great Old Ones Publishing in its first edition on July 5, 2016, is written in English and consists of 198 pages. It has an ISBN-10 of 0692726446 and an ISBN-13 of 978-0692726440. Weighing 10.4 ounces, the book measures 6 inches in width, 0.5 inches in thickness, and 9 inches in height.'}, {'book_id': 'bookid_177', 'title': 'Kennebago Moments', 'avg_rating': 5.0, 'review_count': 1, 'categories': '["Books", "Literature & Fiction", "Poetry"]', 'details': "This book, published by CreateSpace Independent Publishing Platform on November 24, 2010, is written in English and has a total of 52 pages. It is available in paperback format and weighs 3.2 ounces. The book's dimensions are 5.98 x 0.12 x 9.02 inches. It can be identified by its ISBN 10 number, 1453850171, and its ISBN 13 number, 978-1453850176."}, {'book_id': 'bookid_98', 'title': 'Hollywood Confessions: Hollywood Headlines Book #3 (Hollywood Headlines Mysteries)', 'avg_rating': 5.0, 'review_count': 1, 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'details': 'This book, published by CreateSpace Independent Publishing Platform on May 31, 2011, is written in English and features a paperback format consisting of 209 pages. It has an ISBN 10 number of 1463534795 and an ISBN 13 number of 978-1463534790. The item weighs 7.8 ounces and has dimensions of 5.25 x 0.48 x 8 inches.'}], 'total_count': 15}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
