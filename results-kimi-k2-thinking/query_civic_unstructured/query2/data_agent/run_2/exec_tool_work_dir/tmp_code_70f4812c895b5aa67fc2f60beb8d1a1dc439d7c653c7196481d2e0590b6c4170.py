code = """import json
import re

# Load data from files
civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:2']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Documents loaded:', len(civic_docs))
print('Funding records loaded:', len(funding_data))

# Find park-related projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check if document mentions completion in 2022 and parks
    if '2022' in text and 'completed' in lower_text and 'park' in lower_text:
        # Look for project names (typically capitalized, reasonable length)
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if (line and len(line) < 100 and line[0].isupper() and 
                not line.startswith('To:') and not line.startswith('From:') and
                not line.startswith('Date:') and not line.startswith('Subject:')):
                
                lower_line = line.lower()
                if 'park' in lower_line:
                    # Check nearby text for completion and 2022
                    line_idx = lines.index(line)
                    context = ' '.join(lines[max(0, line_idx-2):line_idx+5])
                    if 'completed' in context.lower() and '2022' in context:
                        park_projects.append(line)

# Remove duplicates
unique_park_projects = list(set(park_projects))
print('\nPark projects completed in 2022:')
for proj in unique_park_projects:
    print('-', proj)

# Find funding for these projects
total_funding = 0
funding_matches = []

# Also look for any funding records with park in name and related to 2022 completions
for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    fund_amount = int(fund.get('Amount', 0))
    fund_name_lower = fund_name.lower()
    
    if 'park' in fund_name_lower:
        # Check if this matches any of our identified projects or is a standalone park project
        matched_project = False
        for project in unique_park_projects:
            project_lower = project.lower()
            if (project_lower in fund_name_lower or fund_name_lower in project_lower or
                any(word in fund_name_lower for word in project_lower.split() if len(word) > 4)):
                funding_matches.append({'project': project, 'funding': fund_name, 'amount': fund_amount})
                total_funding += fund_amount
                matched_project = True
                break
        
        # Also include park funding that might be related to 2022 completions
        if not matched_project and ('2022' in fund_name or 'shade' in fund_name_lower or 'structure' in fund_name_lower):
            funding_matches.append({'project': 'Park project (from funding record)', 'funding': fund_name, 'amount': fund_amount})
            total_funding += fund_amount

print('\nFunding matches:', len(funding_matches))
for match in funding_matches:
    print(f"- {match['project']} -> {match['funding']}: ${match['amount']:,}")

answer = f"Total funding for park-related projects completed in 2022 is ${total_funding:,}"
print('\n__RESULT__:')
print(answer)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
