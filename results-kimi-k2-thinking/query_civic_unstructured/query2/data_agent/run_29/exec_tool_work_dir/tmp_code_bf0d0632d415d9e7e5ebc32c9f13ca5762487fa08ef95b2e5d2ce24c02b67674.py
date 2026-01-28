code = """import json
with open('/tmp/tmpz5hptp8z.json', 'r') as f:
    civic_docs = json.load(f)
with open('/tmp/tmphs_qx5r1.json', 'r') as f:
    funding_data = json.load(f)

park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    project_info = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        if len(line) > 5 and not line.startswith('('):
            is_project = False
            for j in range(i+1, min(i+6, len(lines))):
                next_line_lower = lines[j].lower()
                if 'updates:' in next_line_lower or 'project schedule:' in next_line_lower or 'complete construction:' in next_line_lower or '(cid:' in next_line_lower:
                    is_project = True
                    break
            if is_project:
                if current_project and project_info:
                    status = project_info.get('status')
                    et = project_info.get('et', '')
                    topic = project_info.get('topic', '').lower()
                    if status == 'completed' and '2022' in et and 'park' in topic:
                        park_projects.append(project_info)
                current_project = line
                project_info = {'Project_Name': line, 'status': '', 'et': '', 'topic': ''}
                pl = line.lower()
                if 'park' in pl:
                    project_info['topic'] = 'park'
                elif 'playground' in pl:
                    project_info['topic'] = 'playground'
        if current_project and project_info:
            ll = line.lower()
            if 'completed' in ll or 'complete construction' in ll or 'construction was completed' in ll or 'notice of completion' in ll:
                project_info['status'] = 'completed'
                if '2022' in line:
                    project_info['et'] = '2022'
    if current_project and project_info:
        status = project_info.get('status')
        et = project_info.get('et', '')
        topic = project_info.get('topic', '').lower()
        if status == 'completed' and '2022' in et and 'park' in topic:
            park_projects.append(project_info)

matches = []
for proj in park_projects:
    proj_name_lower = proj['Project_Name'].lower()
    for fund in funding_data:
        fund_name_lower = fund['Project_Name'].lower()
        if fund_name_lower == proj_name_lower or fund_name_lower in proj_name_lower or proj_name_lower in fund_name_lower:
            matches.append({'project_name': proj['Project_Name'], 'funding_name': fund['Project_Name'], 'amount': int(fund['Amount'])})

total_funding = sum(m['amount'] for m in matches)
result = {'park_projects_completed_2022': park_projects, 'funding_matches': matches, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
