code = """import json

funding_file_path = str(var_functions.query_db:0)
civic_file_path = str(var_functions.query_db:2)

with open(funding_file_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_records), 'funding records and', len(civic_docs), 'civic documents')

# Find capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    if 'capital improvement' in lower_text and 'design' in lower_text:
        lines = text.split('\n')
        for line in lines:
            clean_line = line.strip()
            if len(clean_line) >= 10:
                check_line = clean_line.lower()
                # Skip administrative lines
                skip_terms = ['updates:', 'schedule:', 'staff', 'city council', 'consultant', 'discussion:', 'page', 'complete design', 'advertise:', 'construction:', 'project ', 'to:', 'from:', 'date:', 'subject:']
                should_skip = False
                for term in skip_terms:
                    if term in check_line:
                        should_skip = True
                        break
                if should_skip:
                    continue
                
                # Check for infrastructure project keywords
                project_keywords = ['road', 'avenue', 'drive', 'park', 'drain', 'bridge', 'walkway', 'sewer', 'water', 'traffic', 'signal', 'sign', 'median', 'crosswalk']
                for keyword in project_keywords:
                    if keyword in check_line:
                        design_projects.append(clean_line)
                        break

# Remove duplicates
design_projects = list(set(design_projects))
print('Capital design project candidates:', len(design_projects))

# Count matches with funding > $50,000
match_count = 0
matched_projects = []

for proj in design_projects:
    proj_lower = proj.lower()
    for fund in funding_records:
        amount = int(fund['Amount'])
        if amount > 50000:
            fund_name_lower = fund['Project_Name'].lower()
            # Check for exact or partial match
            if proj_lower == fund_name_lower or proj_lower in fund_name_lower or fund_name_lower in proj_lower:
                match_count += 1
                matched_projects.append(proj)
                break

print('Final matched count:', match_count)
result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
