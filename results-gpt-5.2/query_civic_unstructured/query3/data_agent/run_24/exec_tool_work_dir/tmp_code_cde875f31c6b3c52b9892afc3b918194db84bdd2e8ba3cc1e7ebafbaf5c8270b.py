code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_2TDRrDVwsUKrDkga09Q6nZ80)
if funding.empty:
    out = []
else:
    # normalize amount to int
    def to_int(x):
        try:
            return int(x)
        except Exception:
            try:
                return int(float(x))
            except Exception:
                return None
    funding['Amount'] = funding['Amount'].apply(to_int)

# load mongo docs (may be file)
path_or_list = var_call_hOeORvEuODPTMDyq3wn3m3k0
if isinstance(path_or_list, str):
    with open(path_or_list, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = path_or_list

text_all = "\n".join(d.get('text','') for d in docs)

# find statuses based on headings in the status report
status_patterns = {
    'design': [r'Capital Improvement Projects \(Design\)', r'Disaster Recovery Projects \(Design\)'],
    'construction': [r'Capital Improvement Projects \(Construction\)', r'Disaster Recovery Projects \(Construction\)'],
    'not started': [r'Capital Improvement Projects \(Not Started\)', r'Disaster Recovery Projects \(Not Started\)'],
    'completed': [r'Capital Improvement Projects \(Completed\)', r'Disaster Recovery Projects \(Completed\)'],
}

# Split into lines for simple parsing
lines = text_all.splitlines()
current_status = None
projects_status = {}

# compile heading regex
heading_re = re.compile(r'^(Capital Improvement Projects|Disaster Recovery Projects) \(([^)]+)\)', re.I)

for ln in lines:
    m = heading_re.match(ln.strip())
    if m:
        st = m.group(2).strip().lower()
        if 'design' in st:
            current_status = 'design'
        elif 'construction' in st:
            current_status = 'construction'
        elif 'not started' in st:
            current_status = 'not started'
        elif 'completed' in st:
            current_status = 'completed'
        else:
            current_status = None
        continue
    # project lines: non-empty, not bullet, not section labels, title-case-ish
    s = ln.strip()
    if not s or current_status is None:
        continue
    if s.startswith('(cid') or s.startswith('Page ') or s.startswith('Agenda'):
        continue
    if s.endswith(':') or s.lower().startswith('updates') or s.lower().startswith('project schedule') or s.lower().startswith('estimated schedule') or s.lower().startswith('project description'):
        continue
    # likely project title lines have no leading bullet and are not too long
    if len(s) <= 120 and not s.startswith(('•','-','*')):
        # store first occurrence
        if s not in projects_status:
            projects_status[s] = current_status

# Now map funding project names to found statuses via fuzzy contains (remove parentheticals)
def base_name(name):
    return re.sub(r'\s*\([^)]*\)\s*', '', name).strip()

status_for_funding = []
for pn in funding['Project_Name'].tolist() if not funding.empty else []:
    bn = base_name(pn)
    found = None
    # exact base in parsed titles
    if bn in projects_status:
        found = projects_status[bn]
    else:
        # try case-insensitive match
        for title, st in projects_status.items():
            if title.lower() == bn.lower():
                found = st
                break
        if found is None:
            # substring match
            for title, st in projects_status.items():
                if bn.lower() in title.lower() or title.lower() in bn.lower():
                    found = st
                    break
    status_for_funding.append(found if found is not None else 'unknown')

if not funding.empty:
    funding['Status'] = status_for_funding
    # keep only emergency/FEMA related already filtered
    funding = funding[['Project_Name','Funding_Source','Amount','Status']]
    funding = funding.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)
    out = funding.to_dict(orient='records')
else:
    out = []

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eyAaozdcMRlbIy450H00HIJH': ['Funding'], 'var_call_krsDMptIIFDLXcUNRUe8jUbf': ['civic_docs'], 'var_call_2TDRrDVwsUKrDkga09Q6nZ80': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_hOeORvEuODPTMDyq3wn3m3k0': 'file_storage/call_hOeORvEuODPTMDyq3wn3m3k0.json'}

exec(code, env_args)
