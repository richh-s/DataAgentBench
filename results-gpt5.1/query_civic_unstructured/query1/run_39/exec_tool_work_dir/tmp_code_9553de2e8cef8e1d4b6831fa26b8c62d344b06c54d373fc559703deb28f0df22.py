code = """import re, json, pandas as pd

with open(var_call_L7vqlHNWEYU5dF63ePQFrPlc, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

civic_source = var_call_GuV3TFmjKHCUlSwgbOD4Z84X
if isinstance(civic_source, str) and civic_source.endswith('.json'):
    with open(civic_source, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_source

texts = ' '.join(doc['text'] for doc in civic_docs)

pattern = r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)"
design_section_match = re.search(pattern, texts, re.S)

design_projects = []
if design_section_match:
    section = design_section_match.group(1)
    for raw_line in section.split('\n'):
        line = raw_line.strip('\r ')
        if not line:
            continue
        skip_substrings = ['Updates', 'Project Schedule', 'Estimated Schedule', 'Page ', 'Agenda Item']
        if any(sub in line for sub in skip_substrings):
            continue
        if len(line.split()) >= 2 and re.match(r'[A-Z0-9]', line):
            design_projects.append(line)

# dedupe
seen = set()
unique_design_projects = []
for proj in design_projects:
    if proj not in seen:
        seen.add(proj)
        unique_design_projects.append(proj)

design_projects = sorted(unique_design_projects)

funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_over = funding_df[funding_df['Amount'] > 50000]
funding_names = set(funding_over['Project_Name'])

count = 0
matched_projects = []
for name in design_projects:
    if name in funding_names:
        count += 1
        matched_projects.append(name)

result = {"count": count, "matched_projects": matched_projects, "design_projects_extracted": design_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_L7vqlHNWEYU5dF63ePQFrPlc': 'file_storage/call_L7vqlHNWEYU5dF63ePQFrPlc.json', 'var_call_GuV3TFmjKHCUlSwgbOD4Z84X': 'file_storage/call_GuV3TFmjKHCUlSwgbOD4Z84X.json'}

exec(code, env_args)
