code = """import json
with open(var_call_vD4zEmrG487DkCnRuuc8jrW7) as f:
    funding_projects = json.load(f)
funding_names = set(p['Project_Name'].strip().lower() for p in funding_projects)
with open(var_call_lanOkBXfzRQGOCcSYpVNQvY3) as f:
    civic_docs = json.load(f)
projects_in_design = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)', 1)[1]
        lines = section.split('\n')
        for line in lines:
            cleaned = line.strip().lower()
            if cleaned and not cleaned.startswith('(') and not cleaned.startswith('updates') and not cleaned.startswith('complete'):
                for f_name in funding_names:
                    if cleaned in f_name:
                        projects_in_design.add(f_name)
            if ('capital improvement projects' in cleaned and '(design)' not in cleaned) or cleaned == '':
                break
print('__RESULT__:')
print(json.dumps(len(projects_in_design)))"""

env_args = {'var_call_vD4zEmrG487DkCnRuuc8jrW7': 'file_storage/call_vD4zEmrG487DkCnRuuc8jrW7.json', 'var_call_lanOkBXfzRQGOCcSYpVNQvY3': 'file_storage/call_lanOkBXfzRQGOCcSYpVNQvY3.json'}

exec(code, env_args)
