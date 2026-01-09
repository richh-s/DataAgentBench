code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_yfj0HigWn5cq9XSOiUWBAJAv)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load mongo docs (may be file path)
raw = var_call_iM6GmRjpmQtcSWtEqj7HGO3i
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

text_all = "\n".join(d.get('text','') for d in docs)

# Extract project names and statuses from typical agenda format
# Status mapping based on section headers
patterns = [
    (r"Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)", "design"),
    (r"Capital Improvement Projects \(Construction\)(.*?)(?=Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)", "construction"),
    (r"Capital Improvement Projects \(Not Started\)(.*?)(?=Disaster Recovery Projects|$)", "not started"),
    (r"Disaster Recovery Projects\s*\(?(Design|Construction|Not Started)?\)?(.*?)(?=\n\s*Page\s+\d+\s+of\s+\d+|$)", None),
]

proj_status = {}

# capital sections
for pat, st in patterns[:3]:
    m = re.search(pat, text_all, flags=re.I|re.S)
    if not m:
        continue
    block = m.group(1)
    # project names are lines with letters/numbers and not bullet lines
    for line in block.splitlines():
        line=line.strip()
        if not line or len(line)<4:
            continue
        # exclude common non-project lines
        if re.search(r"^(\(|cid:|updates|project schedule|estimated schedule|project description|page\s+\d+|agenda item|to:|prepared by:|approved by:|date prepared|meeting date|subject|recommended action|discussion)", line, re.I):
            continue
        if re.search(r"\b(Complete Design|Advertise|Begin Construction|Complete Construction)\b", line, re.I):
            continue
        # likely project name if mostly title case and no colon
        if ':' in line:
            continue
        if len(line.split())<=1:
            continue
        proj_status.setdefault(line, st)

# disaster section heuristic: look for lines containing FEMA/emergency
for line in text_all.splitlines():
    l=line.strip()
    if not l:
        continue
    if re.search(r"(FEMA|emergency)", l, re.I):
        # treat as project name candidate
        if len(l.split())>1 and ':' not in l and len(l)<120:
            proj_status.setdefault(l, 'disaster')

# Normalize names by collapsing spaces
def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()

status_map = {norm(k): v for k,v in proj_status.items()}

# Attach status to funding projects by exact or close match
statuses=[]
for pn in funding['Project_Name']:
    n=norm(pn)
    st = status_map.get(n)
    if st is None:
        # try remove parenthetical
        n2 = norm(re.sub(r"\s*\([^)]*\)", "", pn))
        st = status_map.get(n2)
    statuses.append(st if st is not None else 'unknown')
funding['Status'] = statuses

# only emergency/FEMA related already filtered
out = funding.sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yfj0HigWn5cq9XSOiUWBAJAv': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_iM6GmRjpmQtcSWtEqj7HGO3i': 'file_storage/call_iM6GmRjpmQtcSWtEqj7HGO3i.json'}

exec(code, env_args)
