code = """import json
import re

# Load data
try:
    with open(locals()['var_function-call-6082162408351623791'], 'r') as f:
        funding_records = json.load(f)
except:
    funding_records = locals()['var_function-call-6082162408351623791']

try:
    with open(locals()['var_function-call-12699093529231824248'], 'r') as f:
        civic_docs = json.load(f)
except:
    civic_docs = locals()['var_function-call-12699093529231824248']

# Sort docs by date descending
def get_date(filename):
    match = re.search(r'_(\d{8})', filename)
    if match:
        return match.group(1) # MMDDYYYY
    return "00000000"

# Sort key: year, month, day
def sort_key(doc):
    d = get_date(doc['filename'])
    # Convert MMDDYYYY to YYYYMMDD
    if len(d) == 8:
        return d[4:] + d[0:2] + d[2:4]
    return d

civic_docs.sort(key=sort_key, reverse=True)

# Helper
def get_base_name(name):
    return name.split('(')[0].strip()

# Valid names
valid_names = set()
for r in funding_records:
    valid_names.add(r['Project_Name'])
    valid_names.add(get_base_name(r['Project_Name']))

project_status_map = {}

status_headers = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started",
    "Disaster Recovery Projects (Design)": "design",
    "Disaster Recovery Projects (Construction)": "construction",
    "Disaster Recovery Projects (Not Started)": "not started"
}

# Process docs
for doc in civic_docs:
    lines = doc['text'].splitlines()
    current_status = "Unknown"
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check header
        found_header = False
        lower_line = line.lower()
        for header, status in status_headers.items():
            if header.lower() in lower_line:
                current_status = status
                current_project = None
                found_header = True
                break
        if found_header:
            continue

        # Check project name
        if line in valid_names:
            current_project = line
            # Only set status if not already set (since we process newest docs first)
            if current_project not in project_status_map:
                project_status_map[current_project] = {'status': current_status, 'text': ''}
            # Append text regardless (to capture all keywords)
            # Actually, if we want keywords from the *latest* update, we should prioritize that.
            # But "related to emergency" might be in an old doc.
            # So collecting text from all docs is fine.
            # But we must be careful not to mix statuses.
            # Existing logic: if not in map, set status. (Correct for newest-first)
            # Text accumulation: always append? Or only for the newest?
            # Let's accumulate.
            continue

        if current_project:
            # Add text to the entry in map
            # We need to make sure the map entry exists (it should from above)
            if current_project in project_status_map:
                project_status_map[current_project]['text'] += " " + line

# Refine status "construction" -> "completed"
for proj, data in project_status_map.items():
    txt = data['text'].lower()
    if data['status'] == 'construction':
        if 'completed' in txt and ('notice of completion' in txt or 'construction was completed' in txt):
            data['status'] = 'completed'

# Assemble results
final_results = []
keywords = ['emergency', 'fema']

for record in funding_records:
    name = record['Project_Name']
    base = get_base_name(name)
    
    is_relevant = False
    
    # Check name
    for kw in keywords:
        if kw in name.lower():
            is_relevant = True
            break
            
    # Check text
    proj_data = project_status_map.get(name) or project_status_map.get(base)
    
    if proj_data:
        # Check text for keywords
        txt = proj_data['text'].lower()
        for kw in keywords:
            if kw in txt:
                is_relevant = True
                break
    
    if is_relevant:
        status = "Unknown"
        if proj_data:
            status = proj_data['status']
            
        final_results.append({
            "Project_Name": name,
            "Funding_Source": record['Funding_Source'],
            "Amount": record['Amount'],
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-6082162408351623791': 'file_storage/function-call-6082162408351623791.json', 'var_function-call-6082162408351624496': 'file_storage/function-call-6082162408351624496.json', 'var_function-call-12699093529231824248': 'file_storage/function-call-12699093529231824248.json', 'var_function-call-7232955498272687177': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}]}

exec(code, env_args)
