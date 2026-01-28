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

# Simple extraction - look for project names under design headings
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split on design sections
    design_sections = []
    lines = text.split('\n')
    current_section = []
    in_design = False
    
    for line in lines:
        line_clean = line.strip()
        if '(Design)' in line_clean:
            in_design = True
            if current_section:
                design_sections.append('\n'.join(current_section))
            current_section = []
        elif any(x in line_clean for x in ['(Construction)', '(Completed)', '(Not Started)']):
            in_design = False
        
        if in_design:
            current_section.append(line)
    
    if current_section:
        design_sections.append('\n'.join(current_section))
    
    # Extract project names from design sections
    for section in design_sections:
        section_lines = section.split('\n')
        for i, line in enumerate(section_lines):
            line_clean = line.strip()
            
            # Skip metadata
            if not line_clean or 'Page' in line_clean or 'Agenda Item' in line_clean:
                continue
            
            # Look for potential project names (reasonable length, not common headers)
            if len(line_clean) > 10 and not any(line_clean.startswith(x) for x in ['To:', 'From:', 'Date:', 'Subject:']):
                # Check if it's followed by project indicators
                if i + 2 < len(section_lines):
                    next_lines = section_lines[i+1] + section_lines[i+2]
                    if 'Updates' in next_lines or 'Schedule' in next_lines:
                        # This is likely a project name
                        proj_type = 'disaster' if 'fema' in line_clean.lower() or 'caloes' in line_clean.lower() else 'capital'
                        
                        all_projects.append({
                            'Project_Name': line_clean,
                            'status': 'design',
                            'type': proj_type,
                            'source_file': filename
                        })

# Filter for capital design projects
design_capital = [p for p in all_projects if p['status'] == 'design' and p['type'] == 'capital']

# Match with funding data
count = 0
matched_projects = []

for project in design_capital:
    proj_name = project['Project_Name']
    
    # Check funding table for matches
    for _, fund in funding_df.iterrows():
        fund_name = fund['Project_Name']
        
        # Check if project names match (partial or exact)
        if proj_name.lower() in fund_name.lower() or fund_name.lower() in proj_name.lower():
            if fund['Amount'] > 50000:
                count += 1
                matched_projects.append(proj_name)
                break

# Get unique count
unique_count = len(set(matched_projects))

result = {
    'count': unique_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_documents': 5, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
