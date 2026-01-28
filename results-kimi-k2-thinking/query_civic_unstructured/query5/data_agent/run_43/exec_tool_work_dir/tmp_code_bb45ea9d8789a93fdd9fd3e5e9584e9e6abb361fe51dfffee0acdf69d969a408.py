code = """import json
import re

# Load all civic documents
doc_file_path = locals()['var_functions.query_db:18']
with open(doc_file_path, 'r') as f:
    all_docs = json.load(f)

# Load funding data
funding_data = locals()['var_functions.query_db:12']

# Step 1: Extract all projects with 2022 dates from civic documents
projects_with_2022 = []

# Patterns to match project names
project_patterns = [
    r'([A-Z][A-Za-z0-9\s&\-\(\)]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study|Plan))',
]

# Patterns to find dates
# Look for "Begin Construction", "Complete Design", "Advertise", "Start", etc. followed by 2022
date_patterns = [
    r'(?:Begin|Start|Complete|Advertise|Initiate)\s*(?:Construction|Design|Build)?\s*:?\s*(Spring|Summer|Fall|Winter)?\s*2022',
    r'2022[-\s]?(Spring|Summer|Fall|Winter)',
    r'(Spring|Summer|Fall|Winter)\s*2022',
]

for doc in all_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Find project names near 2022 dates
    for proj_pattern in project_patterns:
        projects = re.findall(proj_pattern, text)
        
        for project in projects:
            project = project.strip()
            if len(project) < 10:  # Skip short matches
                continue
                
            # Find where this project appears in text
            proj_pos = text.find(project)
            if proj_pos == -1:
                continue
            
            # Look for dates in the vicinity of the project name (within 500 chars)
            vicinity = text[proj_pos:proj_pos+500]
            
            has_2022_date = False
            date_found = None
            
            for date_pattern in date_patterns:
                date_match = re.search(date_pattern, vicinity)
                if date_match:
                    has_2022_date = True
                    date_found = date_match.group(0)
                    break
            
            if has_2022_date:
                projects_with_2022.append({
                    'project_name': project,
                    'date_context': date_found,
                    'filename': filename
                })

# Remove duplicates
unique_projects = []
seen = set()
for p in projects_with_2022:
    key = p['project_name'].lower()
    if key not in seen:
        seen.add(key)
        unique_projects.append(p)

print(f"Found {len(unique_projects)} unique projects with 2022 dates")

# Step 2: Filter for disaster-related projects
disaster_keywords = ['fema', 'fire', 'emergency', 'disaster', 'recovery', 'warning', 'siren', 'storm', 'drainage', 'culvert', 'guardrail']
disaster_projects_2022 = []

for proj in unique_projects:
    proj_name_lower = proj['project_name'].lower()
    if any(keyword in proj_name_lower for keyword in disaster_keywords):
        disaster_projects_2022.append(proj)

print(f"\nFound {len(disaster_projects_2022)} disaster-related projects with 2022 dates")
for p in disaster_projects_2022:
    print(f"- {p['project_name']}: {p['date_context']}")

# Step 3: Match with funding data
funding_lookup = {}
for item in funding_data:
    proj_name = item['Project_Name'].lower()
    funding_lookup[proj_name] = int(item['Amount'])

matched_funding = []
total_funding = 0

for proj in disaster_projects_2022:
    proj_name = proj['project_name'].lower()
    
    # Direct match
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        matched_funding.append({
            'project': proj['project_name'],
            'funding': amount,
            'match_type': 'exact'
        })
        total_funding += amount
    else:
        # Try partial match - check if project name contains a funded project name
        for funded_name, amount in funding_lookup.items():
            if funded_name in proj_name or proj_name in funded_name:
                matched_funding.append({
                    'project': proj['project_name'],
                    'funding': amount,
                    'matched_to': item['Project_Name'],
                    'match_type': 'partial'
                })
                total_funding += amount
                break

print(f"\nMatched {len(matched_funding)} projects with funding")
print(f"Total funding for 2022 disaster projects: ${total_funding:,}")

# Also check for any FEMA-named projects in funding data that we might have missed
additional_fema_funding = []
for item in funding_data:
    proj_name = item['Project_Name']
    if 'fema' in proj_name.lower():
        # Check if we already counted this
        already_counted = any(m['project'].lower() in proj_name.lower() or proj_name.lower() in m['project'].lower() for m in matched_funding)
        if not already_counted:
            amount = int(item['Amount'])
            # Check if this might be a 2022 project based on context
            additional_fema_funding.append({
                'project': proj_name,
                'funding': amount
            })

if additional_fema_funding:
    print(f"\nFound {len(additional_fema_funding)} additional FEMA projects (not matched to civic docs)")
    for af in additional_fema_funding:
        print(f"- {af['project']}: ${af['funding']:,}")

result = {
    'disaster_projects_2022': len(disaster_projects_2022),
    'matched_with_funding': len(matched_funding),
    'total_funding': total_funding,
    'funded_projects': matched_funding
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_found': 9, 'projects': [{'project_name': 'PCH Median Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'March 2022'}, {'project_name': 'Permanent Skate Park', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Legacy Park Paver Repair Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': '2022 meeting'}, {'project_name': 'Civic Center Stormwater Diversion Structure', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Malibu Park Drainage Improvements', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'April 2022'}, {'project_name': 'Bluffs Park Shade Structure', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Westward Beach Road Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Fall 2022'}, {'project_name': 'Capital Improvement Projects (Completed)\n\nCivic Center Way Improvements', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'PCH Signal Synchronization System Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}]}, 'var_functions.query_db:12': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.execute_python:12': {'total_records': 20, 'total_funding': 1037000, 'projects': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
