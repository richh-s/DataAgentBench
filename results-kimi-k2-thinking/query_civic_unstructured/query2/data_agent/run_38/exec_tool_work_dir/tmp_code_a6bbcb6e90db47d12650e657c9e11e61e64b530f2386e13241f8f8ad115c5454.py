code = """import json
import pandas as pd

# Load civic documents data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

print(f"Total funding records: {len(funding_df)}")
print(f"Funding columns: {funding_df.columns.tolist()}")
print(f"Sample projects: {funding_df['Project_Name'].head().tolist()}")

# Initialize variables to store results
projects_found = []
matched_funding = 0
match_details = []

# Process each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split into lines and process
    lines = text.split('\n')
    
    # Look for project sections with park, completion, and 2022
    current_project = None
    project_buffer = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this looks like a project title
        if (len(line) < 150 and 
            not line.startswith('(') and 
            not line.startswith('\u2022') and  # bullet point
            not line.startswith('-') and
            not line.startswith('cid:') and
            any(keyword in line.lower() for keyword in ['project', 'repairs', 'improvements', 'construction'])):
            
            # Check previous project buffer before starting new one
            if current_project and project_buffer:
                buffer_text = ' '.join(project_buffer).lower()
                if ('completed' in buffer_text and '2022' in buffer_text and 
                    'park' in buffer_text):
                    projects_found.append(current_project)
            
            # Start new project
            current_project = line
            project_buffer = [line]
        elif current_project:
            project_buffer.append(line)
    
    # Check final project
    if current_project and project_buffer:
        buffer_text = ' '.join(project_buffer).lower()
        if ('completed' in buffer_text and '2022' in buffer_text and 
            'park' in buffer_text):
            projects_found.append(current_project)

# Remove duplicates
projects_found = list(set(projects_found))
print(f"Found {len(projects_found)} unique park projects completed in 2022")
print(f"Sample projects: {projects_found[:5]}")

# Create normalized lookup for funding data
funding_df['normalized'] = funding_df['Project_Name'].str.lower().str.replace('[^a-z0-9]', ' ', regex=True).str.replace('project', '').str.strip()

# Match projects
for project in projects_found:
    norm_project = re.sub('[^a-z0-9]', ' ', project.lower()).replace('project', '').strip()
    
    # Find matches
    for idx, row in funding_df.iterrows():
        if row['normalized'] in norm_project or norm_project in row['normalized']:
            matched_funding += row['Amount']
            match_details.append({
                'civic_project': project,
                'funding_project': row['Project_Name'],
                'amount': row['Amount']
            })

print(f"Total matched funding: ${matched_funding:,.2f}")
print(f"Matches: {len(match_details)}")

# Save detailed results
detailed_results = {
    'total_funding': matched_funding,
    'number_of_matches': len(match_details),
    'projects_found': projects_found,
    'funding_matches': match_details[:10]  # Top 10 matches
}

print('__RESULT__:')
print(json.dumps(detailed_results))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
