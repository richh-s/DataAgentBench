code = """import json
import re

def extract_park_projects(docs):
    park_related = []
    for doc in docs:
        text = doc.get('text','').lower()
        # Find all sentences containing park-related keywords and completion info for 2022
        sentences = re.split('[\.!\n]', text)
        for i, sent in enumerate(sentences):
            if ('park' in sent or 'playground' in sent or 'skate park' in sent or 'shade structure' in sent) \
                and ('completed' in sent or 'notice of completion' in sent) and '2022' in sent:
                # Try to extract project name from previous or current sentence
                prev_sent = sentences[i-1] if i > 0 else ''
                # Try to find project name (before 'project') in previous sentence
                project_name = None
                if 'project' in prev_sent:
                    project_name = prev_sent.split('project')[0].strip()
                elif 'project' in sent:
                    project_name = sent.split('project')[0].strip()
                if project_name:
                    park_related.append(project_name)
    return park_related

with open(var_call_kxhuo5e441S0pbgT5DENba0A, 'r') as f:
    docs = json.load(f)

related_projects = extract_park_projects(docs)
print('__RESULT__:')
print(json.dumps(related_projects))"""

env_args = {'var_call_kxhuo5e441S0pbgT5DENba0A': 'file_storage/call_kxhuo5e441S0pbgT5DENba0A.json'}

exec(code, env_args)
