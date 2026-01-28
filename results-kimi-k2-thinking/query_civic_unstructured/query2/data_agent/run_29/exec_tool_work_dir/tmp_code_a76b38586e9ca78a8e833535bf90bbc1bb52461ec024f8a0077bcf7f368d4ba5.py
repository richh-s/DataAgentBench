code = """import json

# Access data from storage
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:16']

# Parse civic documents more thoroughly
park_projects_2022 = []

for doc in civic_docs:
    if isinstance(doc, dict):
        text = doc.get('text', '')
    else:
        continue
    
    # Look for park projects with completion info
    # Pattern: Project Name followed by status/completion info
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 5:
            continue
        
        # Check if this is likely a project name containing "park"
        if 'park' in line.lower():
            # Store potential project
            project_name = line
            
            # Look ahead for completion status and date
            for j in range(i, min(i+15, len(lines))):
                next_line = lines[j].strip()
                next_lower = next_line.lower()
                
                # Check various completion indicators
                if any(indicator in next_lower for indicator in ['completed', 'completion', 'construction completed']):
                    # Check for 2022 date
                    if '2022' in next_line:
                        # Also check if the document mentions completion in 2022 elsewhere
                        if '2022' in text and 'completed' in text.lower():
                            park_projects_2022.append(project_name)
                            break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Enhanced matching with funding data
funding_matches = {}

# Normalize function
def normalize(s):
    return ' '.join(s.lower().strip().split())

for park in park_projects_2022:
    park_norm = normalize(park)
    park_words = set(park_norm.split())
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_norm = normalize(fund_name)
        fund_words = set(fund_norm.split())
        
        # Match criteria
        is_match = False
        
        # 1. One contains the other
        if park_norm in fund_norm or fund_norm in park_norm:
            is_match = True
        # 2. Share key words (at least 3 words including 'park')
        elif 'park' in fund_norm and len(park_words.intersection(fund_words)) >= 3:
            is_match = True
        # 3. Same park name regardless of suffixes
        elif 'park' in park_norm and 'park' in fund_norm:
            # Extract the part before 'park'
            park_prefix = park_norm.split('park')[0]
            fund_prefix = fund_norm.split('park')[0]
            if park_prefix.strip() == fund_prefix.strip():
                is_match = True
        
        if is_match:
            amount = int(fund['Amount'])
            if park in funding_matches:
                funding_matches[park] += amount
            else:
                funding_matches[park] = amount
            break  # Match to first valid funding record

# Calculate total
total_funding = sum(funding_matches.values())

print('__RESULT__:')
print(json.dumps({
    'park_projects': park_projects_2022,
    'funding_matches': funding_matches,
    'total_funding': total_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': {'civic_docs_count': 38, 'funding_records_count': 39, 'sample_civic_doc': 'f'}, 'var_functions.execute_python:36': {'total_funding': 0}}

exec(code, env_args)
