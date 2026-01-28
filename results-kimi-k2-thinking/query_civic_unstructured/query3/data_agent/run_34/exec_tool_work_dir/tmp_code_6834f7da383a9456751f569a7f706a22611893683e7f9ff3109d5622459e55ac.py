code = """import json
import re

# Read the civic documents file
civic_docs_path = var_functions.query_db:6
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data file
funding_path = var_functions.query_db:7
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Extract project information from civic documents
projects_info = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find project sections - they often start with project names or are in bullet points
    # Looking for patterns like:
    # - Project Name followed by updates/schedule
    
    # Find project name patterns followed by project information
    project_patterns = r'([A-Z][a-zA-Z\s\d\&\-]+?(?:\([^)]*\))?)(?=\s*\(cid:\d+\)\s*Updates:|\s*\(cid:\d+\)\s*Project Schedule:|\n\s*Updates:|\n\s*Project Schedule:)'
    
    matches = re.finditer(project_patterns, text)
    
    for match in matches:
        project_name = match.group(1).strip()
        
        # Check if the project mentions FEMA or emergency
        project_start = match.start()
        # Look ahead for the next project or end of section
        next_project = re.search(project_patterns, text[project_start+1:])
        if next_project:
            project_text = text[project_start:project_start+next_project.start()+1]
        else:
            # Find next all caps heading or end of relevant section
            next_heading = re.search(r'\n\s*[A-Z\s]{15,}\n', text[project_start+1:])
            if next_heading:
                project_text = text[project_start:project_start+next_heading.start()+1]
            else:
                project_text = text[project_start:project_start+2000]  # Look at next 2000 chars
        
        if re.search(r'FEMA|emergency|Emergency|EMERGENCY', project_text):
            # Extract status if available
            status_match = re.search(r'Updates?:.*?(Project is currently under construction|Construction was completed|in design|design phase|not started|awaiting|pending)', project_text, re.IGNORECASE|re.DOTALL)
            if status_match:
                status_text = status_match.group(1)
                if 'construction' in status_text.lower() and 'completed' not in status_text.lower():
                    status = 'construction'
                elif 'completed' in status_text.lower():
                    status = 'completed'
                elif 'design' in status_text.lower() or 'awaiting' in status_text.lower():
                    status = 'design'
                else:
                    status = 'not started'
            else:
                status = 'unknown'
            
            # Extract type if available
            if 'FEMA' in project_text or 'disaster' in project_text.lower():
                project_type = 'disaster'
            else:
                project_type = 'capital'
            
            # Extract schedule if available
            schedule_match = re.search(r'Project Schedule:.*?\n\s*\(cid:\d+\)\s*(.*?)(?:\n\s*\(cid:|\n\s*[A-Z]|\Z)', project_text, re.DOTALL)
            schedule = ''
            if schedule_match:
                schedule = schedule_match.group(1).strip()
            
            projects_info.append({
                'Project_Name': project_name,
                'status': status,
                'type': project_type,
                'schedule': schedule
            })

# Filter funding data for projects related to FEMA or emergency
filtered_funding = []
for fund in funding_data:
    project_name = fund.get('Project_Name', '')
    if re.search(r'FEMA|emergency|Emergency|EMERGENCY', project_name):
        filtered_funding.append({
            'Project_Name': project_name,
            'Funding_Source': fund.get('Funding_Source', ''),
            'Amount': fund.get('Amount', 0)
        })

# Also include projects from civic docs that might not have FEMA in name but in text
civic_project_names = [p['Project_Name'] for p in projects_info]
for fund in funding_data:
    project_name = fund.get('Project_Name', '')
    # Check if this project name appears in our civic docs projects (even if it doesn't have FEMA in the name)
    if any(project_name.lower().replace('(','').replace(')','').strip() in civic_name.lower().replace('(','').replace(')','').strip() 
           or civic_name.lower().replace('(','').replace(')','').strip() in project_name.lower().replace('(','').replace(')','').strip()
           for civic_name in civic_project_names):
        # Check if this project is related to FEMA/emergency by context
        matching_civic = [p for p in projects_info if project_name.lower().replace('(','').replace(')','').strip() in p['Project_Name'].lower().replace('(','').replace(')','').strip() or p['Project_Name'].lower().replace('(','').replace(')','').strip() in project_name.lower().replace('(','').replace(')','').strip()]
        if matching_civic:
            filtered_funding.append({
                'Project_Name': project_name,
                'Funding_Source': fund.get('Funding_Source', ''),
                'Amount': fund.get('Amount', 0)
            })

print('__RESULT__:')
print(json.dumps({
    'projects_from_civic_docs': projects_info,
    'funding_records': filtered_funding
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
