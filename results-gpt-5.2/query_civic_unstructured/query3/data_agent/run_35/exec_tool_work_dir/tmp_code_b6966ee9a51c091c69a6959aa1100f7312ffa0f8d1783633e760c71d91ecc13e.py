code = """import json, re
import pandas as pd

# Load civic docs (may be file path)
path_or_obj = var_call_kbBa8KhrHzw9ZHOkPy4F2CoQ
if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
    with open(path_or_obj, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = path_or_obj

funding = var_call_2pcVG59e9uN8b2oQ5fCK1Uxa

# Build set of relevant project names from funding query
proj_names = sorted({r['Project_Name'] for r in funding})

# Extract status from civic docs by locating project name and nearby text
status_patterns = [
    (re.compile(r'\bcompleted\b', re.I), 'completed'),
    (re.compile(r'\bunder construction\b|\bcurrently under construction\b', re.I), 'construction'),
    (re.compile(r'\bnot started\b', re.I), 'not started'),
    (re.compile(r'\bdesign\b|\bfinal design\b|\bpreliminary design\b', re.I), 'design'),
]

def find_status_for_project(text, project):
    idx = text.lower().find(project.lower())
    if idx == -1:
        return None
    window = text[max(0, idx-250): idx+400]
    # prioritize explicit sections cues
    for pat, lab in status_patterns:
        if pat.search(window):
            # map construction to design/completed/not started? keep as construction if found
            return lab
    # Try infer from headings immediately before
    before = text[max(0, idx-1500):idx]
    m = re.search(r'Capital Improvement Projects \((Design|Construction|Not Started)\)', before, re.I)
    if m:
        val = m.group(1).lower()
        if val == 'construction':
            return 'construction'
        if val == 'design':
            return 'design'
        if val == 'not started':
            return 'not started'
    return None

# compile best status across docs
proj_status = {p: None for p in proj_names}
for doc in civic_docs:
    text = doc.get('text','')
    for p in proj_names:
        st = find_status_for_project(text, p)
        if st:
            # prefer completed over construction over design over not started
            order = {'completed':4,'construction':3,'design':2,'not started':1}
            cur = proj_status.get(p)
            if (cur is None) or (order.get(st,0) > order.get(cur,0)):
                proj_status[p]=st

# Assemble final rows
rows=[]
for r in funding:
    rows.append({
        'Project_Name': r['Project_Name'],
        'Funding_Source': r['Funding_Source'],
        'Amount': int(r['Amount']) if r['Amount'] is not None and str(r['Amount']).isdigit() else r['Amount'],
        'Status': proj_status.get(r['Project_Name'])
    })

# If multiple funding records per project, keep as separate lines (as asked)
df = pd.DataFrame(rows)
# Sort for readability
if not df.empty:
    df = df.sort_values(['Project_Name','Funding_Source'], kind='mergesort')

result = df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_SAobHOvFnLvXsDtT4fV8nVkM': ['Funding'], 'var_call_wZLz2gRm7c4IY5cqjQU63h1s': ['civic_docs'], 'var_call_2pcVG59e9uN8b2oQ5fCK1Uxa': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_kbBa8KhrHzw9ZHOkPy4F2CoQ': 'file_storage/call_kbBa8KhrHzw9ZHOkPy4F2CoQ.json'}

exec(code, env_args)
