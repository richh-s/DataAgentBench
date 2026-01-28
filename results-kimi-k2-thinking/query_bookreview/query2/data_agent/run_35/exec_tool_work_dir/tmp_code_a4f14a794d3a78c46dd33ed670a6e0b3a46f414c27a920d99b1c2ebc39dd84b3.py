code = """import json
import pandas as pd

# Load books data from the query result
books_file_path = var_functions.query_db:6
with open(books_file_path, 'r') as f:
    books_data = json.load(f)

# Convert to DataFrame
books_df = pd.DataFrame(books_data)

# Load reviews data from the query result
reviews_file_path = var_functions.query_db:14
with open(reviews_file_path, 'r') as f:
    reviews_data = json.load(f)

# Convert to DataFrame
reviews_df = pd.DataFrame(reviews_data)

# Ensure rating is numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'])

print("__RESULT__:")
print(f"Books count: {len(books_df)}, Reviews count: {len(reviews_df)}")
print(f"Sample books: {books_df[['book_id', 'title']].head(3).to_dict('records')}")
print(f"Sample reviews: {reviews_df[['purchase_id', 'rating']].head(3).to_dict('records')}")"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'title': 'Four Stars'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'title': 'A wonderful adventure in France'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.'}, {'purchase_id': 'purchaseid_178', 'rating': '4', 'title': 'Referance Guide'}, {'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'A Good read for Meat Eaters, and Veggie Heads as well'}, {'purchase_id': 'purchaseid_76', 'rating': '5', 'title': 'Greet book'}, {'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'For anyone except avid non-hunters.'}, {'purchase_id': 'purchaseid_115', 'rating': '5', 'title': 'Highly recommend this book if you love history of Mid Atlantic wrestling...'}, {'purchase_id': 'purchaseid_167', 'rating': '2', 'title': 'Heroine blames others for things & feels her bad behavior is justified'}], 'var_functions.query_db:12': [{'count': '1833'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
