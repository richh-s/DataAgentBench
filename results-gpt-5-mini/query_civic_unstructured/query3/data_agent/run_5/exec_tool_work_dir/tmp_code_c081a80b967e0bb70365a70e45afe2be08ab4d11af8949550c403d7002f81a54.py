code = """import json, re
import pandas as pd

# Load funding records (available as var_call_jTsXQw1bOdBZwMfCZjRo1wZs)
funding = var_call_jTsXQw1bOdBZwMfCZjRo1wZs

# Load civic docs from JSON file path stored in var_call_ruDa8GVl5sjqpyoXNReBhgpD
with open(var_call_ruDa8GVl5sjqpyoXNReBhgpD, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Helper functions

def base_name(name):
    # remove parenthetical suffixes like (FEMA Project)
    return re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()

# Status detection
completed_kw = [
    'construction was completed', 'complete construction', 'complete construction:', 'completed', 'notice of completion', 'notice of completion filed'
]
design_kw = [
    'complete design', 'final design', 'preliminary design', 'design plans', 'design phase', 'design', 'preliminary design phase'
]
not_started_kw = [
    'not started', 'not started)', 'not started.'
]
under_const_kw = [
    'under construction', 'currently under construction', 'begin construction', 'begin construction:'
]

# Topic keywords
topic_keywords = ['fema', 'emergency', 'sirens', 'outdoor warning', 'guardrail', 'storm drain', 'drainage', 'road', 'bridge', 'park', 'fire', 'culvert', 'retaining wall', 'latigo', 'corral', 'encinal', 'clover']

results = []

for rec in funding:
    pname = rec.get('Project_Name')
    pbase = base_name(pname)
    pbase_low = pbase.lower()
    found = False
    inferred_status = 'unknown'
    found_topics = set()
    # Search docs for the base project name or key tokens
    for d in docs:
        text = d.get('text', '')
        text_low = text.lower()
        if pbase_low and pbase_low in text_low:
            found = True
            # get context around first occurrence
            idx = text_low.index(pbase_low)
            start = max(0, idx-200)
            end = min(len(text_low), idx+200)
            context = text_low[start:end]
            # detect status with priority
            if any(k in context for k in completed_kw) or any(k in text_low for k in completed_kw):
                inferred_status = 'completed'
            elif any(k in context for k in not_started_kw) or any(k in text_low for k in not_started_kw):
                inferred_status = 'not started'
            elif any(k in context for k in design_kw) or any(k in text_low for k in design_kw) or any(k in context for k in under_const_kw):
                # map under construction to design per allowed statuses
                inferred_status = 'design'
            # topics
            for tk in topic_keywords:
                if tk in context or tk in text_low:
                    found_topics.add(tk)
            break
    # If not found by base name, attempt fuzzy token match (first 3 words)
    if not found:
        tokens = re.findall(r"[A-Za-z0-9]+", pbase_low)
        if len(tokens) >= 3:
            key = ' '.join(tokens[:3])
            for d in docs:
                text_low = d.get('text','').lower()
                if key in text_low:
                    found = True
                    context = text_low[text_low.index(key)-200:text_low.index(key)+200]
                    if any(k in context for k in completed_kw) or any(k in text_low for k in completed_kw):
                        inferred_status = 'completed'
                    elif any(k in context for k in not_started_kw) or any(k in text_low for k in not_started_kw):
                        inferred_status = 'not started'
                    elif any(k in context for k in design_kw) or any(k in text_low for k in design_kw) or any(k in context for k in under_const_kw):
                        inferred_status = 'design'
                    for tk in topic_keywords:
                        if tk in context or tk in text_low:
                            found_topics.add(tk)
                    break

    # If still not found, leave status unknown but attempt topic detection across all docs
    if not found:
        for d in docs:
            tl = d.get('text','').lower()
            if any(tk in tl for tk in topic_keywords):
                for tk in topic_keywords:
                    if tk in tl:
                        found_topics.add(tk)
    # Prepare result record
    try:
        amount = int(rec.get('Amount'))
    except:
        try:
            amount = int(float(rec.get('Amount')))
        except:
            amount = rec.get('Amount')
    results.append({
        'Project_Name': pname,
        'Funding_Source': rec.get('Funding_Source'),
        'Amount': amount,
        'Status': inferred_status,
        'Topics': sorted(list(found_topics))
    })

# Output JSON string
out = json.dumps(results)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ruDa8GVl5sjqpyoXNReBhgpD': 'file_storage/call_ruDa8GVl5sjqpyoXNReBhgpD.json', 'var_call_jTsXQw1bOdBZwMfCZjRo1wZs': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
