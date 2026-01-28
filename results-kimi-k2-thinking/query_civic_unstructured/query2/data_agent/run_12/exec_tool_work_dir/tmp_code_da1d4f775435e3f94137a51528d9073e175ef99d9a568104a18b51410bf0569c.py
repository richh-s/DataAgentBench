code = """import json
import pandas as pd
import re

# Load funding data
with open('funding_data.json', 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open('civic_docs_data.json', 'r') as f:
    civic_docs_data = json.load(f)

# Create funding dataframe
df_funding = pd.DataFrame(funding_data)

# Function to extract project information from civic docs text
def extract_projects_from_doc(doc_text):
    projects = []
    
    # Look for project sections - they often start with project names in a specific format
    # Common patterns: project name followed by updates or status
    lines = doc_text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Look for project names (often bolded or with specific markers)
        # Pattern: project name line, often followed by updates
        if line.endswith('Project') or 'Park' in line or ('Updates:' in line and current_project):
            
            # If we were tracking a project, save it
            if current_project and project_info.get('status') == 'completed':
                projects.append({
                    'Project_Name': current_project,
                    'topic': project_info.get('topic', ''),
                    'status': project_info.get('status', ''),
                    'et': project_info.get('et', '')
                })
            
            # Start new project
            if 'Updates:' not in line:
                current_project = line.replace('\u2013', '-').replace('\u201c', '"').replace('\u201d', '"')
                project_info = {'topic': '', 'status': '', 'et': ''}
                
                # Determine topic based on project name
                if 'park' in line.lower():
                    project_info['topic'] = 'park'
                elif 'drain' in line.lower() or 'storm' in line.lower():
                    project_info['topic'] = 'drainage,storm drain'
                elif 'road' in line.lower():
                    project_info['topic'] = 'road'
                elif 'FEMA' in line:
                    project_info['topic'] = 'FEMA'
                
        # Look for status information
        if 'completed' in line.lower() and current_project:
            project_info['status'] = 'completed'
            
            # Extract date information
            date_patterns = [
                r'(?:completed|completion)[\s,]*([A-Za-z]+\s*\d{4})',
                r'(?:completed|completion)[\s,]*(\d{4}-[A-Za-z]+)',
                r'([A-Za-z]+\s*\d{4})[\s,-]*completed',
                r'(\d{4})[\s,-]*completed'
            ]
            
            for pattern in date_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    date_str = match.group(1)
                    if '2022' in date_str:
                        project_info['et'] = date_str
                    break
    
    # Don't forget the last project
    if current_project and project_info.get('status') == 'completed':
        projects.append({
            'Project_Name': current_project,
            'topic': project_info.get('topic', ''),
            'status': project_info.get('status', ''),
            'et': project_info.get('et', '')
        })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs_data:
    projects = extract_projects_from_doc(doc['text'])
    all_projects.extend(projects)

# Create projects dataframe
df_projects = pd.DataFrame(all_projects)

# Print extraction results for debugging
print("Extracted projects:")
for proj in all_projects[:10]:
    print(f"  {proj}")

print(f"\nTotal extracted projects: {len(all_projects)}")

# Filter for park-related projects completed in 2022
park_projects_2022 = df_projects[
    (df_projects['topic'].str.contains('park', case=False, na=False)) &
    (df_projects['status'] == 'completed') &
    (df_projects['et'].str.contains('2022', na=False))
]

print(f"\nPark projects completed in 2022: {len(park_projects_2022)}")
print(park_projects_2022[['Project_Name', 'et']].head(10))

# Clean project names for matching
park_projects_2022['Project_Name_Clean'] = park_projects_2022['Project_Name'].str.replace(
    r'\s*Project\s*$', '', regex=True, case=False
).str.strip()

# Clean funding project names
df_funding['Project_Name_Clean'] = df_funding['Project_Name'].str.replace(
    r'\s*Project\s*$', '', regex=True, case=False
).str.strip()

# Merge with funding data
merged = pd.merge(
    park_projects_2022, 
    df_funding, 
    left_on='Project_Name_Clean', 
    right_on='Project_Name_Clean',
    how='inner'
)

print(f"\nMerged records: {len(merged)}")
if len(merged) > 0:
    print(merged[['Project_Name_x', 'Amount']].head())
    total_funding = merged['Amount'].astype(int).sum()
    print(f"\nTotal funding: ${total_funding:,}")
else:
    print("No matches found - trying fuzzy matching")
    
    # Try to find matches manually
    park_names = set(park_projects_2022['Project_Name_Clean'].tolist())
    funding_names = set(df_funding['Project_Name_Clean'].tolist())
    
    matches = []
    for park_name in park_names:
        for fund_name in funding_names:
            if park_name.lower() in fund_name.lower() or fund_name.lower() in park_name.lower():
                matches.append((park_name, fund_name))
    
    print(f"Potential matches: {matches[:10]}")
    
    # Collect amounts for matched projects
    total_funding = 0
    matched_projects = []
    
    for park_name, fund_name in matches:
        park_rows = park_projects_2022[park_projects_2022['Project_Name_Clean'] == park_name]
        fund_rows = df_funding[df_funding['Project_Name_Clean'] == fund_name]
        
        if not park_rows.empty and not fund_rows.empty:
            amount = int(fund_rows.iloc[0]['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': park_name,
                'amount': amount
            })
    
    print(f"\nMatched projects: {len(matched_projects)}")
    for proj in matched_projects:
        print(f"  {proj['project']}: ${proj['amount']:,}")
    
    print(f"\nTotal funding: ${total_funding:,}")

# Save results for final answer
result = {
    'total_funding': total_funding if 'total_funding' in locals() else 0,
    'matched_projects': matched_projects if 'matched_projects' in locals() else []
}"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
