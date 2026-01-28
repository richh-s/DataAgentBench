code = """import json
import pandas as pd

with open(locals()['var_function-call-14770944468380468337'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-14241512510866870290'], 'r') as f:
    civic_docs = json.load(f)

def is_park(name):
    keywords = ['park', 'playground', 'recreation']
    n = name.lower()
    for k in keywords:
        if k in n:
            return True
    return False

def check_comp(text):
    t = text.lower()
    if '2022' not in t:
        return False
    if 'completed' in t or 'complete construction' in t:
        lines = text.split('\n')
        for l in lines:
            ll = l.lower()
            if '2022' in ll:
                if 'construction' in ll and ('completed' in ll or 'complete' in ll):
                    return True
                if 'construction was completed' in ll:
                    return True
    return False

projects = []
for doc in civic_docs:
    lines = [l.strip() for l in doc['text'].split('\n') if l.strip()]
    i = 0
    while i < len(lines):
        line = lines[i]
        if i + 1 < len(lines):
            nxt = lines[i+1]
            if 'Updates:' in nxt or 'Project Description:' in nxt:
                if 'Capital Improvement Projects' not in line:
                    p_name = line
                    blk = []
                    j = i + 1
                    while j < len(lines):
                        s = lines[j]
                        if j + 1 < len(lines):
                            nn = lines[j+1]
                            if ('Updates:' in nn or 'Project Description:' in nn) and not ('Updates:' in s or 'Project Description:' in s):
                                if not (s.startswith('(') or s.startswith('-')):
                                    break
                        blk.append(s)
                        j += 1
                    projects.append({'name': p_name, 'text': '\n'.join(blk)})
                    i = j
                    continue
        i += 1

matches = []
total = 0
funding_df = pd.DataFrame(funding_data)

for p in projects:
    if is_park(p['name']) and check_comp(p['text']):
        nm = p['name']
        match = funding_df[funding_df['Project_Name'] == nm]
        if match.empty:
            match = funding_df[funding_df['Project_Name'].str.lower() == nm.lower()]
        
        amt = 0
        if not match.empty:
            amt = int(match['Amount'].sum())
            total += amt
        matches.append({'name': nm, 'amount': amt})

print("__RESULT__:")
print(json.dumps({'matches': matches, 'total': total}))"""

env_args = {'var_function-call-18374819534709684417': 'file_storage/function-call-18374819534709684417.json', 'var_function-call-14770944468380468337': 'file_storage/function-call-14770944468380468337.json', 'var_function-call-14241512510866870290': 'file_storage/function-call-14241512510866870290.json'}

exec(code, env_args)
