code = """import json
import re
import pandas as pd

# Load civic documents from file path
civic_doc_path = locals().get('var_functions.query_db:10', '')
if isinstance(civic_doc_path, str) and civic_doc_path:
    with open(civic_doc_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals().get('var_functions.query_db:10', [])

# Load funding data from file path
funding_path = locals().get('var_functions.query_db:2', '')
if isinstance(funding_path, str) and funding_path:
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals().get('var_functions.query_db:2', [])

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Function to extract projects from civic document text
def extract_projects_from_text(text, filename):
    projects = []
    lines = text.split('\n')
    
    current_section = None
    current_status = None
    
    # Look for section headers that indicate status
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Skip empty lines and page markers
        if not line_clean or line_clean.startswith('Page') or line_clean.startswith('Agenda Item'):
            continue
        
        # Detect section based on keywords
        if '(Design)' in line_clean or 'Under Design' in line_clean:
            current_status = 'design'
            continue
        elif '(Construction)' in line_clean:
            current_status = 'construction'
            continue
        elif '(Completed)' in line_clean:
            current_status = 'completed'
            continue
        elif '(Not Started)' in line_clean:
            current_status = 'not_started'
            continue
        
        # Only look for projects when we're in a design section
        if current_status != 'design':
            continue
            
        # Look for project names - they're typically after blank lines and followed by indented content
        if len(line_clean) > 10 and not line_clean.endswith(':'):
            # Skip headers
            if any(header in line_clean for header in ['To:', 'From:', 'Date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION']):
                continue
            if line_clean.startswith('(') and line_clean.endswith(')'):
                continue
                
            # Check if next lines contain project descriptors
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if next_line.startswith('(') and 'cid' in next_line:
                    # This is likely a project name
                    proj_name = line_clean
                    
                    # Determine type
                    proj_type = 'capital'
                    if 'fema' in proj_name.lower() or 'caloes' in proj_name.lower():
                        proj_type = 'disaster'
                    
                    # Extract topics
                    topics = []
                    proj_lower = proj_name.lower()
                    topic_list = ['park', 'road', 'fema', 'fire', 'emergency warning', 'drainage', 
                                 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 
                                 'guardrail', 'resurfacing', 'sidewalk', 'culvert', 'retaining wall', 
                                 'signals', 'median', 'crosswalk', 'walkway']
                    for topic in topic_list:
                        if topic in proj_lower:
                            topics.append(topic)
                    
                    projects.append({
                        'Project_Name': proj_name,
                        'status': current_status,
                        'type': proj_type,
                        'topics': ','.join(topics),
                        'source_file': filename
                    })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'], doc['filename'])
    all_projects.extend(projects)

# Create DataFrame and filter for design status and capital type
projects_df = pd.DataFrame(all_projects)
if not projects_df.empty:
    design_capital = projects_df[
        (projects_df['status'] == 'design') & 
        (projects_df['type'] == 'capital')
    ]
    design_capital_names = design_capital['Project_Name'].tolist()
else:
    design_capital_names = []

# Match with funding data
matched_projects = []
if not funding_df.empty and design_capital_names:
    for _, project in design_capital.iterrows():
        proj_name = project['Project_Name']
        
        # Exact match
        funding_matches = funding_df[funding_df['Project_Name'] == proj_name]
        
        if funding_matches.empty:
            # Try partial matching
            for _, funding in funding_df.iterrows():
                f_name = funding['Project_Name']
                if (proj_name.lower() in f_name.lower() or f_name.lower() in proj_name.lower()):
                    funding_matches = funding_matches.append(funding)
        
        for _, funding in funding_matches.iterrows():
            if funding['Amount'] > 50000:
                matched_projects.append({
                    'Project_Name': proj_name,
                    'Funding_Project_Name': funding['Project_Name'],
                    'Amount': funding['Amount']
                })

# Count unique projects
count = len(set([p['Project_Name'] for p in matched_projects]))

result = {'count_design_capital_over_50000': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
