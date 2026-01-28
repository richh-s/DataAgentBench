code = """import json
import pandas as pd
import re

# Load data
f_file = locals()['var_functions.query_db:9']
c_file = locals()['var_functions.query_db:5']

with open(f_file, 'r') as f:
    funding_data = json.load(f)
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract projects from civic documents
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (not bullet points, not headers, reasonable length)
        if (line and 
            not line.startswith('(') and 
            not any(header in line for header in ['Page', 'Agenda', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Item #']) and
            len(line) > 5 and 
            len(line.split()) <= 15 and
            i + 1 < len(lines)):
            
            # Check if next line is project details
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line or any(keyword in next_line for keyword in ['Complete Design', 'Begin Construction', 'Advertise', 'Project Schedule']):
                
                # Look for date information after this project (next few lines)
                project_info = {
                    'Project_Name': line,
                    'Has_2022_Date': False,
                    'Is_Disaster': False,
                    'Date_Info': '',
                    'Context': ''
                }
                
                # Search for 2022 dates in following lines
                for j in range(i+1, min(i+8, len(lines))):
                    check_line = lines[j].strip()
                    if '2022' in check_line:
                        project_info['Has_2022_Date'] = True
                        project_info['Date_Info'] = check_line
                        # Get context (3 lines before and after)
                        context_start = max(0, j-3)
                        context_end = min(len(lines), j+4)
                        project_info['Context'] = ' '.join([l.strip() for l in lines[context_start:context_end]])
                        break
                
                # Check if disaster-related (in name or context)
                disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'woolsey', 'recovery']
                project_lower = line.lower()
                context_lower = project_info['Context'].lower()
                
                project_info['Is_Disaster'] = any(kw.lower() in project_lower or kw.lower() in context_lower for kw in disaster_keywords)
                
                extracted_projects.append(project_info)

# Filter for disaster projects with 2022 dates
disaster_projects_2022 = [p for p in extracted_projects if p['Is_Disaster'] and p['Has_2022_Date']]

print('Total extracted projects:', len(extracted_projects))
print('Disaster projects with 2022 dates:', len(disaster_projects_2022))

# Get project names for matching
project_names_2022 = [p['Project_Name'] for p in disaster_projects_2022]

# Match with funding data
matched_funding = funding_df[funding_df['Project_Name'].isin(project_names_2022)]

# Also check for partial matches and similar names
partial_matches = []
for proj_name in project_names_2022:
    # Try to find funding records that contain this project name or are very similar
    matching = funding_df[funding_df['Project_Name'].str.contains(proj_name.split('(')[0].strip()[:30], case=False, na=False)]
    if not matching.empty:
        partial_matches.append(matching)

if partial_matches:
    partial_funding = pd.concat(partial_matches).drop_duplicates()
else:
    partial_funding = pd.DataFrame()

print('Exact name matches in funding:', len(matched_funding))
print('Partial matches found:', len(partial_funding))

total_funding = 0
if not matched_funding.empty:
    total_funding += matched_funding['Amount'].sum()
if not partial_funding.empty:
    total_funding += partial_funding['Amount'].sum()

# Also check funding records with 2022 and disaster indicators
funding_disaster_2022 = funding_df[
    (funding_df['Project_Name'].str.contains('|'.join(['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster']), case=False, na=False)) &
    (funding_df['Project_Name'].str.contains('2022', case=False, na=False))
]

print('Direct funding matches (2022+disaster):', len(funding_disaster_2022))
if not funding_disaster_2022.empty:
    print('Direct funding amount:', funding_disaster_2022['Amount'].sum())
    total_funding = funding_disaster_2022['Amount'].sum()

# Show sample disaster projects with 2022 dates
print('\nSample disaster projects starting in 2022:')
for p in disaster_projects_2022[:5]:
    print(f"  {p['Project_Name']}")
    print(f"  Date: {p['Date_Info']}")
    print()

result = {
    'total_funding': int(total_funding),
    'disaster_2022_projects_found': len(disaster_projects_2022),
    'exact_funding_matches': len(matched_funding),
    'partial_funding_matches': len(partial_funding)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:18': {'total_disaster_funding': 1410000, 'disaster_project_count': 27, 'sample_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': 85000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': 14000}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': 81000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': 43000}]}, 'var_functions.execute_python:26': {'all_disaster': 1410000, 'twentytwo_disaster': 0}}

exec(code, env_args)
