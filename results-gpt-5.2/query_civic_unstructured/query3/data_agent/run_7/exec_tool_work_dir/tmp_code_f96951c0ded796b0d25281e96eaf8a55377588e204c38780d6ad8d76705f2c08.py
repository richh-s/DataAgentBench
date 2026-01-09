code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_TaLoQJVYJvrcElu4upRHQ9py)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Load mongo docs (may be a filepath)
docs = var_call_vjJ6bgwabkzaJi8CISmR62Ui
if isinstance(docs, str) and docs.endswith('.json'):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

# Extract status lines for projects from docs
project_status = {}
# precompile patterns
status_patterns = [
    (re.compile(r"^\s*(?P<name>.+?)\s*\(?(?:FEMA|CalOES|CalJPIA)[^)]*\)?\s*$", re.I), None),
]
updates_re = re.compile(r"^\s*(?P<label>Updates)\s*:\s*(?P<rest>.*)$", re.I)
# If project title line then later line starting with 'Updates:' contains status.

def norm_name(n):
    n = re.sub(r"\s+", " ", n).strip()
    return n

for d in docs:
    text = d.get('text','')
    lines = text.splitlines()
    current_project = None
    for line in lines:
        l = line.strip()
        if not l:
            continue
        # Detect a likely project header: title-cased line with FEMA or emergency terms
        if re.search(r"\b(FEMA|CalOES|CalJPIA|Emergency|Warning)\b", l, re.I):
            # exclude generic headings
            if len(l) < 5 or len(l) > 120:
                pass
            else:
                # remove bullet artifacts
                l2 = re.sub(r"^[\(\)cid:0-9;\.\-\*\u2022\s]+", "", l).strip()
                # skip if it's a section header
                if re.search(r"Projects|Report|Commission|Meeting|Agenda|Subject|Prepared|Approved|Recommended", l2, re.I):
                    pass
                else:
                    current_project = norm_name(l2)
                    continue
        m = updates_re.match(l)
        if m and current_project:
            rest = m.group('rest').strip()
            # derive status
            status = None
            rlow = rest.lower()
            if 'completed' in rlow or 'construction was completed' in rlow or 'notice of completion' in rlow:
                status = 'completed'
            elif 'currently under construction' in rlow or 'begin construction' in rlow or 'out to bid' in rlow or 'construction' in rlow:
                # treat active as design unless explicitly construction; but output only known statuses
                status = 'design'
            elif 'working with' in rlow or 'finalize the design' in rlow or 'under review' in rlow or 'submitted plans' in rlow or 'awaiting' in rlow or 'preliminary design' in rlow:
                status = 'design'
            elif 'not started' in rlow:
                status = 'not started'
            # store first seen status
            if status:
                project_status.setdefault(current_project, status)
            current_project = None

# Join funding with status by best match: exact or startswith (handle slight name differences)

def find_status(pname):
    if pname in project_status:
        return project_status[pname]
    # try remove parenthetical suffixes
    base = re.sub(r"\s*\([^\)]*\)\s*$", "", pname).strip()
    if base in project_status:
        return project_status[base]
    # try contains match
    for k,v in project_status.items():
        if base.lower() == re.sub(r"\s*\([^\)]*\)\s*$", "", k).strip().lower():
            return v
    return None

funding['Status'] = funding['Project_Name'].apply(find_status)

# Filter to emergency/FEMA related (already) and order
out = funding.sort_values(['Project_Name','Funding_Source']).fillna({'Status':'unknown'})
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TaLoQJVYJvrcElu4upRHQ9py': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_vjJ6bgwabkzaJi8CISmR62Ui': 'file_storage/call_vjJ6bgwabkzaJi8CISmR62Ui.json'}

exec(code, env_args)
