code = """import json

# Load data from storage paths provided by previous tool calls
with open(var_call_1sy2EAmn2hPEFkep0c11JWFu, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_EfxXsrQD5f5UJ8SOm4SNG3rz, 'r') as f:
    funding = json.load(f)

# Prepare funding dict and list of unique project names with amounts
funding_by_project = {}
for rec in funding:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    try:
        amt_int = int(amt)
    except Exception:
        try:
            amt_int = int(float(amt))
        except Exception:
            amt_int = 0
    funding_by_project[name] = funding_by_project.get(name, 0) + amt_int

project_names = list(funding_by_project.keys())

# months in spring
spring_months = ['march', 'mar', 'april', 'apr', 'may']

matched_projects = set()

for pname in project_names:
    pname_lower = pname.lower()
    found = False
    for doc in civic_docs:
        text = doc.get('text','')
        text_lower = text.lower()
        start = 0
        while True:
            idx = text_lower.find(pname_lower, start)
            if idx == -1:
                break
            win_start = max(0, idx-300)
            win_end = min(len(text_lower), idx + len(pname_lower) + 300)
            window = text_lower[win_start:win_end]
            # Conditions for spring 2022:
            # 1) both 'spring' and '2022' in window
            if 'spring' in window and '2022' in window:
                matched_projects.add(pname)
                found = True
                break
            # 2) a spring month and 2022 both present
            if any(m in window for m in spring_months) and '2022' in window:
                matched_projects.add(pname)
                found = True
                break
            # 3) year-month formats for 2022-03, 2022-04, 2022-05 or 03/2022 etc
            if ('2022-03' in window) or ('2022-04' in window) or ('2022-05' in window) or ('03/2022' in window) or ('04/2022' in window) or ('05/2022' in window) or ('03.2022' in window) or ('04.2022' in window) or ('05.2022' in window) or ('03/22' in window) or ("'22" in window and any(m in window for m in spring_months)):
                matched_projects.add(pname)
                found = True
                break
            # 4) phrases like 'Begin Construction: Spring 2023' we already cover with spring+year
            start = idx + 1
        if found:
            break

matched_list = sorted(list(matched_projects))
count = len(matched_list)

# Sum funding for matched projects
total_funding = 0
for p in matched_list:
    total_funding += funding_by_project.get(p, 0)

result = {
    'count': count,
    'total_funding': total_funding,
    'projects': matched_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kSM3FdQY4FQ0hzQ5QbDB9gSg': ['civic_docs'], 'var_call_AkSZPXv5Eo9yhyVh4kfApsb3': ['Funding'], 'var_call_1sy2EAmn2hPEFkep0c11JWFu': 'file_storage/call_1sy2EAmn2hPEFkep0c11JWFu.json', 'var_call_EfxXsrQD5f5UJ8SOm4SNG3rz': 'file_storage/call_EfxXsrQD5f5UJ8SOm4SNG3rz.json'}

exec(code, env_args)
