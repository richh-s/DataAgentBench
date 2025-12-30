code = """import re, json, pandas as pd

# Load funding records (>50k)
funding_records = var_call_ZaBv4CT9khVOZ5Vz17idIjRZ

# Load civic docs texts
civic_docs = var_call_KNM0vc8gFhiuPuDdkHKway03
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Very simple heuristic: capture lines under "Capital Improvement Projects (Design)" section
design_sections = []
pattern = r"Capital Improvement Projects \(Design\)([\s\S]*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects|$)"
for match in re.finditer(pattern, full_text):
    design_sections.append(match.group(1))

design_text = '\n'.join(design_sections)

# Extract candidate project name lines: non-empty lines that don't start with bullets and are title-like
project_names = set()
for line in design_text.split('\n'):
    line = line.strip()
    if not line:
        continue
    if line.startswith('(cid:') or line.lower().startswith('updates') or line.lower().startswith('project'):
        continue
    # Heuristic: lines with multiple words and at least one capital letter
    if len(line.split()) >= 2:
        project_names.add(line)

# Build DataFrame for funding
fund_df = pd.DataFrame(funding_records)

# Normalize names for matching
def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

fund_df['norm_name'] = fund_df['Project_Name'].apply(norm)

design_norms = {norm(n): n for n in project_names}

# Inner join on normalized name
design_funding = fund_df[fund_df['norm_name'].isin(design_norms.keys())]

# We also need only capital projects; assume that any matched here under Capital Improvement Projects (Design) are capital.
count = int(len(design_funding))

result = json.dumps({"count_capital_design_over_50000": count})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ZaBv4CT9khVOZ5Vz17idIjRZ': 'file_storage/call_ZaBv4CT9khVOZ5Vz17idIjRZ.json', 'var_call_KNM0vc8gFhiuPuDdkHKway03': 'file_storage/call_KNM0vc8gFhiuPuDdkHKway03.json'}

exec(code, env_args)
