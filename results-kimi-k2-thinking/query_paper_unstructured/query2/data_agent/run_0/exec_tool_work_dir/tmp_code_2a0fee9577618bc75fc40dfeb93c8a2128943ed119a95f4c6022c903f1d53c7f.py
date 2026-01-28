code = """import json
import pandas as pd

# Access the stored data directly using the variable names
citations_2018 = var_functions.query_db_7
paper_docs = var_functions.query_db_3

# Debug: Print first few items to check structure
print('Citations sample:', citations_2018[:2] if citations_2018 else 'No data')
print('Paper docs sample:', paper_docs[:1] if paper_docs else 'No data')"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
