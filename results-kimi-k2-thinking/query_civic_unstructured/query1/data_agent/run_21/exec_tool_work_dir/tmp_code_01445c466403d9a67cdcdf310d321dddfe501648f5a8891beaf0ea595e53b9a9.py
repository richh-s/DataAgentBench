code = """import json
import pandas as pd

# Load funding data
funding_path = locals().get('var_functions.query_db:2', '')
if isinstance(funding_path, str) and funding_path:
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals().get('var_functions.query_db:2', [])

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Load civic documents
civic_doc_path = locals().get('var_functions.query_db:10', '')
if isinstance(civic_doc_path, str) and civic_doc_path:
    with open(civic_doc_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals().get('var_functions.query_db:10', [])

# Extract projects by analyzing document structure
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    current_status = None
    in_design_section = False
    
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        # Skip empty lines and page markers
        if not line_clean or 'Page' in line_clean or 'Agenda Item' in line_clean:
            continue
        
        # Check for section headers with status information
        if '(Design)' in line_clean:
            current_status = 'design'
            in_design_section = True
            continue
        elif '(Construction)' in line_clean or '(Completed)' in line_clean or '(Not Started)' in line_clean:
            in_design_section = False
            continue
        
        # Extract project names in design sections
        if in_design_section and current_status == 'design':
            # Look for lines that appear to be project names (not headers, not bullet points)
            if (len(line_clean) > 10 and 
                not line_clean.endswith(':') and 
                not line_clean.startswith('To:') and
                not line_clean.startswith('From:') and
                not line_clean.startswith('Date:') and
                not line_clean.startswith('Subject:') and
                not 'RECOMMENDED ACTION' in line_clean and
                not 'DISCUSSION' in line_clean):
                
                # Check if next line suggests this is a project
                if i + 1 < len(lines):
                    next_line = lines[i+1].strip()
                    if '(cid' in next_line and 'Updates' in lines[i+2] if i+2 < len(lines) else False:
                        project_name = line_clean
                        
                        # Determine type (capital vs disaster)
                        project_type = 'disaster' if 'fema' in project_name.lower() or 'caloes' in project_name.lower() else 'capital'
                        
                        # Extract topics
                        topics = []
                        pname_lower = project_name.lower()
                        topic_list = ['park', 'road', 'drainage', 'storm drain', 'bridge', 'playground', 
                                     'water treatment', 'guardrail', 'resurfacing', 'culvert', 'retaining wall', 
                                     'signals', 'median', 'crosswalk', 'walkway', 'fema', 'fire']
                        for topic in topic_list:
                            if topic in pname_lower:
                                topics.append(topic)
                        
                        all_projects.append({
                            'Project_Name': project_name,
                            'status': current_status,
                            'type': project_type,
                            'topics': ','.join(topics),
                            'source_file': filename
                        })

# Create DataFrame and filter
df_projects = pd.DataFrame(all_projects)
design_capital_projects = df_projects[
    (df_projects['status'] == 'design') & 
    (df_projects['type'] == 'capital')
]

# Match design capital projects with funding > 50000
matched_count = 0
matched_names = []

for _, project in design_capital_projects.iterrows():
    proj_name = project['Project_Name']
    
    # Try exact match first
    funding_match = funding_df[funding_df['Project_Name'] == proj_name]
    
    # If no exact match, try to find if project name is contained in any funding name
    if funding_match.empty:
        for _, fund in funding_df.iterrows():
            if proj_name.lower() in fund['Project_Name'].lower():
                funding_match = funding_match.append(fund)
    
    # Check if any match has Amount > 50000
    if not funding_match.empty:
        for _, fund in funding_match.iterrows():
            if fund['Amount'] > 50000:
                matched_names.append(proj_name)
                matched_count += 1
                break

# Count unique projects
unique_matched = len(set(matched_names))

result = {
    'count_design_capital_projects_with_funding_over_50000': unique_matched,
    'sample_matched_projects': list(set(matched_names))[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
