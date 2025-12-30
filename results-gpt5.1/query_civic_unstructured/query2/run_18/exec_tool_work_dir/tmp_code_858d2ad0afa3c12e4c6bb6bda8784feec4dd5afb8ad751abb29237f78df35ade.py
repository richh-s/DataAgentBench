code = """import re, json
from collections import defaultdict

# Load full civic docs
path_docs = var_call_mGnqprHFQ73hu7YqB1PojDBr
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding = var_call_d8vdXEINxieaknusctMc4gFi

# Very simple heuristic: park-related if 'park' in project name (case-insensitive)
# Need projects completed in 2022 based on civic text. We'll scan for lines with 'Construction was completed' or 'Construction was completed,' and a month 2022

park_completed_2022 = set()

for doc in civic_docs:
    text = doc.get('text','')
    # Split to lines
    lines = text.split('\n')
    for i, line in enumerate(lines):
        l = line.strip()
        if 'Construction was completed' in l and '2022' in l:
            # look backwards for a likely project name (previous non-empty line)
            pname = None
            for j in range(i-1, max(-1, i-5), -1):
                prev = lines[j].strip()
                if prev:
                    pname = prev
                    break
            if pname:
                park_completed_2022.add(pname)

# Now match these names to funding project names using simple case-insensitive equality or containment either way

park_funding_total = 0
matched_projects = []

for row in funding:
    fname = row['Project_Name']
    if 'park' not in fname.lower():
        continue
    # check if this funding project corresponds to a completed-2022 project name
    for cname in park_completed_2022:
        if fname.lower() in cname.lower() or cname.lower() in fname.lower():
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
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mGnqprHFQ73hu7YqB1PojDBr': 'file_storage/call_mGnqprHFQ73hu7YqB1PojDBr.json', 'var_call_d8vdXEINxieaknusctMc4gFi': 'file_storage/call_d8vdXEINxieaknusctMc4gFi.json'}

exec(code, env_args)
