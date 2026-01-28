code = """import json
import re

# Load all civic documents
doc_file_path = locals()['var_functions.query_db:18']
with open(doc_file_path, 'r') as f:
    all_docs = json.load(f)

# Load funding data
funding_data = locals()['var_functions.query_db:12']

# Create funding lookup
funding_lookup = {}
for item in funding_data:
    proj_name = item['Project_Name'].lower()
    funding_lookup[proj_name] = int(item['Amount'])

# Find all disaster-related projects with 2022 start dates
disaster_projects_2022 = []

disaster_keywords = ['fema', 'fire', 'emergency', 'disaster', 'recovery', 'warning', 'siren', 'storm', 'drainage', 'culvert', 'guardrail']

for doc in all_docs:
    text = doc.get('text', '')
    
    # Find FEMA/parenthetical projects first - these are definitely disaster projects
    fema_pattern = r'([A-Z][A-Za-z0-9\s&\-\(\)]+?\((?:FEMA|CalOES|CalJPIA)[^\)]*\))'
    fema_matches = re.findall(fema_pattern, text)
    
    for proj_name in fema_matches:
        proj_name_clean = proj_name.strip()
        
        # Find where this project appears
        proj_pos = text.find(proj_name_clean)
        if proj_pos == -1:
            continue
        
        # Look for 2022 in the vicinity
        vicinity = text[proj_pos:proj_pos+1000]
        
        if re.search(r'2022', vicinity):
            # Extract the base name (without suffix) for matching
            base_name = re.sub(r'\s*\([^\)]*\)', '', proj_name_clean).strip()
            
            disaster_projects_2022.append({
                'full_name': proj_name_clean,
                'base_name': base_name,
                'is_fema': True
            })

# Also look for projects with disaster keywords that have 2022 dates
for doc in all_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    if any(keyword in lower_text for keyword in disaster_keywords):
        # Find project names
        proj_pattern = r'([A-Z][A-Za-z0-9\s&\-\(\)]+?(?:Project|Improvements|Repair|Drainage|System|Facility|Park|Road|Structure|Study|Plan|Sirens|Warning))'
        projects = re.findall(proj_pattern, text)
        
        for proj_name in projects:
            proj_name_clean = proj_name.strip()
            if len(proj_name_clean) < 10:
                continue
            
            # Check if it has disaster keywords
            proj_lower = proj_name_clean.lower()
            if not any(keyword in proj_lower for keyword in disaster_keywords):
                continue
            
            # Find position and look for 2022
            proj_pos = text.find(proj_name_clean)
            if proj_pos == -1:
                continue
            
            vicinity = text[proj_pos:proj_pos+500]
            
            if re.search(r'2022', vicinity):
                # Check if we already have this project
                already_have = any(p['full_name'] == proj_name_clean for p in disaster_projects_2022)
                if not already_have:
                    disaster_projects_2022.append({
                        'full_name': proj_name_clean,
                        'base_name': proj_name_clean,
                        'is_fema': False
                    })

# Remove duplicates
unique_projects = []
seen_names = set()
for p in disaster_projects_2022:
    if p['full_name'] not in seen_names:
        seen_names.add(p['full_name'])
        unique_projects.append(p)

print('Found', len(unique_projects), 'unique disaster projects with 2022 mentions')
for p in unique_projects[:15]:
    print('-', p['full_name'])

# Match with funding data
matched_projects = []
total_funding = 0

for proj in unique_projects:
    # Try full name first
    full_lower = proj['full_name'].lower()
    if full_lower in funding_lookup:
        amount = funding_lookup[full_lower]
        matched_projects.append({
            'project': proj['full_name'],
            'funding': amount
        })
        total_funding += amount
        continue
    
    # Try base name
    base_lower = proj['base_name'].lower()
    if base_lower in funding_lookup:
        amount = funding_lookup[base_lower]
        matched_projects.append({
            'project': proj['full_name'],
            'funding': amount
        })
        total_funding += amount
        continue
    
    # Try partial matching - check if base name is contained in any funded project
    for funded_name, amount in funding_lookup.items():
        if base_lower in funded_name or funded_name.startswith(base_lower):
            matched_projects.append({
                'project': proj['full_name'],
                'matched_to': funded_name,
                'funding': amount
            })
            total_funding += amount
            break

print('\nMatched', len(matched_projects), 'projects with funding')
print('Total funding:', total_funding)

result = {
    'total_projects': len(unique_projects),
    'matched_projects': len(matched_projects),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_found': 9, 'projects': [{'project_name': 'PCH Median Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'March 2022'}, {'project_name': 'Permanent Skate Park', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Legacy Park Paver Repair Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': '2022 meeting'}, {'project_name': 'Civic Center Stormwater Diversion Structure', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Malibu Park Drainage Improvements', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'April 2022'}, {'project_name': 'Bluffs Park Shade Structure', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'Westward Beach Road Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Fall 2022'}, {'project_name': 'Capital Improvement Projects (Completed)\n\nCivic Center Way Improvements', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}, {'project_name': 'PCH Signal Synchronization System Improvements Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'start_date': 'Spring 2022'}]}, 'var_functions.query_db:12': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.execute_python:12': {'total_records': 20, 'total_funding': 1037000, 'projects': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
