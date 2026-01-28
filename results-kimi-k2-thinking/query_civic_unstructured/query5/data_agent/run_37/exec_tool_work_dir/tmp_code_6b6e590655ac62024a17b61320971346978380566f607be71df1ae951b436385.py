code = """import json
import pandas as pd
import re

# Load the data files
f_file = locals()['var_functions.query_db:9']
with open(f_file, 'r') as f:
    funding_data = json.load(f)

c_file = locals()['var_functions.query_db:5']
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Step 1: Extract all information about projects from civic documents
disaster_projects_with_2022 = []

# Keywords to identify disaster projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'recovery', 'woolsey']

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check if this document mentions 2022
    if '2022' in text:
        # Look for lines that contain both disaster indicators and dates
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if '2022' in line:
                # Check if this line or nearby lines contain disaster indicators
                context = ' '.join(lines[max(0,i-3):min(len(lines),i+4)])
                
                # Check for disaster indicators
                has_disaster = any(keyword.lower() in context for keyword in disaster_keywords)
                
                if has_disaster:
                    # Try to find the project name (usually on previous lines)
                    project_name = 'Unknown'
                    for j in range(i-1, max(-1, i-10), -1):
                        prev_line = lines[j].strip()
                        if prev_line and not prev_line.startswith('(') and not any(x in prev_line for x in ['updates:', 'project schedule:', 'page', 'agenda']):
                            if len(prev_line) > 10 and len(prev_line.split()) <= 15:
                                project_name = prev_line
                                break
                    
                    disaster_projects_with_2022.append({
                        'Project_Name': project_name,
                        'Date_Information': line,
                        'Context': context[:150]
                    })

print('Disaster projects with 2022 dates found:', len(disaster_projects_with_2022))

# Step 2: Find all disaster-related funding projects
all_disaster_funding = []
disaster_pattern = re.compile(r'(FEMA|CalOES|CalJPIA|fire|disaster|recovery)', re.IGNORECASE)

for _, row in funding_df.iterrows():
    project_name = row['Project_Name']
    if disaster_pattern.search(project_name):
        all_disaster_funding.append({
            'Project_Name': project_name,
            'Amount': row['Amount'],
            'Funding_Source': row['Funding_Source']
        })

disaster_funding_df = pd.DataFrame(all_disaster_funding)
total_disaster_funding = disaster_funding_df['Amount'].sum()

print('Total disaster funding (all years):', total_disaster_funding)
print('Disaster project count (all years):', len(disaster_funding_df))

# Step 3: Check which disaster projects have indicators of 2022 start
# Projects with 2022 in their name
funding_with_2022_in_name = disaster_funding_df[disaster_funding_df['Project_Name'].str.contains('2022', case=False, na=False)]
total_2022_in_name = funding_with_2022_in_name['Amount'].sum()

print('Disaster projects with 2022 in name count:', len(funding_with_2022_in_name))
print('Total funding for these projects:', total_2022_in_name)

# Show sample projects
print('\nSample disaster projects with 2022 indicators:')
for _, proj in funding_with_2022_in_name.head(5).iterrows():
    print(f"  {proj['Project_Name']}: ${proj['Amount']}")

# Also check civic documents for 2022 Morning View project specifically
morning_view_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022 Morning View' in text and ('Storm Drain' in text or 'Resurfacing' in text):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '2022' in line and 'Morning View' in line:
                morning_view_2022.append(line)

print('\n2022 Morning View project mentions:', len(morning_view_2022))

result = {
    'disaster_projects_2022_from_docs': len(disaster_projects_with_2022),
    'total_disaster_funding_all_years': int(total_disaster_funding),
    'disaster_funding_2022_in_name': int(total_2022_in_name),
    'all_disaster_project_count': len(disaster_funding_df)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:18': {'total_disaster_funding': 1410000, 'disaster_project_count': 27, 'sample_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': 85000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': 14000}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': 81000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': 43000}]}}

exec(code, env_args)
