code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:28']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_path = locals()['var_functions.query_db:6']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Funding records count', len(funding_data))
print('Civic documents count', len(civic_docs))

# Patterns for Spring 2022
patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        # Check for Spring 2022 patterns
        for pattern in patterns:
            if pattern in line_clean:
                # Find project name backwards
                project = 'Unknown Project'
                for j in range(i-1, max(0, i-10), -1):
                    prev = lines[j].strip()
                    
                    if not prev or prev.startswith('('):
                        continue
                    
                    prev_lower = prev.lower()
                    # Skip metadata
                    meta_terms = ['page', 'agenda item', 'updates', 'cid']
                    has_meta = False
                    for term in meta_terms:
                        if term in prev_lower:
                            has_meta = True
                            break
                    
                    if has_meta:
                        continue
                    
                    if 10 < len(prev) < 150 and prev[0].isupper():
                        project = prev
                        break
                
                if project not in spring_projects:
                    spring_projects.append(project)
                break

# Normalize function
def normalize(n):
    n = re.sub(r'\s*\(.*?\)\s*$', '', n)
    return n.strip().lower()

# Build funding map
funding_map = {}
for r in funding_data:
    name = r['Project_Name']
    norm = normalize(name)
    amount = int(r['Amount'])
    if norm not in funding_map or amount > funding_map[norm]:
        funding_map[norm] = amount

print('Spring projects found', len(spring_projects))
for p in spring_projects:
    print('-', p)

# Partial matching
def partial_match(n1, n2):
    w1 = set(n1.lower().split())
    w2 = set(n2.lower().split())
    common = w1 & w2
    # Remove generic words
    generic = {'project', 'improvements', 'repairs', 'design', 'construction', 'citywide', 'phase'}
    common = common - generic
    return len(common) >= 2

# Match with funding
matched = []
total = 0

for proj in spring_projects:
    norm_proj = normalize(proj)
    found = False
    
    if norm_proj in funding_map:
        amount = funding_map[norm_proj]
        matched.append({'Project_Name': proj, 'Funding': amount})
        total += amount
        found = True
    else:
        for fund_norm in funding_map:
            if norm_proj in fund_norm or fund_norm in norm_proj or partial_match(proj, fund_norm):
                amount = funding_map[fund_norm]
                matched.append({'Project_Name': proj, 'Funding': amount, 'Matched': fund_norm})
                total += amount
                found = True
                break
    
    if not found:
        print('No funding for', proj)

result = {
    'count': len(matched),
    'total_funding': total,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
