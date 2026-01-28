code = """import json, re
import pandas as pd

def load_mongo_result(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

funding = pd.DataFrame(var_call_Bpn07o1iKHf34lrBdnuBNmI1)
# normalize amount to int
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Build set of project names we care about from funding side
proj_names = sorted(set(funding['Project_Name'].dropna().tolist()))

mongo_docs = load_mongo_result(var_call_KRgDxSAlRPEuv06aT5O7qr6H)

# For each project name, find a status in any doc text near its mention
status_priority = {'completed': 3, 'design': 2, 'not started': 1}

def infer_status(text, proj):
    # Find occurrences; inspect a window around each occurrence
    tlow = text.lower()
    plow = proj.lower()
    out = None
    for m in re.finditer(re.escape(plow), tlow):
        start = max(0, m.start()-600)
        end = min(len(tlow), m.end()+600)
        window = tlow[start:end]
        # section based
        candidates = []
        if re.search(r'\(design\)|capital improvement projects \(design\)|\bdesign phase\b|final design|complete design', window):
            candidates.append('design')
        if re.search(r'capital improvement projects \(not started\)|\bnot started\b', window):
            candidates.append('not started')
        if re.search(r'\bcompleted\b|construction was completed|notice of completion filed|complete construction', window):
            candidates.append('completed')
        # If none, but FEMA context often under disaster projects; leave unknown
        if candidates:
            # pick highest priority within this window
            cand = sorted(candidates, key=lambda x: status_priority[x], reverse=True)[0]
            if out is None or status_priority[cand] > status_priority[out]:
                out = cand
    return out

status_map = {}
for proj in proj_names:
    best = None
    for d in mongo_docs:
        s = infer_status(d.get('text',''), proj)
        if s is not None and (best is None or status_priority[s] > status_priority[best]):
            best = s
            if best == 'completed':
                break
    status_map[proj] = best if best is not None else 'unknown'

funding['Status'] = funding['Project_Name'].map(status_map)

# Keep only emergency/FEMA-related projects already filtered; group by project/source/amount/status
out_df = funding[['Project_Name','Funding_Source','Amount','Status']].copy()
out_df = out_df.sort_values(['Project_Name','Funding_Source','Amount'], na_position='last')

result = out_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Bpn07o1iKHf34lrBdnuBNmI1': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_KRgDxSAlRPEuv06aT5O7qr6H': 'file_storage/call_KRgDxSAlRPEuv06aT5O7qr6H.json'}

exec(code, env_args)
