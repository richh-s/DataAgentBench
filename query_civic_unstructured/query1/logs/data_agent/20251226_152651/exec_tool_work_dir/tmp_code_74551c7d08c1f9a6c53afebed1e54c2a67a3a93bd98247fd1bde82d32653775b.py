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
        design_section = text.split('Capital Improvement Projects (Design)')[1]
        lines = design_section.split('\n')
        for line in lines:
            candidate = line.strip().lower()
            if candidate and not candidate.startswith('(') and not candidate.startswith('updates') and not candidate.startswith('complete'):
                for f_name in funding_names:
                    if candidate in f_name:
                        projects_in_design.add(f_name)
            if candidate == '' or ('capital improvement projects' in candidate and '(design)' not in candidate):
                break
print('__RESULT__:')
print(json.dumps(len(projects_in_design)))"""

env_args = {'var_call_vD4zEmrG487DkCnRuuc8jrW7': 'file_storage/call_vD4zEmrG487DkCnRuuc8jrW7.json', 'var_call_lanOkBXfzRQGOCcSYpVNQvY3': 'file_storage/call_lanOkBXfzRQGOCcSYpVNQvY3.json'}

exec(code, env_args)
