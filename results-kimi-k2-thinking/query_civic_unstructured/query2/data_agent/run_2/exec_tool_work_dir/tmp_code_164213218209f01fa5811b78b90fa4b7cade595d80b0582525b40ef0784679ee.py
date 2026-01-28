code = """import json
import re

# Load the civic documents data
civic_docs_path = var_functions.query_db:0
funding_path = var_functions.query_db:2

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create a list to store extracted projects
extracted_projects = []

# Process all documents to find park projects completed in 2022
for doc in civic_docs:
    if 'text' in doc:
        text = doc['text']
        lines = text.split('\n')
        
        current_project = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Skip metadata lines
            if line.startswith('To:') or line.startswith('From:') or line.startswith('Date:') or line.startswith('Subject:'):
                continue
            
            # Look for project indicators in the line
            has_park_topic = 'park' in line.lower() or 'playground' in line.lower()
            
            if has_park_topic and len(line) < 100:
                # Check if this might be a project name
                if line[0].isupper() and 'Updates:' not in line and 'Project Schedule:' not in line:
                    current_project = line
            
            # If we have a current project, look for completion in 2022
            if current_project:
                # Look ahead for completion status and date
                next_lines = '\n'.join(lines[i:i+5])
                if 'completed' in next_lines.lower() and '2022' in next_lines:
                    topics = []
                    if 'park' in current_project.lower():
                        topics.append('park')
                    if 'playground' in current_project.lower():
                        topics.append('playground')
                    
                    # Check if it's specifically park-related
                    if topics:
                        extracted_projects.append({
                            'Project_Name': current_project,
                            'topics': topics,
                            'status': 'completed',
                            'year': '2022'
                        })
                        current_project = None

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in extracted_projects:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

print('Found projects:', len(unique_projects))
for proj in unique_projects:
    print('-', proj['Project_Name'])

# Find funding for park projects completed in 2022
total_funding = 0
funded_projects = []

for proj in unique_projects:
    proj_name = proj['Project_Name']
    proj_name_lower = proj_name.lower()
    
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '').lower()
        fund_amount = int(fund.get('Amount', 0))
        
        # Check if this funding matches our project
        if proj_name_lower in fund_name or fund_name in proj_name_lower:
            if 'park' in fund_name or 'playground' in fund_name:
                funded_projects.append({
                    'project': proj_name,
                    'funding_record': fund.get('Project_Name'),
                    'amount': fund_amount
                })
                total_funding += fund_amount

# Remove duplicate funding records
seen_funding = set()
unique_funded = []
for item in funded_projects:
    funding_record = item['funding_record']
    if funding_record not in seen_funding:
        unique_funded.append(item)
        seen_funding.add(funding_record)

print('\nMatching funding records:', len(unique_funded))
for item in unique_funded:
    print(f"- {item['project']}: ${item['amount']:,}")

result = f"Total funding for park projects completed in 2022: ${total_funding:,}"
print('\n__RESULT__:', result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
