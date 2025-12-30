code = """import json

# Load the result from the previous query_db call
with open(locals()['var_function-call-14549722995805523735'], 'r') as f:
    data = json.load(f)

# data is a list of records. We took limit 1.
doc = data[0]
text = doc['text']

print("__RESULT__:")
print(json.dumps({
    "filename": doc['filename'],
    "preview": text[:2000],
    "has_empirical": "empirical" in text.lower(),
    "has_contribution": "contribution" in text.lower()
}))"""

env_args = {'var_function-call-14549722995805523735': 'file_storage/function-call-14549722995805523735.json', 'var_function-call-9109662763408237056': ['Citations', 'sqlite_sequence'], 'var_function-call-6745088051019410329': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}]}

exec(code, env_args)
