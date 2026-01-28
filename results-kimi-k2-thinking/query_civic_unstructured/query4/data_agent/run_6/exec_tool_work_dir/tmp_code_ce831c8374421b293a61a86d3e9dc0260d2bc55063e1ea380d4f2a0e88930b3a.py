code = """import json
import re

civic_file = locals()['var_functions.query_db:38']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = locals()['var_functions.query_db:28']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

spring_patterns = ['Spring 2022', 'Spring/Summer 2022', '2022-Spring', '2022-March', '2022-April', '2022-May']

projects_found = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        for pattern in spring_patterns:
            if pattern in line and ('Begin' in line or 'Start' in line or 'Construction' in line or 'Design' in line):
                project_name = 'Unknown'
                # Look backwards for project name
                for j in range(i-1, max(0, i-5), -1):
                    prev = lines[j].strip()
                    if prev and not prev.startswith('(') and 10 < len(prev) < 150:
                        if prev[0].isupper() and not any(x in prev.lower() for x in ['page', 'agenda item']):
                            project_name = prev
                            break
                
                if project_name not in [p['name'] for p in projects_found] and project_name != 'Unknown':
                    projects_found.append({'name': project_name, 'schedule_line': line})

# Normalize names for matching
def normalize(n):
    return re.sub(r'\s*\(.*?\)\s*$', '', n).strip().lower()

# Build funding map
funding_map = {}
for rec in funding_data:
    name = rec['Project_Name']
    norm = normalize(name)
    amount = int(rec['Amount'])
    if norm not in funding_map or amount > funding_map[norm]:
        funding_map[norm] = amount

# Match and calculate
matched = []
total = 0

for project in projects_found:
    proj_name = project['name']
    norm_proj = normalize(proj_name)
    
    if norm_proj in funding_map:
        amount = funding_map[norm_proj]
        matched.append({'name': proj_name, 'funding': amount})
        total += amount
    else:
        # Try partial match
        for fund_norm in funding_map:
            if norm_proj in fund_norm or fund_norm in norm_proj:
                amount = funding_map[fund_norm]
                matched.append({'name': proj_name, 'funding': amount, 'matched': fund_norm})
                total += amount
                break

print('Found', len(matched), 'Spring 2022 projects with funding')
print('Total funding', total)
for m in matched:
    print('-', m['name'], ': $', m['funding'])

result = {
    'count': len(matched),
    'total_funding': total
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
