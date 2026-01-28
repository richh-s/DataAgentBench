code = """import json
import re

# Read civic documents
civic_path = var_functions.query_db:6
civic_file = open(civic_path, 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Read funding data
funding_path = var_functions.query_db:7
funding_file = open(funding_path, 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Process documents
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Find sections with FEMA or emergency
    if 'FEMA' in text or 'emergency' in text.lower():
        # Extract project names and status
        # Look for common project patterns
        pattern = r'([A-Z][A-Za-z0-9\s\&\-\.]+(?:\([^\)]*\))?)\s*(?:\(cid:\d+\)\s*)?(?:Updates|Project Schedule)'
        matches = re.finditer(pattern, text)
        for match in matches:
            name = match.group(1).strip()
            if len(name) < 150:  # Filter out garbage
                # Check if this project section mentions FEMA/emergency
                start = match.start()
                end = text.find('\n\n', start)
                if end == -1:
                    end = start + 1000
                section = text[start:end]
                
                if 'FEMA' in section or 'emergency' in section.lower():
                    status = 'unknown'
                    section_lower = section.lower()
                    if 'under construction' in section_lower:
                        status = 'construction'
                    elif 'completed' in section_lower:
                        status = 'completed'
                    elif 'design' in section_lower:
                        status = 'design'
                    
                    project_type = 'disaster' if 'FEMA' in section else 'capital'
                    
                    all_projects.append({
                        'Project_Name': name,
                        'status': status,
                        'type': project_type
                    })

# Get funding records
funding_list = []
for item in funding_data:
    name = item.get('Project_Name', '')
    if 'FEMA' in name or 'emergency' in name.lower():
        funding_list.append({
            'Project_Name': name,
            'Funding_Source': item.get('Funding_Source'),
            'Amount': item.get('Amount')
        })

result = {
    'projects': all_projects,
    'funding': funding_list
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
