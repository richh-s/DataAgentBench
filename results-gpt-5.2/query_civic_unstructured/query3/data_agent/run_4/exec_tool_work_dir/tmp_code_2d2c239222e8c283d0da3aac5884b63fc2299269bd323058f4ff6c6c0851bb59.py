code = """import json, re
import pandas as pd

# Load mongo results (may be file path)
mongo_res = var_call_YjW8kGxRsKLgkxPBCzvdTWAA
if isinstance(mongo_res, str):
    with open(mongo_res, 'r', encoding='utf-8') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_res

funding = pd.DataFrame(var_call_JZMQhn9rtdSygn8wF7VdVrPY)
# normalize amount
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Extract project statuses from docs using simple heuristics
status_map = {}
for d in mongo_docs:
    text = d.get('text','')
    # sections
    # status = Design
    design_block = re.split(r'Capital Improvement Projects \(Design\)', text, flags=re.I)
    if len(design_block) > 1:
        after = design_block[1]
        end = re.split(r'Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects', after, flags=re.I)
        block = end[0]
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        for ln in lines:
            if re.search(r'\bproject\b|\bupdates\b|\bschedule\b|\bpage\b|\bagenda\b', ln, flags=re.I):
                continue
            if len(ln) > 3 and not ln.startswith('(') and not ln.endswith(':'):
                status_map.setdefault(ln, 'design')

    # status = Construction/Completed (treat as design? we map construction as design? user asked statuses; use 'design'/'completed'/'not started'. infer completed if contains 'completed')
    constr_block = re.split(r'Capital Improvement Projects \(Construction\)', text, flags=re.I)
    if len(constr_block) > 1:
        after = constr_block[1]
        end = re.split(r'Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects', after, flags=re.I)
        block = end[0]
        # identify project headings as lines without bullets
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        current = None
        for ln in lines:
            if re.search(r'\bupdates\b', ln, flags=re.I):
                continue
            if re.match(r'^[A-Za-z0-9].{3,}$', ln) and not ln.startswith('(cid') and ':' not in ln and 'Page' not in ln and 'Agenda' not in ln:
                # possible heading
                current = ln
                continue
            if current and re.search(r'completed', ln, flags=re.I):
                status_map[current] = 'completed'
            if current and re.search(r'currently under construction|begin construction|out to bid', ln, flags=re.I):
                # treat as design if not completed
                status_map.setdefault(current, 'design')

    # status = Not Started
    ns_block = re.split(r'Capital Improvement Projects \(Not Started\)', text, flags=re.I)
    if len(ns_block) > 1:
        after = ns_block[1]
        end = re.split(r'Disaster Recovery Projects', after, flags=re.I)
        block = end[0]
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        for ln in lines:
            if re.search(r'\bproject\b|\bdescription\b|\bupdates\b|\bschedule\b|\bpage\b|\bagenda\b', ln, flags=re.I):
                continue
            if len(ln) > 3 and ':' not in ln and not ln.startswith('(cid'):
                status_map.setdefault(ln, 'not started')

# Match statuses to funding project names by substring match ignoring parenthetical suffixes

def norm_name(s):
    s = re.sub(r'\s+', ' ', s.strip())
    s2 = re.sub(r'\s*\([^)]*\)\s*', '', s).strip()
    return s2.lower()

status_items = [(k, v, norm_name(k)) for k,v in status_map.items()]

statuses = []
for pn in funding['Project_Name']:
    base = norm_name(pn)
    st = None
    # exact base match
    for k,v,kn in status_items:
        if kn == base:
            st = v
            break
    if st is None:
        # substring match
        for k,v,kn in status_items:
            if base in kn or kn in base:
                st = v
                break
    statuses.append(st)

funding['Status'] = statuses

# Filter for emergency/FEMA related per question
mask = funding['Project_Name'].str.contains('emergency|fema', case=False, na=False) | funding['Funding_Source'].str.contains('emergency|fema', case=False, na=False)
res = funding.loc[mask, ['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source'])

result = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_JZMQhn9rtdSygn8wF7VdVrPY': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_YjW8kGxRsKLgkxPBCzvdTWAA': 'file_storage/call_YjW8kGxRsKLgkxPBCzvdTWAA.json'}

exec(code, env_args)
