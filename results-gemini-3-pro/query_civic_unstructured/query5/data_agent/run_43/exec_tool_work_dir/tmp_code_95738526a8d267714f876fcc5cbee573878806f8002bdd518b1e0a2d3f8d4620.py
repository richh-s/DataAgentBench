code = """import json
import re

# Load data
funding_path = locals()['var_function-call-15640139870961926103']
civic_path = locals()['var_function-call-15640139870961922644']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

def parse_document(text, filename):
    lines = text.splitlines()
    current_category = "Unknown"
    
    current_project_name = None
    current_project_text = []
    
    projects = []
    
    def save_project(name, text_lines, category):
        if not name: return
        full_text = " ".join(text_lines)
        
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
            'full_text': full_text
        })

    header_pattern = r'^(Capital Improvement Projects|Disaster Recovery Projects)\s*(?:\((.*)\))?'
    
    iterator = range(len(lines))
    for i in iterator:
        line = lines[i].strip()
        if not line: continue
        
        match = re.match(header_pattern, line, re.IGNORECASE)
        if match:
            save_project(current_project_name, current_project_text, current_category)
            current_project_name = None
            current_project_text = []
            current_category = match.group(1)
            continue
            
        is_project_start = False
        for offset in range(1, 6):
            if i + offset >= len(lines): break
            next_l = lines[i+offset].strip()
            if "Updates:" in next_l or "Project Description:" in next_l or "Project Schedule:" in next_l:
                if "Updates:" not in line and "Project Description:" not in line:
                    is_project_start = True
                    break
        
        if is_project_start:
            save_project(current_project_name, current_project_text, current_category)
            current_project_name = line
            current_project_text = []
        else:
            if current_project_name:
                current_project_text.append(line)
    
    save_project(current_project_name, current_project_text, current_category)
    return projects

all_extracted = []
for doc in civic_data:
    all_extracted.extend(parse_document(doc['text'], doc['filename']))

disaster_projects = [p for p in all_extracted if p['type'] == 'disaster']

results = []
for p in disaster_projects:
    # Find mentions of 2022
    matches = re.findall(r'[^.]*2022[^.]*', p['full_text'])
    if matches:
        results.append({
            'name': p['Project_Name'],
            'mentions': matches
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15640139870961926103': 'file_storage/function-call-15640139870961926103.json', 'var_function-call-15640139870961922644': 'file_storage/function-call-15640139870961922644.json', 'var_function-call-4280233803932826645': {'total_funding': 91000.0, 'matched_projects': [{'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000.0}], 'missing_projects': []}, 'var_function-call-15849578272413360394': 'file_storage/function-call-15849578272413360394.json'}

exec(code, env_args)
