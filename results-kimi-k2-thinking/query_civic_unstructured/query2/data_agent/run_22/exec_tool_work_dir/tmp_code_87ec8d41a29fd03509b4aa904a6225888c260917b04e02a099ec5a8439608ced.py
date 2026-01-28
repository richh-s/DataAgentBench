code = """import json
import re

civic_docs = json.load(open('var_functions.query_db_36'))
funding_data = json.load(open('var_functions.query_db_8'))

projects_completed_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for park projects completed in 2022
    if 'park' in lower_text and '2022' in lower_text and 'completed' in lower_text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if 'Park' in line_clean and len(line_clean) < 150:
                skip_words = ['updates:', 'schedule:', 'description:', 'page', 'agenda', 'item']
                should_skip = any(word in line_clean.lower() for word in skip_words)
                if not should_skip:
                    # Check nearby lines for completion status
                    nearby = ' '.join(lines[max(0,i-3):min(len(lines),i+4)])
                    if 'completed' in nearby.lower() and '2022' in nearby:
                        if line_clean not in projects_completed_2022:
                            projects_completed_2022.append(line_clean)

# Match with funding records
total_funding = 0
funding_matches = []

for project in projects_completed_2022:
    proj_key = project.lower().strip()
    
    for record in funding_data:
        fund_name = record['Project_Name'].lower()
        
        # Match if names are equal or fund name starts with project name
        if proj_key == fund_name or fund_name.startswith(proj_key):
            amount = int(record['Amount'])
            total_funding += amount
            funding_matches.append(record)

result = {
    'total_funding': total_funding,
    'num_projects': len(projects_completed_2022),
    'num_matches': len(funding_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
