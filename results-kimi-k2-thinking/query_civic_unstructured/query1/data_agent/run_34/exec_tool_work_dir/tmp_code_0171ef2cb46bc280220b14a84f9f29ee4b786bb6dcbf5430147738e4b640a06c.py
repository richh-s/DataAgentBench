code = """import json, pandas as pd, re

# Load data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_functions.query_db:12'], 'r') as f:
    civic_data = json.load(f)

# Process funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Extract all design projects systematically
design_projects = []
for doc in civic_data:
    text = doc['text']
    # Find boundaries
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start > 0 and construction_start > design_start:
        design_section = text[design_start:construction_start]
        # Extract lines that are project names (uppercase titles followed by marker)
        lines = design_section.splitlines()
        for i in range(len(lines)-1):
            line = lines[i].strip()
            next_line = lines[i+1].strip() if i+1 < len(lines) else ''
            if (line and 
                any(c.isupper() for c in line[:5]) and
                '(cid:190)' in next_line and
                len(line) > 10 and
                not '(' in line[:3]):
                # Also check if this is truly a project name by seeing if it's capitalized
                words = line.split()
                if len(words) >= 2 and sum(1 for w in words[:3] if w[0].isupper()) >= 2:
                    design_projects.append(line)

# Remove exact duplicates
design_projects = list(set(design_projects))

# Find matches with funding > 50000
matched = []
for idx, row in funding_df.iterrows():
    if row['Amount'] > 50000:
        proj_name = row['Project_Name']
        if proj_name in design_projects:
            matched.append({'name': proj_name, 'amount': row['Amount']})

print('__RESULT__:')
print(json.dumps({
    'design_projects_extracted': len(design_projects),
    'funding_projects_over_50k': len(funding_df[funding_df['Amount'] > 50000]),
    'matches': matched,
    'count': len(matched)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_length': 38, 'civic_length': 39}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_documents': 5, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'count': 2, 'projects': ['Birdview Avenue Improvements (CalOES Project)', 'Point Dume Walkway Repairs']}}

exec(code, env_args)
