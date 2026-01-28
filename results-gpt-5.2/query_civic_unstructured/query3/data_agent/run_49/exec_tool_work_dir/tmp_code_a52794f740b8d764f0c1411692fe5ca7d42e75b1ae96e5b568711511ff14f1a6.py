code = """import json, re
import pandas as pd

# Load mongo docs (may be file path)
raw = var_call_QvoOvLl0Sh5WaynBE6vh0bSA
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

fund = pd.DataFrame(var_call_hzvzjtNTEYxfxW4YD2ji67RA)
if not fund.empty:
    fund['Amount'] = pd.to_numeric(fund['Amount'], errors='coerce')

# Extract project status lines from docs: locate sections and infer status
statuses = {}

status_markers = {
    'design': re.compile(r'\(Design\)|Capital Improvement Projects \(Design\)|Disaster Recovery Projects \(Design\)', re.I),
    'construction': re.compile(r'\(Construction\)|Capital Improvement Projects \(Construction\)|Disaster Recovery Projects \(Construction\)', re.I),
    'not started': re.compile(r'\(Not Started\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects \(Not Started\)', re.I)
}

# We'll parse by scanning lines; when a marker encountered, set current status
for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    cur_status = None
    for ln in lines:
        for st, pat in status_markers.items():
            if pat.search(ln):
                cur_status = 'design' if st=='design' else ('not started' if st=='not started' else 'construction')
        # project name heuristic: line with FEMA or emergency and not bullet headers
        if cur_status:
            if re.search(r'(FEMA|Emergency|Warning)', ln, re.I):
                if len(ln) > 3 and not ln.lower().startswith(('updates','project schedule','estimated schedule','project description')):
                    pname = re.sub(r'\s+', ' ', ln).strip(' -•\t')
                    # ignore if clearly a sentence
                    if pname and len(pname.split())<=12:
                        statuses.setdefault(pname, cur_status)

# Normalize and map statuses to funding project names via substring match
fund_status = []
for pname in fund['Project_Name'].tolist():
    st = None
    # direct match
    if pname in statuses:
        st = statuses[pname]
    else:
        # try match without parentheses suffixes
        base = re.sub(r'\s*\([^\)]*\)\s*$', '', pname).strip()
        # find a status key contained
        candidates = []
        for k,v in statuses.items():
            kb = re.sub(r'\s*\([^\)]*\)\s*$', '', k).strip()
            if kb and (kb.lower() in base.lower() or base.lower() in kb.lower()):
                candidates.append((k,v))
        if candidates:
            st = candidates[0][1]
    fund_status.append(st)

fund['Status'] = fund_status
fund = fund.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

result = fund[['Project_Name','Funding_Source','Amount','Status']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_yH32kvznwOKtNF1RNJXl5GmL': ['Funding'], 'var_call_28zAwTTi5mzcfPvu9pEEwjyJ': ['civic_docs'], 'var_call_QvoOvLl0Sh5WaynBE6vh0bSA': 'file_storage/call_QvoOvLl0Sh5WaynBE6vh0bSA.json', 'var_call_hzvzjtNTEYxfxW4YD2ji67RA': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
