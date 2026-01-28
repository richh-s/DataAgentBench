code = """# First, let's query books with Children's Books category
books_query = """
SELECT book_id, title, categories 
FROM books_info 
WHERE categories LIKE '%Children\'s Books%'
"""

# Also query reviews from 2020 onwards
reviews_query = """
SELECT purchase_id, rating, review_time
FROM review 
WHERE review_time >= '2020-01-01'
"""

print('__RESULT__:')
print(json.dumps({
    "books_query": books_query,
    "reviews_query": reviews_query
}))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.list_db:2': ['review'], 'var_functions.query_db:5': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'categories': '["Books", "Reference", "Words, Language & Grammar"]'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]'}]}

exec(code, env_args)
