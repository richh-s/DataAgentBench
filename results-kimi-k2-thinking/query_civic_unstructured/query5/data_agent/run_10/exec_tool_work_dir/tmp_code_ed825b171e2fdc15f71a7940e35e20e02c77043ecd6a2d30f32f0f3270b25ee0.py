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

# Step 1: Identify disaster-related projects that started in 2022
disaster_projects_2022 = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and irrelevant content
        if not line or line.lower() in ['updates:', 'project schedule:', 'estimated schedule:']:
            i += 1
            continue
        
        # Check if this line might be a project name
        # Projects often contain these keywords
        project_keywords = ['project', 'improvements', 'repairs', 'replacement', 'renovation', 
                           'drainage', 'resurfacing', 'bridge', 'culvert', 'guardrail', 'sirens']
        
        has_project_keyword = any(keyword in line.lower() for keyword in project_keywords)
        is_not_schedule = not any(schedule in line for schedule in ['Complete Design:', 'Begin Construction:', 
                                                                   'Advertise:', 'Complete Construction:'])
        is_not_header = not any(header in line.lower() for header in ['agenda report', 'public works commission',
                                                                      'prepared by', 'approved by', 'subject:', 'discussion:'])
        
        if has_project_keyword and is_not_schedule and is_not_header and len(line) > 10:
            project_name = line
            
            # Look ahead for schedule information (next 10 lines)
            has_2022_date = False
            schedule_info = None
            
            for j in range(i, min(i+10, len(lines))):
                schedule_line = lines[j].strip()
                
                # Look for dates
                if '2022' in schedule_line:
                    has_2022_date = True
                    
                    # Extract the specific schedule info
                    sched_match = re.search(r'(?:Complete Design|Begin Construction|Advertise|Complete Construction):\s*([^\n]+)', schedule_line)
                    if sched_match:
                        schedule_info = sched_match.group(1).strip()
                    break
            
            # If we found a 2022 date, check if it's disaster-related
            if has_2022_date:
                # Check if this project is disaster-related
                is_disaster = False
                
                # Check project name
                if any(keyword in project_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'fire']):
                    is_disaster = True
                
                # Also check the surrounding context
                if not is_disaster:
                    context_start = max(0, i-5)
                    context_end = min(len(lines), i+15)
                    context = ' '.join(lines[context_start:context_end]).lower()
                    
                    if any(keyword in context for keyword in ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'fire']):
                        is_disaster = True
                
                if is_disaster:
                    disaster_projects_2022[project_name] = {
                        'Project_Name': project_name,
                        'Start_Date': schedule_info or '2022'
                    }
        
        i += 1

# Step 2: Also find projects with explicit (FEMA Project), (CalOES Project) suffixes
# Look for these throughout all documents
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find projects with FEMA/CalOES/CalJPIA suffixes
    matches = re.findall(r'([^\n]+\((?:FEMA|CalOES|CalJPIA)(?:\s+Project)?\))', text, re.IGNORECASE)
    
    for match in matches:
        project_name = match.strip()
        
        # Look for 2022 dates in the surrounding context
        pos = text.find(match)
        if pos != -1:
            context_start = max(0, pos-300)
            context_end = min(len(text), pos+300)
            context = text[context_start:context_end]
            
            if '2022' in context:
                # Try to find schedule info
                sched_match = re.search(r'(?:Complete Design|Begin Construction|Advertise|Complete Construction):\s*([^\n]+)', context)
                schedule_info = sched_match.group(1).strip() if sched_match else '2022'
                
                disaster_projects_2022[project_name] = {
                    'Project_Name': project_name,
                    'Start_Date': schedule_info
                }

# Convert dictionary to list
unique_projects = list(disaster_projects_2022.values())

# Step 3: Find matching funding records
disaster_project_names = [proj['Project_Name'] for proj in unique_projects]

# Also add simplified names (without suffixes) for matching
simplified_names = {}
for full_name in disaster_project_names:
    # Remove suffixes like (FEMA Project) for better matching
    simplified = re.sub(r'\s*\([^)]*\)$', '', full_name).strip()
    if simplified != full_name:
        simplified_names[simplified] = full_name

matching_funding = []

for funding_item in funding_data:
    funding_name = funding_item['Project_Name']
    
    # Check for exact match or match without suffix
    if funding_name in disaster_project_names:
        matching_funding.append(funding_item)
    elif funding_name in simplified_names:
        # Use the full project name from civic docs
        full_name = simplified_names[funding_name]
        matched_item = funding_item.copy()
        matched_item['Civic_Docs_Project_Name'] = full_name
        matching_funding.append(matched_item)
    else:
        # Check if funding name contains disaster keywords
        if any(keyword in funding_name.lower() for keyword in ['fema', 'caloes', 'caljpia']) and '2022' in funding_name:
            matching_funding.append(funding_item)

# Calculate total funding
total_funding = sum(int(item['Amount']) for item in matching_funding)

print("__RESULT__:")
print(json.dumps({
    "disaster_projects_found": len(unique_projects),
    "example_projects": unique_projects[:5],
    "matching_funding_records": len(matching_funding),
    "total_funding": total_funding,
    "funding_details": matching_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 0, 'file_exists': False, 'error': 'File not found: /tmp/tmphn4t1u8a.json'}, 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'funding_type': 'str', 'civic_docs_type': 'str', 'funding_preview': 'file_storage/functions.query_db:18.json', 'civic_docs_preview': 'file_storage/functions.query_db:14.json'}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json'}

exec(code, env_args)
