code = """import json
import re
import pandas as pd

# Load data from storage variables
civic_docs_path = locals()['var_functions.query_db:36']
funding_path = locals()['var_functions.query_db:37']

with open(civic_docs_path, 'r') as f:
    civic_docs_list = json.load(f)

with open(funding_path, 'r') as f:
    funding_list = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_list)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Extract projects from civic documents
extracted_projects = []

for doc in civic_docs_list:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Detect project name (uppercase or lines ending with Project)
        if (line.isupper() and len(line) > 10) or (line.endswith('Project') and len(line) > 15):
            current_project = line
        
        # Look for status updates
        if current_project and ('Updates:' in line or 'cid:190' in line):
            # Check next few lines for status info
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip()
                if not next_line:
                    continue
                    
                # Look for completion info
                if 'completed' in next_line.lower():
                    # Look for year
                    year_match = re.search(r'(20\d\d)', next_line)
                    if year_match:
                        year = year_match.group(1)
                        # Check if park-related
                        is_park = 'park' in current_project.lower() or 'park' in next_line.lower()
                        
                        if is_park:
                            extracted_projects.append({
                                'Project_Name': current_project,
                                'status': 'completed',
                                'year': year,
                                'is_park': True
                            })
                        break

# Create projects DataFrame
projects_df = pd.DataFrame(extracted_projects)

# Filter for park projects completed in 2022
park_completed_2022 = projects_df[
    (projects_df['is_park'] == True) & 
    (projects_df['status'] == 'completed') & 
    (projects_df['year'] == '2022')
]

# Get unique project names
project_names_2022 = park_completed_2022['Project_Name'].unique()

# Match with funding data
total_funding = 0
matched_projects = []

for project_name in project_names_2022:
    # Normalize project name for matching
    norm_name = project_name.lower()
    norm_name = norm_name.replace('(caloes project)', '').replace('(fema project)', '').strip()
    
    # Find matching funding records
    for _, fund_row in funding_df.iterrows():
        fund_name = fund_row['Project_Name'].lower()
        
        # Check for direct match or key term overlap
        proj_terms = set(norm_name.split())
        fund_terms = set(fund_name.split())
        
        # Simple matching: check if first word matches and both contain 'park'
        if ('park' in fund_name and 'park' in norm_name) or \
           any(term in fund_name for term in ['bluffs', 'trancas', 'malibu', 'legacy'] if term in norm_name):
            # Additional check for project type match
            if any(word in fund_name for word in norm_name.split()[:3]):
                amount = fund_row['Amount']
                if amount > 0:
                    total_funding += amount
                    matched_projects.append({
                        'civic_project': project_name,
                        'funding_project': fund_row['Project_Name'],
                        'amount': int(amount)
                    })

# Deduplicate matches
unique_matches = []
seen_funding = set()
for m in matched_projects:
    if m['funding_project'] not in seen_funding:
        unique_matches.append(m)
        seen_funding.add(m['funding_project'])

result = {
    'total_funding': int(total_funding),
    'matched_projects': unique_matches,
    'project_count': len(project_names_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:34': [], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:37': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
