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

# Extract projects from civic documents with their status and type
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects sections with Design status
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \((Construction|Not Started)\)|Disaster Recovery Projects|$)'
    design_match = re.search(design_section_pattern, text, re.DOTALL)
    
    if design_match:
        design_section = design_match.group(1)
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip metadata and process lines
            if (line and 
                not line.startswith('(') and 
                not line.startswith('\\u2022') and 
                not line.startswith('cid:') and
                'Updates:' not in line and
                'Schedule:' not in line and
                'Complete Design:' not in line and
                'Advertise:' not in line and
                'Begin Construction:' not in line and
                'Project Description:' not in line and
                len(line) > 10):
                
                if any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Infrastructure', 'Master Plan', 'Study', 'Replacement', 'Facility', 'Road', 'Park', 'Beach', 'Highway']):
                    project_name = re.sub(r'^[^a-zA-Z]*', '', line)
                    
                    if project_name and len(project_name) > 5:
                        extracted_projects.append({
                            'Project_Name': project_name,
                            'type': 'capital',
                            'status': 'design'
                        })

# Remove duplicates
unique_projects = {}
for proj in extracted_projects:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

extracted_projects = list(unique_projects.values())

# Match with funding data
matched_projects = []
for proj in extracted_projects:
    proj_name = proj['Project_Name']
    
    for funding_proj in funding_data:
        funding_name = funding_proj['Project_Name']
        
        # Simple substring matching
        proj_lower = proj_name.lower()
        fund_lower = funding_name.lower()
        
        if (proj_lower in fund_lower or 
            fund_lower in proj_lower):
            matched_projects.append(proj)
            break
        
        # Word overlap check
        proj_words = set(re.findall(r'\\b\\w+\\b', proj_lower))
        fund_words = set(re.findall(r'\\b\\w+\\b', fund_lower))
        
        if len(proj_words.intersection(fund_words)) >= 3:
            matched_projects.append(proj)
            break

count = len(matched_projects)

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'matched_projects': matched_projects[:10],
    'total_extracted': len(extracted_projects),
    'total_funding_over_50k': len(funding_data)
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
