code = """import json
import re

# Load all data
civic_docs = json.load(open(locals()['var_functions.query_db:0'], 'r'))
funding_data = json.load(open(locals()['var_functions.query_db:1'], 'r'))

# Convert amounts
for f in funding_data:
    f['Amount'] = int(f['Amount'])

# Comprehensive search for park projects completed in 2022
park_projects = []
project_details = []

for doc in civic_docs:
    text = doc['text']
    # Look for patterns indicating park projects completed in 2022
    completion_patterns = [
        r'([A-Z][A-Za-z0-9 &\-\(\)]+)\s*\n.*Construction was completed[^\n]*2022',
        r'([A-Z][A-Za-z0-9 &\-\(\)]+)\s*\n.*completed[^\n]*2022[^\n]*park',
        r'([A-Z][A-Za-z0-9 &\-\(\)]+Park[A-Za-z0-9 &\-\(\)]+)\s*\n.*completed[^\n]*2022'
    ]
    
    for pattern in completion_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if match not in park_projects:
                park_projects.append(match)
                project_details.append({
                    'name': match,
                    'source': doc['filename']
                })

# Also scan line by line to catch any that regex missed
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        # Check if line looks like a project name and contains 'Park'
        if ('Park' in line and len(line) > 10 and len(line) < 150 and 
            not line.startswith(('(', 'Page', 'Agenda')) and
            line[0].isupper()):
            
            # Look ahead for completion in 2022
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j]
                if ('completed' in next_line.lower() or 'completion' in next_line.lower()) and '2022' in next_line:
                    if line not in park_projects:
                        park_projects.append(line)
                        project_details.append({
                            'name': line,
                            'source': doc['filename']
                        })

# Match with funding records
total_funding = 0
matched_projects = []

for project in park_projects:
    proj_lower = project.lower().strip()
    best_match = None
    best_score = 0
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_lower = fund_name.lower().strip()
        
        # Exact match
        if proj_lower == fund_lower:
            best_match = fund
            best_score = 100
            break
        # Contains match
        elif proj_lower in fund_lower or fund_lower in proj_lower:
            if len(proj_lower) > 10:  # Avoid matching short names
                best_match = fund
                best_score = 80
        # Word overlap
        else:
            proj_words = set(proj_lower.split())
            fund_words = set(fund_lower.split())
            common = proj_words & fund_words
            if len(common) >= 2:
                score = len(common) * 20
                if score > best_score:
                    best_match = fund
                    best_score = score
    
    if best_match:
        total_funding += best_match['Amount']
        matched_projects.append({
            'project': project,
            'matched_funding': best_match['Project_Name'],
            'amount': best_match['Amount'],
            'source': best_match['Funding_Source']
        })

print('__RESULT__:')
print(json.dumps({
    'park_projects_found': len(park_projects),
    'projects': park_projects,
    'total_funding': total_funding,
    'matched_records': matched_projects,
    'record_count': len(matched_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:24': {'civic_docs': 5, 'funding': 500}, 'var_functions.execute_python:26': {'specific_park_projects': ['Bluffs Park Shade Structure', 'Point Dume Walkway Repairs'], 'funding_matches': [{'project': 'Bluffs Park Shade Structure', 'funding_record': 'Bluffs Park Shade Structure', 'amount': 21000, 'source': 'Government Grant'}, {'project': 'Point Dume Walkway Repairs', 'funding_record': 'Point Dume Walkway Repairs', 'amount': 59000, 'source': 'International Aid'}], 'total_funding': 80000, 'record_count': 2}}

exec(code, env_args)
