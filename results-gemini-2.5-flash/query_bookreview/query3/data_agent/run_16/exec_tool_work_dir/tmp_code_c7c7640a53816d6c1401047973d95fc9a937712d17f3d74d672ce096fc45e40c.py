code = """import pandas as pd
import json

books_data = pd.read_json(locals()['var_function-call-8951325410737213505'])

childrens_books = books_data[books_data['categories'].str.contains("Children's Books")]

__RESULT__:
print(childrens_books.to_json(orient='records'))"""

env_args = {'var_function-call-8951325410737213505': 'file_storage/function-call-8951325410737213505.json'}

exec(code, env_args)
