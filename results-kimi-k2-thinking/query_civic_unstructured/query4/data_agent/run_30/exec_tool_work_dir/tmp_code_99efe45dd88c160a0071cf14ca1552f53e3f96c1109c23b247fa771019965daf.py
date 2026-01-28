code = """import json
import re

# Load civic documents data
civic_docs_path = locals()['var_functions.query_db:5']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:8']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Initialize list to store projects
projects = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Look for project names (lines with certain patterns)
        if (line.istitle() or any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Installation', 'Replacement', 'Upgrade', 'Study'])) and len(line) > 10:
            
            project_name = line
            start_date = None
            end_date = None
            status = None
            
            # Look ahead for schedule info (up to 25 lines ahead)
            j = i + 1
            while j < min(i + 25, len(lines)):
                next_line = lines[j].strip()
                
                # Look for date patterns in schedule lines
                if 'Project Schedule:' in next_line or 'Estimated Schedule:' in next_line or 'Complete' in next_line:
                    # Check following lines for dates
                    k = j + 1
                    while k < min(j + 15, len(lines)):
                        schedule_line = lines[k].strip()
                        
                        # Match date patterns like "2022-Spring", "2022-March", etc.
                        date_match = re.search(r'\d{4}-(Spring|Fall|Summer|Winter|January|February|March|April|May|June|July|August|September|October|November|December)', schedule_line)
                        if date_match:
                            if not start_date:
                                start_date = date_match.group(0)
                            elif not end_date:
                                end_date = date_match.group(0)
                        
                        # Stop when we hit a line that doesn't contain schedule info
                        if ':' in schedule_line and not any(x in schedule_line for x in ['Complete', 'Design', 'Construction', 'Advertise', 'Begin', 'Summer', 'Fall', 'Spring', 'Winter']):
                            break
                        
                        k += 1
                
                # Try to find status
                if 'Updates:' in next_line:
                    k = j + 1
                    while k < min(j + 10, len(lines)):
                        update_line = lines[k].strip().lower()
                        if 'currently under construction' in update_line:
                            status = 'construction'
                            break
                        elif 'completed' in update_line and 'construction was completed' in update_line:
                            status = 'completed'
                            break
                        elif 'design' in update_line or 'finalize the design' in update_line:
                            status = 'design'
                            break
                        elif update_line and not update_line.startswith('('):
                            break
                        k += 1
                
                j += 1
            
            # Add project if valid
            if project_name and len(project_name) > 5:
                projects.append({
                    'Project_Name': project_name,
                    'st': start_date,
                    'et': end_date,
                    'status': status,
                    'source_file': filename
                })
        
        i += 1

# Filter for Spring 2022 projects
spring_2022_projects = []
for project in projects:
    if project['st'] and '2022' in project['st']:
        if any(season in project['st'] for season in ['Spring', 'March', 'April', 'May']):
            spring_2022_projects.append(project)

# Get project names for Spring 2022
spring_2022_names = [p['Project_Name'] for p in spring_2022_projects]

# Find matching funding records
matching_funding = []
for funding in funding_data:
    if funding['Project_Name'] in spring_2022_names:
        matching_funding.append(funding)

# Alternative: Try fuzzy matching - look for funding records with similar names
from collections import defaultdict

# Build a name index of all funding projects
funding_name_index = defaultdict(list)
for funding in funding_data:
    name = funding['Project_Name'].lower()
    funding_name_index[name].append(funding)
    # Also add variations with/without suffixes
    base_name = re.sub(r'\s*\([^)]*\)$', '', funding['Project_Name'])
    funding_name_index[base_name.lower()].append(funding)

# Try to find more matches by checking each Spring 2022 project
enhanced_funding_matches = []
for spring_project in spring_2022_projects:
    spring_name = spring_project['Project_Name']
    
    # Direct match
    if spring_name in [f['Project_Name'] for f in funding_data]:
        for funding in funding_data:
            if funding['Project_Name'] == spring_name:
                enhanced_funding_matches.append(funding)
    else:
        # Try variations
        spring_name_lower = spring_name.lower()
        
        # Check if ends with common disaster suffixes
        for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)', '(FEMA/CalOES Project)']:
            if spring_name_lower.endswith(suffix.lower()):
                base_name = spring_name[:-(len(suffix)+1)]
                if base_name.lower() in funding_name_index:
                    enhanced_funding_matches.extend(funding_name_index[base_name.lower()])
                break
        else:
            # Try adding common disaster suffixes
            for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)']:
                var_name = f"{spring_name} {suffix}"
                if var_name.lower() in funding_name_index:
                    enhanced_funding_matches.extend(funding_name_index[var_name.lower()])
                    break
            
            # Try removing suffix from spring project name
            base_name = re.sub(r'\s*\([^)]*\)$', '', spring_name)
            if base_name.lower() in funding_name_index:
                enhanced_funding_matches.extend(funding_name_index[base_name.lower()])
            elif base_name.lower() == spring_name_lower:
                # Try direct match with base name
                base_name_variations = [base_name, f"{base_name} (FEMA Project)", f"{base_name} (CalOES Project)", f"{base_name} (CalJPIA Project)"]
                for var in base_name_variations:
                    if var.lower() in funding_name_index:
                        enhanced_funding_matches.extend(funding_name_index[var.lower()])
                        break

# Remove duplicates
unique_funding_matches = []
seen_ids = set()
for funding in enhanced_funding_matches:
    if funding['Funding_ID'] not in seen_ids:
        unique_funding_matches.append(funding)
        seen_ids.add(funding['Funding_ID'])

# Calculate total funding
total_funding = sum(int(f['Amount']) for f in unique_funding_matches)

print("__RESULT__:")
print(json.dumps({
    "spring_2022_projects_found": len(spring_2022_projects),
    "spring_2022_projects": spring_2022_names,
    "matching_funding_records": len(unique_funding_matches),
    "total_funding": total_funding,
    "funding_records": unique_funding_matches
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}}

exec(code, env_args)
