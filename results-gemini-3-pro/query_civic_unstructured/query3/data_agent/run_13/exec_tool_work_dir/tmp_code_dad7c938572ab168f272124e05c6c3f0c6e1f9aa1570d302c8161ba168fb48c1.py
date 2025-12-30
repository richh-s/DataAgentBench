code = """import json
import re

# Load Funding
with open(locals()['var_function-call-10026752535853149452'], 'r') as f:
    funding_data = json.load(f)

# Funding Lookup
funding_lookup = {}
all_project_names = set()
for item in funding_data:
    pname = item['Project_Name'].strip()
    if pname not in funding_lookup:
        funding_lookup[pname] = []
    funding_lookup[pname].append({'Source': item['Funding_Source'], 'Amount': item['Amount']})
    all_project_names.add(pname)

# Load Docs
with open(locals()['var_function-call-10964084464339468277'], 'r') as f:
    docs_data = json.load(f)

# Sort docs
def get_date(filename):
    m = re.search(r'_(\d{8})-', filename)
    if m:
        d = m.group(1)
        return d[4:] + d[0:2] + d[2:4]
    return "00000000"

docs_data.sort(key=lambda x: get_date(x['filename']))

# Parse Docs
project_info = {}
all_project_names_lower = {n.lower(): n for n in all_project_names}

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = ""
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Identify Section
        if "Capital Improvement Projects" in line and "(" in line:
            current_section = line
            current_project = None
            continue
        if "Disaster Recovery Projects" in line:
            current_section = line
            current_project = None
            continue
            
        # Identify Project
        pname_match = None
        if line in all_project_names:
            pname_match = line
        elif line.lower() in all_project_names_lower:
            pname_match = all_project_names_lower[line.lower()]
            
        if pname_match:
            current_project = pname_match
            if current_project not in project_info:
                project_info[current_project] = {'Status': 'Unknown', 'Text': '', 'Section': ''}
            
            project_info[current_project]['Section'] = current_section
            project_info[current_project]['Text'] = ""
            continue
            
        if current_project:
            project_info[current_project]['Text'] += " " + line

# Build Results
results = []
processed_projects = set()

for pname, info in project_info.items():
    processed_projects.add(pname)
    text = info['Text']
    section = info['Section']
    
    # Determine Status
    status = "not started"
    if "Not Started" in section:
        status = "not started"
    elif "Design" in section:
        status = "design"
    elif "Construction" in section:
        if "completed" in text.lower() or "notice of completion" in text.lower():
            status = "completed"
        else:
            status = "construction"
    elif "Disaster" in section:
        if "completed" in text.lower():
            status = "completed"
        elif "design" in text.lower():
            status = "design"
        elif "construction" in text.lower():
            status = "construction"
        else:
            status = "not started"
            
    # Check Relevance
    is_related = False
    keywords = ["emergency", "fema", "disaster", "fire", "warning", "evacuation"]
    
    if any(k in pname.lower() for k in keywords):
        is_related = True
    if not is_related and any(k in text.lower() for k in keywords):
        is_related = True
        
    if is_related:
        fundings = funding_lookup.get(pname, [])
        for f in fundings:
            results.append({
                "Project_Name": pname,
                "Funding_Source": f['Source'],
                "Amount": f['Amount'],
                "Status": status
            })

for pname in all_project_names:
    if pname not in processed_projects:
        if any(k in pname.lower() for k in ["emergency", "fema", "disaster"]):
            fundings = funding_lookup[pname]
            for f in fundings:
                results.append({
                    "Project_Name": pname,
                    "Funding_Source": f['Source'],
                    "Amount": f['Amount'],
                    "Status": "not started"
                })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4124616707303630081': 'file_storage/function-call-4124616707303630081.json', 'var_function-call-10026752535853149452': 'file_storage/function-call-10026752535853149452.json', 'var_function-call-10718390349076741334': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-10964084464339468277': 'file_storage/function-call-10964084464339468277.json'}

exec(code, env_args)
