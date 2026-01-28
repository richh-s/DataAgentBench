code = """import json
import re

funding_path = locals()['var_function-call-14803134734020214920']
civic_path = locals()['var_function-call-14803134734020215365']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Use chr(10) for newline to avoid string literal issues
full_text = chr(10).join([doc.get('text', '') for doc in civic_docs])

# Define section headers using re.escape to avoid backslash issues
h_design = "Capital Improvement Projects (Design)"
h_construction = "Capital Improvement Projects (Construction)"
h_not_started = "Capital Improvement Projects (Not Started)"

match_design = re.search(re.escape(h_design), full_text, re.IGNORECASE)
match_construction = re.search(re.escape(h_construction), full_text, re.IGNORECASE)
match_not_started = re.search(re.escape(h_not_started), full_text, re.IGNORECASE)

sections = []
if match_design:
    sections.append({'label': 'design', 'start': match_design.start()})
if match_construction:
    sections.append({'label': 'construction', 'start': match_construction.start()})
if match_not_started:
    sections.append({'label': 'not_started', 'start': match_not_started.start()})

sections.sort(key=lambda x: x['start'])

# Add end indices
for i in range(len(sections)):
    if i + 1 < len(sections):
        sections[i]['end'] = sections[i+1]['start']
    else:
        sections[i]['end'] = len(full_text)

# Clean names
clean_names = {}
for fund in funding_data:
    raw_name = fund['Project_Name']
    # Regex: remove suffix in parens at end
    # Use simple pattern
    clean = re.sub(r"\s*\(.*?\)$", "", raw_name).strip()
    if clean not in clean_names:
        clean_names[clean] = []
    clean_names[clean].append(fund)

# Find positions
project_positions = []
for c_name in clean_names:
    escaped = re.escape(c_name)
    # Regex: start of line, name, end of line (ignoring whitespace)
    # Avoid \s inside regex string literals if problematic? No, r"" should work.
    # But let's use carefully constructed pattern.
    pattern = r"^\s*" + escaped + r"\s*$"
    for match in re.finditer(pattern, full_text, re.MULTILINE | re.IGNORECASE):
        project_positions.append({'start': match.start(), 'end': match.end(), 'name': c_name})

project_positions.sort(key=lambda x: x['start'])

final_list = []
# Keywords
keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail", "disaster", "recovery", "siren", "warning"]

found_names = set()

for i, proj in enumerate(project_positions):
    found_names.add(proj['name'])
    start = proj['start']
    end = proj['end']
    
    if i + 1 < len(project_positions):
        next_start = project_positions[i+1]['start']
        block_text = full_text[end:next_start]
    else:
        block_text = full_text[end:]
    
    status = "Unknown"
    for sec in sections:
        s_end = sec.get('end', len(full_text))
        if sec['start'] <= start < s_end:
            if sec['label'] == 'design':
                status = "design"
            elif sec['label'] == 'not_started':
                status = "not started"
            elif sec['label'] == 'construction':
                if "completed" in block_text.lower():
                    status = "completed"
                elif "under construction" in block_text.lower():
                    status = "under construction"
                else:
                    status = "under construction"
            break
            
    is_related = False
    
    matched_funds = clean_names[proj['name']]
    for fund in matched_funds:
        if any(k in fund['Project_Name'].lower() for k in ['emergency', 'fema']) or \
           any(k in fund['Funding_Source'].lower() for k in ['emergency', 'fema']):
            is_related = True
    
    if any(k.lower() in block_text.lower() for k in ['emergency', 'fema']):
        is_related = True
    
    if is_related:
        for fund in matched_funds:
            final_list.append({
                "Project_Name": fund['Project_Name'],
                "Funding_Source": fund['Funding_Source'],
                "Amount": fund['Amount'],
                "Status": status
            })

for c_name, funds in clean_names.items():
    if c_name not in found_names:
        for fund in funds:
            if any(k in fund['Project_Name'].lower() for k in ['emergency', 'fema']) or \
               any(k in fund['Funding_Source'].lower() for k in ['emergency', 'fema']):
                final_list.append({
                    "Project_Name": fund['Project_Name'],
                    "Funding_Source": fund['Funding_Source'],
                    "Amount": fund['Amount'],
                    "Status": "Unknown"
                })

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-3621504545855713981': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-3621504545855717196': 'file_storage/function-call-3621504545855717196.json', 'var_function-call-14803134734020214920': 'file_storage/function-call-14803134734020214920.json', 'var_function-call-14803134734020215365': 'file_storage/function-call-14803134734020215365.json'}

exec(code, env_args)
