code = """import json

funding_path = var_functions.query_db_6
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Get projects with funding > 50000
funding_over_50k = [f for f in funding_data if f['Amount'] > 50000]
print('Records > 50000:', len(funding_over_50k))

# Try to access mongo data
mongo_path = var_functions.query_db_2
with open(mongo_path, 'r') as f:
    mongo_data = json.load(f)

print('Mongo document count:', len(mongo_data))

# Debug first doc
first_doc = mongo_data[0]
text = first_doc.get('text', '')
print('First doc text length:', len(text))
print('Has Design section:', 'Capital Improvement Projects (Design)' in text)

__RESULT__:
print(json.dumps({'funding_over_50k_count': len(funding_over_50k), 'mongo_docs': len(mongo_data)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
