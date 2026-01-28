code = """import json
import re

# Load books data
books_file = locals()['var_functions.query_db:5']
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Extract numeric IDs from book_ids
book_id_map = {}
for book in books_data:
    book_id = book['book_id']
    match = re.match(r'bookid_(\d+)', book_id)
    if match:
        numeric_id = match.group(1)
        book_id_map[numeric_id] = {
            'book_id': book_id,
            'title': book['title'],
            'author': book['author'],
            'categories': book['categories']
        }

print('Books in Literature & Fiction:', len(book_id_map))
print('Sample mapping:', list(book_id_map.items())[:3])

# Generate purchase_ids for review query
purchase_ids = [f'purchaseid_{num}' for num in book_id_map.keys()]
print('Total purchase IDs to check:', len(purchase_ids))

# Prepare for export
result = {
    'book_count': len(book_id_map),
    'purchase_ids': purchase_ids,
    'book_map': book_id_map
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'num_books': 40, 'total_book_ids': 40, 'first_few_book_ids': ['bookid_1', 'bookid_9', 'bookid_13', 'bookid_30', 'bookid_36']}, 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'num_reviews': '15'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'num_reviews': '14'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'num_reviews': '11'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'num_reviews': '8'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'num_reviews': '6'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'num_reviews': '4'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'num_reviews': '3'}, {'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'num_reviews': '2'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'num_reviews': '2'}], 'var_functions.query_db:18': [{'book_id': 'bookid_1', 'title': 'Chaucer'}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher'}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War'}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still'}, {'book_id': 'bookid_5', 'title': 'Parker & Knight'}, {'book_id': 'bookid_6', 'title': 'Writings from a Black Woman Living in the Land of the "Free": Strength, Power, Resilience'}, {'book_id': 'bookid_7', 'title': "Child Development: A Practitioner's Guide:2nd (Second) edition"}, {'book_id': 'bookid_8', 'title': 'Make: Electronics: Learning Through Discovery'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park'}, {'book_id': 'bookid_10', 'title': 'Four Centuries of American Education'}]}

exec(code, env_args)
