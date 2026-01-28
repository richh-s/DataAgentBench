code = """import json
import pandas as pd

# Access the stored variables properly
books_result = locals()['var_functions.query_db:4']
reviews_result = locals()['var_functions.query_db:5']

# Check if results are file paths or direct data
if isinstance(books_result, str) and books_result.endswith('.json'):
    with open(books_result, 'r') as f:
        books_data = json.load(f)
else:
    books_data = books_result
    
if isinstance(reviews_result, str) and reviews_result.endswith('.json'):
    with open(reviews_result, 'r') as f:
        reviews_data = json.load(f)
else:
    reviews_data = reviews_result

result_dict = {
    'books_count': len(books_data),
    'reviews_count': len(reviews_data),
    'first_book': books_data[0] if books_data else None,
    'first_review': reviews_data[0] if reviews_data else None
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}], 'var_functions.query_db:6': [{'total_books': '200'}]}

exec(code, env_args)
