code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_rH31QG4iEz97agytyQXsJwLk)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Load mongo results (may be file)
raw = var_call_SXebeHhCfkjeersIMozC1VP3
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

# Build status map by scanning documents for project names and nearby status keywords
projects = funding['Project_Name'].unique().tolist()

status_map = {}
for d in docs:
    txt = d.get('text','')
    low = txt.lower()
    for p in projects:
        plow = p.lower()
        idx = low.find(plow)
        if idx == -1:
            continue
        window = low[max(0, idx-250): idx+250]
        status = None
        if 'completed' in window or 'construction was completed' in window or 'notice of completion' in window:
            status = 'completed'
        elif 'under construction' in window or 'currently under construction' in window or 'begin construction' in window or 'construction:' in window:
            # treat as design if it says complete design; but here under construction
            status = 'design'
        elif 'design' in window or 'final design' in window or 'complete design' in window or 'preliminary design' in window:
            status = 'design'
        elif 'not started' in window:
            status = 'not started'
        if status:
            # keep most advanced: completed > design > not started
            rank = {'not started':0,'design':1,'completed':2}
            cur = status_map.get(p)
            if (cur is None) or (rank[status] > rank[cur]):
                status_map[p] = status

funding['Status'] = funding['Project_Name'].map(status_map)

# Aggregate amounts per project/source/status
out = (funding.groupby(['Project_Name','Funding_Source','Status'], dropna=False, as_index=False)
              .agg(Amount=('Amount','sum'))
      )

# Order and format
out = out.sort_values(['Project_Name','Funding_Source'])
records = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_rH31QG4iEz97agytyQXsJwLk': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_SXebeHhCfkjeersIMozC1VP3': 'file_storage/call_SXebeHhCfkjeersIMozC1VP3.json', 'var_call_V5xhGfX58onEHx3wKNfKPofc': ['Funding'], 'var_call_zC18sIEDlqu4dMjGC20mQTIR': ['civic_docs']}

exec(code, env_args)
