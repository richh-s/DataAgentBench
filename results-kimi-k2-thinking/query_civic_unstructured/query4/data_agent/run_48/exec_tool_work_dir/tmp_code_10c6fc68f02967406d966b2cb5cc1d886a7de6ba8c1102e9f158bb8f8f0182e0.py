code = """import json, re

funding_file = open('var_functions.query_db:8', 'r')
funding_data = json.load(funding_file)
funding_file.close()

civic_file = open('var_functions.query_db:14', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(item.get('Amount', 0))

spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        line_lower = line.lower()
        if 'page' in line_lower or 'agenda item' in line_lower or 'public works commission' in line_lower:
            continue
            
        if 'updates:' in line_lower or 'project schedule:' in line_lower or 'complete design:' in line_lower or 'advertise:' in line_lower:
            continue
            
        if (not line.startswith('(') and 
            not line.startswith('-') and 
            not line.startswith('·') and
            (line.istitle() or (sum(1 for c in line if c.isupper()) >= 3 and not line.isupper()))):
            
            has_spring_2022 = False
            for j in range(i, min(i+15, len(lines))):
                context_line = lines[j].strip()
                
                if '2022' in context_line:
                    if 'Spring' in context_line or 'March' in context_line or 'April' in context_line or 'May' in context_line:
                        has_spring_2022 = True
                        break
                    if '2022-03' in context_line or '2022-04' in context_line or '2022-05' in context_line:
                        has_spring_2022 = True
                        break
            
            if has_spring_2022:
                spring_2022_projects.append(line)

spring_2022_projects = list(set(spring_2022_projects))

matched_projects = []
total_funding = 0

for project_name in spring_2022_projects:
    if project_name in funding_lookup:
        amount = funding_lookup[project_name]
        total_funding += amount
        matched_projects.append({'name': project_name, 'funding': amount})
    else:
        if len(project_name) > 15:
            for fund_name, amount in funding_lookup.items():
                if project_name.lower() in fund_name.lower() or fund_name.lower() in project_name.lower():
                    total_funding += amount
                    matched_projects.append({'name': project_name, 'matched_fund': fund_name, 'funding': amount})
                    break

additional_2022 = []
for fund_name, amount in funding_lookup.items():
    if '2022' in fund_name and amount > 0:
        if not any(p.get('name') == fund_name or p.get('matched_fund') == fund_name for p in matched_projects):
            additional_2022.append({'name': fund_name, 'funding': amount})
            total_funding += amount

all_matched_projects = matched_projects + additional_2022

result = {
    'project_count': len(all_matched_projects),
    'total_funding': total_funding,
    'projects': all_matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.query_db:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:40': [], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [], 'var_functions.list_db:66': ['civic_docs'], 'var_functions.list_db:68': ['civic_docs']}

exec(code, env_args)
