code = """import json
import re

# Load civic documents from file path
civic_path = 'file_storage/functions.query_db:38.json'
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data from file path
funding_path = 'file_storage/functions.query_db:8.json'
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Extract projects with Spring 2022 start dates
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or len(line) < 10:
            i += 1
            continue
            
        # Look for project names (title case and contains keywords)
        if line.istitle() and (line.find('Project') >= 0 or 
                              line.find('Improvements') >= 0 or 
                              line.find('Repairs') >= 0 or
                              line.find('Installation') >= 0 or
                              line.find('Replacement') >= 0):
            
            proj_name = line
            st_date = None
            
            # Look ahead for schedule information
            for j in range(i+1, min(i+30, len(lines))):
                next_line = lines[j].strip()
                if 'Schedule' in next_line:
                    # Check following lines for dates
                    for k in range(j+1, min(j+15, len(lines))):
                        s_line = lines[k].strip()
                        date_match = re.search(r'2022-Spring', s_line)
                        if date_match and not st_date:
                            st_date = date_match.group(0)
                            break
                        # Stop when hitting a colon line (usually a new field)
                        if ':' in s_line and (s_line.find('Design') < 0 and 
                                            s_line.find('Construction') < 0 and
                                            s_line.find('Complete') < 0):
                            break
            
            if proj_name and st_date:
                projects.append({
                    'Project_Name': proj_name,
                    'st': st_date,
                    'source_file': filename
                })
        
        i += 1

# Filter for Spring 2022 projects
spring_2022_projects = []
for p in projects:
    st = p.get('st')
    if st and '2022' in st and 'Spring' in st:
        spring_2022_projects.append(p)

# Remove duplicates based on project name
unique_projects = []
seen_names = set()
for p in spring_2022_projects:
    if p['Project_Name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['Project_Name'])

# Create funding map for lookup
funding_map = {f['Project_Name']: f for f in funding_data}

# Match projects with funding records
matched_funding = []
matched_projects = []

for project in unique_projects:
    name = project['Project_Name']
    found_match = False
    
    # Try exact match
    if name in funding_map:
        matched_funding.append(funding_map[name])
        matched_projects.append(project)
        found_match = True
    else:
        # Try variations with disaster project suffixes
        suffixes = [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)']
        for suffix in suffixes:
            var_name = name + suffix
            if var_name in funding_map:
                matched_funding.append(funding_map[var_name])
                matched_projects.append(project)
                found_match = True
                break
        
        if not found_match:
            # Try removing parenthetical suffix and adding disaster suffixes
            base_name = re.sub(r'\s*\([^)]*\)$', '', name)
            if base_name != name:
                for suffix in suffixes:
                    var_name = base_name + suffix
                    if var_name in funding_map:
                        matched_funding.append(funding_map[var_name])
                        matched_projects.append(project)
                        found_match = True
                        break

# Calculate total funding
total_funding = sum(int(f['Amount']) for f in matched_funding)

# Prepare result
result = {
    'spring_2022_projects_count': len(unique_projects),
    'matched_funding_records': len(matched_funding),
    'total_funding_amount': total_funding,
    'projects': unique_projects,
    'matching_funds': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:58': {'var_type': "<class 'str'>", 'var_value': 'file_storage/functions.query_db:38.json', 'is_string': True, 'is_list': False, 'endswith_json': True, 'file_exists': True, 'first_bytes': '[\n  {\n    "_id": "694eef5c4ec675b6b5f5a285",\n    "'}}

exec(code, env_args)
