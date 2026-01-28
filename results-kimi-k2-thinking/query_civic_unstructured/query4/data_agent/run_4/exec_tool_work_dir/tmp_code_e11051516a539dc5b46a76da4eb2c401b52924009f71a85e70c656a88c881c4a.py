code = """import json

# Load the data files
civic_docs_file = var_functions.query_db_2
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = var_functions.query_db_4
funding_data = []
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for fund in funding_data:
    proj_name = fund['Project_Name']
    amount = int(fund['Amount'])
    funding_lookup[proj_name] = amount

# Now extract projects from civic documents looking for Spring 2022
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project patterns
    # Pattern 1: Project name followed by dates
    project_patterns = [
        r'([A-Z][a-zA-Z\s&\-]+?(?:Project)?(?:\s*\(FEMA[^\)]*\))?\s*\(Cal(?:JPIA|OES)[^\)]*\)?)?)\s*\n\s*\(cid:\d+\)\s*Project Schedule:\s*\n\s*\(cid:\d+\)\s*(?:Complete|Begin|Advertise|Final)\s*(?:Design)?:\s*(Spring\s+2022)',
        r'([A-Z][a-zA-Z\s&\-]+?(?:Project)?)\s*\n\s*\(cid:\d+\)\s*Project Schedule:\s*\n[^\n]*\n\s*\(cid:\d+\)[^\n]*Spring\s+2022',
        r'([A-Z][a-zA-Z\s&\-]+?(?:Project)?)\s*\n\s*\(cid:\d+\)\s*Updates:[^\n]*\n[^\n]*Spring\s+2022'
    ]
    
    for pattern in project_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if isinstance(match, tuple):
                proj_name = match[0].strip()
            else:
                proj_name = match.strip()
            
            # Clean up project name
            proj_name = re.sub(r'\s+', ' ', proj_name)
            proj_name = re.sub(r'\n', '', proj_name)
            
            if proj_name and len(proj_name) > 5:
                spring_2022_projects.append(proj_name)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

# Match with funding data
total_funding = 0
matched_projects = []

for proj in spring_2022_projects:
    if proj in funding_lookup:
        matched_projects.append({
            'project_name': proj,
            'funding': funding_lookup[proj]
        })
        total_funding += funding_lookup[proj]
    else:
        # Try partial matching
        for fund_proj, amount in funding_lookup.items():
            if proj.lower() in fund_proj.lower() or fund_proj.lower() in proj.lower():
                matched_projects.append({
                    'project_name': f'{proj} -> {fund_proj}',
                    'funding': amount
                })
                total_funding += amount
                break

result = {
    'spring_2022_projects_count': len(spring_2022_projects),
    'matched_projects': matched_projects,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
