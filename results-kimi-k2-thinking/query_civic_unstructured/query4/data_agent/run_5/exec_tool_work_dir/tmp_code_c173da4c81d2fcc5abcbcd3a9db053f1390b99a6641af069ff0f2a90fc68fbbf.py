code = """import json
import re

def load_data_from_key(key):
    data = locals().get(key)
    if isinstance(data, str) and data.endswith('.json'):
        with open(data, 'r') as f:
            return json.load(f)
    return data

# Load data from variables
civic_docs = load_data_from_key('var_functions.query_db:82')
funding_data = load_data_from_key('var_functions.query_db:83')

# Build funding lookup: project name -> total amount
funding_lookup = {}
for rec in funding_data:
    amount = int(rec['Amount'])
    name = rec['Project_Name']
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

# Find Spring 2022 projects in civic documents
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        lines = [ln.strip() for ln in text.split('\n') if ln.strip()]
        
        current_project = None
        for i, line in enumerate(lines):
            # Ignore short lines and markers
            if len(line) < 10 or line.startswith('(') or 'cid:' in line:
                continue
                
            # Project names often appear before "Updates:" or "Schedule:"
            if i + 1 < len(lines):
                next_line = lines[i+1]
                if any(marker in next_line for marker in ['Updates:', 'Project Schedule:', 'Project Description:']):
                    current_project = line
            
            # Check for 2022 in line
            if '2022' in line:
                # Skip schedule instruction lines
                skip_words = ['Complete:', 'Begin:', 'Advertise:', 'Construction:']
                if not any(word in line for word in skip_words):
                    # This is likely a project name with 2022
                    spring_2022_projects.append(line)
                elif current_project:
                    # This is a schedule line mentioning 2022
                    spring_2022_projects.append(current_project)
                    current_project = None

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_2022_projects))

# Find projects explicitly mentioning "Spring" with 2022 (for strict Spring 2022)
strict_spring_2022 = []
for project in unique_projects:
    if 'Spring' in project and '2022' in project:
        strict_spring_2022.append(project)
    # Also include projects that clearly started in 2022 based on name
    elif project.startswith('2022'):
        strict_spring_2022.append(project)

# Match with funding data
total_funding = 0
matched_count = 0

for project in strict_spring_2022:
    # Direct match
    if project in funding_lookup:
        total_funding += funding_lookup[project]
        matched_count += 1
    else:
        # Try matching by first word (for cases like "2022 Morning View...")
        words = project.split()
        if words:
            first_word = words[0]
            if first_word == '2022' and len(words) > 1:
                # Look for projects starting with the second word
                search_term = ' '.join(words[1:])
                for funded_name in funding_lookup:
                    if funded_name.startswith(search_term) or search_term in funded_name:
                        total_funding += funding_lookup[funded_name]
                        matched_count += 1
                        break
            else:
                # Look for funded projects starting with this project name
                for funded_name in funding_lookup:
                    if funded_name.startswith(project) or project in funded_name:
                        total_funding += funding_lookup[funded_name]
                        matched_count += 1
                        break

# Also include any funding records with 2022 in their name that aren't already counted
for funded_name, amount in funding_lookup.items():
    if '2022' in funded_name:
        # Check if already counted
        if funded_name not in strict_spring_2022:
            # These are likely Spring 2022 projects mentioned directly in funding
            total_funding += amount
            matched_count += 1

# Final result
result = {
    'count': matched_count,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
