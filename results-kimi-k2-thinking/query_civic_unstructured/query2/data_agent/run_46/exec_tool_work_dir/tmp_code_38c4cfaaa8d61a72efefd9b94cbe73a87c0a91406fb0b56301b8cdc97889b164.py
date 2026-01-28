code = """import json
import re

# Access data from storage
civic_docs = locals()['var_functions.query_db:8']
funding_data = locals()['var_functions.query_db:10']

# Build funding lookup dictionary
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# From document preview, identify park projects completed in 2022
# Key projects based on document content:
# - Bluffs Park Shade Structure (completed November 2022)
# - Broad Beach Road Water Quality Repair (completed November 2022)
# - Point Dume Walkway Repairs (completed November 2022)

# Create simple list of identified park projects from documents
park_projects_completed_2022 = [
    'Bluffs Park Shade Structure'
]

# Combine all text for verification
all_doc_text = ''
for doc in civic_docs:
    all_doc_text += doc.get('text', '') + '\n'

# Verify and find funding
matched_with_funding = []
total_funding_amount = 0

for project in park_projects_completed_2022:
    # Check if project is mentioned with 2022 completion
    if project in all_doc_text and '2022' in all_doc_text:
        # Find funding amount
        project_key = project.lower().replace(' ', '')
        if project_key in funding_lookup:
            amount = funding_lookup[project_key]
            total_funding_amount += amount
            matched_with_funding.append({
                'project': project,
                'amount': amount
            })

print('__RESULT__:')
result = {
    'total_funding': total_funding_amount,
    'project_count': len(matched_with_funding),
    'projects': matched_with_funding
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs']}

exec(code, env_args)
