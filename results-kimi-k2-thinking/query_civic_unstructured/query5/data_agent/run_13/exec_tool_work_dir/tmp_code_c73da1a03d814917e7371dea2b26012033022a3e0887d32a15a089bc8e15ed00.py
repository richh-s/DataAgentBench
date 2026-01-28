code = """import json
import re

# Load the full civic documents dataset
civic_docs_path = locals()['var_functions.query_db:2']
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs_full = json.load(f)
else:
    civic_docs_full = locals()['var_functions.query_db:2']

# Load the funding data
funding_data = locals()['var_functions.query_db:0']
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Initialize data structures
all_projects = []
disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'warning', 'siren']

# Parse each civic document
for doc in civic_docs_full:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections (each project typically has a name followed by details)
    # Split by common project markers
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Skip header/footer lines
        if any(skip in line for skip in ['Page', 'Agenda', 'Public Works', 'Commission', 'Item', 'To:', 'Prepared by', 'Approved by']):
            continue
            
        # Look for project names (they often appear as standalone lines, sometimes ending with "Project")
        # and are followed by status or schedule info
        if (i + 1 < len(lines) and 
            ('Updates:' in lines[i+1] or 'Schedule:' in lines[i+1] or 'Project Description:' in lines[i+1] or 
             lines[i+1].strip().startswith('(')) and
            len(line) < 150 and
            not line.startswith('-') and
            not line.startswith('•')):
            
            # Check if this looks like a project name (contains location + type)
            has_location = bool(re.search(r'[A-Z][a-z]+\s+(?:Road|Park|Canyon|Beach|Drive|Lane|Highway|Bridge|Street|Avenue)', line))
            has_type = bool(re.search(r'(?:Project|Improvements|Repairs|Replacement|Study|System|Drain|Drainage|Warning|Sirens)', line))
            
            if has_location or has_type:
                current_project = line
                project_info = {
                    'Project_Name': line,
                    'filename': filename,
                    'start_date': None,
                    'is_disaster': any(indicator.lower() in line.lower() for indicator in disaster_indicators)
                }
                
                # Look forward for schedule/start date info
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    if 'Begin' in next_line or 'Start' in next_line or 'Complete' in next_line:
                        if '2022' in next_line:
                            project_info['start_date'] = '2022'
                        elif any(season in next_line for season in ['Spring 2022', 'Summer 2022', 'Fall 2022', 'Winter 2022']):
                            project_info['start_date'] = '2022'
                    elif next_line.startswith('Project Description:'):
                        # Check project description for disaster indicators
                        desc = next_line
                        if any(indicator.lower() in desc.lower() for indicator in disaster_indicators):
                            project_info['is_disaster'] = True
                
                all_projects.append(project_info)

print("__RESULT__:")
print(json.dumps({
    "total_projects_parsed": len(all_projects),
    "sample_projects": all_projects[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}, 'var_functions.execute_python:14': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'civic_docs_full_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'civic_docs_total': 5, 'funding_records_total': 500, 'sample_doc_filename': 'malibucity_agenda_03222023-2060.txt'}}

exec(code, env_args)
