code = """import json
import re

# Read the civic documents to extract disaster projects with 2022 start dates
doc_file_path = locals()['var_functions.query_db:2']
with open(doc_file_path, 'r') as f:
    documents = json.load(f)

# Read the funding data
funding_data = locals()['var_functions.query_db:12']

# Step 1: Extract all disaster projects from civic docs with 2022 start dates
disaster_projects_2022 = []

disaster_keywords = ['fema', 'fire', 'emergency', 'disaster', 'recovery', 'woolsey', 'warning', 'siren']

for doc in documents:
    text = doc.get('text', '').lower()
    
    # Check if document is disaster-related
    if any(keyword in text for keyword in disaster_keywords):
        
        # Find FEMA/project suffix patterns first (these are definitely disaster projects)
        fema_pattern = r'([A-Z][A-Za-z0-9\s&\-\(\)]+?\((?:FEMA|CalOES|CalJPIA)\s*(?:Project)?\))'
        fema_projects = re.findall(fema_pattern, doc.get('text', ''), re.MULTILINE)
        
        for proj_name in fema_projects:
            proj_name_clean = proj_name.strip()
            
            # Find the section for this project
            proj_pos = doc.get('text', '').find(proj_name_clean)
            if proj_pos == -1:
                continue
                
            proj_section = doc.get('text', '')[proj_pos:proj_pos+1500]
            
            # Look for 2022 start date
            date_patterns = [
                r'Begin(?:ning)?\s*(?:Construction)?:\s*(\w+\s*2022)',
                r'Complete\s*Design:\s*(\w+\s*2022)',
                r'Advertise:\s*(\w+\s*2022)',
                r'(Spring\s*2022)',
                r'(Summer\s*2022)',
                r'(Fall\s*2022)',
                r'(Winter\s*2022)',
            ]
            
            start_date = None
            for dp in date_patterns:
                match = re.search(dp, proj_section)
                if match:
                    start_date = match.group(1)
                    break
            
            if start_date:
                # Remove the suffix for matching
                base_name = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA)[^\)]*\)', '', proj_name_clean).strip()
                
                disaster_projects_2022.append({
                    'full_name': proj_name_clean,
                    'base_name': base_name,
                    'start_date': start_date,
                    'filename': doc.get('filename', '')
                })

# Remove duplicates
seen = set()
unique_projects = []
for p in disaster_projects_2022:
    key = p['full_name']
    if key not in seen:
        seen.add(key)
        unique_projects.append(p)

print(f"Found {len(unique_projects)} unique FEMA/disaster projects starting in 2022")
for p in unique_projects:
    print(f"- {p['full_name']} (base: {p['base_name']}), starts: {p['start_date']}")

# Step 2: Match with funding data
funding_lookup = {item['Project_Name'].lower(): int(item['Amount']) for item in funding_data}
matched_projects = []
total_funding = 0

for proj in unique_projects:
    # Try to match with funding data
    full_name_lower = proj['full_name'].lower()
    base_name_lower = proj['base_name'].lower()
    
    # Direct match
    if full_name_lower in funding_lookup:
        amount = funding_lookup[full_name_lower]
        matched_projects.append({
            'project': proj['full_name'],
            'start_date': proj['start_date'],
            'funding': amount
        })
        total_funding += amount
    else:
        # Try partial matching - check if base name matches start of any funded project
        for funded_name, amount in funding_lookup.items():
            if funded_name.startswith(base_name_lower) or base_name_lower in funded_name:
                matched_projects.append({
                    'project': proj['full_name'],
                    'start_date': proj['start_date'],
                    'funding': amount,
                    'matched_to': funded_name
                })
                total_funding += amount
                break

print(f"\nMatched {len(matched_projects)} projects with funding")
print(f"Total funding: ${total_funding:,}")

# Also check funding data for any projects with 2022 in the name (some might not have FEMA suffix in docs)
additional_matches = []
for item in funding_data:
    proj_name = item['Project_Name']
    # Check if it might be a 2022 project based on name patterns
    if any(keyword in proj_name.lower() for keyword in ['warning', 'siren', 'emergency']):
        # Check if we already matched it
        already_matched = any(m['project'].lower() in proj_name.lower() or proj_name.lower() in m['project'].lower() for m in matched_projects)
        if not already_matched:
            additional_matches.append({
                'project': proj_name,
                'funding': int(item['Amount'])
            })

if additional_matches:
    print(f"\nFound {len(additional_matches)} additional potential matches")
    for am in additional_matches:
        print(f"- {am['project']}: ${am['funding']:,}")
        total_funding += am['funding']

print(f"\nFinal total funding: ${total_funding:,}")

result = {
    'total_projects': len(matched_projects) + len(additional_matches),
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'additional_matches': additional_matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_found': 9, 'projects': [{'project_name': 'PCH Median Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'March 2022'}, {'project_name': 'Permanent Skate Park', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Legacy Park Paver Repair Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': '2022 meeting'}, {'project_name': 'Civic Center Stormwater Diversion Structure', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Malibu Park Drainage Improvements', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'April 2022'}, {'project_name': 'Bluffs Park Shade Structure', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Westward Beach Road Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Fall 2022'}, {'project_name': 'Capital Improvement Projects (Completed)\n\nCivic Center Way Improvements', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'PCH Signal Synchronization System Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}]}, 'var_functions.query_db:12': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.execute_python:12': {'total_records': 20, 'total_funding': 1037000, 'projects': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}}

exec(code, env_args)
