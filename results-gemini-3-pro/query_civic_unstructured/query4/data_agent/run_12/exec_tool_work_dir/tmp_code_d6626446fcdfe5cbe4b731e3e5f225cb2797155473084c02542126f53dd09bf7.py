code = """import json
import re

c_path = locals()['var_function-call-2424790631309893722']
with open(c_path, "r") as f:
    docs = json.load(f)

projs = []
b_char = chr(190)
nl_char = chr(10)

for d in docs:
    txt = d["text"]
    chunks = txt.split(b_char)
    for i in range(1, len(chunks)):
        chunk_curr = chunks[i]
        chunk_prev = chunks[i-1].strip()
        
        if not chunk_prev: continue
        lines = chunk_prev.split(nl_char)
        name = None
        for line in reversed(lines):
            line = line.strip()
            if not line: continue
            if "Capital" in line: continue
            if "Agenda" in line: continue
            if "Page" in line: continue
            if line.endswith(":"): line = line[:-1]
            name = line
            break
            
        if not name: continue
        
        # Try finding date
        pattern = "Begin Construction:[ \t]*(.*)"
        m = re.search(pattern, chunk_curr, re.IGNORECASE)
        if m:
            dt = m.group(1).strip()
            projs.append({"n": name, "d": dt})
        else:
            # Also look for "Start:" just in case
            m2 = re.search("Start:[ \t]*(.*)", chunk_curr, re.IGNORECASE)
            if m2:
                dt = m2.group(1).strip()
                projs.append({"n": name, "d": dt, "type": "Start"})

print("__RESULT__:")
print(json.dumps(projs[:20]))"""

env_args = {'var_function-call-16991084151717076996': ['civic_docs'], 'var_function-call-16991084151717078539': ['Funding'], 'var_function-call-14749918171882353165': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14749918171882355006': 'file_storage/function-call-14749918171882355006.json', 'var_function-call-2424790631309893722': 'file_storage/function-call-2424790631309893722.json', 'var_function-call-2424790631309895007': 'file_storage/function-call-2424790631309895007.json', 'var_function-call-11236971759880299880': 'Check OK', 'var_function-call-17499494812927848584': {'count': 0, 'total_funding': 0, 'matched_projects': []}}

exec(code, env_args)
