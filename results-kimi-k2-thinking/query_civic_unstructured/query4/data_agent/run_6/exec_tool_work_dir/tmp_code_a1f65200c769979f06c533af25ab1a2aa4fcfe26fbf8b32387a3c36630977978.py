code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:28']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
civic_file = locals()['var_functions.query_db:6']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Spring 2022 patterns
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

# Find projects with Spring 2022 start dates
spring_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Check if line contains Spring 2022 date
        for pattern in spring_patterns:
            if pattern in line:
                # Look backwards for project name (up to 10 lines)
                project_name = 'Unknown Project'
                for j in range(i-1, max(0, i-10), -1):
                    prev_line = lines[j].strip()
                    
                    # Skip empty lines and lines starting with parentheses
                    if not prev_line or prev_line.startswith('('):
                        continue
                    
                    # Skip metadata lines
                    prev_lower = prev_line.lower()
                    stop_words = ['page', 'agenda item', 'updates:', 'project schedule:', 'project description:', 'estimated schedule:', 'cid']
                    if any(word in prev_lower for word in stop_words):
                        continue
                    
                    # Valid project names are typically 10-150 chars, start with uppercase
                    if 10 < len(prev_line) < 150:
                        if prev_line[0].isupper():
                            project_name = prev_line
                            break
                
                if project_name != 'Unknown Project' and project_name not in spring_project_names:
                    spring_project_names.append(project_name)
                break

print('Found', len(spring_project_names), 'projects with Spring 2022 start dates:')
for name in spring_project_names:
    print('-', name)

# Function to normalize project names
def normalize_name(name):
    # Remove parenthetical suffixes and normalize whitespace
    name = re.sub(r'\s*\(.*?\)\s*$', '', name)
    return name.strip().lower()

# Create funding lookup map
funding_map = {}
for record in funding_data:
    proj_name = record['Project_Name']
    normalized = normalize_name(proj_name)
    # Keep the largest amount if multiple records exist
    amount = int(record['Amount'])
    if normalized not in funding_map or amount > funding_map[normalized]:
        funding_map[normalized] = amount

print('Funding records map size:', len(funding_map))

# Function for partial name matching
def match_partial_names_func(name1, name2):
    words1 = set(name1.lower().split())
    words2 = set(name2.lower().split())
    # Check if they share key words
    common_words = words1.intersection(words2)
    # Remove common/generic words
    generic_words = {'project', 'improvements', 'repairs', 'design', 'construction', 'citywide', 'phase'}
    common_words = common_words - generic_words
    return len(common_words) >= 2

# Match projects with funding records
matched_projects = []
total_funding = 0

for proj_name in spring_project_names:
    normalized = normalize_name(proj_name)
    matched = False
    
    # Exact match first
    if normalized in funding_map:
        amount = funding_map[normalized]
        matched_projects.append({
            'Project_Name': proj_name,
            'Funding': amount
        })
        total_funding += amount
        matched = True
    else:
        # Try partial matching
        for fund_name_normalized in funding_map:
            if (normalized in fund_name_normalized or 
                fund_name_normalized in normalized or
                match_partial_names_func(proj_name, fund_name_normalized)):
                amount = funding_map[fund_name_normalized]
                matched_projects.append({
                    'Project_Name': proj_name,
                    'Funding': amount,
                    'Matched_With': fund_name_normalized
                })
                total_funding += amount
                matched = True
                break
    
    if not matched:
        print('No funding found for:', proj_name)

print('Matched', len(matched_projects), 'projects with funding')
print('Total funding:', total_funding)

# Prepare final result
final_result = {
    'count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
