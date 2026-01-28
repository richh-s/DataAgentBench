code = """import json
import re

# Load data
funding_path = locals()['var_function-call-14803134734020214920']
civic_path = locals()['var_function-call-14803134734020215365']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

full_text = "\n".join([doc.get('text', '') for doc in civic_docs])

# Define section headers
match_design = re.search(r"Capital Improvement Projects \(Design\)", full_text, re.IGNORECASE)
match_construction = re.search(r"Capital Improvement Projects \(Construction\)", full_text, re.IGNORECASE)
match_not_started = re.search(r"Capital Improvement Projects \(Not Started\)", full_text, re.IGNORECASE)

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
    # Remove suffixes like (FEMA Project), (CalOES Project)
    clean = re.sub(r"\s*\(.*?\)$", "", raw_name).strip()
    if clean not in clean_names:
        clean_names[clean] = []
    clean_names[clean].append(fund)

# Find project positions in text
project_positions = []
for c_name in clean_names:
    escaped = re.escape(c_name)
    # Search for line matches
    for match in re.finditer(rf"^\s*{escaped}\s*$", full_text, re.MULTILINE | re.IGNORECASE):
        project_positions.append({'start': match.start(), 'end': match.end(), 'name': c_name})

# Sort positions
project_positions.sort(key=lambda x: x['start'])

final_list = []
keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail", "disaster", "recovery", "siren", "warning"]

found_names = set()

for i, proj in enumerate(project_positions):
    found_names.add(proj['name'])
    start = proj['start']
    end = proj['end']
    
    # Determine text block
    if i + 1 < len(project_positions):
        next_start = project_positions[i+1]['start']
        # If the next project is very far, maybe limit the block? 
        # But section headers are not included in project_positions.
        # We should respect section boundaries.
        # But for now, let's just take to next project.
        block_text = full_text[end:next_start]
    else:
        block_text = full_text[end:] # to end of text
    
    # Determine Section/Status
    status = "Unknown"
    for sec in sections:
        if sec['start'] <= start < sec.get('end', len(full_text)):
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
                    status = "under construction" # Default for construction section
            break
            
    # Check relevance
    is_related = False
    
    # Check matched funding records
    matched_funds = clean_names[proj['name']]
    for fund in matched_funds:
        if any(k in fund['Project_Name'].lower() for k in ['emergency', 'fema']) or \
           any(k in fund['Funding_Source'].lower() for k in ['emergency', 'fema']):
            is_related = True
    
    # Check text
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

# Handle not found in text
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
