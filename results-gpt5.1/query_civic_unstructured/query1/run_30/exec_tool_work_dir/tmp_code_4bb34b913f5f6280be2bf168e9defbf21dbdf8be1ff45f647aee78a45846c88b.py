code = """import re, json, pandas as pd, os

funding = var_call_zwHFFIQM0e7Toet188ASgghM
civic_raw = var_call_tIzAtB6dvfaFzpdbsfLhXHsl

if isinstance(civic_raw, str) and os.path.exists(civic_raw):
    import json as _json
    with open(civic_raw, 'r') as f:
        civic_docs = _json.load(f)
else:
    civic_docs = civic_raw

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

pattern = r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|$)'
section_match = re.search(pattern, full_text, re.S)
projects_design = []
if section_match:
    section = section_match.group(1)
    for line in section.split('\n'):
        line = line.strip('\r ')
        if not line:
            continue
        if line.startswith('(cid:') or line.startswith('Updates') or line.startswith('Project Schedule') or line.startswith('Estimated Schedule'):
            continue
        if 'Updates' in line or 'Schedule' in line or 'Project Description' in line:
            continue
        if re.search('[a-z]', line) and re.search('[A-Z]', line):
            projects_design.append(line)

projects_design = list(dict.fromkeys(projects_design))

fund_df = pd.DataFrame(funding)

def norm(name):
    return re.sub('[^a-z0-9]+', ' ', name.lower()).strip()

fund_df['norm'] = fund_df['Project_Name'].apply(norm)

design_norm = [norm(p) for p in projects_design]

matched_projects = set()
for pn, nn in zip(projects_design, design_norm):
    for _, row in fund_df.iterrows():
        fn = row['norm']
        if nn == fn or nn in fn or fn in nn:
            matched_projects.add(row['Project_Name'])

count = len(matched_projects)

out = json.dumps({"count_capital_design_over_50000": int(count)})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zwHFFIQM0e7Toet188ASgghM': 'file_storage/call_zwHFFIQM0e7Toet188ASgghM.json', 'var_call_tIzAtB6dvfaFzpdbsfLhXHsl': 'file_storage/call_tIzAtB6dvfaFzpdbsfLhXHsl.json'}

exec(code, env_args)
