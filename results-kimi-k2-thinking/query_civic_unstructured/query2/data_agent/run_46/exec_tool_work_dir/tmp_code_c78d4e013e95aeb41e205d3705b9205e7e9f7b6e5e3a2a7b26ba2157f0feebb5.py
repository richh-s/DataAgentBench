code = """import json
import re

# Read data from storage keys
civic_docs_file = '../var_functions.query_db:8'
funding_file = '../var_functions.query_db:10'

import sys
if len(sys.argv) > 0:
    pass

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# From the document preview, identify park projects completed in 2022
text_content = str(docs)

# Look for specific patterns based on the preview
candidates = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair', 
    'Point Dume Walkway Repairs'
]

# Check which ones have 2022 completion
completed_2022 = []
for cand in candidates:
    if cand in text_content and '2022' in text_content:
        # Verify it's actually completed in 2022
        before = text_content.find(cand)
        after = text_content[before:before+500]
        if 'completed' in after.lower() and '2022' in after:
            completed_2022.append(cand)

# Get funding amounts
total=0
matched=[]
for proj in completed_2022:
    key=proj.lower().replace(' ','')
    if key in funding_lookup:
        amt=funding_lookup[key]
        total+=amt
        matched.append({'project':proj,'amount':amt})

print('__RESULT__:')
print(json.dumps({'total_funding':total,'projects':matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
