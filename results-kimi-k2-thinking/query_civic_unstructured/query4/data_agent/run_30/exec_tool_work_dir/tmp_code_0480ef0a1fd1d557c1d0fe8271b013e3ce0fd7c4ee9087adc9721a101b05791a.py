code = """import json
import re

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:38']
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# Load funding data
funding_data_path = locals()['var_functions.query_db:8']
with open(funding_data_path) as f:
    funding_data = json.load(f)

# Extract projects and their start dates from civic documents
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        # Check if line looks like a project name (title case and contains "Project" or similar)
        if line.istitle() and ('Project' in line or 'Improvements' in line or 'Repairs' in line):
            proj_name = line
            st_date = None
            # Look ahead for schedule information (up to 30 lines)
            for j in range(i+1, min(i+30, len(lines))):
                next_line = lines[j].strip()
                if 'Schedule:' in next_line:
                    # Check following lines for dates (up to 15 lines)
                    for k in range(j+1, min(j+15, len(lines))):
                        s_line = lines[k].strip()
                        # Extract date pattern like "2022-Spring"
                        date_match = re.search(r'\d{4}-Spring', s_line)
                        if date_match and not st_date:
                            st_date = date_match.group(0)
                        # Stop when hitting a line with colon not related to schedule
                        if ':' in s_line and not any(x in s_line for x in ['Complete', 'Design', 'Construction', 'Advertise', 'Begin', 'Spring', 'Summer', 'Fall', 'Winter']):
                            break
            # Add project if valid name found
            if proj_name:
                projects.append({'Project_Name': proj_name, 'st': st_date})

# Filter for projects starting in Spring 2022
spring_2022_projects = []
for project in projects:
    st = project.get('st')
    if st and '2022' in st and 'Spring' in st:
        spring_2022_projects.append(project)

# Match with funding records
funding_map = {f['Project_Name']: f for f in funding_data}
matched_funding = []
for project in spring_2022_projects:
    name = project['Project_Name']
    # Try exact match
    if name in funding_map:
        matched_funding.append(funding_map[name])
    else:
        # Try variations with disaster project suffixes
        suffixes = [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)']
        for suffix in suffixes:
            var_name = name + suffix
            if var_name in funding_map:
                matched_funding.append(funding_map[var_name])
                break

# Calculate total funding
total_funding = sum(int(f['Amount']) for f in matched_funding)

# Prepare result
result = {
    'spring_2022_projects_count': len(spring_2022_projects),
    'matched_funding_records': len(matched_funding),
    'total_funding_amount': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'sample_civic_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:12': {'num_civic_docs': 5, 'num_funding_records': 500}, 'var_functions.execute_python:18': {'civic_type': "<class 'str'>", 'is_str': True, 'endswith_json': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
