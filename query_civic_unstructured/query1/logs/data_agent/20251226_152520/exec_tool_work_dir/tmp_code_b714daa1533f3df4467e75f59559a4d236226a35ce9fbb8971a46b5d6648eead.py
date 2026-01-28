code = """import json
import pandas as pd

with open(var_call_MCzLUN1aQngiKrENJOovZ4JX, 'r') as f:
    funding_projects = json.load(f)
project_names = set([item['Project_Name'] for item in funding_projects])

with open(var_call_LxqvxIRagmf62s3IGxebkxzW, 'r') as f:
    civic_docs = json.load(f)

# We'll scan the text for mentions of project names and extract those mentioned as 'capital' projects in 'design' status
capital_design_projects = set()
for doc in civic_docs:
    text = doc['text'].lower()
    for name in project_names:
        pname = name.lower()
        # Rough NLP: look for 'design' near the project name and 'capital' in description
        if pname in text:
            # Find a window around the project name
            idx = text.find(pname)
            window = text[max(0, idx-100):idx+len(pname)+100]
            if ('design' in window) and ('capital' in window):
                capital_design_projects.add(name)

# Result: how many unique capital projects with 'design' status also have funding > $50,000?
result = len(capital_design_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MCzLUN1aQngiKrENJOovZ4JX': 'file_storage/call_MCzLUN1aQngiKrENJOovZ4JX.json', 'var_call_LxqvxIRagmf62s3IGxebkxzW': 'file_storage/call_LxqvxIRagmf62s3IGxebkxzW.json'}

exec(code, env_args)
