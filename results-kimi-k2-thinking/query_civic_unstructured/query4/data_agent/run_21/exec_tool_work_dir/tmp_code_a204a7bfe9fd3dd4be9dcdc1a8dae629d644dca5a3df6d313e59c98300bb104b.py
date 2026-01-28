code = """import json, re, os

# Load data from files
with open(var_functions.query_db_48, 'r') as f:
    funding_records = json.load(f)

with open(var_functions.query_db_74, 'r') as f:
    spring_docs = json.load(f)

print(f"Loaded {len(funding_records)} funding records")
print(f"Loaded {len(spring_docs)} documents containing Spring 2022 references")

# Create funding lookup
funding_lookup = {}
for record in funding_records:
    funding_lookup[record['Project_Name']] = int(record['Amount'])

spring_projects = set()

for doc in spring_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Detect Spring 2022 mentions
        if 'Spring 2022' in line or '2022-Spring' in line:
            # Look backwards for project name
            for j in range(i-1, max(0, i-5), -1):
                prev_line = lines[j].strip().replace('•', '').replace('·', '')
                if prev_line and len(prev_line) > 5 and len(prev_line) < 200:
                    # Check for project indicators
                    project_indicators = ['project', 'improvements', 'repairs', 'repaving', 'installation', 'construction', 'upgrades', 'development', 'renovation', 'replacement']
                    has_indicator = any(keyword in prev_line.lower() for keyword in project_indicators)
                    
                    # Check for title case pattern
                    words = prev_line.split()
                    if words:
                        capitalized = sum(1 for w in words if w and w[0].isupper())
                        capital_ratio = capitalized / len(words)
                        is_title_case = capital_ratio > 0.4
                        
                        if has_indicator or is_title_case:
                            spring_projects.add(prev_line)
                            break

print(f"Found {len(spring_projects)} Spring 2022 projects")
print("Sample projects found:")
for sp in list(spring_projects)[:10]:
    print(f"  - {sp}")

# Match with funding
def normalize_name(name):
    return ''.join(c for c in name if c.isalnum() or c.isspace()).lower().strip()

matched_projects = {}
for proj_name in spring_projects:
    # Exact match
    if proj_name in funding_lookup:
        matched_projects[proj_name] = funding_lookup[proj_name]
        continue
    
    # Try base name match
    base_proj = proj_name.split('(')[0].strip()
    for fund_name, amount in funding_lookup.items():
        base_fund = fund_name.split('(')[0].strip()
        if normalize_name(base_proj) == normalize_name(base_fund):
            matched_projects[fund_name] = amount
            break

print(f"\nMatched {len(matched_projects)} projects with funding data")

# Calculate totals
total_projects = len(matched_projects)
total_funding = sum(matched_projects.values())

print(f"\n{'='*70}")
print(f"SPRING 2022 PROJECTS: {total_projects}")
print(f"TOTAL FUNDING: ${total_funding:,}")
print(f"{'='*70}")

for proj_name, amount in matched_projects.items():
    print(f"• {proj_name}: ${amount:,}")

result = {
    'total_projects': total_projects,
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print("\\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
