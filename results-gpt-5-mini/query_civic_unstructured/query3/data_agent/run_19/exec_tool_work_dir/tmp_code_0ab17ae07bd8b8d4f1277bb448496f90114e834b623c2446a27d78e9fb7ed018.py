code = """import json, re

civic_var = var_call_BAS2RGfY0bj1Wd8QeyPkbyl7
funding_var = var_call_diHd1eOfOdEqcQSpMdCe0Vwl

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

civic_docs = load_var(civic_var)
funding_records = load_var(funding_var)

# normalize funding amounts
for fr in funding_records:
    fr['Amount'] = int(fr.get('Amount') or 0)

results = []

for fr in funding_records:
    name = fr['Project_Name']
    core = re.sub(r"\s*\(.*?\)", "", name).strip()
    core_low = core.lower()
    matched = False
    snippets = []
    for doc in civic_docs:
        text = doc.get('text','')
        text_low = text.lower()
        # try exact core name
        idx = text_low.find(core_low)
        if idx == -1:
            # try requiring all tokens longer than 3 to be present
            tokens = [t for t in re.split(r"\W+", core_low) if len(t)>3]
            if tokens and all(t in text_low for t in tokens):
                # find first occurrence of any token sequence
                # find earliest index of any token
                idxs = [text_low.find(t) for t in tokens]
                idx = min([i for i in idxs if i>=0]) if any(i>=0 for i in idxs) else -1
        if idx != -1:
            matched = True
            # extract surrounding snippet: 300 chars before and after
            start = max(0, idx-300)
            end = min(len(text), idx+len(core)+300)
            snippet = text[start:end]
            # simplify whitespace
            snippet = re.sub(r"\s+", ' ', snippet).strip()
            snippets.append({'filename': doc.get('filename'), 'snippet': snippet})
    # infer status from snippets
    status = None
    status_phrases = []
    status_keywords = [
        r'complete construction', r'begin construction', r'complete design', r'advertise', r'under construction',
        r'awaiting', r'awaiting final', r'in the preliminary design', r'project is currently', r'project is delayed', r'final design',
        r'project schedule', r'updates:', r'not started', r'preliminary design'
    ]
    for s in snippets:
        s_low = s['snippet'].lower()
        for kw in status_keywords:
            m = re.search(kw, s_low)
            if m:
                # get sentence containing match
                # find nearest sentence boundaries
                start = s_low.rfind('.', 0, m.start())
                end = s_low.find('.', m.end())
                sent = s['snippet'][ (start+1 if start!=-1 else 0) : (end if end!=-1 else None) ].strip()
                status_phrases.append(sent)
        # fallback: if no keywords, take short snippet as context
        if not status_phrases:
            status_phrases.append(s['snippet'][:300])
    if not snippets:
        status_phrases = ['No matching project text found in civic documents.']
    results.append({
        'Project_Name': name,
        'Funding_Source': fr.get('Funding_Source'),
        'Amount': fr.get('Amount'),
        'Status_Snippets': status_phrases
    })

# Only include projects that are clearly related to FEMA or emergency (we already filtered funding for FEMA or Outdoor Warning)
# Prepare output
out = results
print("__RESULT__:")
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_BAS2RGfY0bj1Wd8QeyPkbyl7': 'file_storage/call_BAS2RGfY0bj1Wd8QeyPkbyl7.json', 'var_call_KYYyJ3WPdtaRwmCRGz8qjTEz': 'file_storage/call_KYYyJ3WPdtaRwmCRGz8qjTEz.json', 'var_call_JeGir6xl4TQOThEgVpw1bjge': [], 'var_call_diHd1eOfOdEqcQSpMdCe0Vwl': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
