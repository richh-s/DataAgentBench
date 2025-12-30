code = """import json
import re

# Load data
funding_path = locals()['var_function-call-15640139870961926103']
civic_path = locals()['var_function-call-15640139870961922644']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

funding_map = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data}

extracted_projects = []

def parse_document(text, filename):
    lines = text.split('\n')
    current_category = "Unknown"
    current_status = "Unknown"
    
    current_project_name = None
    current_project_text = []
    
    projects = []
    
    def save_project(name, text_lines, category, status):
        if not name: return
        full_text = "\n".join(text_lines)
        
        # Extract Start Date
        st = None
        # Look for "Begin Construction: <value>" or "Start Date"
        # Regex: Begin Construction:\s*(.*)
        st_match = re.search(r'Begin Construction:\s*(.*)', full_text, re.IGNORECASE)
        if st_match:
            st = st_match.group(1).strip()
        
        # Determine Type
        p_type = category.lower()
        if "fema" in name.lower() or "caloes" in name.lower() or "caljpia" in name.lower() or "woolsey" in name.lower():
            p_type = "disaster"
        elif "disaster" in category.lower():
            p_type = "disaster"
        elif "capital" in category.lower():
            p_type = "capital"
            
        projects.append({
            'Project_Name': name,
            'type': p_type,
            'st': st,
            'filename': filename
        })

    # Regex for section headers
    header_re = re.compile(r'^(Capital Improvement Projects|Disaster Recovery Projects)\s*(?:\((.*)\))?', re.IGNORECASE)
    
    iterator = range(len(lines))
    for i in iterator:
        line = lines[i].strip()
        if not line: continue
        
        match = header_re.match(line)
        if match:
            save_project(current_project_name, current_project_text, current_category, current_status)
            current_project_name = None
            current_project_text = []
            
            current_category = match.group(1)
            if match.group(2):
                current_status = match.group(2)
            continue
            
        is_project_start = False
        # Look ahead 1 to 5 lines
        for offset in range(1, 6):
            if i + offset >= len(lines): break
            next_l = lines[i+offset].strip()
            # Check for keywords that indicate the previous line was a header
            if "Updates:" in next_l or "Project Description:" in next_l or "Project Schedule:" in next_l:
                if "Updates:" not in line and "Project Description:" not in line:
                    is_project_start = True
                    break
        
        if is_project_start:
            save_project(current_project_name, current_project_text, current_category, current_status)
            current_project_name = line
            current_project_text = []
        else:
            if current_project_name:
                current_project_text.append(line)
    
    save_project(current_project_name, current_project_text, current_category, current_status)
    return projects

all_extracted = []
for doc in civic_data:
    all_extracted.extend(parse_document(doc['text'], doc['filename']))

target_projects = []
for p in all_extracted:
    # Check for disaster type and 2022 start
    if p['type'] == 'disaster':
        if p['st'] and '2022' in p['st']:
            target_projects.append(p)

total_funding = 0
matched_projects = []
missing_projects = []

for p in target_projects:
    name = p['Project_Name'].strip()
    if name in funding_map:
        amount = funding_map[name]
        total_funding += amount
        matched_projects.append({'name': name, 'amount': amount})
    else:
        missing_projects.append(name)

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "matched_projects": matched_projects,
    "missing_projects": missing_projects
}))"""

env_args = {'var_function-call-15640139870961926103': 'file_storage/function-call-15640139870961926103.json', 'var_function-call-15640139870961922644': 'file_storage/function-call-15640139870961922644.json'}

exec(code, env_args)
