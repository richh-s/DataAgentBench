code = """import json
import re

# Load data
with open('var_function-call-16455850891903614580.json', 'r') as f:
    civic_docs = json.load(f)
with open('var_function-call-16455850891903614945.json', 'r') as f:
    funding_records = json.load(f)

def get_date_from_filename(fn):
    match = re.search(r'agenda_(\\d{8})', fn)
    if match:
        return match.group(1)
    return "00000000"

civic_docs.sort(key=lambda x: get_date_from_filename(x['filename']), reverse=True)
full_text = civic_docs[0]['text']

lines = full_text.splitlines()

project_data = {} 
current_section = "Unknown"
current_project = None

date_pattern = re.compile(r'Begin Construction:\\s*(.*)', re.IGNORECASE)

for i, line in enumerate(lines):
    line_strip = line.strip()
    if not line_strip:
        continue
        
    if "Disaster Recovery Projects" in line_strip:
        current_section = "Disaster"
        current_project = None
        continue
    elif "Capital Improvement Projects" in line_strip:
        current_section = "Capital"
        current_project = None
        continue
        
    if i + 1 < len(lines):
        next_line = lines[i+1].strip()
        if next_line.startswith("(cid:190)") or next_line.startswith("Updates:"):
            if "Projects" not in line_strip:
                current_project = line_strip
                if current_project not in project_data:
                    project_data[current_project] = {"section": current_section, "start_dates": []}
                if current_section != "Unknown":
                    project_data[current_project]["section"] = current_section
    
    if current_project:
        m = date_pattern.search(line_strip)
        if m:
            date_val = m.group(1).strip()
            project_data[current_project]["start_dates"].append(date_val)

def normalize(name):
    # Remove suffixes like (FEMA Project), (CalOES Project)
    # The parentheses need to be escaped in regex
    name = re.sub(r'\\s*\\(.*?\\)$', '', name)
    return name.strip()

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"]
total_funding = 0
matched_log = []

for record in funding_records:
    amt = record['Amount']
    if isinstance(amt, str):
        amt = float(amt)
    fname = record['Project_Name']
    
    is_disaster_name = any(k in fname for k in disaster_keywords)
    
    norm_fname = normalize(fname)
    found_info = None
    
    # Matching strategy:
    if fname in project_data:
        found_info = project_data[fname]
    elif norm_fname in project_data:
        found_info = project_data[norm_fname]
    
    is_disaster_section = False
    if found_info and found_info['section'] == 'Disaster':
        is_disaster_section = True
        
    # Condition: Must be disaster related (by name or section)
    if not (is_disaster_name or is_disaster_section):
        continue
        
    # Condition: Must start in 2022
    started_2022 = False
    if found_info:
        for d in found_info['start_dates']:
            if "2022" in d:
                started_2022 = True
                break
    
    if started_2022:
        total_funding += amt
        matched_log.append(fname)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_log}))"""

env_args = {'var_function-call-16455850891903611214': ['civic_docs'], 'var_function-call-16455850891903614945': 'file_storage/function-call-16455850891903614945.json', 'var_function-call-16455850891903614580': 'file_storage/function-call-16455850891903614580.json'}

exec(code, env_args)
