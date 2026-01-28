code = """import json, re
# Load storage variables
civic_docs_path = var_call_Ab04Aj8UGYYXnQQMGznl3hZJ
funding_records = var_call_d61XIieKVm9zIvfY72CaqXgo

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Preprocess civic docs: lowercase text
for doc in civic_docs:
    doc['text_lower'] = doc.get('text','').lower()

results = []

# helper to find status near a match
def extract_status(text, start_idx):
    window = text[start_idx:start_idx+800]  # look ahead
    # search for strong indicators
    if re.search(r"completed|completion|notice of completion", window):
        return 'completed'
    if re.search(r"not started|not begun|identified but not begun", window):
        return 'not started'
    # design indicators
    if re.search(r"design|complete design|final design|preliminary design|design plans|design phase", window):
        return 'design'
    # construction indicators (map to design as ongoing/planned construction)
    if re.search(r"under construction|begin construction|construction was completed|begin construction|advertise:|advertise\b", window):
        # if explicitly completed caught above, else treat as design/ongoing
        return 'design'
    # awaiting approval or review - treat as design
    if re.search(r"awaiting|awaiting .*approval|awaiting final|pending", window):
        return 'design'
    return None

for fr in funding_records:
    proj_name = fr.get('Project_Name')
    funding_source = fr.get('Funding_Source')
    try:
        amount = int(fr.get('Amount'))
    except:
        try:
            amount = int(float(fr.get('Amount')))
        except:
            amount = fr.get('Amount')

    base_name = proj_name.split('(')[0].strip() if proj_name else ''
    base_lower = base_name.lower()
    status = None

    # Try direct exact base name match
    for doc in civic_docs:
        txt = doc['text_lower']
        idx = txt.find(base_lower)
        if idx != -1:
            st = extract_status(txt, idx)
            if st:
                status = st
                break
    # If not found, try flexible token matching: all tokens of base_name present in doc within 100 chars
    if not status and base_lower:
        tokens = [t for t in re.split(r"\W+", base_lower) if t]
        for doc in civic_docs:
            txt = doc['text_lower']
            # find first token match positions
            positions = [m.start() for t in tokens for m in re.finditer(re.escape(t), txt)]
            if not positions:
                continue
            # heuristic: check if tokens appear in order within 200 chars
            pattern = '.*?'.join([re.escape(t) for t in tokens[:6]])  # limit tokens for safety
            m = re.search(pattern, txt)
            if m:
                st = extract_status(txt, max(0, m.start()))
                if st:
                    status = st
                    break
    if not status:
        status = 'unknown'

    results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding_source,
        'Amount': amount,
        'Status': status
    })

# Print result as JSON string
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Ab04Aj8UGYYXnQQMGznl3hZJ': 'file_storage/call_Ab04Aj8UGYYXnQQMGznl3hZJ.json', 'var_call_d61XIieKVm9zIvfY72CaqXgo': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
