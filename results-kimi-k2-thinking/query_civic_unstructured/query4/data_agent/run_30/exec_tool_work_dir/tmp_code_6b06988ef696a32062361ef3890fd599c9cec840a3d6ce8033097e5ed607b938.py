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

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
        
        # Look for project names
        if (line.istitle() or any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Installation', 'Replacement'])) and len(line) > 10:
            
            project_name = line
            start_date = None
            end_date = None
            
            # Look ahead for schedule info
            j = i + 1
            while j < min(i + 30, len(lines)):
                next_line = lines[j].strip()
                
                if 'Project Schedule:' in next_line or 'Estimated Schedule:' in next_line:
                    # Check following lines for dates
                    k = j + 1
                    while k < min(j + 15, len(lines)):
                        schedule_line = lines[k].strip()
                        
                        # Match date patterns
                        date_pattern = r'\d{4}-(Spring|Fall|Summer|Winter|March|April|May|January|February|June|July|August|September|October|November|December)'
                        date_match = re.search(date_pattern, schedule_line)
                        if date_match:
                            if not start_date:
                                start_date = date_match.group(0)
                            elif not end_date:
                                end_date = date_match.group(0)
                        
                        if ':' in schedule_line and not any(x in schedule_line for x in ['Complete', 'Design', 'Construction', 'Advertise', 'Begin', 'Summer', 'Fall', 'Spring', 'Winter', 'March', 'April', 'May']):
                            break
                        
                        k += 1
                
                j += 1
            
            if project_name and len(project_name) > 5:
                projects.append({
                    'Project_Name': project_name,
                    'st': start_date,
                    'et': end_date,
                    'source_file': filename
                })
        
        i += 1

# Filter for Spring 2022 projects
spring_2022_projects = []
for project in projects:
    if project['st'] and '2022' in project['st']:
        season_month = project['st'].lower()
        if any(season in season_month for season in ['spring', 'march', 'april', 'may']):
            spring_2022_projects.append(project)

# Get all unique funding records
unique_funding_records = []
seen_names = set()

# Build mapping of funding records by name
funding_by_name = {}
for funding in funding_data:
    name = funding['Project_Name']
    funding_by_name[name] = funding

# Try to match Spring 2022 projects with funding records
matched_funding = []
matched_project_names = []

for spring_project in spring_2022_projects:
    spring_name = spring_project['Project_Name']
    
    # Direct match
    if spring_name in funding_by_name:
        matched_funding.append(funding_by_name[spring_name])
        matched_project_names.append(spring_name)
    else:
        # Try variations with disaster suffixes
        suffixes = [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)']
        matched = False
        for suffix in suffixes:
            var_name = spring_name + suffix
            if var_name in funding_by_name:
                matched_funding.append(funding_by_name[var_name])
                matched_project_names.append(var_name)
                matched = True
                break
        
        if not matched:
            # Try removing parenthetical suffix and adding disaster suffixes
            base_name = re.sub(r'\s*\([^)]*\)$', '', spring_name)
            if base_name != spring_name:
                for suffix in suffixes:
                    var_name = base_name + suffix
                    if var_name in funding_by_name:
                        matched_funding.append(funding_by_name[var_name])
                        matched_project_names.append(var_name)
                        matched = True
                        break

# Calculate total funding
total_funding = sum(int(f['Amount']) for f in matched_funding)

result = {
    "spring_2022_projects_count": len(spring_2022_projects),
    "spring_2022_projects": [p['Project_Name'] for p in spring_2022_projects],
    "matched_funding_records": len(matched_funding),
    "total_funding": total_funding,
    "matched_project_names": matched_project_names
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}}

exec(code, env_args)
