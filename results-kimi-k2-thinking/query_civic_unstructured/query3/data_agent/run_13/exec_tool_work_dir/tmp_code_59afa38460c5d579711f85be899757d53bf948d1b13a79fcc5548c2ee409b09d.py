code = """import json

# Load MongoDB results
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Now let's extract project information
# We'll search for projects related to emergency/FEMA in both datasets

relevant_funding = []
for rec in funding_data:
    project_name = rec.get('Project_Name', '').lower()
    funding_source = rec.get('Funding_Source', '').lower()
    if 'emergency' in project_name or 'fema' in project_name or 'emergency' in funding_source:
        relevant_funding.append(rec)

print('Relevant funding records found:', len(relevant_funding))

# Let's also extract projects from civic documents
# For now, let's just save our progress
output = {
    'relevant_funding': relevant_funding,
    'civic_docs_count': len(civic_docs)
}

# Print in the required format
import json as js
print('__RESULT__:')
print(js.dumps(output))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
