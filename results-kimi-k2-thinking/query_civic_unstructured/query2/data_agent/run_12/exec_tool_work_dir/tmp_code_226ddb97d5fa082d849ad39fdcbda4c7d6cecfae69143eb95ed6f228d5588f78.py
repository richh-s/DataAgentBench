code = """import json
import re

# Load data from storage
civic_file = var_functions.query_db_106
funding_file = var_functions.query_db_107

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_records)} funding records")

# Extract park-related projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Look for project lines that mention "park"
        if 'park' in line.lower() and len(line) < 150 and not line.startswith('(') and not line.startswith('•'):
            # Check context for completion status
            context_start = max(0, i-3)
            context_end = min(len(lines), i+10)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            # Check if the project was completed in 2022
            if 'completed' in context and '2022' in context:
                project_name = line.replace('\u2013', '-').replace('\u201c', '"').replace('\u201d', '"').strip()
                if project_name and project_name not in park_projects_2022:
                    park_projects_2022.append(project_name)

print(f"Found {len(park_projects_2022)} park projects completed in 2022:")
for proj in park_projects_2022:
    print(f"  - {proj}")

# Clean project names for better matching
def clean_project_name(name):
    if not name:
        return ''
    # Remove common suffixes
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

# Match park projects with funding records and calculate total
total_funding = 0
matched_pairs = []
matched_funding_projects = set()

for park_proj in park_projects_2022:
    park_clean = clean_project_name(park_proj)
    if not park_clean:
        continue
    
    for fund in funding_records:
        fund_name = fund.get('Project_Name', '')
        if not fund_name:
            continue
            
        fund_clean = clean_project_name(fund_name)
        if not fund_clean:
            continue
            
        # Check for name similarity (one contains the other)
        if (park_clean in fund_clean or fund_clean in park_clean):
            fund_amount = int(fund.get('Amount', 0))
            
            # Avoid duplicate funding
            if fund_name not in matched_funding_projects:
                total_funding += fund_amount
                matched_funding_projects.add(fund_name)
                matched_pairs.append({
                    'park_project': park_proj,
                    'funding_project': fund_name,
                    'amount': fund_amount
                })
                print(f"Match: {park_proj} -> {fund_name} = ${fund_amount:,}")

print(f"\n{'='*60}")
print(f"Total funding for park projects completed in 2022: ${total_funding:,}")
print(f"{'='*60}")

result = {
    'total_funding': total_funding,
    'unique_projects_matched': len(matched_pairs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.list_db:104': ['civic_docs'], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json'}

exec(code, env_args)
