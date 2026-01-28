code = """import json

# Load the sample records
db_file = '/tmp/patent_dbs/publication_database.db'

# Check if file exists
import os
print("File exists:", os.path.exists(db_file))

# Check file size
print("File size:", os.path.getsize(db_file) if os.path.exists(db_file) else "File not found")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_uc_patents': 8, 'sample_pub_numbers': ['US-202117472182-A', 'TW-107142982-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'patents_with_citations': 5}}

exec(code, env_args)
