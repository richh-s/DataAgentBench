code = """import json
import re

c_p = locals()['var_function-call-2424790631309893722']
f_p = locals()['var_function-call-2424790631309895007']

with open(c_p, 'r') as f:
    docs = json.load(f)
with open(f_p, 'r') as f:
    funds = json.load(f)

projs = []
b = chr(190)

for d in docs:
    txt = d['text']
    pts = txt.split(b)
    for i in range(1, len(pts)):
        det = pts[i]
        prv = pts[i-1].strip()
        if not prv: continue
        
        lns = prv.split('\n')
        nm = None
        for l in reversed(lns):
            l = l.strip()
            if not l: continue
            if 'Capital' in l: continue
            if 'Agenda' in l: continue
            if l.startswith('Page'): continue
            if l.endswith(':'): l = l[:-1]
            nm = l
            break
        
        if not nm: continue
        
        # Date
        # Begin Construction: ...
        m = re.search('Begin Construction:\\s*(.*)', det, re.IGNORECASE)
        if m:
            dt = m.group(1).strip()
            projs.append({'n': nm, 'd': dt})

# Filter
tn = []
sp = ['March', 'April', 'May', 'Spring']
for p in projs:
    ds = p['d']
    if '2022' in ds:
        isp = False
        for s in sp:
            if s.lower() in ds.lower():
                isp = True
        if isp:
            tn.append(p['n'])

# Unique names
tn = list(set(tn))

# Sum
tot = 0
cnt = 0
mp = {}
for r in funds:
    fn = r['Project_Name'].strip()
    fa = int(r['Amount'])
    mp[fn] = mp.get(fn, 0) + fa

m_l = []
for n in tn:
    if n in mp:
        tot += mp[n]
        cnt += 1
        m_l.append(n)

print('__RESULT__:')
print(json.dumps({'count': cnt, 'total': tot, 'matched': m_l}))"""

env_args = {'var_function-call-16991084151717076996': ['civic_docs'], 'var_function-call-16991084151717078539': ['Funding'], 'var_function-call-14749918171882353165': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14749918171882355006': 'file_storage/function-call-14749918171882355006.json', 'var_function-call-2424790631309893722': 'file_storage/function-call-2424790631309893722.json', 'var_function-call-2424790631309895007': 'file_storage/function-call-2424790631309895007.json'}

exec(code, env_args)
