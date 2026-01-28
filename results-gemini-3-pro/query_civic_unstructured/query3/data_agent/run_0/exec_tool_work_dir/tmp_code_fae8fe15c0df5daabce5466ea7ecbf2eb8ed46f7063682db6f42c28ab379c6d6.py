code = """import json
import re

# Load data
with open(locals()['var_function-call-4694039731328856667'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-11052254391267769107'], 'r') as f:
    civic_docs = json.load(f)

# Create a map of Project Name to Funding Info
funding_map = {item['Project_Name']: item for item in funding_data}
funding_names = set(funding_map.keys())

extracted_projects = []

# Regex to find section headers
# Escaping backslashes for JSON: \\s
section_regex = re.compile(r'(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started)\)', re.IGNORECASE)

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status_section = 'unknown'
    current_project_name = None
    current_project_text = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Check for section header
        sec_match = section_regex.search(stripped)
        if sec_match:
            # Save previous project if exists
            if current_project_name:
                extracted_projects.append({
                    'name': current_project_name,
                    'section_status': current_status_section,
                    'text': " ".join(current_project_text)
                })
                current_project_name = None
                current_project_text = []
            
            header_type = sec_match.group(2).lower()
            if 'design' in header_type:
                current_status_section = 'design'
            elif 'not started' in header_type:
                current_status_section = 'not started'
            elif 'construction' in header_type:
                current_status_section = 'construction'
            else:
                current_status_section = 'unknown'
            continue
        
        # Check if line is a project name
        if stripped in funding_names:
            if current_project_name:
                extracted_projects.append({
                    'name': current_project_name,
                    'section_status': current_status_section,
                    'text': " ".join(current_project_text)
                })
            current_project_name = stripped
            current_project_text = []
        else:
            if current_project_name:
                current_project_text.append(stripped)

    # Add last project
    if current_project_name:
        extracted_projects.append({
            'name': current_project_name,
            'section_status': current_status_section,
            'text': " ".join(current_project_text)
        })

# Process results
final_results = []
seen_projects = set()

for proj in extracted_projects:
    p_name = proj['name']
    p_text = proj['text'].lower()
    p_section = proj['section_status']
    
    # Determine Status
    status = p_section
    
    # Check for completion in text
    if 'completed' in p_text and ('construction was completed' in p_text or 'notice of completion' in p_text):
        status = 'completed'
    elif status == 'construction':
        status = 'design' # Map active construction to design
    
    # Check relevance
    is_related = False
    if 'fema' in p_name.lower() or 'emergency' in p_name.lower():
        is_related = True
    if 'fema' in p_text or 'emergency' in p_text:
        is_related = True
    
    if is_related:
        if p_name not in seen_projects:
            f_info = funding_map.get(p_name, {})
            final_results.append({
                "Project_Name": p_name,
                "Funding_Source": f_info.get("Funding_Source"),
                "Amount": f_info.get("Amount"),
                "Status": status
            })
            seen_projects.add(p_name)

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-4694039731328856667': 'file_storage/function-call-4694039731328856667.json', 'var_function-call-11052254391267769107': 'file_storage/function-call-11052254391267769107.json'}

exec(code, env_args)
