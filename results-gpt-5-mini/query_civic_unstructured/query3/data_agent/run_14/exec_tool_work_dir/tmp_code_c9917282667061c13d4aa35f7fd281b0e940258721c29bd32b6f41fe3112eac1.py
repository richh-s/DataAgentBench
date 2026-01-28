code = """import json, re
# Access variables from storage
funding_records = var_call_aEkzOpEyor4Kyk0YTbyY3zlx
# civic docs file path
docs_path = var_call_9wQ7vn4CR1fSbTxXKjr8pRsi
with open(docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Helper to normalize text
def find_status_in_snippet(snippet):
    s = snippet.lower()
    # prioritize completed
    if 'construction was completed' in s or 'complete construction' in s or 'notice of completion' in s or 'completed,' in s:
        return 'completed'
    if 'project is currently under construction' in s or 'begin construction' in s or 'begin construction:' in s or 'begin construction' in s:
        return 'design'
    if 'complete design' in s or 'final design' in s or 'preliminary design' in s or 'design plans' in s or 'working with the consultant' in s or 'plans and specifications' in s:
        return 'design'
    if 'not started' in s or 'identified' in s or 'waiting for the agreement' in s or 'waiting for' in s or 'rejected all bids' in s or 'will be discussed' in s:
        return 'not started'
    # fallback: look for 'advertise' or 'schedule' as not started/design
    if 'advertise' in s or 'estimated schedule' in s or 'project schedule' in s or 'updates:' in s:
        return 'design'
    return None

results = []
for fr in funding_records:
    pname = fr.get('Project_Name')
    fund = fr.get('Funding_Source')
    amt = fr.get('Amount')
    # convert amount to int if possible
    try:
        amt_val = int(amt)
    except:
        try:
            amt_val = int(float(amt))
        except:
            amt_val = None

    # create base name without parenthetical suffix
    base = re.split(r'\s*\(', pname)[0].strip()

    found = False
    status = None
    for doc in civic_docs:
        text = doc.get('text','')
        # do case-insensitive search for full project name or base name
        if re.search(re.escape(pname), text, re.I) or re.search(re.escape(base), text, re.I):
            found = True
            # find all occurrences of base or full name
            m = re.search(re.escape(pname), text, re.I)
            if not m:
                m = re.search(re.escape(base), text, re.I)
            if m:
                start = max(0, m.start()-400)
                end = min(len(text), m.end()+400)
                snippet = text[start:end]
                st = find_status_in_snippet(snippet)
                if st:
                    status = st
                    break
    if not found:
        # try search for keywords 'FEMA' or 'emergency' near base in docs
        for doc in civic_docs:
            text = doc.get('text','')
            if re.search(re.escape(base), text, re.I):
                # even if not full match earlier
                m = re.search(re.escape(base), text, re.I)
                start = max(0, m.start()-400)
                end = min(len(text), m.end()+400)
                snippet = text[start:end]
                st = find_status_in_snippet(snippet)
                if st:
                    status = st
                    found = True
                    break
    if not status:
        status = 'unknown'

    results.append({
        'Project_Name': pname,
        'Funding_Source': fund,
        'Amount': amt_val,
        'Status': status
    })

# Deduplicate by Project_Name keeping first occurrence
seen = set()
final = []
for r in results:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name'])
        final.append(r)

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_9wQ7vn4CR1fSbTxXKjr8pRsi': 'file_storage/call_9wQ7vn4CR1fSbTxXKjr8pRsi.json', 'var_call_FRQjwA6Kvi6yX9yyqmJVWN6S': [], 'var_call_McnlZwIrCVzXzekDzS6hNTG6': ['Funding'], 'var_call_pM5XQR3I7ph2hkabPGYDDNQv': 'file_storage/call_pM5XQR3I7ph2hkabPGYDDNQv.json', 'var_call_aEkzOpEyor4Kyk0YTbyY3zlx': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
