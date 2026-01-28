code = """import json
import pandas as pd
import re

# Load the data from the files
with open('data/query_result_694eef5c4ec675b6b5f5a285.json', 'r') as f:
    civic_docs = json.load(f)

with open('data/query_result_funding.json', 'r') as f:
    funding_data = json.load(f)

# Convert to DataFrames
funding_df = pd.DataFrame(funding_data)

# Extract project information from civic documents
projects = []
for doc in civic_docs:
    text = doc['text']
    
    # Find project sections - look for patterns like project names followed by details
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        # Check if this looks like a project name (often on its own line, title case)
        line = line.strip()
        if len(line) > 10 and line == line.title() and not line.startswith('(') and not line.isupper():
            # This could be a project name
            if current_project:
                projects.append(current_project)
            current_project = {'name': line, 'text': line + '\n'}
        elif current_project and (line.startswith('(') or line.startswith('•') or 'Updates:' in line or 'Project Schedule:' in line or 'cid:' in line):
            current_project['text'] += line + '\n'
    
    if current_project:
        projects.append(current_project)

# Parse project details
parsed_projects = []
for proj in projects:
    parsed = {'Project_Name': proj['name']}
    text = proj['text']
    
    # Extract type - look for disaster-related indicators
    if '(FEMA' in text or '(CalOES' in text or '(CalJPIA' in text:
        parsed['type'] = 'disaster'
    elif any(keyword in text.lower() for keyword in ['disaster', 'fema', 'fire recovery', 'emergency']):
        parsed['type'] = 'disaster'
    else:
        parsed['type'] = 'capital'  # Default to capital if not disaster
    
    # Extract start date/time
    st_match = re.search(r'(?:st:|Start|Begin|Advertise):\s*([^\n]+)', text, re.IGNORECASE)
    if st_match:
        parsed['st'] = st_match.group(1).strip()
    else:
        # Look for year patterns
        year_match = re.search(r'(202\d)\s*(?:Spring|Fall|Summer|Winter)?', text)
        if year_match:
            parsed['st'] = year_match.group(1)
    
    # Extract topic/keywords
    topic_keywords = []
    if 'FEMA' in text:
        topic_keywords.append('FEMA')
    if 'drainage' in text.lower() or 'storm' in text.lower():
        topic_keywords.append('drainage')
    if 'road' in text.lower():
        topic_keywords.append('road')
    if 'park' in text.lower():
        topic_keywords.append('park')
    if 'fire' in text.lower():
        topic_keywords.append('fire')
    if 'emergency' in text.lower():
        topic_keywords.append('emergency')
    
    parsed['topic'] = ', '.join(topic_keywords) if topic_keywords else ''
    
    parsed_projects.append(parsed)

# Create DataFrame of projects
projects_df = pd.DataFrame(parsed_projects)

# Filter for disaster projects that started in 2022
disaster_projects = projects_df[
    (projects_df['type'] == 'disaster') & 
    (projects_df['st'].str.contains('2022', na=False))
]

print(f"Found {len(disaster_projects)} disaster projects that started in 2022")
print("Projects:")
for _, proj in disaster_projects.iterrows():
    print(f"  - {proj['Project_Name']}")

# Join with funding data
# Look for exact matches or partial matches
matched_funding = []
for _, proj in disaster_projects.iterrows():
    proj_name = proj['Project_Name']
    
    # Direct match
    direct_match = funding_df[funding_df['Project_Name'] == proj_name]
    if not direct_match.empty:
        matched_funding.extend(direct_match.to_dict('records'))
    else:
        # Look for partial matches - project name appears in funding project name
        partial_match = funding_df[funding_df['Project_Name'].str.contains(proj_name, case=False, na=False)]
        if not partial_match.empty:
            matched_funding.extend(partial_match.to_dict('records'))
        else:
            # Try reverse - funding project name appears in project name
            for _, fund in funding_df.iterrows():
                if fund['Project_Name'].lower() in proj_name.lower():
                    matched_funding.append(fund.to_dict())

# Remove duplicates
matched_funding_df = pd.DataFrame(matched_funding).drop_duplicates()

# Also find all disaster-related projects in funding data that started in 2022
# This includes projects with FEMA/CalOES/CalJPIA in their names
disaster_funding = funding_df[
    funding_df['Project_Name'].str.contains(r'\(FEMA|\(CalOES|\(CalJPIA|Disaster|Fire|Emergency', case=False, na=False)
]

print(f"\nFound {len(disaster_funding)} disaster-related funding records")

# Sum up amounts
total_funding = disaster_funding['Amount'].astype(int).sum()

print(f"\nTotal funding for disaster-related projects: ${total_funding:,}")

# For debugging, show some matches
print("\nSample disaster funding records:")
print(disaster_funding.head(10).to_string())

print('__RESULT__:')
print(json.dumps({
    'total_funding': int(total_funding),
    'num_projects': len(disaster_funding),
    'sample_projects': disaster_funding.head(5).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
