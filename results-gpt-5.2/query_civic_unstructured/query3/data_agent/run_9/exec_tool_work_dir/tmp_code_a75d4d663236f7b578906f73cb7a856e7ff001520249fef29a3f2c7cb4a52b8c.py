code = """import json, re, pandas as pd

# Load civic docs from file if needed
civic_res = var_call_6AjnVQvphdSTTLZeet2DAOiJ
if isinstance(civic_res, str) and civic_res.endswith('.json'):
    with open(civic_res, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_res

funding = var_call_PhHZoIk2RMfjakbHfFnAV72t
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce')

# Extract statuses for funded projects from docs (simple heuristic: find nearby 'Updates' line)
project_names = fund_df['Project_Name'].dropna().unique().tolist()

def norm(s):
    return re.sub(r'\s+', ' ', s.strip().lower())

proj_to_status = {}
for doc in civic_docs:
    text = doc.get('text','')
    low = text.lower()
    for pn in project_names:
        if pn.lower() in low:
            # take window around occurrence
            idx = low.find(pn.lower())
            win = text[max(0, idx-500): idx+1000]
            wlow = win.lower()
            status = None
            # look for 'Updates:' then take rest of line
            m = re.search(r'updates\s*:\s*([^\n\r]{0,200})', win, flags=re.I)
            if m:
                status = m.group(1).strip()
            # map common phrases
            mapped = None
            if status:
                sl = status.lower()
                if 'completed' in sl or 'construction was completed' in sl or 'notice of completion' in sl:
                    mapped = 'completed'
                elif 'under construction' in sl or 'currently under construction' in sl or 'construction' in sl and 'complete' in sl:
                    mapped = 'design'
                elif 'working with' in sl or 'finalize the design' in sl or 'plans' in sl or 'review' in sl or 'design' in sl:
                    mapped = 'design'
                elif 'not started' in wlow or 'capital improvement projects (not started)' in wlow:
                    mapped = 'not started'
            # fallback: section headers
            if mapped is None:
                if 'capital improvement projects (not started)' in wlow:
                    mapped = 'not started'
                elif 'capital improvement projects (design)' in wlow or 'disaster recovery projects (design)' in wlow:
                    mapped = 'design'
                elif 'completed' in wlow:
                    mapped = 'completed'
            if mapped:
                proj_to_status[pn] = mapped

# Build output table
out_df = fund_df.copy()
out_df['Status'] = out_df['Project_Name'].map(proj_to_status)
# If status missing, label as 'unknown'
out_df['Status'] = out_df['Status'].fillna('unknown')

# Aggregate by project_name + funding_source (keep as is) and sort
out_df = out_df.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)
result = out_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6AjnVQvphdSTTLZeet2DAOiJ': 'file_storage/call_6AjnVQvphdSTTLZeet2DAOiJ.json', 'var_call_PhHZoIk2RMfjakbHfFnAV72t': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
