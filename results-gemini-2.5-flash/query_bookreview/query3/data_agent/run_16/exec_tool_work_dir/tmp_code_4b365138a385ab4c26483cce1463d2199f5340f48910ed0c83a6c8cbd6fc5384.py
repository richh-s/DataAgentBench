code = """import pandas as pd
import json

books_data = pd.read_json(locals()['var_function-call-8951325410737213505'])

def parse_categories(categories_str):
    try:
        return json.loads(categories_str)
    except json.JSONDecodeError:
        return []

books_data['categories_list'] = books_data['categories'].apply(parse_categories)
childrens_books = books_data[books_data['categories_list'].apply(lambda x: 'Children\\'s Books' in x)]

__RESULT__:
print(childrens_books.to_json(orient='records'))"""

env_args = {'var_function-call-8951325410737213505': 'file_storage/function-call-8951325410737213505.json'}

exec(code, env_args)
