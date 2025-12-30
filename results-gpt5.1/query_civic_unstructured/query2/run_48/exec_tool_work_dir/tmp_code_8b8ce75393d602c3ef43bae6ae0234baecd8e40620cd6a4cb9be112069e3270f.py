code = """import re, json, pandas as pd

# Load civic docs full result
path = var_call_AzxNLzQYErCuP7tasW38dzUp
with open(path, 'r') as f:
    civic_docs = json.load(f)
texts = [d.get('text','') for d in civic_docs]
full_text = '\n'.join(texts)

# Very rough project extraction: split on double newlines and treat lines that look like project titles
blocks = re.split(r"\n\n+", full_text)
projects = []
current = None
for block in blocks:
    line = block.strip().split('\n')[0].strip()
    if not line:
        continue
    # Heuristic: title case words and contains keywords like 'Project', 'Park', 'Playground', 'Shade', 'Walkway'
    if re.search(r"(Project|Park|Playground|Shade|Walkway)", line):
        current = {'Project_Name': line}
        # search topic keywords in block
        topics = []
        for kw in ['park','playground','shade','walkway','road','bridge','storm drain','drainage']:
            if re.search(kw, block, re.IGNORECASE):
                topics.append(kw)
        current['topic'] = ','.join(sorted(set(topics))) if topics else ''
        # status
        status = None
        if re.search(r"construction was completed,? 2022", block, re.IGNORECASE):
            status = 'completed'
        elif re.search(r"construction was completed,? November 2022", block, re.IGNORECASE):
            status = 'completed'
        elif re.search(r"Notice of completion", block, re.IGNORECASE):
            status = 'completed'
        elif re.search(r"project is currently under construction", block, re.IGNORECASE):
            status = 'design'
        current['status'] = status or ''
        # end time/date (et): search for 'completed' lines
        et = None
        m = re.search(r"Construction was completed,? ([A-Za-z]+ 2022|2022)", block, re.IGNORECASE)
        if m:
            et = m.group(1)
        m2 = re.search(r"Construction was completed ([A-Za-z]+ 2022)", block, re.IGNORECASE)
        if m2:
            et = m2.group(1)
        current['et'] = et or ''
        projects.append(current)

# Filter park-related projects completed in 2022
park_projects_2022 = [p for p in projects if 'park' in p.get('topic','') and p.get('status')=='completed' and ('2022' in p.get('et','') or '2022' in p.get('et',''))]

# Funding data
funding = pd.DataFrame(var_call_QE590y2beo7xdcETCshsds0E)
funding['Amount'] = funding['Amount'].astype(int)

# Join on Project_Name using simple exact match
proj_names = [p['Project_Name'] for p in park_projects_2022]
matched = funding[funding['Project_Name'].isin(proj_names)]

result = {
    'projects': park_projects_2022,
    'matched_funding_records': matched.to_dict(orient='records'),
    'total_funding': int(matched['Amount'].sum()) if not matched.empty else 0
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_AzxNLzQYErCuP7tasW38dzUp': 'file_storage/call_AzxNLzQYErCuP7tasW38dzUp.json', 'var_call_QE590y2beo7xdcETCshsds0E': 'file_storage/call_QE590y2beo7xdcETCshsds0E.json'}

exec(code, env_args)
