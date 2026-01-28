code = """import json
import re

# Load the data
funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from all civic documents
def extract_projects_from_civic_docs(civic_docs):
    all_projects = []
    
    for doc in civic_docs:
        text = doc['text']
        
        # Look for Capital Improvement Projects sections with Design status
        # Pattern to find "Capital Improvement Projects (Design)" sections
        design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(|Disaster Recovery Projects \(|\Z)'
        design_matches = re.finditer(design_section_pattern, text, re.DOTALL)
        
        for match in design_matches:
            design_section = match.group(1)
            
            # Extract project names from this section
            # Look for project name lines (typically title case, not bullet points)
            lines = design_section.split('\n')
            for line in lines:
                line = line.strip()
                # Skip empty lines, bullet points, status markers
                if (line and 
                    not line.startswith('(') and 
                    not line.startswith('cid:') and 
                    not line.startswith('•') and
                    not line.startswith('-') and
                    not line.startswith('□') and
                    'Updates:' not in line and
                    'Project Schedule:' not in line and
                    'Complete Design:' not in line and
                    'Advertise:' not in line and
                    'Begin Construction:' not in line and
                    len(line) > 10):
                    
                    # Clean up the line
                    clean_line = re.sub(r'\s*-\s*', '', line)  # Remove leading dashes
                    clean_line = re.sub(r'\(.*\)$', '', clean_line).strip()  # Remove trailing parentheticals
                    clean_line = re.sub(r'^\d+\s*\.\s*', '', clean_line)  # Remove numbering
                    
                    if clean_line and not clean_line.endswith(':'):
                        all_projects.append({
                            'Project_Name': clean_line,
                            'status': 'design',
                            'type': 'capital'
                        })
    
    return all_projects

# Extract projects
projects_from_docs = extract_projects_from_civic_docs(civic_docs)

# Remove duplicates by project name
unique_projects = {}
for proj in projects_from_docs:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

deduplicated_projects = list(unique_projects.values())

result = {
    'total_projects_extracted': len(projects_from_docs),
    'unique_projects': len(deduplicated_projects),
    'sample_projects': deduplicated_projects[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:32': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}}

exec(code, env_args)
