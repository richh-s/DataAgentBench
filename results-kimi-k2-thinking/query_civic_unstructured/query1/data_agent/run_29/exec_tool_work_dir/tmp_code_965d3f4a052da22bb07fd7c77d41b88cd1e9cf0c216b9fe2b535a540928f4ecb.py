code = """import json
import pandas as pd

# Load the data from the stored files
funding_file = 'file_storage/functions.query_db:32.json'
civic_file = 'file_storage/functions.query_db:9.json'

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Create funding dataframe
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Extract projects from civic documents with design status
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    
    if design_start != -1:
        # Find the end of the design section
        end_markers = [
            text.find('Capital Improvement Projects (Construction)', design_start),
            text.find('Capital Improvement Projects (Not Started)', design_start),
            text.find('Disaster Recovery Projects', design_start)
        ]
        end_pos = min([pos for pos in end_markers if pos > 0], default=len(text))
        
        design_section = text[design_start:end_pos]
        lines = design_section.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            # Filter out noise
            if 5 < len(line) < 200 and not line.isupper():
                # Skip known headers and patterns
                skip_terms = ('Updates', 'Schedule', 'Advertise', 'Construction', 'Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement')
                if not any(term in line for term in skip_terms):
                    if not line.startswith(('(', '•', '-')):
                        # Check if followed by project indicators
                        if i < len(lines) - 2:
                            next_lines = ' '.join(lines[i+1:i+4])
                            if 'Updates' in next_lines or 'Complete Design' in next_lines:
                                design_projects.append(line)

# Remove duplicates while preserving order
unique_design_projects = []
seen = set()
for proj in design_projects:
    if proj not in seen:
        unique_design_projects.append(proj)
        seen.add(proj)

# Match with funding data - find exact and similar matches
funding_project_names = set(df_funding['Project_Name'])
matched_design_projects = []

for design_proj in unique_design_projects:
    # Check for exact match
    if design_proj in funding_project_names:
        matched_design_projects.append(design_proj)
    else:
        # Check for partial matches
        for funded_name in funding_project_names:
            if (design_proj in funded_name or funded_name in design_proj) and len(design_proj) > 10:
                matched_design_projects.append(design_proj)
                break

# Count projects with funding over $50,000
count_result = len(matched_design_projects)

print('__RESULT__:')
print(json.dumps({
    'count': count_result,
    'sample_projects': matched_design_projects[:10]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9'], 'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9', '__builtins__', 'json', 'pd', 'available_vars']}, 'var_functions.execute_python:14': {'funding_storage_type': "<class 'str'>", 'funding_storage_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'total_funding_records': 276, 'funding_over_50k': 276, 'sample_projects': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs']}, 'var_functions.execute_python:18': {'civic_docs_count': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_documents': 5, 'first_doc_keys': ['_id', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
