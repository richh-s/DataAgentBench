code = """import json
import re

civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding = json.load(f)

print(f"Processing {len(civic_docs)} documents and {len(funding)} funding records")

# Extract projects with their dates from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split into sections for different project categories
    sections = re.split(r'\n\s*\n', text)
    
    current_category = None
    current_project = None
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
        
        # Identify category headers
        if 'Capital Improvement Projects (Design)' in section:
            current_category = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in section:
            current_category = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in section:
            current_category = 'not_started'
            continue
        elif 'Disaster Recovery Projects' in section:
            current_category = 'disaster'
            continue
        
        # Look for project names (typically first line of a project block)
        lines = section.split('\n')
        if len(lines) > 0:
            first_line = lines[0].strip()
            # Skip lines that look like headers, bullet points, or contain special chars
            if (first_line and 
                not first_line.startswith('cid:') and 
                not re.match(r'^[\u2022â€¢\-\*]', first_line) and
                not re.match(r'^(Capital|Disaster|Public Works|Agenda|To:|Prepared|Approved|Date|Meeting|Subject|RECOMMENDED|DISCUSSION)', first_line) and
                len(first_line) < 200):  # Reasonable length for a project name
                
                project_name = first_line
                
                # Determine status based on category
                if current_category == 'design':
                    status = 'design'
                elif current_category == 'construction':
                    status = 'construction'
                elif current_category == 'not_started':
                    status = 'not started'
                else:
                    status = None
                
                # Extract dates from the section
                start_date = None
                end_date = None
                
                # Look for schedule items
                schedule_patterns = [
                    r'Complete Design:\s*([^\n]+)',
                    r'Advertise:\s*([^\n]+)',
                    r'Begin Construction:\s*([^\n]+)',
                    r'Complete Construction:\s*([^\n]+)',
                    r'Estimated Schedule:[^\n]*\n\s*Complete Design:\s*([^\n]+)',
                ]
                
                found_dates = []
                for pattern in schedule_patterns:
                    matches = re.findall(pattern, section, re.IGNORECASE)
                    for match in matches:
                        date_str = match.strip()
                        if date_str and '202' in date_str:
                            found_dates.append(date_str)
                
                # If we found dates, the first is likely the start date
                if found_dates:
                    start_date = found_dates[0]
                    if len(found_dates) > 1:
                        end_date = found_dates[-1]
                
                # Check if project is completed (special case)
                if 'completed' in section.lower() or 'construction was completed' in section.lower():
                    status = 'completed'
                    # Try to extract completion date
                    comp_match = re.search(r'construction was completed[^\n]*?(\w+\s+202\d)', section, re.IGNORECASE)
                    if comp_match:
                        end_date = comp_match.group(1)
                
                # Determine project type
                project_type = 'disaster' if current_category == 'disaster' else 'capital'
                
                projects.append({
                    'Project_Name': project_name,
                    'status': status,
                    'st': start_date,
                    'et': end_date,
                    'type': project_type,
                    'source': filename
                })

# Clean up project names
for p in projects:
    p['Project_Name'] = re.sub(r'^(cid:\d+|[\u2022â€¢\-\*]+\s*)', '', p['Project_Name']).strip()
    p['Project_Name'] = re.sub(r'\s+', ' ', p['Project_Name'])

# Filter out invalid entries
valid_projects = [p for p in projects if p['Project_Name'] and len(p['Project_Name']) > 5]

print(f"Extracted {len(valid_projects)} projects")

# Show some examples
for p in valid_projects[:10]:
    print(f"  {p['Project_Name']}: start={p['st']}, status={p['status']}, type={p['type']}")

__RESULT__:
json.dumps({'extracted_count': len(valid_projects)})"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}}

exec(code, env_args)
