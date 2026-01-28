code = """import json, re
import pandas as pd

# Load civic docs results (may be file path)
docs = var_call_yNDmcPPnLnOlczorQeukIG5r
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

fund = pd.DataFrame(var_call_t7m2JIfrvzupmok7fp1t6Rz3)
if not fund.empty:
    fund['Amount'] = pd.to_numeric(fund['Amount'], errors='coerce')

texts = "\n\n".join([d.get('text','') for d in docs])

# candidate project names from funding list (these are FEMA/emergency-related)
proj_names = fund['Project_Name'].dropna().unique().tolist() if not fund.empty else []

# Find status from civic texts near mentions. Use simple heuristics.
status_map = {}
for name in proj_names:
    # search for a window around the first occurrence
    m = re.search(re.escape(name), texts, flags=re.IGNORECASE)
    if not m:
        # also try without parenthetical suffix
        base = re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()
        if base and base != name:
            m = re.search(re.escape(base), texts, flags=re.IGNORECASE)
    status = None
    if m:
        start = max(0, m.start()-500)
        end = min(len(texts), m.end()+500)
        window = texts[start:end].lower()
        # infer statuses
        if re.search(r"\bcompleted\b|construction was completed|notice of completion", window):
            status = 'completed'
        elif re.search(r"\bunder construction\b|currently under construction|begin construction", window):
            status = 'design'
        elif re.search(r"\bunder design\b|finalize the design|complete design|preliminary design|plans (are|is) under review|awaiting|working with", window):
            status = 'design'
        elif re.search(r"\bnot started\b|identified|to request proposal|will be issuing|project to be discussed", window):
            status = 'not started'
    status_map[name] = status

fund['Status'] = fund['Project_Name'].map(status_map)

# Include projects related to emergency or FEMA: current fund list is already filtered.
# Summarize by project & funding source/amount rows.
fund_sorted = fund.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)
records = fund_sorted[['Project_Name','Funding_Source','Amount','Status']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_yNDmcPPnLnOlczorQeukIG5r': 'file_storage/call_yNDmcPPnLnOlczorQeukIG5r.json', 'var_call_t7m2JIfrvzupmok7fp1t6Rz3': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
