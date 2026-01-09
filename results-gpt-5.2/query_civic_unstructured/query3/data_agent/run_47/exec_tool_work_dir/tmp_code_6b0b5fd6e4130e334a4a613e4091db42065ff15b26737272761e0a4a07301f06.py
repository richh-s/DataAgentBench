code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_b2Bz06VqrdCj545wV2lljVNl)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load civic docs (may be stored as file path)
raw = var_call_RawYiRHR6GZwLqYYR6urtkPu
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

# build status map by scanning for each funded project name within docs and extracting nearby status section
project_names = funding['Project_Name'].dropna().unique().tolist()

status_map = {}
pattern_cache = {}
for pn in project_names:
    # flexible regex: ignore extra spaces, escape special chars
    if pn not in pattern_cache:
        esc = re.escape(pn)
        pattern_cache[pn] = re.compile(esc, re.IGNORECASE)

for d in docs:
    text = d.get('text','')
    # quick prefilter
    if not re.search(r'(FEMA|emergency)', text, re.IGNORECASE):
        continue
    for pn in project_names:
        if pn in status_map:
            continue
        if not pattern_cache[pn].search(text):
            continue
        # try to infer status from section headers in document
        # Find which of the three buckets the project appears under
        idx = pattern_cache[pn].search(text).start()
        window = text[max(0, idx-2000): idx+2000]
        status = None
        for cand, label in [(r'Capital Improvement Projects \(Design\)', 'design'),
                            (r'Capital Improvement Projects \(Construction\)', 'design'),
                            (r'Capital Improvement Projects \(Not Started\)', 'not started'),
                            (r'Disaster Recovery Projects \(Design\)', 'design'),
                            (r'Disaster Recovery Projects \(Construction\)', 'design'),
                            (r'Disaster Recovery Projects \(Not Started\)', 'not started')]:
            # use last occurrence before idx in full text for robustness
            for m in re.finditer(cand, text, re.IGNORECASE):
                if m.start() < idx:
                    status = label
        # If within window says construction completed
        if re.search(r'Construction was completed|Notice of completion|Complete Construction', window, re.IGNORECASE):
            status = 'completed'
        # if within window says under construction
        if re.search(r'currently under construction|Begin Construction', window, re.IGNORECASE) and status != 'completed':
            status = status or 'design'
        # if contains awaiting approval/finalize plans
        if re.search(r'awaiting|finalize|under review|submit', window, re.IGNORECASE) and status is None:
            status = 'design'
        status_map[pn] = status or 'unknown'

result = funding.copy()
result['Status'] = result['Project_Name'].map(status_map).fillna('unknown')
# topic for filter
result = result[result['Project_Name'].str.contains('FEMA|emergency', case=False, na=False) | result['Funding_Source'].str.contains('FEMA|emergency', case=False, na=False)]

result = result.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

answer_records = result[['Project_Name','Funding_Source','Amount','Status']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(answer_records))"""

env_args = {'var_call_b2Bz06VqrdCj545wV2lljVNl': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_RawYiRHR6GZwLqYYR6urtkPu': 'file_storage/call_RawYiRHR6GZwLqYYR6urtkPu.json'}

exec(code, env_args)
