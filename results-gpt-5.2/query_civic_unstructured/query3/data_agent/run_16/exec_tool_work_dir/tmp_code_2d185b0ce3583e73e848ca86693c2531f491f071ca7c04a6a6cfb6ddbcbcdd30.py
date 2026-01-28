code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_CN4C5WCtWAFoLxqzXntRPuYY)
# normalize amount
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load civic docs results (may be file path)
docs_obj = var_call_aTOmP5IfgZNT02XICGUfslFQ
if isinstance(docs_obj, str) and docs_obj.endswith('.json'):
    with open(docs_obj, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_obj

texts = "\n".join(d.get('text','') for d in docs)

proj_names = sorted(funding['Project_Name'].dropna().unique().tolist(), key=len, reverse=True)

def find_status(name, corpus):
    # grab local context around first match
    m = re.search(re.escape(name), corpus, flags=re.IGNORECASE)
    if not m:
        return None
    start = max(0, m.start()-600)
    end = min(len(corpus), m.end()+600)
    ctx = corpus[start:end]
    # look for Updates line
    # common phrases: 'Updates:' then status sentences
    updates = None
    um = re.search(r"Updates\s*:\s*(.{0,250})", ctx, flags=re.IGNORECASE)
    if um:
        updates = um.group(1).strip()
    low = ctx.lower()
    # map to canonical
    if 'completed' in low or 'construction was completed' in low or 'notice of completion' in low:
        return 'completed'
    if 'not started' in low:
        return 'not started'
    if 'design' in low or 'final design' in low or 'preliminary design' in low or 'working with the consultant' in low or 'plans and specifications are being finalized' in low:
        return 'design'
    if 'under construction' in low or 'currently under construction' in low:
        # not in allowed set, but closest is design vs completed; keep as 'construction'
        return 'construction'
    return None

status_map = {name: find_status(name, texts) for name in proj_names}

out = funding.copy()
out['Status'] = out['Project_Name'].map(status_map)

# group by project+source+status summing amount
outg = (out.groupby(['Project_Name','Funding_Source','Status'], dropna=False, as_index=False)
          .agg({'Amount':'sum'}))

# sort
outg = outg.sort_values(['Project_Name','Funding_Source'])

result = outg.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CN4C5WCtWAFoLxqzXntRPuYY': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_aTOmP5IfgZNT02XICGUfslFQ': 'file_storage/call_aTOmP5IfgZNT02XICGUfslFQ.json'}

exec(code, env_args)
