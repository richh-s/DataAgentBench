code = """import json

f_file = globals()['var_functions.query_db:4']
c_file = globals()['var_functions.query_db:5']

with open(f_file) as f:
    funding = json.load(f)
with open(c_file) as f:
    civic = json.load(f)

# Build funded projects dict (amount > 50000)
funded = {}
for rec in funding:
    if int(rec['Amount']) > 50000:
        funded[rec['Project_Name']] = int(rec['Amount'])

# Find distinct capital design projects with funding
capital_design_projects = set()

for doc in civic:
    txt = doc.get('text', '')
    txt_lower = txt.lower()
    
    # Check if document contains capital improvement design section
    if 'capital improvement' in txt_lower and 'design' in txt_lower:
        lines = txt.split('\n')
        for line in lines:
            line_clean = line.strip()
            # Check if this is likely a project name (not empty, starts uppercase, in funded list)
            if line_clean and line_clean[0].isupper() and line_clean in funded:
                # Verify this appears in a design context
                line_pos = txt.find(line_clean)
                if line_pos > 0:
                    context = txt[line_pos:line_pos+500].lower()
                    if 'design' in context:
                        capital_design_projects.add(line_clean)

result = {'distinct_count': len(capital_design_projects), 'projects': sorted(list(capital_design_projects))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'var_functions.execute_python:20': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding_name': 'Birdview Avenue Improvements'}, 'var_functions.execute_python:22': {'projects_with_funding': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:24': {'funding_projects': 276, 'message': 'Loaded funding data'}, 'var_functions.execute_python:26': {'total_funding_projects': 276, 'funding_dict_size': 276}, 'var_functions.execute_python:46': {'count': 62, 'sample': ['PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Permanent Skate Park']}}

exec(code, env_args)
