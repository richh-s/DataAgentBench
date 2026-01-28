code = """import json

# Define file paths
funding_path = var_functions.query_db:0
civic_path = var_functions.query_db:2

# Load data
with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    docs = json.load(f)

print('Loaded', len(funding), 'funding records and', len(docs), 'civic docs')

# Process the data to answer the query
# The question: How many capital projects with 'design' status have funding > $50,000?

# Strategy: Iterate through funding records > $50,000 and check if they appear in civic docs as capital design projects
count = 0

for fund in funding:
    if int(fund['Amount']) > 50000:
        fund_name = fund['Project_Name']
        # Search in civic docs for this project
        for doc in docs:
            text = doc.get('text', '').lower()
            if fund_name.lower() in text:
                # Check if context indicates capital design project
                if 'capital' in text and 'design' in text:
                    count += 1
                    break

print('Answer:', count)
print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
