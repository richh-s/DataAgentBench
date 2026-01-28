code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:1
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:1

# Load civic documents  
civic_file = var_functions.query_db:2
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

# Print some debugging info
print('Funding records:', len(funding_data))
print('Civic docs:', len(civic_docs))

# Basic project extraction - look for lines that seem like project names
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        # Split by sections
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_part = parts[1].split('Capital Improvement Projects (')[0]
            lines = design_part.split('\n')
            
            for line in lines:
                line = line.strip()
                if len(line) > 15 and not any(x in line for x in ['(', 'cid:', 'Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction']):
                    if any(word in line for word in ['Project', 'Improvements', 'Repairs', 'Master Plan', 'Study', 'Replacement']):
                        name = re.sub(r'^[\\u2022\\s-]+', '', line)
                        if name:
                            extracted_projects.append(name)

# Remove duplicates
unique_projects = list(set(extracted_projects))
print('Extracted projects:', len(unique_projects))

# Match with funding data (projects with > $50k funding)
funding_names = [f['Project_Name'] for f in funding_data]
print('Funding projects to match:', len(funding_names))

matched_count = 0
matched_list = []

for proj in unique_projects:
    proj_lower = proj.lower()
    
    for fund_name in funding_names:
        fund_lower = fund_name.lower()
        
        # Direct substring match
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matched_count += 1
            matched_list.append(proj)
            break
            
        # Word overlap check  
        proj_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            matched_count += 1
            matched_list.append(proj)
            break

print('Matched projects:', matched_count)

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
