code = """import json

# Load the data from files
with open('/tmp/tmpg9c5v2d2.json', 'r') as f:
    funding_data = json.load(f)

with open('/tmp/tmp5u3g0g7j.json', 'r') as f:
    civic_docs = json.load(f)

print(f"Funding data: {len(funding_data)} records")
print(f"Civic docs: {len(civic_docs)} documents")

# Find disaster projects from funding data
print("\nAnalyzing funding data...")
projects_2022_disaster = []
total_funding = 0

for record in funding_data:
    project_name = record['Project_Name'].upper()
    
    # Check if disaster project (FEMA, CALOES, CALJPIA)
    if any(kw in project_name for kw in ['FEMA', 'CALOES', 'CALJPIA']):
        amount = int(record['Amount'])
        
        # Check if 2022 project (contains 2022 in name)
        if '2022' in project_name:
            projects_2022_disaster.append({
                'Project_Name': record['Project_Name'],
                'Amount': amount
            })
            total_funding += amount

print(f"Found {len(projects_2022_disaster)} disaster projects with 2022 in name")

# Also check civic documents for additional 2022 disaster projects
print("\nAnalyzing civic documents...")

additional_projects = []
project_names = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_upper = line.upper()
        
        # Look for 2022 and disaster markers
        if '2022' in line and any(ind in line_upper for ind in ['FEMA', 'CALOES', 'CALJPIA']):
            # Look nearby for project name
            for lookback in range(max(0, i-2), min(len(lines), i+3)):
                proj_line = lines[lookback].strip()
                if (len(proj_line) > 10 and 
                    proj_line == proj_line.title() and 
                    not proj_line.startswith('(') and 
                    not proj_line.isupper()):
                    project_names.add(proj_line)
                    break

print(f"Found {len(project_names)} project names in documents with 2022+disaster context")

# Try to match document projects with funding data
for doc_project_name in project_names:
    # Look for matching funding record
    doc_proj_clean = doc_project_name.split('(')[0].strip().upper()
    
    for fund_record in funding_data:
        fund_name_upper = fund_record['Project_Name'].upper()
        fund_name_clean = fund_name_upper.split('(')[0].strip()
        
        if (doc_proj_clean in fund_name_clean or 
            fund_name_clean in doc_proj_clean or
            doc_proj_clean[:20] == fund_name_clean[:20]):
            
            if any(kw in fund_name_upper for kw in ['FEMA', 'CALOES', 'CALJPIA']):
                if fund_record['Project_Name'] not in [p['Project_Name'] for p in projects_2022_disaster]:
                    amount = int(fund_record['Amount'])
                    projects_2022_disaster.append({
                        'Project_Name': fund_record['Project_Name'],
                        'Amount': amount
                    })
                    total_funding += amount
                    print(f"Added from docs: {fund_record['Project_Name']}")
                    break

# Remove duplicates
unique_projects = []
seen = set()
for proj in projects_2022_disaster:
    if proj['Project_Name'] not in seen:
        seen.add(proj['Project_Name'])
        unique_projects.append(proj)

total_funding = sum(p['Amount'] for p in unique_projects)
num_projects = len(unique_projects)

print(f"\n{'='*60}")
print(f"TOTAL 2022 DISASTER PROJECTS: {num_projects}")
print(f"TOTAL FUNDING: ${total_funding:,}")
print(f"{'='*60}")

# Result
result = {
    'total_funding': total_funding,
    'num_projects': num_projects,
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:64': {'error': 'Data access failed'}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': []}

exec(code, env_args)
