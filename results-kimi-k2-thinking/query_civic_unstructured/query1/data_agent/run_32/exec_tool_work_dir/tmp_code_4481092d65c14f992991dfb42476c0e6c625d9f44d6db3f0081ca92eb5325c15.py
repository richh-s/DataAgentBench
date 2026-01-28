code = """import json, sys

# Get the data from storage
civic_docs = var_functions.query_db:5
funding_data = var_functions.query_db:30

# Print type info for debugging
print('Types:', type(civic_docs), type(funding_data))

# Try simple approach - if it's a list, work with it directly
if isinstance(civic_docs, list) and isinstance(funding_data, list):
    funded = {rec['Project_Name']: int(rec['Amount']) for rec in funding_data}
    count = 0
    
    for doc in civic_docs:
        txt = doc.get('text', '')
        # Look for capital design projects
        if 'Capital Improvement Projects (Design)' in txt:
            # Extract section
            lines = txt.split('\n')
            in_design = False
            for line in lines:
                if 'Capital Improvement Projects (Design)' in line:
                    in_design = True
                elif 'Capital Improvement Projects (Construction)' in line:
                    in_design = False
                elif in_design and line.strip() in funded:
                    count += 1
    
    print('__RESULT__:')
    print(count)
else:
    print('__RESULT__:')
    print(0)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
