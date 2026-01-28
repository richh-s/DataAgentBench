code = """import json

# Query funding database for all disaster projects
# Disaster projects contain FEMA, CalOES, or CalJPIA

funding_data = var_functions.query_db_66
print(f"Total funding records: {len(funding_data)}")

# Filter for disaster projects
disaster_projects = []
for record in funding_data:
    project_name = record['Project_Name'].upper()
    if 'FEMA' in project_name or 'CALOES' in project_name or 'CALJPIA' in project_name:
        disaster_projects.append({
            'name': record['Project_Name'],
            'amount': int(record['Amount']),
            'id': record['Funding_ID']
        })

print(f"Found {len(disaster_projects)} disaster projects")

# Query civic documents
print("\nAnalyzing civic documents...")
civic_docs = var_functions.query_db_50

# Projects mentioned in documents with 2022 and disaster context
doc_projects_2022 = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_upper = line.upper()
        
        # Check if this line mentions both 2022 and disaster indicators
        if '2022' in line and any(indicator in line_upper for indicator in ['FEMA', 'CALOES', 'CALJPIA']):
            # Look back/forwards for project name
            for lookback in range(max(0, i-3), i):
                prev_line = lines[lookback].strip()
                if (len(prev_line) > 10 and 
                    prev_line == prev_line.title() and 
                    not prev_line.startswith('(') and 
                    not prev_line.isupper()):
                    doc_projects_2022[prev_line] = True
                    break
            
        elif '2022' in line and i > 0:
            # Check if previous line is a project name in disaster context
            prev_line = lines[i-1].strip()
            if (len(prev_line) > 10 and 
                prev_line == prev_line.title() and 
                not prev_line.startswith('(')):
                
                # Check surrounding context for disaster indicators
                context_start = max(0, i-5)
                context_end = min(len(lines), i+5)
                context = ' '.join(lines[context_start:context_end])
                context_upper = context.upper()
                
                if any(indicator in context_upper for indicator in ['FEMA', 'CALOES', 'CALJPIA']):
                    doc_projects_2022[prev_line] = True

print(f"Found {len(doc_projects_2022)} potential 2022 disaster projects in documents")
for proj in doc_projects_2022:
    print(f"  - {proj}")

# Try to match document projects with funding data
matched_projects = []
for doc_proj in doc_projects_2022:
    doc_proj_clean = doc_proj.split('(')[0].strip().lower()
    
    for fund_proj in disaster_projects:
        fund_name_clean = fund_proj['name'].split('(')[0].strip().lower()
        
        # Check if they match
        if doc_proj_clean == fund_name_clean or doc_proj_clean in fund_name_clean or fund_name_clean in doc_proj_clean:
            matched_projects.append(fund_proj)
            print(f"Matched: '{doc_proj}' -> '{fund_proj['name']}'")

# Also include projects that explicitly have 2022 in their funding name
explicit_2022 = []
for proj in disaster_projects:
    if '2022' in proj['name']:
        explicit_2022.append(proj)
        print(f"Found explicit 2022 disaster project: {proj['name']}")

# Combine matches
all_matches = {}
for proj in matched_projects + explicit_2022:
    all_matches[proj['id']] = proj

total_funding = sum(proj['amount'] for proj in all_matches.values())
num_projects = len(all_matches)

print(f"\n{'='*60}")
print(f"FINAL RESULT:")
print(f"Total 2022 Disaster Projects: {num_projects}")
print(f"Total Funding: ${total_funding:,}")
print(f"\nProject Details:")
for proj in all_matches.values():
    print(f"  - {proj['name']}: ${proj['amount']:,}")

# Result dictionary
result = {
    'total_funding': total_funding,
    'num_projects': num_projects,
    'projects': list(all_matches.values())
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:64': {'error': 'Data access failed'}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': []}

exec(code, env_args)
