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

# All project names from funding (for matching)
funding_project_names = funding_df['Project_Name'].tolist()

# Function to extract projects from civic document text
def extract_projects_from_text(text, filename):
    projects = []
    
    # Split text into lines for processing
    lines = text.split('\n')
    
    # Patterns to identify sections and projects
    current_section = None
    current_status = None
    
    section_patterns = {
        'design': r'(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Design Phase\)|Projects Under Design)',
        'construction': r'(Capital Improvement Projects \(Construction\)|Construction Projects)',
        'completed': r'(Capital Improvement Projects \(Completed\)|Completed Projects)',
        'not_started': r'(Capital Improvement Projects \(Not Started\)|Future Projects)'
    }
    
    # Look for project names typically on their own line after bullet points or similar
    # Common patterns: project name, then updates/schedule info
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers
        for status_key, pattern in section_patterns.items():
            if re.search(pattern, line, re.IGNORECASE):
                current_section = status_key
                current_status = status_key
                break
        
        # Skip empty lines or common header/footer lines
        if not line or line.startswith('Page') or line.startswith('Agenda Item'):
            i += 1
            continue
            
        # Look for project names - they're typically capitalized, descriptive
        # and followed by update/project schedule sections
        # Pattern: line is not a header, not empty, reasonably long, and appears to be a title
        if (current_status and 
            len(line) > 10 and 
            not line.startswith('To:') and 
            not line.startswith('From:') and 
            not line.startswith('Date:') and
            not line.startswith('Subject:') and
            not line.startswith('RECOMMENDED ACTION:') and
            not line.startswith('DISCUSSION:') and
            not any(keyword in line.upper() for keyword in ['UPDATES:', 'SCHEDULE:', 'DESCRIPTION:']) and
            not line.startswith('(') and  # Not a sub-bullet
            line == line.strip()):  # Clean line
            
            # Check if next few lines contain project indicators
            next_lines = ' '.join(lines[i+1:i+4]).lower()
            if 'update' in next_lines or 'schedule' in next_lines or 'description' in next_lines:
                
                # Determine type (capital or disaster)
                project_type = 'capital'  # default in these sections
                if 'fema' in line.lower() or 'caloes' in line.lower() or 'disaster' in filename.lower():
                    project_type = 'disaster'
                
                # Extract topics from the line
                topics = []
                line_lower = line.lower()
                topic_keywords = ['park', 'road', 'fema', 'fire', 'emergency warning', 
                                 'drainage', 'storm drain', 'highway', 'bridge', 
                                 'playground', 'water treatment', 'guardrail', 'resurfacing',
                                 'sidewalk', 'culvert', 'retaining wall', 'signals',
                                 'median', 'crosswalk', 'walkway']
                for keyword in topic_keywords:
                    if keyword in line_lower:
                        topics.append(keyword)
                
                projects.append({
                    'Project_Name': line,
                    'status': current_status,
                    'type': project_type,
                    'topics': ','.join(topics),
                    'source_file': filename
                })
        
        i += 1
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc['text'], doc['filename'])
    all_projects.extend(projects)

# Create DataFrame
projects_df = pd.DataFrame(all_projects)

# Filter for design status and capital type
design_capital = projects_df[
    (projects_df['status'] == 'design') & 
    (projects_df['type'] == 'capital')
]

# Get project names
design_capital_names = design_capital['Project_Name'].tolist()

# Match with funding data
# For each design capital project, check if it exists in funding data and has amount > 50000
matched_projects = []
for _, project in design_capital.iterrows():
    proj_name = project['Project_Name']
    
    # Find matching funding records - exact match first
    funding_matches = funding_df[funding_df['Project_Name'] == proj_name]
    
    # If no exact match, try to find if project name is contained in funding name or vice versa
    if funding_matches.empty:
        funding_matches = funding_df[
            funding_df['Project_Name'].str.contains(re.escape(proj_name), case=False, na=False) |
            pd.Series([proj_name.lower() in name.lower() for name in funding_df['Project_Name']])
        ]
    
    for _, funding in funding_matches.iterrows():
        if funding['Amount'] > 50000:
            matched_projects.append({
                'Project_Name': proj_name,
                'Funding_Project_Name': funding['Project_Name'],
                'Amount': funding['Amount'],
                'Funding_Source': funding['Funding_Source']
            })

# Count unique projects
unique_project_names = set([p['Project_Name'] for p in matched_projects])
count = len(unique_project_names)

result = {
    'count_design_capital_over_50000': count,
    'sample_matches': matched_projects[:5] if matched_projects else []
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
