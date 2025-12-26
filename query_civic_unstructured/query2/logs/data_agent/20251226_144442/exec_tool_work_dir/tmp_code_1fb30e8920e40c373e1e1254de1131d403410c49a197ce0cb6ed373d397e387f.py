code = """import json
import pandas as pd
import re

def extract_park_projects(documents):
    projects = []
    year_regex = r'\b2022\b'
    park_regex = r'(park|playground|skate park|shade structure)'
    completed_regex = r'(completed|construction was completed|notice of completion filed)'
    for doc in documents:
        text = doc.get('text', '').lower()
        # Split into sentences
        sentences = re.split(r'[\n\.!]', text)
        for i, sent in enumerate(sentences):
            if re.search(park_regex, sent) and re.search(completed_regex, sent):
                # Look up to 2 sentences forward/backward for year
                context = ' '.join(sentences[max(0,i-2):min(len(sentences),i+3)])
                if re.search(year_regex, context):
                    # Try to extract project name
                    pnm = None
                    if 'project' in sent:
                        pnm = sent.split('project')[0].strip()
                    elif i>0 and 'project' in sentences[i-1]:
                        pnm = sentences[i-1].split('project')[0].strip()
                    # Fallback: look for anything in the previous line that matches park_regex
                    if not pnm:
                        park_match = re.search(park_regex, sentences[max(0,i-1)])
                        if park_match:
                            pnm = park_match.group(0).title()
                    projects.append({'Project_Name': pnm or 'Unknown', 'context': context})
    return projects

with open(var_call_kxhuo5e441S0pbgT5DENba0A, 'r') as f:
    civic_docs = json.load(f)

park_projects = extract_park_projects(civic_docs)
result = [p['Project_Name'] for p in park_projects if p['Project_Name'] != 'Unknown']

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kxhuo5e441S0pbgT5DENba0A': 'file_storage/call_kxhuo5e441S0pbgT5DENba0A.json'}

exec(code, env_args)
