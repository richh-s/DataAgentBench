code = """import json
import re

# Read civic documents
civic_docs_path = 'var_functions.query_db:8'
funding_path = 'var_functions.query_db:5'

civic_docs = json.load(open(civic_docs_path, 'r'))
funding_data = json.load(open(funding_path, 'r'))

print('Loaded %d civic documents and %d funding records' % (len(civic_docs), len(funding_data)))

# Create funding map
funding_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[name] = amount

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for park projects with 2022 completion
    # Pattern: Project name followed by completion info
    
    # Find all occurrences of completion in 2022
    completion_matches = re.finditer(r'(?:completed|completion).*?2022', text, re.IGNORECASE)
    
    for match in completion_matches:
        # Get context around the completion mention
        start = max(0, match.start() - 500)
        end = min(len(text), match.end() + 200)
        context = text[start:end]
        
        # Look for park-related project names in this context
        lines = context.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 10 and ('park' in line.lower() or 'playground' in line.lower()):
                # Skip headings
                skip = False
                for heading in ['capital improvement', 'disaster recovery', 'prepared by', 'approved by']:
                    if heading in line.lower():
                        skip = True
                        break
                
                if not skip:
                    # Clean the name
                    clean_name = re.sub(r'\(cid:\d+\)', '', line).strip()
                    
                    # Check funding
                    funding_amount = 0
                    for funded_name in funding_map:
                        if (clean_name.lower() in funded_name.lower() or 
                            funded_name.lower() in clean_name.lower()):
                            funding_amount = funding_map[funded_name]
                            break
                    
                    park_projects.append({
                        'name': clean_name,
                        'funding': funding_amount
                    })

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in park_projects:
    if proj['name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['name'])

# Calculate totals
total_funding = sum(p['funding'] for p in unique_projects)
projects_with_funding = [p for p in unique_projects if p['funding'] > 0]

print('\nFound %d park projects completed in 2022' % len(unique_projects))
print('%d have funding data' % len(projects_with_funding))
print('\nProjects with funding:')
for proj in projects_with_funding:
    print('- %s: $%d' % (proj['name'], proj['funding']))

print('\nTotal funding for park-related projects completed in 2022: $%d' % total_funding)

# Return result
result = {
    'total_funding': total_funding,
    'project_count': len(projects_with_funding)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
