code = """import json
import re

# Access the stored data results
funding_data = var_functions.query_db_66
civic_docs_data = var_functions.query_db_65

print(f"Loaded {len(funding_data)} funding records")
print(f"Loaded {len(civic_docs_data)} civic documents")

# Extract park-related projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for park projects completed in 2022
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        # Look for lines mentioning park projects
        if 'park' in line.lower() and len(line) < 150 and not line.startswith('(') and not line.startswith('•'):
            # Check surrounding context for completion status and date
            context_start = max(0, i-3)
            context_end = min(len(lines), i+10)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            # Check if completed in 2022
            if 'completed' in context and '2022' in context:
                project_name = line.replace('\u2013', '-').replace('\u201c', '"').replace('\u201d', '"').strip()
                if project_name and project_name not in park_projects_2022:
                    park_projects_2022.append(project_name)

print(f"Found {len(park_projects_2022)} park projects completed in 2022:")
for proj in park_projects_2022:
    print(f"  - {proj}")

# Clean project names for matching
def clean_project_name(name):
    if not name:
        return ''
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

# Match with funding records and calculate total
total_funding = 0
matched_pairs = []

for park_proj in park_projects_2022:
    park_clean = clean_project_name(park_proj)
    if not park_clean:
        continue
    
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        if not fund_name:
            continue
            
        fund_clean = clean_project_name(fund_name)
        if not fund_clean:
            continue
            
        # Check for name similarity
        if (park_clean in fund_clean or fund_clean in park_clean or 
            abs(len(park_clean) - len(fund_clean)) < 10):
            
            fund_amount = int(fund.get('Amount', 0))
            total_funding += fund_amount
            matched_pairs.append({
                'park_project': park_proj,
                'funding_project': fund_name,
                'amount': fund_amount
            })
            print(f"Match: {park_proj} -> {fund_name} = ${fund_amount}")

# Remove duplicate funding (same project might match multiple times)
unique_funding = {}
for match in matched_pairs:
    fund_proj = match['funding_project']
    if fund_proj not in unique_funding:
        unique_funding[fund_proj] = match['amount']

final_total = sum(unique_funding.values())

print("\\n" + "="*60)
print(f"Total funding for park projects completed in 2022: ${final_total}")
print("="*60)

result = {
    'total_funding': final_total,
    'unique_projects_funded': len(unique_funding),
    'matched_pairs': len(matched_pairs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
