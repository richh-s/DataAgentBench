code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_TTRz13Rmh4qh0LiTwZbQ4qrj)
# normalize amount to int
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce').fillna(0).astype(int)

# load civic docs (may be file path)
text_recs = var_call_NUsVwLESouXKKYBN5GZqZUD8
if isinstance(text_recs, str):
    with open(text_recs, 'r', encoding='utf-8') as f:
        text_recs = json.load(f)

# Build status map from docs by scanning for project name lines and nearby Updates
status_map = {}

def infer_status(update_text):
    t = update_text.lower()
    if any(k in t for k in ['completed', 'was completed', 'notice of completion', 'completed,', 'complete construction', 'construction was completed']):
        return 'completed'
    if any(k in t for k in ['not started', 'identified', 'waiting for the agreement']):
        return 'not started'
    if any(k in t for k in ['design', 'finalize the design', 'plans are under review', 'preliminary design', 'submit plans', 'final design', 'awaiting', 'working with consultant']):
        return 'design'
    if 'under construction' in t or 'currently under construction' in t:
        return 'construction'
    return None

# For each doc, try to locate each funded project name and capture surrounding lines
for rec in text_recs:
    txt = rec.get('text','')
    lines = txt.splitlines()
    # index lines for search
    for pname in funding['Project_Name'].unique():
        # simple contains match ignoring multiple spaces
        pattern = re.escape(pname)
        # find line indices containing key part (strip suffix variants)
        key = re.sub(r"\s*\([^)]*\)\s*$","", pname).strip()
        if not key:
            continue
        # search for key line
        for i, line in enumerate(lines):
            if key.lower() in line.lower():
                # look ahead for 'Updates' lines within next 15 lines
                window = "\n".join(lines[i:i+20])
                m = re.search(r"Updates[:\s]*([^\n]+(?:\n(?!\s*Project Schedule|\s*Estimated Schedule|\s*Project Description).+)*)", window, flags=re.IGNORECASE)
                utext = None
                if m:
                    utext = m.group(1)
                else:
                    # fallback: use window itself
                    utext = window
                st = infer_status(utext)
                if st:
                    status_map[pname] = st
                break

# join funding with status
def map_status(pname):
    if pname in status_map:
        return status_map[pname]
    # fallback by FEMA/emergency heuristic
    return None

funding['Status'] = funding['Project_Name'].map(map_status)

# aggregate multiple funding sources per project
agg = (funding.groupby('Project_Name', as_index=False)
       .apply(lambda g: {
           'Project_Name': g['Project_Name'].iloc[0],
           'Status': g['Status'].dropna().iloc[0] if g['Status'].notna().any() else None,
           'Funding': [{
               'Funding_Source': r['Funding_Source'],
               'Amount': int(r['Amount'])
           } for _, r in g.iterrows()],
           'Total_Amount': int(g['Amount'].sum())
       })
      )

result = agg.tolist()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TTRz13Rmh4qh0LiTwZbQ4qrj': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_NUsVwLESouXKKYBN5GZqZUD8': 'file_storage/call_NUsVwLESouXKKYBN5GZqZUD8.json', 'var_call_OkYJzOFekPgiCrTCBoNMXFUJ': ['Funding']}

exec(code, env_args)
