code = """import json, re, pandas as pd

# funding records already filtered on emergency/FEMA
fund = pd.DataFrame(var_call_oTavc83ubrQ9CI4heObf8KBU)
fund['Amount'] = pd.to_numeric(fund['Amount'], errors='coerce')

# load civic docs containing emergency/FEMA mentions
path = var_call_aj3fX3UuFvIcSn4kPJNfRdkL
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

texts = "\n".join(d.get('text','') for d in docs)

# For each project in funding list, find a nearby 'Updates:' line to infer status
statuses = {}
for pn in fund['Project_Name'].unique():
    # loosen matching: ignore parenthetical suffix when searching
    base = re.sub(r"\s*\([^)]*\)\s*$", "", pn).strip()
    patterns = [re.escape(pn), re.escape(base)] if base and base != pn else [re.escape(pn)]
    found_status = None
    for pat in patterns:
        m = re.search(pat + r"\s*\n\s*\(cid:190\)\s*Updates:\s*\n\s*\(cid:131\)\s*(.*?)\n", texts, flags=re.IGNORECASE)
        if m:
            upd = m.group(1).strip()
            u = upd.lower()
            if 'completed' in u or 'notice of completion' in u or 'was completed' in u:
                found_status = 'completed'
            elif 'under construction' in u or 'currently under construction' in u or 'out to bid' in u or 'bids are due' in u or 'begin construction' in u:
                found_status = 'design'
            elif 'working with' in u or 'plans' in u or 'design' in u or 'awaiting' in u or 'submitted' in u:
                found_status = 'design'
            else:
                found_status = None
            break
    statuses[pn] = found_status

fund['Status'] = fund['Project_Name'].map(statuses)

# also catch explicit emergency-related projects without FEMA in name: Outdoor Warning Signs from docs
# But question: projects related to 'emergency' or 'FEMA' -> include any with emergency in civic docs.
# We'll expand by taking any project in Funding whose name includes 'warning' and is present in docs with 'Outdoor Warning'
# However, to keep consistent, use FEMA/emergency filter only on funding query already used.

out = fund.sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oTavc83ubrQ9CI4heObf8KBU': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_aj3fX3UuFvIcSn4kPJNfRdkL': 'file_storage/call_aj3fX3UuFvIcSn4kPJNfRdkL.json', 'var_call_00LYo36WhaWRHvRY8CUe53Jg': 'file_storage/call_00LYo36WhaWRHvRY8CUe53Jg.json', 'var_call_Q3UaQKUgpHae6GYmItrpCteG': 'file_storage/call_Q3UaQKUgpHae6GYmItrpCteG.json'}

exec(code, env_args)
