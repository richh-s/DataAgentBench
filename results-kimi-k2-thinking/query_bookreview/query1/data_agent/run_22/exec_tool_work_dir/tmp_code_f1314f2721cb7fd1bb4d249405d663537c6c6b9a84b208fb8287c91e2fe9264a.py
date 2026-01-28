code = """import json
import re
from datetime import datetime

# Load variables properly using locals()
books_file = locals()['var_functions.query_db:8']
review_file = locals()['var_functions.query_db:10']

# Load the books data
books_dict = []
with open(books_file, 'r', encoding='utf-8') as f:
    for line in f:
        books_dict.extend(json.loads(line))

# Load the review data
review_dict = []
with open(review_file, 'r', encoding='utf-8') as f:
    for line in f:
        review_dict.extend(json.loads(line))

print('__RESULT__:')
print(json.dumps({'books_count': len(books_dict), 'reviews_count': len(review_dict)}))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
