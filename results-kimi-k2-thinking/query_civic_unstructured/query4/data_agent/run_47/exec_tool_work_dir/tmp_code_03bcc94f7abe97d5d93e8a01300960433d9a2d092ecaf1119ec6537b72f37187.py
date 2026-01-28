code = """import json

# Load funding data
with open('/tmp/results/20250219_143343_sqlite_funding_database_query_12.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('/tmp/results/20250219_143343_mongodb_civic_docs_database_query_42.json', 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents with 2022: {len(civic_docs)}")

# Find project names from civic documents that started in Spring 2022
spring_2022_project_names = set()

# Look for specific Spring 2022 patterns in the text
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Skip header lines
        if any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:', 'PREPARED BY', 'APPROVED BY']):
            continue
        
        # Check if this could be a project name
        if line.isupper() and len(line) > 15:
            # Look ahead for Spring 2022 indicators
            following = '\n'.join(lines[i:i+20])
            spring_indicators = ['Spring 2022', '2022-Spring', '2022-03', '2022-04', '2022-05', 'Mar 2022', 'Apr 2022', 'May 2022']
            for indicator in spring_indicators:
                if indicator in following or indicator.lower() in following.lower():
                    spring_2022_project_names.add(line)
                    break
        # Projects with year in name
        elif '2022' in line and len(line) > 10:
            if not any(skip in line for skip in ['Page', 'AGENDA ITEM', 'SUBJECT:', 'DATE']):
                spring_2022_project_names.add(line)

# Filter out the specific project that actually started in Spring 2022
confirmed_spring_2022 = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for explicit Spring 2022 scheduling
    if 'Advertise: Spring 2022' in text or 'Begin: Spring 2022' in text or 'Spring-2022' in text:
        lines = text.split('\n')
        found_spring_2022 = False
        spring_section = ''
        
        # Check if this document has Spring 2022 scheduling specifically
        for line in lines:
            if '2022' in line and ('Spring' in line or 'pring' in line.lower()):
                found_spring_2022 = True
                spring_section += line + '\n'
        
        if found_spring_2022:
            # Look for project name before the Spring 2022 mention
            for i, line in enumerate(lines):
                line = line.strip()
                if line.isupper() and len(line) > 15 and not any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING']):
                    # Check if this project has Spring 2022 in its following lines
                    follow = '\n'.join(lines[i:i+20])
                    if 'Advertise' in follow and '2022' in follow and 'pring' in follow.lower():
                        confirmed_spring_2022.add(line)

# Also check for specific project with year in name
for name in spring_2022_project_names:
    if '2022' in name:
        confirmed_spring_2022.add(name)

final_projects = sorted(list(confirmed_spring_2022))
print(f"Spring 2022 projects: {len(final_projects)}")
for proj in final_projects:
    print(f"  - {proj}")

# Find funding for these projects
total_funding = 0
funded_projects = []
for project_name in final_projects:
    for funding in funding_data:
        if funding['Project_Name'] == project_name:
            amount = int(funding['Amount'])
            total_funding += amount
            funded_projects.append((project_name, amount))

print(f"Total funding: ${total_funding:,}")
for proj, amt in funded_projects:
    print(f"  - {proj}: ${amt:,}")

result = {
    'project_count': len(final_projects),
    'total_funding': total_funding,
    'projects': final_projects,
    'funded_projects': funded_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
