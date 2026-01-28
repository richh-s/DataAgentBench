code = """import json
import re
import pandas as pd

# Load children's books and reviews
books = [{"book_id": "bookid_1", "title": "Chaucer", "categories": "[\"Books\", \"Literature & Fiction\", \"History & Criticism\"]"}, {"book_id": "bookid_2", "title": "Notes from a Kidwatcher", "categories": "[\"Books\", \"Reference\", \"Words, Language & Grammar\"]"}, {"book_id": "bookid_3", "title": "Service: A Navy SEAL at War", "categories": "[\"Books\", \"Biographies & Memoirs\", \"Leaders & Notable People\"]"}, {"book_id": "bookid_4", "title": "Monstrous Stories #4: The Day the Mice Stood Still", "categories": "[\"Books\", \"Children's Books\", \"Science Fiction & Fantasy\"]"}, {"book_id": "bookid_5", "title": "Parker & Knight", "categories": "[\"Books\", \"Mystery, Thriller & Suspense\", \"Thrillers & Suspense\"]"}]

reviews = [{"rating": "4", "title": "Ha! On me!  I thought this was a cookbook!", "purchase_id": "purchaseid_186", "review_time": "2012-11-24 18:52:00"}, {"rating": "4", "title": "Four Stars", "purchase_id": "purchaseid_191", "review_time": "2015-12-31 13:35:00"}, {"rating": "4", "title": "A wonderful adventure in France", "purchase_id": "purchaseid_190", "review_time": "2013-05-05 10:47:00"}, {"rating": "5", "title": "Best beginner book.  Been looking for something like this for a long time.", "purchase_id": "purchaseid_8", "review_time": "2020-08-12 11:06:00"}, {"rating": "4", "title": "Referance Guide", "purchase_id": "purchaseid_178", "review_time": "2014-11-13 18:55:00"}]

# Function to check if a book is in Children's category
def is_childrens_book(categories_str):
    try:
        categories = eval(categories_str)
        return "Children's Books" in categories
    except:
        return False

# Filter children's books
childrens_books = []
for book in books:
    if is_childrens_book(book['categories']):
        childrens_books.append(book)

print('__RESULT__:')
print(json.dumps(childrens_books))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.list_db:2': ['review'], 'var_functions.query_db:5': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_functions.query_db:6': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'purchase_id': 'purchaseid_186', 'review_time': '2012-11-24 18:52:00'}, {'rating': '4', 'title': 'Four Stars', 'purchase_id': 'purchaseid_191', 'review_time': '2015-12-31 13:35:00'}, {'rating': '4', 'title': 'A wonderful adventure in France', 'purchase_id': 'purchaseid_190', 'review_time': '2013-05-05 10:47:00'}, {'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'purchase_id': 'purchaseid_8', 'review_time': '2020-08-12 11:06:00'}, {'rating': '4', 'title': 'Referance Guide', 'purchase_id': 'purchaseid_178', 'review_time': '2014-11-13 18:55:00'}], 'var_functions.query_db:8': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}]}

exec(code, env_args)
