code = """import json
import re

# Get file paths from locals()
civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:2']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print("Loaded data:", len(civic_docs), "documents,", len(funding_data), "funding records")

park_projects_2022 = []

# Extract park-related projects completed in 2022
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for completion patterns
    completion_patterns = [
        r'([A-Z][^\n]{3,120})\s*\n[^\n]*completed[^\n]*2022',
        r'completed[^\n]*2022[^\n]*([A-Z][^\n]{3,120})(?=\s*\n)',
        r'([A-Z][^\n]*(?:Park|Playground)[^\n]{3,80})\s*\n[^\n]{0,200}completed[^\n]{0,200}2022'
    ]
    
    for pattern in completion_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            project_name = match.strip()
            if len(project_name) < 150 and 'park' in project_name.lower():
                park_projects_2022.append(project_name)

# Remove duplicates
unique_projects = list(set(park_projects_2022))
print("Found park projects:", len(unique_projects))
for proj in unique_projects:
    print("-", proj)

# Match with funding data
total_funding = 0
matched_records = []

for project_name in unique_projects:
    proj_lower = project_name.lower()
    
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '').lower()
        fund_amount = int(fund.get('Amount', 0))
        
        # Check if funding matches project (park-related and close name match)
        if ('park' in fund_name and 
            (proj_lower in fund_name or fund_name in proj_lower or 
             any(word in fund_name for word in proj_lower.split() if len(word) > 4))):
            matched_records.append({
                'project': project_name,
                'funding': fund.get('Project_Name'),
                'amount': fund_amount
            })
            total_funding += fund_amount

# Remove duplicates
seen_funding = set()
final_matches = []
for rec in matched_records:
    key = rec['funding']
    if key not in seen_funding:
        final_matches.append(rec)
        seen_funding.add(key)

print("\nMatched funding:", len(final_matches))
for rec in final_matches:
    print(f"- {rec['project']} -> {rec['funding']}: ${rec['amount']:,}")

answer = f"Total funding for park-related projects completed in 2022 is ${total_funding:,}"
print("\n__RESULT__:", answer)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
