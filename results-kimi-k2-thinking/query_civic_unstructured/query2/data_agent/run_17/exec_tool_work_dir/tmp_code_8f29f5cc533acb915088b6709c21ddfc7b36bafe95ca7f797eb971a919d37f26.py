code = """import json
import re
import pandas as pd

# Load data
civic_docs_file = globals()['var_functions.query_db:5']
funding_file = globals()['var_functions.query_db:6']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Better extraction focusing on complete project names
park_completed_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        # Look for strong indicators of project name with Park
        if re.search(r'park', line_clean, re.IGNORECASE) and len(line_clean) > 5:
            # Check if this is a clean project name (not a fragment)
            if (not line_clean.endswith('.') and 
                not line_clean.lower().startswith('to ') and
                not line_clean.lower().startswith('and ') and
                len(line_clean) < 100):  # Reasonable project name length
                
                # Check following lines for completed and 2022
                snippet = '\n'.join(lines[i:i+8])
                if (re.search(r'completed.*2022|2022.*completed', snippet, re.IGNORECASE) or
                    ('completed' in snippet.lower() and any(m in snippet for m in ['November 2022', 'December 2022', 'January 2023']))):
                    park_completed_2022.append(line_clean)
            
            # Also check specific patterns
            elif re.search(r'completed.*2022|2022.*completed', line_clean, re.IGNORECASE):
                # Extract just the project name part
                if line_clean not in ['Construction (Completed)', 'Status: Completed', 'Project Status: Completed']:
                    # This might be the project name itself
                    park_completed_2022.append(line_clean)

# Clean and deduplicate
unique_projects = []
seen = set()
for proj in park_completed_2022:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

print('Raw extracted projects:', len(unique_projects))
print('List:', unique_projects)

# Filter only clean project names (not fragments)
clean_projects = []
for proj in unique_projects:
    # Skip if it's clearly a fragment or description
    if (not proj.startswith('to ') and 
        not 'would include' in proj and
        not 'layer of the' in proj and
        not 'of the' in proj and
        len(proj.split()) >= 3):  # At least 3 words
        clean_projects.append(proj)

print('\nClean projects:', len(clean_projects))
print('List:', clean_projects)

# Match with funding records - use exact matching first
def find_funding_match(project_name, funding_df):
    matches = []
    # Exact match
    exact = funding_df[funding_df['Project_Name'].str.lower() == project_name.lower()]
    if not exact.empty:
        return exact.to_dict('records')
    
    # Partial matching for "Park" in name
    for _, row in funding_df.iterrows():
        if project_name.lower() in row['Project_Name'].lower() or row['Project_Name'].lower() in project_name.lower():
            matches.append(row.to_dict())
    return matches

# Find funding for clean projects
all_funding = []
matched_project_names = set()

for proj in clean_projects:
    matches = find_funding_match(proj, funding_df)
    for match in matches:
        all_funding.append({
            'project_name': proj,
            'funding_name': match['Project_Name'],
            'amount': match['Amount']
        })
        matched_project_names.add(proj)

print('\nMatched funding records:', len(all_funding))
for f in all_funding:
    print(f"- {f['project_name']}: ${f['amount']} ({f['funding_name']})")

# Also check funding data for projects with "Park" and completed 2022
additional_funding = []
for _, row in funding_df.iterrows():
    funding_name = row['Project_Name']
    if 'park' in funding_name.lower():
        # Check if this appears in any doc as completed 2022
        for doc in civic_docs:
            if (funding_name.lower() in doc.get('text', '').lower() and
                'completed' in doc.get('text', '').lower() and
                '2022' in doc.get('text', '')):
                additional_funding.append({
                    'project_name': 'Found in docs',
                    'funding_name': funding_name,
                    'amount': row['Amount']
                })
                break

# Combine and deduplicate by funding name
combined = {}
for f in all_funding + additional_funding:
    key = f['funding_name']
    if key not in combined:
        combined[key] = f

final_funding = list(combined.values())
total_amount = sum(f['amount'] for f in final_funding)

print('\nFinal funding records count:', len(final_funding))
print('Final total funding:', total_amount)

for f in final_funding:
    print(f"${f['amount']}: {f['funding_name']}")

result = {
    'park_projects_2022': clean_projects,
    'funding_amounts': final_funding,
    'total_funding': total_amount
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'status': 'data loaded'}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_count': 500}, 'var_functions.execute_python:22': {'park_projects_2022': ['Bluffs Park Shade Structure', 'to Malibu Bluffs Park. The project would include parking and additional site', 'layer of the playground surfacing at Trancas Canyon Park.', 'Malibu Park Drainage Improvements', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'to Malibu Bluffs Park. The project would include parking and additional site', 'layer of the playground surfacing at Trancas Canyon Park.', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'funding_records': [{'project_name': 'Bluffs Park Shade Structure', 'funding_project_name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'project_name': 'Malibu Park Drainage Improvements', 'funding_project_name': 'Malibu Park Drainage Improvements', 'amount': 17000}, {'project_name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'funding_project_name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'amount': 32000}, {'project_name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'funding_project_name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'amount': 43000}], 'total_funding': 113000}}

exec(code, env_args)
