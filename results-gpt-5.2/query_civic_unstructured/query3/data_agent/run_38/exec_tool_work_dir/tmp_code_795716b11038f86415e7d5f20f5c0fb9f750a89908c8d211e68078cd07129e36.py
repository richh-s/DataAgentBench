code = """import json, re
import pandas as pd

# funding rows
funding = pd.DataFrame(var_call_vWdkByXM2f7pC9qQWh2PZCgm)
if not funding.empty:
    funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load civic docs full
path = var_call_syaOYGPUCE4KBdQXiUMdEsiJ
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# project name candidates from funding table
proj_names = sorted(set(funding['Project_Name'].dropna().tolist()))

# helper normalize
def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

# map from project -> status inferred
status_map = {p: None for p in proj_names}

# detect status by locating project under headings
headings = [
    (re.compile(r'Capital Improvement Projects\s*\(Design\)', re.I), 'design'),
    (re.compile(r'Capital Improvement Projects\s*\(Construction\)', re.I), 'design'),
    (re.compile(r'Capital Improvement Projects\s*\(Not Started\)', re.I), 'not started'),
    (re.compile(r'Disaster Recovery Projects\s*\(Design\)', re.I), 'design'),
    (re.compile(r'Disaster Recovery Projects\s*\(Construction\)', re.I), 'design'),
    (re.compile(r'Disaster Recovery Projects\s*\(Not Started\)', re.I), 'not started'),
]

# Build per-doc sections based on headings order
for d in docs:
    text = d.get('text','')
    if not text:
        continue
    # positions of headings
    positions = []
    for rgx, label in headings:
        for m in rgx.finditer(text):
            positions.append((m.start(), m.end(), label))
    if not positions:
        continue
    positions.sort(key=lambda x: x[0])
    # create segments
    segments = []
    for i,(s,e,label) in enumerate(positions):
        seg_start = e
        seg_end = positions[i+1][0] if i+1 < len(positions) else len(text)
        segments.append((label, text[seg_start:seg_end]))
    # search project names in each segment
    for label, seg in segments:
        for p in proj_names:
            if status_map[p] is None and re.search(re.escape(p), seg, flags=re.I):
                status_map[p] = label

# fallback status: if contains 'completed' near project mention
if any(v is None for v in status_map.values()):
    for d in docs:
        text = d.get('text','')
        for p in proj_names:
            if status_map[p] is None:
                m = re.search(re.escape(p)+r'.{0,120}?completed', text, flags=re.I|re.S)
                if m:
                    status_map[p] = 'completed'

# final join
funding['Status'] = funding['Project_Name'].map(status_map).fillna('unknown')

# aggregate funding lines per project/source/amount (keep as rows)
out = funding[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source','Amount'])
result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vWdkByXM2f7pC9qQWh2PZCgm': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_syaOYGPUCE4KBdQXiUMdEsiJ': 'file_storage/call_syaOYGPUCE4KBdQXiUMdEsiJ.json'}

exec(code, env_args)
