code = """import re, json
from collections import defaultdict

path_docs = var_call_mGnqprHFQ73hu7YqB1PojDBr
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding = var_call_d8vdXEINxieaknusctMc4gFi

park_completed_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        l = line.strip()
        if 'Construction was completed' in l and '2022' in l:
            pname = None
            for j in range(i-1, max(-1, i-5), -1):
                prev = lines[j].strip()
                if prev:
                    pname = prev
                    break
            if pname:
                park_completed_2022.add(pname)

park_funding_total = 0
matched_projects = []

for row in funding:
    fname = row['Project_Name']
    if 'park' not in fname.lower():
        continue
    for cname in park_completed_2022:
        fl = fname.lower()
        cl = cname.lower()
        if fl in cl or cl in fl:
            amt = int(row['Amount'])
            park_funding_total += amt
            matched_projects.append({'fund_name': fname, 'civic_name': cname, 'amount': amt})
            break

result = {
    'total_funding_park_completed_2022': park_funding_total,
    'matched_projects': matched_projects,
    'identified_completed_2022_projects': list(park_completed_2022)
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_mGnqprHFQ73hu7YqB1PojDBr': 'file_storage/call_mGnqprHFQ73hu7YqB1PojDBr.json', 'var_call_d8vdXEINxieaknusctMc4gFi': 'file_storage/call_d8vdXEINxieaknusctMc4gFi.json'}

exec(code, env_args)
