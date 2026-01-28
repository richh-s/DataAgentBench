code = """import json
import re

# Load data from previous tool calls available in storage
civic_docs_path = var_call_QMqljVvuhK67qBr9fNixxMoe
funding_records = var_call_6Bj66qSlAIifpECww67AhOpW

# Read the civic docs JSON file
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Keyword lists (lowercase)
completed_kw = [
    'construction was completed', 'was completed', 'notice of completion', 'complete construction', 'completed', 'notice of completion filed'
]
design_kw = [
    'complete design', 'final design', 'finalizing the design', 'finalizing plans', 'design plans', 'design phase', 'preliminary design', 'working with the consultant', 'submitted plans', 'staff is working with the consultant', 'finalizing plans and specifications'
]
not_started_kw = [
    'not started', 'identified but not begun', 'not begun', 'project was identified', 'waiting for the agreement', 'was identified in the'
]
under_construction_kw = [
    'project is currently under construction', 'begin construction', 'begin construction:', 'begin construction;', 'begin construction.'
]

results = []

for rec in funding_records:
    pname = rec.get('Project_Name')
    fs = rec.get('Funding_Source')
    amt = rec.get('Amount')

    # Normalize amount to int if possible
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = amt

    # Derive base name by stripping parenthetical suffixes and trailing descriptors like '- Design'
    base = re.sub('\s*[-–—]\s*design$', '', pname, flags=re.IGNORECASE)
    base = re.sub('\s*\(.*?\)\s*$', '', base).strip()
    base_lower = base.lower()

    status = 'unknown'
    matched = False

    # Search across all civic docs for the base name
    for doc in civic_docs:
        text = doc.get('text','')
        text_norm = re.sub('\s+', ' ', text).strip().lower()
        if base_lower in text_norm:
            matched = True
            # Determine status by checking keywords in the document (prefer more specific completed)
            if any(k in text_norm for k in completed_kw):
                status = 'completed'
            elif any(k in text_norm for k in not_started_kw):
                status = 'not started'
            elif any(k in text_norm for k in design_kw):
                status = 'design'
            elif any(k in text_norm for k in under_construction_kw):
                status = 'design'
            else:
                # As fallback, inspect nearby snippet around first occurrence
                idx = text_norm.find(base_lower)
                if idx != -1:
                    start = idx-200 if idx-200>0 else 0
                    end = idx+200 if idx+200<len(text_norm) else len(text_norm)
                    snippet = text_norm[start:end]
                    if any(k in snippet for k in completed_kw):
                        status = 'completed'
                    elif any(k in snippet for k in design_kw):
                        status = 'design'
                    elif any(k in snippet for k in not_started_kw):
                        status = 'not started'
                    elif any(k in snippet for k in under_construction_kw):
                        status = 'design'
                    else:
                        status = 'unknown'
            break

    if not matched:
        # try looser matching: check if significant tokens of base appear
        tokens = [t for t in re.split('\W+', base_lower) if len(t)>3]
        found_token = False
        for doc in civic_docs:
            text_norm = re.sub('\s+', ' ', doc.get('text','')).strip().lower()
            # require up to first 3 tokens to be present
            if tokens and all(token in text_norm for token in tokens[:3]):
                found_token = True
                if any(k in text_norm for k in completed_kw):
                    status = 'completed'
                elif any(k in text_norm for k in not_started_kw):
                    status = 'not started'
                elif any(k in text_norm for k in design_kw):
                    status = 'design'
                elif any(k in text_norm for k in under_construction_kw):
                    status = 'design'
                else:
                    status = 'unknown'
                break

    results.append({
        'Project_Name': pname,
        'Funding_Source': fs,
        'Amount': amt_int,
        'Status': status
    })

# Build a readable plain-text answer
lines = []
for r in results:
    lines.append('Project: {}'.format(r['Project_Name']))
    lines.append('  Funding Source: {}'.format(r['Funding_Source']))
    lines.append('  Amount: ${}'.format(r['Amount']))
    lines.append('  Status: {}'.format(r['Status']))
    lines.append('')
final_text = '\n'.join(lines).strip()

# Print per required format as a JSON string
print('__RESULT__:')
print(json.dumps(final_text))"""

env_args = {'var_call_o1BWtTd1tSx4vPqmWXNGZDBX': ['civic_docs'], 'var_call_QMqljVvuhK67qBr9fNixxMoe': 'file_storage/call_QMqljVvuhK67qBr9fNixxMoe.json', 'var_call_QGnkg9EbqJE14q5U5ShRskU0': ['Funding'], 'var_call_6Bj66qSlAIifpECww67AhOpW': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
