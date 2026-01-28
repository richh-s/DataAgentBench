code = """import json
import pandas as pd

NEWLINE = chr(10)

path_docs = locals()['var_function-call-10835669272488718990']
path_fund = locals()['var_function-call-10835669272488721645']

with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

for r in funding_data:
    r['Amount'] = int(r['Amount'])

df_funding = pd.DataFrame(funding_data)

# Helper to normalize names
def normalize(name):
    # Remove (...)
    if '(' in name:
        name = name.split('(')[0]
    return name.strip().lower()

# Map normalized base name to funding rows
funding_map = {}
for _, row in df_funding.iterrows():
    norm = normalize(row['Project_Name'])
    if norm not in funding_map:
        funding_map[norm] = []
    funding_map[norm].append(row)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + NEWLINE

# Segment by 'Updates:'
# We assume the separator is unique enough.
segments = full_text.split('Updates:')

extracted_projects = []
total_amount = 0
matched_names = set()

headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

for i in range(1, len(segments)):
    # Name is at end of segments[i-1]
    prev_seg = segments[i-1].strip()
    lines = [l.strip() for l in prev_seg.split(NEWLINE) if l.strip()]
    
    if not lines:
        continue
    
    name_line = lines[-1]
    # Check if header
    is_header = False
    for h in headers:
        if h in name_line:
            is_header = True
            break
            
    if is_header and len(lines) > 1:
        name_line = lines[-2]
    elif is_header:
        # Should not happen if format is correct
        continue
        
    # Body is segments[i]
    # We take first 1000 chars to avoid bleeding into next project
    body = segments[i][:1000]
    
    # Extract Start
    st = None
    marker = "Begin Construction:"
    if marker in body:
        after = body.split(marker)[1]
        st = after.split(NEWLINE)[0].strip()
    
    # Extract Type/Disaster
    is_disaster = False
    
    # Check name
    name_lower = name_line.lower()
    if 'fema' in name_lower or 'caloes' in name_lower or 'disaster' in name_lower:
        is_disaster = True
        
    # Check body keywords
    body_lower = body.lower()
    if 'fema' in body_lower or 'caloes' in body_lower or 'disaster' in body_lower or 'woolsey' in body_lower:
        is_disaster = True
        
    # Match with DB to check suffixes
    norm_name = normalize(name_line)
    
    # Check suffixes in DB for this name
    if norm_name in funding_map:
        for row in funding_map[norm_name]:
            rn = row['Project_Name'].lower()
            if 'fema' in rn or 'caloes' in rn or 'disaster' in rn:
                is_disaster = True
                break
    
    # Final check
    if st and '2022' in st:
        if is_disaster:
            if norm_name in funding_map and norm_name not in matched_names:
                # Sum funding
                rows = funding_map[norm_name]
                amount = sum(r['Amount'] for r in rows)
                total_amount += amount
                extracted_projects.append({'name': name_line, 'amount': amount, 'start': st})
                matched_names.add(norm_name)

print('__RESULT__:')
print(json.dumps({'total_amount': total_amount, 'projects': extracted_projects}))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json', 'var_function-call-474033538740406040': {'status': 'loaded', 'docs_count': 5, 'funding_count': 500}, 'var_function-call-6347203935522351673': {'total_amount': 1184000, 'projects': [{'name': '2021 Annual Street Maintenance', 'amount': 24000, 'start': 'Spring 2022'}, {'name': 'Annual Street Maintenance', 'amount': 23000, 'start': 'Spring 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000, 'start': 'Spring 2022'}, {'name': 'Civic Center Stormwater Diversion Structure', 'amount': 64000, 'start': 'Spring 2022'}, {'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022'}]}, 'var_function-call-2203215841011505581': {'total_amount': 905000, 'projects': [{'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022', 'section': 'Unknown'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022', 'section': 'Unknown'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022', 'section': 'Capital'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022', 'section': 'Unknown'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022', 'section': 'Unknown'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022', 'section': 'Unknown'}]}, 'var_function-call-7890869682996152425': {'total_amount': 2085000, 'projects': [{'name': '2021 Annual Street Maintenance', 'amount': 24000, 'start': 'Spring 2022'}, {'name': 'Annual Street Maintenance', 'amount': 23000, 'start': 'Spring 2022'}, {'name': 'Birdview Avenue Improvements', 'amount': 178000, 'start': 'April 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000, 'start': 'Spring 2022'}, {'name': 'City Traffic Signals Backup Power', 'amount': 85000, 'start': 'Spring 2022'}, {'name': 'Civic Center Stormwater Diversion Structure', 'amount': 64000, 'start': 'Spring 2022'}, {'name': 'Civic Center Way Improvements', 'amount': 37000, 'start': 'Spring 2022'}, {'name': 'Corral Canyon Culvert Repairs', 'amount': 112000, 'start': 'April 2022'}, {'name': 'Corral Canyon Road Bridge Repairs', 'amount': 151000, 'start': 'April 2022'}, {'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022'}, {'name': 'Guardrail Replacement Citywide', 'amount': 106000, 'start': 'April 2022'}, {'name': 'Kanan Dume Biofilter', 'amount': 56000, 'start': 'Spring 2022'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022'}, {'name': 'Legacy Park Paver Repair Project', 'amount': 69000, 'start': 'Spring 2022'}, {'name': 'Malibu Park Drainage Improvements', 'amount': 17000, 'start': 'April 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022'}, {'name': 'Trancas Playground Resurfacing', 'amount': 90000, 'start': 'Spring 2022'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022'}]}}

exec(code, env_args)
