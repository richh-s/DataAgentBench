code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_3oZiiLPBexltekS4tyepXa5d)
# load civic docs full
path = var_call_lAOwo1ZeZd4f7B60oB27mriJ
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
text_all = "\n".join(d.get('text','') for d in docs)

# helper to find status for a project by locating nearest header section
status_headers = [
    ('design', re.compile(r'Capital Improvement Projects \(Design\)|\(Design\)', re.I)),
    ('completed', re.compile(r'\(Completed\)|Construction was completed|Notice of completion', re.I)),
    ('not started', re.compile(r'Capital Improvement Projects \(Not Started\)|\(Not Started\)', re.I)),
    ('construction', re.compile(r'Capital Improvement Projects \(Construction\)', re.I)),
]

def find_status_for_project(project):
    # search in each doc separately for better context
    for d in docs:
        t = d.get('text','')
        m = re.search(re.escape(project), t, flags=re.I)
        if not m:
            continue
        idx = m.start()
        window_start = max(0, idx-2000)
        context = t[window_start:idx]
        # find last occurrence of headers in context
        best = None
        best_pos = -1
        for label, pat in status_headers:
            for hm in pat.finditer(context):
                if hm.start() > best_pos:
                    best_pos = hm.start()
                    best = label
        if best == 'construction':
            # treat as design? but requested statuses; map construction to design? keep 'construction'
            return 'construction'
        if best:
            return best
        # fallback based on nearby keywords after project
        after = t[idx:idx+500]
        if re.search(r'currently under construction|out to bid|Begin Construction', after, re.I):
            return 'design'
        if re.search(r'Construction was completed|Notice of completion', after, re.I):
            return 'completed'
    return None

funding['Status'] = funding['Project_Name'].apply(find_status_for_project)

# if not found, infer from name: contains 'Design' => design; else FEMA projects typically design/active
funding.loc[funding['Status'].isna() & funding['Project_Name'].str.contains('Design', case=False, na=False), 'Status'] = 'design'
funding.loc[funding['Status'].isna(), 'Status'] = 'unknown'

# format amounts as int
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce').fillna(0).astype(int)

result = funding[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3oZiiLPBexltekS4tyepXa5d': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_lAOwo1ZeZd4f7B60oB27mriJ': 'file_storage/call_lAOwo1ZeZd4f7B60oB27mriJ.json'}

exec(code, env_args)
