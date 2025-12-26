code = """import json
import re
with open(var_call_kxhuo5e441S0pbgT5DENba0A, 'r') as f:
    docs = json.load(f)
park_projects = []
for doc in docs:
    text = doc.get('text', '').lower()
    sentences = re.split('[\.!\n]', text)
    for i, sent in enumerate(sentences):
        if ('park' in sent or 'playground' in sent or 'skate park' in sent or 'shade structure' in sent) and ('completed' in sent or 'notice of completion' in sent) and '2022' in sent:
            prev_sent = sentences[i-1] if i>0 else ''
            project_name = None
            if 'project' in prev_sent:
                project_name = prev_sent.split('project')[0].strip()
            elif 'project' in sent:
                project_name = sent.split('project')[0].strip()
            if project_name:
                park_projects.append(project_name)
print('__RESULT__:')
print(json.dumps(park_projects))"""

env_args = {'var_call_kxhuo5e441S0pbgT5DENba0A': 'file_storage/call_kxhuo5e441S0pbgT5DENba0A.json'}

exec(code, env_args)
