code = """import json
import re
import os

# Load the full datasets from files
funding_file_path = 'file_storage/functions.query_db:18.json'
civic_docs_file_path = 'file_storage/functions.query_db:14.json'

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Extract project information from civic documents
project_info = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in the text
    # Common patterns: project name followed by schedule/progress updates
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or 'Agenda Report' in line or 'Public Works Commission' in line or 'Prepared by' in line:
            continue
            
        # Look for project names (typically title case or with year prefixes)
        # Pattern: lines that look like project names followed by schedule info
        if (line and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('–') and
            len(line) > 10 and
            not any(keyword in line.lower() for keyword in ['updates', 'schedule', 'page', 'item', 'subject:', 'discussion:'])):
            
            # Look ahead for schedule information
            if 'project' in line.lower() or 'improvements' in line.lower() or 'repairs' in line.lower():
                current_project = line
                
                # Look for dates in subsequent lines
                schedule_match = re.search(r'(Complete Design|Begin Construction|Advertise|Complete Construction):\s*(\S+\s+\S+\s+\S*|\S+\s+\S*|\S+)', text)
                if schedule_match:
                    date_info = schedule_match.group(2)
                    
                    # Check if this is a 2022 start
                    if '2022' in date_info:
                        project_type = 'disaster' if any(keyword in line.lower() for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency']) else 'capital'
                        
                        project_info.append({
                            'Project_Name': line,
                            'Type': project_type,
                            'Start_Date': date_info,
                            'Year': '2022'
                        })

# Also look for project names with parentheses (FEMA, CalOES, etc.)
fema_pattern = r'([^\n]+\((?:FEMA|CalOES|CalJPIA)\s+[^)]+\))'
fema_matches = re.findall(fema_pattern, text, re.IGNORECASE)

for match in fema_matches:
    if '2022' in text:
        project_info.append({
            'Project_Name': match.strip(),
            'Type': 'disaster',
            'Start_Date': '2022',
            'Year': '2022'
        })

print("__RESULT__:")
print(json.dumps({
    "projects_found": project_info,
    "project_count": len(project_info)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 0, 'file_exists': False, 'error': 'File not found: /tmp/tmphn4t1u8a.json'}, 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'funding_type': 'str', 'civic_docs_type': 'str', 'funding_preview': 'file_storage/functions.query_db:18.json', 'civic_docs_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
