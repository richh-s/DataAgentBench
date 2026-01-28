code = """import json

civic_docs_data = var_functions.query_db:22
funding_data = var_functions.query_db:5

# Handle file paths
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Build funding map
funding_map = {}
for rec in funding_data:
    funding_map[rec['Project_Name'].strip().lower()] = int(rec['Amount'])

spring_projects = []

# Helper to clean lines
def clean_line(line):
    return line.strip().replace('●', '').replace('■', '').replace('□', '').strip()

# Check each document
for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    text_lower = text.lower()
    
    # Check if document mentions Spring 2022
    if '2022-spring' in text_lower or '2022-march' in text_lower or '2022-april' in text_lower or '2022-may' in text_lower:
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            # Check for Spring 2022 date indicators
            if '2022-spring' in line_lower or '2022-march' in line_lower or '2022-april' in line_lower or '2022-may' in line_lower:
                project_name = None
                
                # Look backwards for project name (check previous few lines)
                for j in range(i-1, max(i-6, -1), -1):
                    prev_line = clean_line(lines[j])
                    
                    # Skip lines that are not likely project names
                    skip_terms = [
                        'project schedule', 'updates:', 'complete design', 'advertise:', 
                        'begin construction:', 'recommended action', 'discussion:',
                        'capital improvement', 'disaster recovery', 'staff will provide'
                    ]
                    
                    if (prev_line and len(prev_line) > 10 and 
                        not any(term in prev_line.lower() for term in skip_terms) and
                        not prev_line.startswith('(') and not prev_line.startswith('●')):
                        
                        # Check if it's a likely project name (starts with capital, not too long)
                        if prev_line[0].isupper() and len(prev_line) < 150:
                            project_name = prev_line
                            break
                
                if project_name:
                    # Get funding amount for this project
                    amount = 0
                    key = project_name.lower()
                    
                    # Try exact match
                    if key in funding_map:
                        amount = funding_map[key]
                    else:
                        # Try variations
                        for funded_key, funded_amount in funding_map.items():
                            # Remove common suffixes and compare
                            clean_key = key.replace(' project', '').strip()
                            clean_funded = funded_key.replace(' project', '').strip()
                            
                            if (clean_key in clean_funded or clean_funded in clean_key or
                                clean_key.replace(' improvements', '') in clean_funded or
                                clean_funded.replace(' improvements', '') in clean_key):
                                amount = funded_amount
                                break
                    
                    spring_projects.append({
                        'name': project_name,
                        'funding': amount
                    })

# Remove duplicates (keep highest funding amount if duplicate)
unique_projects = {}
for proj in spring_projects:
    name = proj['name']
    if name not in unique_projects or proj['funding'] > unique_projects[name]['funding']:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())

# Calculate totals
total_count = len(final_projects)
total_funding = sum(p['funding'] for p in final_projects)

# Get projects with funding
funded_projects = [p for p in final_projects if p['funding'] > 0]

print('Spring 2022 Projects Analysis:')
print('===============================')
print(f'Total projects found: {total_count}')
print(f'Total funding: ${total_funding:,}')
print(f'Projects with funding: {len(funded_projects)}')

if funded_projects:
    print('\nTop funded projects:')
    for proj in sorted(funded_projects, key=lambda x: x['funding'], reverse=True)[:10]:
        print(f'  - {proj["name"][:80]}: ${proj["funding"]:,}')

result = {
    'project_count': total_count,
    'total_funding': total_funding
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
