code = """import json

# Access the funding data from the stored result
funding_data = var_functions.query_db:84

# Access the civic documents from the stored result
civic_docs = var_functions.query_db:6

# Process the data directly (they should be lists, not file paths)
print('Funding data type:', type(funding_data))
print('Civic docs type:', type(civic_docs))

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    # It's a file path, load it
    funding_records = json.load(open(funding_data))
else:
    # It's the actual data
    funding_records = funding_data

if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    # It's a file path, load it
    civic_documents = json.load(open(civic_docs))
else:
    # It's the actual data
    civic_documents = civic_docs

# Build funding map
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_records}

# Find design projects
all_design = set()
for doc in civic_documents:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        for line in text.split('\n'):
            line = line.strip()
            if line and len(line) > 10 and line[0].isalpha():
                all_design.add(line)

# Count matches
matched = 0
for proj in all_design:
    for funded in funding_map:
        if funding_map[funded] > 50000:
            p = proj.lower()
            f = funded.lower()
            if p in f or f in p:
                if abs(len(proj) - len(funded)) < 40:
                    matched += 1
                    break

result = dict(count=matched)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': []}

exec(code, env_args)
