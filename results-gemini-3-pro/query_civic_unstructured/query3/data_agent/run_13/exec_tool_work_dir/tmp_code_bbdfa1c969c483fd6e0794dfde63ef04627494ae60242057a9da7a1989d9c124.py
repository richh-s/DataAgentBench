code = """import json
import re

# Load Funding
with open(locals()['var_function-call-10026752535853149452'], 'r') as f:
    funding_data = json.load(f)

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
    parts = filename.split('_')
    for p in parts:
        if '-' in p:
            sub = p.split('-')[0]
            if len(sub) == 8 and sub.isdigit():
                return sub[4:] + sub[0:2] + sub[2:4]
    return "00000000"

docs_data.sort(key=lambda x: get_date(x['filename']))

# Normalization Helper
def normalize(name):
    # Remove suffixes
    name = re.sub(r'\s*\(FEMA.*?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES.*?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA.*?\)', '', name, flags=re.IGNORECASE)
    return name.strip()

# Parse Docs
project_info = {} # ExactName -> {Status, Text, Section}
all_project_names_lower = {n.lower(): n for n in all_project_names}

for doc in docs_data:
    text = doc['text']
    lines = text.splitlines()
    
    current_section = ""
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Identify Section
        if "Projects" in line and "(" in line:
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

# Build map of NormalizedName -> Status from found projects
normalized_status_map = {} # NormName -> Status
exact_status_map = {}      # ExactName -> Status

for pname, info in project_info.items():
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
            if "preliminary design" in text.lower():
                status = "design"
            else:
                status = "not started"
    else:
        # Fallback
        if "completed" in text.lower():
            status = "completed"
        elif "design" in text.lower():
            status = "design"
        elif "construction" in text.lower():
            status = "construction"
            
    exact_status_map[pname] = status
    normalized_status_map[normalize(pname)] = status

# Compile Results
results = []
keywords = ["emergency", "fema", "disaster", "fire", "warning", "evacuation"]

for pname in all_project_names:
    norm_name = normalize(pname)
    
    # Check Relevance
    is_related = False
    if any(k in pname.lower() for k in keywords):
        is_related = True
    
    if pname in project_info:
        if any(k in project_info[pname]['Text'].lower() for k in keywords):
            is_related = True
            
    elif norm_name in project_info:
         if any(k in project_info[norm_name]['Text'].lower() for k in keywords):
            is_related = True
            
    if is_related:
        final_status = "not started"
        if pname in exact_status_map:
            final_status = exact_status_map[pname]
        elif norm_name in normalized_status_map:
            final_status = normalized_status_map[norm_name]
        else:
            final_status = "not started"
            
        fundings = funding_lookup[pname]
        for f in fundings:
            results.append({
                "Project_Name": pname,
                "Funding_Source": f['Source'],
                "Amount": f['Amount'],
                "Status": final_status
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4124616707303630081': 'file_storage/function-call-4124616707303630081.json', 'var_function-call-10026752535853149452': 'file_storage/function-call-10026752535853149452.json', 'var_function-call-10718390349076741334': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-10964084464339468277': 'file_storage/function-call-10964084464339468277.json', 'var_function-call-13111615141746118151': [{'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000', 'Status': 'not started'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000', 'Status': 'design'}, {'Project_Name': 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'Funding_Source': 'Research Institution Funding', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'not started'}]}

exec(code, env_args)
