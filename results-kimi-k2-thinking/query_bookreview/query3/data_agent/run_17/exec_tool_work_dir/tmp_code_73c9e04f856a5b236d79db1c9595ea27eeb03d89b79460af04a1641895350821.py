code = """import json

# Sample data from the previous queries
books_sample = [{"book_id": "bookid_1", "title": "Chaucer", "categories": '["Books", "Literature & Fiction", "History & Criticism"]'}, 
                {"book_id": "bookid_2", "title": "Notes from a Kidwatcher", "categories": '["Books", "Reference", "Words, Language & Grammar"]'}, 
                {"book_id": "bookid_4", "title": "Monstrous Stories #4: The Day the Mice Stood Still", "categories": '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}]

reviews_sample = [{"purchase_id": "purchaseid_186", "title": "Ha! On me!  I thought this was a cookbook!", "rating": "4", "review_time": "2012-11-24 18:52:00"},
                  {"purchase_id": "purchaseid_8", "title": "Best beginner book.  Been looking for something like this for a long time.", "rating": "5", "review_time": "2020-08-12 11:06:00"}]

# Check children's books
childrens_books = []
for book in books_sample:
    categories = json.loads(book['categories'])
    if "Children's Books" in categories:
        childrens_books.append(book)

print('__RESULT__:')
print(json.dumps(childrens_books, indent=2))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.list_db:1': ['review'], 'var_functions.query_db:4': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}], 'var_functions.query_db:5': [{'purchase_id': 'purchaseid_186', 'title': 'Ha! On me!  I thought this was a cookbook!', 'rating': '4', 'review_time': '2012-11-24 18:52:00'}, {'purchase_id': 'purchaseid_191', 'title': 'Four Stars', 'rating': '4', 'review_time': '2015-12-31 13:35:00'}, {'purchase_id': 'purchaseid_190', 'title': 'A wonderful adventure in France', 'rating': '4', 'review_time': '2013-05-05 10:47:00'}, {'purchase_id': 'purchaseid_8', 'title': 'Best beginner book.  Been looking for something like this for a long time.', 'rating': '5', 'review_time': '2020-08-12 11:06:00'}, {'purchase_id': 'purchaseid_178', 'title': 'Referance Guide', 'rating': '4', 'review_time': '2014-11-13 18:55:00'}]}

exec(code, env_args)
