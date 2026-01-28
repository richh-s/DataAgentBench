code = """import json
import re

funding = var_call_vdX59qe1pTla9sl0WesBpRST
civic_docs_path = var_call_rHRczMIJPO629lmxlTRznRDK

# Load civic docs full result from file path
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Helper to normalize and extract core name
def core_name(name):
    # remove parenthetical suffixes
    return re.sub(r"\s*\(.*?\)", "", name).strip()

# Helper to find best matching doc and extract status
status_keywords = {
    'completed': [r'construction was completed', r'complete construction', r'notice of completion', r'completed'],
    'design': [r'complete design', r'final design', r'preliminary design', r'design'],
    'not started': [r'not started', r'not yet started', r'identifi?ed but not begun']
}

results = []

for rec in funding:
    proj = rec.get('Project_Name')
    funding_source = rec.get('Funding_Source')
    try:
        amount = int(rec.get('Amount'))
    except:
        # try to clean
        try:
            amount = int(str(rec.get('Amount')).replace(',', ''))
        except:
            amount = None

    core = core_name(proj)
    core_lower = core.lower()
    tokens = [t.lower() for t in re.split(r'[^A-Za-z0-9]+', core) if len(t) > 3]

    matched = False
    extracted_status = None

    # Search each document for the best occurrence
    for doc in civic_docs:
        text = doc.get('text', '')
        text_lower = text.lower()
        idx = text_lower.find(core_lower)
        if idx == -1:
            # try token-based fuzzy match: count token hits
            hits = sum(1 for tk in tokens if tk in text_lower)
            if hits >= max(1, len(tokens)//2):
                # approximate match
                idx = text_lower.find(tokens[0]) if tokens else -1
        if idx != -1 and idx != -1:
            matched = True
            # get line window
            lines = text.splitlines()
            # find line containing the first token or core
            line_idx = None
            for i, line in enumerate(lines):
                if core_lower in line.lower() or any(tk in line.lower() for tk in tokens):
                    line_idx = i
                    break
            if line_idx is None:
                # fallback: use position to estimate line
                char_count = 0
                for i, line in enumerate(lines):
                    char_count += len(line) + 1
                    if char_count > idx:
                        line_idx = i
                        break
            start = max(0, line_idx - 4) if line_idx is not None else 0
            end = min(len(lines), (line_idx + 5) if line_idx is not None else 10)
            window = "\n".join(lines[start:end]).lower()
            # search for status keywords in window
            found = False
            for st, patterns in status_keywords.items():
                for pat in patterns:
                    if re.search(pat, window):
                        extracted_status = st
                        found = True
                        break
                if found:
                    break
            if not found:
                # look for 'under construction' specifically
                if 'under construction' in window:
                    extracted_status = 'under construction'
                else:
                    # look for 'advertise' and 'begin construction' to infer design
                    if 'complete design' in window or 'advertise' in window or 'begin construction' in window or 'final design' in window:
                        extracted_status = 'design'
                    else:
                        extracted_status = None
            break

    results.append({
        'Project_Name': proj,
        'Funding_Source': funding_source,
        'Amount': amount,
        'Status': extracted_status
    })

# Keep only projects related to 'fema' or 'emergency' -- funding query already filtered, but double-check
final = [r for r in results if ('fema' in (r['Project_Name'] or '').lower()) or ('emergency' in (r['Project_Name'] or '').lower()) or ('fema' in (r['Funding_Source'] or '').lower()) or ('emergency' in (r['Funding_Source'] or '').lower())]

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_vdX59qe1pTla9sl0WesBpRST': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_rHRczMIJPO629lmxlTRznRDK': 'file_storage/call_rHRczMIJPO629lmxlTRznRDK.json'}

exec(code, env_args)
