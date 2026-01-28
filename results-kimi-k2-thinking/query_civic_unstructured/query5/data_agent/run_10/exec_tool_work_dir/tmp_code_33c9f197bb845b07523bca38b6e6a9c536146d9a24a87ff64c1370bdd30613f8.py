code = """import json
import re

# Load funding data
funding_file = 'file_storage/functions.query_db:18.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = 'file_storage/functions.query_db:14.json'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Extract disaster-related projects that started in 2022 from civic documents
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections
    # Pattern to find project names and their schedules
    project_blocks = re.findall(r'([^\n]{5,100}\n(?:[\s\S]{0,500}?)(?:Complete Design|Begin Construction|Advertise|Complete Construction):[\s\S]{0,200})', text)
    
    for block in project_blocks:
        lines = block.split('\n')
        project_name = None
        start_date = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check if this line is a project name (not a schedule line)
            if not any(schedule in line for schedule in ['Complete Design:', 'Begin Construction:', 'Advertise:', 'Complete Construction:', 'Updates:']):
                if len(line) > 5 and not line.startswith('(') and not any(keyword in line.lower() for keyword in ['page', 'item', 'subject:', 'discussion:', 'recommended action']):
                    # This could be a project name
                    if any(project_keyword in line.lower() for project_keyword in ['project', 'improvements', 'repairs', 'replacement', 'renovation', 'drainage', 'resurfacing']):
                        project_name = line
            
            # Look for schedule information
            schedule_match = re.search(r'(?:Complete Design|Begin Construction|Advertise|Complete Construction):\s*(.+)', line)
            if schedule_match:
                date_info = schedule_match.group(1).strip()
                if '2022' in date_info:
                    start_date = date_info
        
        # If we found a project with a 2022 date, check if it's disaster-related
        if project_name and start_date:
            # Check if it's a disaster project (FEMA, CalOES, CalJPIA, or disaster-related keywords)
            is_disaster = any(keyword in project_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'fire'])
            
            # Also check the text block for disaster-related context
            block_lower = block.lower()
            if not is_disaster:
                is_disaster = any(keyword in block_lower for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'fire'])
            
            if is_disaster:
                disaster_projects_2022.append({
                    'Project_Name': project_name,
                    'Start_Date': start_date
                })

# Step 2: Also look for projects with explicit (FEMA Project), (CalOES Project), etc. suffixes
# These might not have explicit 2022 dates in the schedule but could be in the document
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all projects with FEMA/CalOES/CalJPIA suffixes
    matches = re.findall(r'([^\n]+\((?:FEMA|CalOES|CalJPIA)(?:\s+Project)?\))', text, re.IGNORECASE)
    
    for match in matches:
        project_name = match.strip()
        
        # Look for any 2022 date in the vicinity (within 500 chars before or after)
        pos = text.find(match)
        context = text[max(0, pos-500):min(len(text), pos+500)]
        
        if '2022' in context:
            # Extract the date information
            date_match = re.search(r'(?:Complete Design|Begin Construction|Advertise|Complete Construction):\s*([^\n]+)', context)
            if date_match:
                date_info = date_match.group(1).strip()
                if '2022' in date_info:
                    disaster_projects_2022.append({
                        'Project_Name': project_name,
                        'Start_Date': date_info
                    })
                else:
                    # Still count it if 2022 appears elsewhere in context
                    disaster_projects_2022.append({
                        'Project_Name': project_name,
                        'Start_Date': '2022 (implied)'
                    })

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in disaster_projects_2022:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

print("__RESULT__:")
print(json.dumps({
    "disaster_projects_2022": unique_projects,
    "count": len(unique_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 0, 'file_exists': False, 'error': 'File not found: /tmp/tmphn4t1u8a.json'}, 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'funding_type': 'str', 'civic_docs_type': 'str', 'funding_preview': 'file_storage/functions.query_db:18.json', 'civic_docs_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
