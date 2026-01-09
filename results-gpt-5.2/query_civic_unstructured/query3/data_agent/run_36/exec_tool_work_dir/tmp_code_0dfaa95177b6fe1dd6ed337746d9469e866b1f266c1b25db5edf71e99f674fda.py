code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_6FH0upUqaGoqPAiaFfKGDHEh)
# ensure numeric amount
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load mongo results (may be file path)
mongo_res = var_call_sMswgJU0KlLM7ZbL80o4I3fb
if isinstance(mongo_res, str) and mongo_res.endswith('.json'):
    with open(mongo_res, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = mongo_res

project_names = sorted(funding['Project_Name'].dropna().unique().tolist())

# compile regexes for project name detection
name_patterns = {name: re.compile(re.escape(name), re.IGNORECASE) for name in project_names}

# status keyword detection
status_patterns = [
    ('completed', re.compile(r'\b(completed|notice of completion filed|construction was completed)\b', re.I)),
    ('design', re.compile(r'\b(under design|design phase|final design|complete design|plans? (are|is) (under review|being finalized|have been completed)|working with.*finalize the design)\b', re.I)),
    ('not started', re.compile(r'\b(not started|identified|waiting for the agreement|preliminary design will determine)\b', re.I)),
    ('construction', re.compile(r'\b(under construction|begin construction|out to bid|advertise)\b', re.I)),
]

def infer_status(context):
    ctx = context.lower()
    for label, pat in status_patterns:
        if pat.search(context):
            if label in ['construction']:
                return 'design' if 'design' in ctx else 'not started' if 'not started' in ctx else 'construction'
            return label
    return None

rows=[]
for name in project_names:
    status = None
    for d in docs:
        text = d.get('text','')
        m = name_patterns[name].search(text)
        if not m:
            continue
        # grab context around match
        start = max(0, m.start()-400)
        end = min(len(text), m.end()+400)
        context = text[start:end]
        status = infer_status(context) or status
        if status:
            break
    # map construction to design/completed/not started if needed; keep as-is if found
    rows.append({'Project_Name': name, 'Status': status or 'unknown'})

status_df = pd.DataFrame(rows)

out = funding.merge(status_df, on='Project_Name', how='left')
# sort by project then funding source
out = out.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)
result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6FH0upUqaGoqPAiaFfKGDHEh': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_sMswgJU0KlLM7ZbL80o4I3fb': 'file_storage/call_sMswgJU0KlLM7ZbL80o4I3fb.json', 'var_call_qzPntM3zUdt0VNd3uSmuSlQR': ['Funding'], 'var_call_AuQpZ9hOorXL8nZcPAgIySQb': ['civic_docs']}

exec(code, env_args)
