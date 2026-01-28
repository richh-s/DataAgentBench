code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_l8SPMCnE3P2cIgpLFYcHijsF)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Load mongo docs from file
path = var_call_chtqC9ATqBxCkYExRKJKd2NO
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Parse project status sections from each doc
status_map = {}  # Project_Name -> status

def norm_name(s):
    s = re.sub(r'\s+', ' ', s.strip())
    return s

for d in docs:
    text = d.get('text','')
    # normalize bullets artifacts
    lines = [re.sub(r'\(cid:[0-9]+\)', '', ln).strip() for ln in text.splitlines()]
    current_status = None
    for ln in lines:
        m = re.search(r'^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started)\)\s*$', ln, flags=re.I)
        if m:
            st = m.group(2).lower()
            if st == 'not started':
                current_status = 'not started'
            elif st == 'design':
                current_status = 'design'
            elif st == 'construction':
                # map construction to design? keep as design? spec has 3 statuses; map construction to design? better map to design/in-progress; but asked statuses; keep 'design'??
                current_status = 'design'
            continue
        # also sometimes section headings are just like "Capital Improvement Projects (Design)"
        m = re.search(r'^(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started)\)\s*$', ln, flags=re.I)
        if m:
            st = m.group(2).lower()
            current_status = 'not started' if st=='not started' else ('design' if st in ['design','construction'] else st)
            continue
        # project name lines: non-empty, not too long, no colon, not bullet, and status known
        if current_status and ln and len(ln) < 120 and ':' not in ln and not re.match(r'^(To|Prepared by|Approved by|Date prepared|Meeting date|Subject|RECOMMENDED ACTION|DISCUSSION|Page \d+ of \d+|Agenda Item)', ln, flags=re.I):
            # common pattern: project names often Title Case; accept
            # exclude purely section headers
            if re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)$', ln, flags=re.I):
                continue
            # exclude lines that are obviously sentences
            if re.search(r'\.$', ln):
                continue
            pname = norm_name(ln)
            # store first seen status, but if later completed? none in parsed; keep most advanced? we'll prefer completed > design > not started
            prev = status_map.get(pname)
            rank = {'not started':0,'design':1,'completed':2}
            if prev is None or rank[current_status] > rank.get(prev, -1):
                status_map[pname] = current_status

status_df = pd.DataFrame([{'Project_Name':k,'Status':v} for k,v in status_map.items()])

# Join funding with statuses using exact match, then fallback fuzzy by stripping parenthetical suffix
joined = funding.merge(status_df, on='Project_Name', how='left')

def strip_suffix(n):
    return re.sub(r'\s*\([^)]*\)\s*$', '', n).strip()

joined['Base_Name'] = joined['Project_Name'].map(strip_suffix)
status_df['Base_Name'] = status_df['Project_Name'].map(strip_suffix)

base_status = status_df.sort_values('Status').drop_duplicates('Base_Name', keep='last')[['Base_Name','Status']]
joined = joined.merge(base_status, on='Base_Name', how='left', suffixes=('','_base'))
joined['Status'] = joined['Status'].fillna(joined['Status_base']).fillna('unknown')
joined = joined.drop(columns=['Status_base'])

# Filter for emergency/FEMA related
mask = joined['Project_Name'].str.contains(r'emergency|fema', case=False, na=False) | joined['Funding_Source'].str.contains(r'emergency|fema', case=False, na=False)
res = joined.loc[mask, ['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source'])

# Convert amount to int where possible
res['Amount'] = res['Amount'].fillna(0).astype(int)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_l8SPMCnE3P2cIgpLFYcHijsF': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_chtqC9ATqBxCkYExRKJKd2NO': 'file_storage/call_chtqC9ATqBxCkYExRKJKd2NO.json'}

exec(code, env_args)
