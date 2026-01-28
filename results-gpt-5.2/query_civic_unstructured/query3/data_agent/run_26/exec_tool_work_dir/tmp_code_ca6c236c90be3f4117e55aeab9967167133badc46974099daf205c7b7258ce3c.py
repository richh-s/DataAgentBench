code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_ssTZ4kECu1KiB6SNeq5weJz7)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Load civic docs (may be in file)
docs_obj = var_call_4pjcEAk912jD9q8JOpSW8lOR
if isinstance(docs_obj, str) and docs_obj.endswith('.json'):
    with open(docs_obj, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_obj

# Build a big text corpus for status inference
corpus = []
for d in docs:
    corpus.append({'filename': d.get('filename'), 'text': d.get('text','')})

# function to infer status by locating project name in text and nearby context
status_patterns = [
    ('design', re.compile(r'\b(Design|Final Design|Complete Design|preliminary design)\b', re.I)),
    ('completed', re.compile(r'\b(Construction was completed|completed|Notice of completion filed|Complete Construction)\b', re.I)),
    ('not started', re.compile(r'\b(Not Started|identified|preliminary design phase)\b', re.I)),
    ('construction', re.compile(r'\b(under construction|currently under construction|Begin construction)\b', re.I)),
]

def infer_status(project_name):
    pn = re.escape(project_name)
    for doc in corpus:
        text = doc['text']
        m = re.search(pn, text, flags=re.I)
        if not m:
            # try match without parenthetical suffixes
            base = re.sub(r'\s*\([^\)]*\)\s*$', '', project_name).strip()
            if base and base != project_name:
                m = re.search(re.escape(base), text, flags=re.I)
        if m:
            start = max(0, m.start()-800)
            end = min(len(text), m.end()+800)
            ctx = text[start:end]
            # Also consider headings like "Capital Improvement Projects (Design)" nearby
            # If heading present in ctx, use it
            if re.search(r'Capital Improvement Projects\s*\(Design\)', ctx, re.I) or re.search(r'Disaster Recovery Projects\s*\(Design\)', ctx, re.I):
                return 'design'
            if re.search(r'Capital Improvement Projects\s*\(Construction\)', ctx, re.I):
                return 'construction'
            if re.search(r'Capital Improvement Projects\s*\(Not Started\)', ctx, re.I):
                return 'not started'
            for label, pat in status_patterns:
                if pat.search(ctx):
                    # map construction to design/completed/not started? keep construction as-is
                    if label == 'construction':
                        return 'design/active construction'
                    return label
            return None
    return None

funding['Status'] = funding['Project_Name'].apply(infer_status)
funding['Status'] = funding['Status'].fillna('unknown')

# aggregate by project+source+status (keep as listed; amounts may have duplicates)
out = funding.sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ssTZ4kECu1KiB6SNeq5weJz7': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_4pjcEAk912jD9q8JOpSW8lOR': 'file_storage/call_4pjcEAk912jD9q8JOpSW8lOR.json'}

exec(code, env_args)
