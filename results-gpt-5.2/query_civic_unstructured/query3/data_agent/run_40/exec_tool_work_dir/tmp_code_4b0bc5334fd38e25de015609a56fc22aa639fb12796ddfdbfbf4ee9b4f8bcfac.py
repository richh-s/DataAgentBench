code = """import json, re, pandas as pd
from pathlib import Path

# Load civic docs results (may be a filepath)
docs = var_call_tDSr1LyYPwefqQNVuD6KIEI1
if isinstance(docs, str) and docs.endswith('.json'):
    docs = json.loads(Path(docs).read_text())

fund = var_call_MHuOjR3GLo9Ojar7aXz1cJW2

doc_text = "\n".join(d.get('text','') for d in docs)

# Parse project sections from status report-style doc
# Capture headings like: 'Capital Improvement Projects (Design)' or 'Disaster Recovery Projects (Construction)'
section_pat = re.compile(r"^(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started)\)\s*$", re.IGNORECASE | re.MULTILINE)

# Find section boundaries
sections = []
for m in section_pat.finditer(doc_text):
    sections.append((m.start(), m.end(), m.group(1), m.group(2)))
sections_sorted = sorted(sections, key=lambda x: x[0])

# Helper to clean line
def clean(s):
    s = re.sub(r"\(cid:[^)]+\)", "", s)
    s = s.replace('\u2019', "'")
    return s.strip()

# Extract project names within each section by looking for lines that are title-cased and not bullets
proj_status = {}

for i, (s0, e0, sec_type, sec_status) in enumerate(sections_sorted):
    end = sections_sorted[i+1][0] if i+1 < len(sections_sorted) else len(doc_text)
    block = doc_text[e0:end]
    # split lines
    lines = [clean(l) for l in block.splitlines()]
    # project name heuristic: non-empty, not starting with common words, limited length
    for l in lines:
        if not l: continue
        if l.lower().startswith(('updates', 'project schedule', 'estimated schedule', 'project description', 'page ', 'agenda item', 'staff', 'city ')):
            continue
        if l.startswith(('-', '•', '*')): 
            continue
        # avoid sentences
        if len(l) > 90: 
            continue
        if any(kw in l.lower() for kw in ['receive and file', 'recommended action', 'discussion']):
            continue
        # likely a project title if it has multiple words and no trailing punctuation
        if re.search(r"[\.!?:;]$", l):
            continue
        if len(l.split()) < 2:
            continue
        # register
        # Keep first status found
        proj_status.setdefault(l, sec_status.lower())

# Filter projects containing emergency or fema keywords
keywords = re.compile(r"\b(fema|emergency)\b", re.IGNORECASE)
proj_status_filtered = {p:s for p,s in proj_status.items() if keywords.search(p)}

# Normalize funding project name typos
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce')

# Build status lookup by fuzzy-ish normalization
def norm(name):
    return re.sub(r"\s+", " ", re.sub(r"[^A-Za-z0-9 ]+", " ", (name or '').lower())).strip()

status_norm = {norm(k):v for k,v in proj_status_filtered.items()}

statuses = []
for pn in fund_df['Project_Name'] if not fund_df.empty else []:
    n = norm(pn)
    # direct
    st = status_norm.get(n)
    if st is None:
        # try remove parenthetical suffixes
        n2 = re.sub(r"\s*\bfema\b.*$", "", n).strip()
        st = status_norm.get(n2)
    statuses.append(st)

if not fund_df.empty:
    fund_df['Status'] = statuses

# Keep all funding rows where project name includes fema/emergency OR status found
if not fund_df.empty:
    mask = fund_df['Project_Name'].str.contains('fema|emergency', case=False, regex=True) | fund_df['Status'].notna()
    out_df = fund_df.loc[mask, ['Project_Name','Funding_Source','Amount','Status']].copy()
    out_df = out_df.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)
    result = out_df.to_dict(orient='records')
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_tDSr1LyYPwefqQNVuD6KIEI1': 'file_storage/call_tDSr1LyYPwefqQNVuD6KIEI1.json', 'var_call_MHuOjR3GLo9Ojar7aXz1cJW2': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
