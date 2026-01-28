code = """import json
import re

# Get file paths  
funding_path = locals()['var_functions.query_db:10']
civic_path = locals()['var_functions.query_db:11']

# Load funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

print('Loaded', len(funding_data), 'funding records and', len(civic_data), 'civic documents')

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_data:
    text = doc['text'].lower()
    
    # Check if document mentions park and 2022 completion
    if 'park' in text and '2022' in text:
        # Look for completion indicators
        completion_terms = ['completed', 'completion', 'complete construction', 'construction was completed']
        if any(term in text for term in completion_terms):
            # Extract relevant lines
            lines = doc['text'].split('\n')
            for line in lines:
                line_lower = line.lower()
                if 'park' in line_lower and '2022' in line_lower and any(term in line_lower for term in completion_terms):
                    park_projects_2022.append(line.strip())

print('\nFound', len(park_projects_2022), 'potential park projects completed in 2022')
for i, proj in enumerate(park_projects_2022[:10]):
    print('  ', i+1, '.', proj)

# More targeted extraction - find project names and completion status
park_project_details = []

for doc in civic_data:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        # Look for park project names (capitalized, contains 'Park' or 'park')
        if 'park' in line_lower and len(line.strip()) > 5:
            words = line.strip().split()
            if any(word[0].isupper() for word in words if word):
                # Check following lines for 2022 completion
                for j in range(i, min(i+5, len(lines))):
                    next_line = lines[j].lower()
                    if '2022' in next_line and any(term in next_line for term in ['completed', 'completion']):
                        amount = None
                        # Look for funding amount in funding data
                        for funding in funding_data:
                            if funding['Project_Name'].lower() in line.lower() or line.lower() in funding['Project_Name'].lower():
                                amount = int(funding['Amount'])
                                break
                        
                        park_project_details.append({
                            'name': line.strip(),
                            'status': lines[j].strip(),
                            'amount': amount
                        })
                        break

print('\nDetailed extraction:', len(park_project_details), 'projects')
for p in park_project_details[:5]:
    print('   Name:', p['name'])
    print('   Status:', p['status'])
    print('   Amount:', p['amount'])
    print()"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
