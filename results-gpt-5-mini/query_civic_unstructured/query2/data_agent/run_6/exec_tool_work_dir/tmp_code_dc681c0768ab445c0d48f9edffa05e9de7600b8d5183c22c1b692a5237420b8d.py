code = """import json, re

civic_docs_path = var_call_r892hONIdSNhSOVoSwLtYDDb
funding_records = var_call_sy1V1coTcc1dbPbkKC4k3sSv

# Read file robustly, remove null bytes
with open(civic_docs_path, 'r', encoding='utf-8', errors='replace') as f:
    raw = f.read()
# remove any null characters
raw = raw.replace('\x00', '')

civic_docs = json.loads(raw)

completed_2022_parks = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    text_lower = text.lower()
    # find passages that indicate construction completed in 2022
    # look for lines with 'construction was completed' or 'completed' near park mentions
    for match in re.finditer(r'(?i)(?:construction was completed|construction was completed,|completed,|completed)\s*(?:,?\s*november|january|december|february|march|april|may|june|july|august|september|october)?\s*\d{0,4}', text_lower):
        span_start = match.start()
        # search backwards for the nearest line containing 'park' within 300 chars
        window_start = max(0, span_start - 500)
        window = text[window_start:span_start+200]
        if 'park' in window.lower():
            # extract possible project title by taking the nearest preceding non-empty line
            lines = window.splitlines()
            # iterate backwards to find line with 'park'
            for ln in reversed(lines):
                if 'park' in ln.lower():
                    title = ln.strip()
                    title = re.sub(r"\s+\(cid:\d+\)", '', title)
                    title = re.sub(r'[^\x00-\x7F]+', ' ', title)
                    title = title.strip(' -:\t')
                    if title:
                        completed_2022_parks.add(title)
                    break

# Also fallback: search for project headings like lines containing 'park' and then look ahead for 'completed' and '2022'
lines_all = []
for doc in civic_docs:
    lines_all.extend(doc.get('text','').splitlines())
for i, line in enumerate(lines_all):
    if 'park' in line.lower():
        # look ahead
        look = ' '.join(lines_all[i+1:i+12]).lower()
        if 'completed' in look and '2022' in look:
            title = re.sub(r"\s+\(cid:\d+\)", '', line).strip()
            title = re.sub(r'[^\x00-\x7F]+', ' ', title).strip(' -:\t')
            if title:
                completed_2022_parks.add(title)

completed_list = sorted(completed_2022_parks)

# Match funding records
matched_funding = []
for fr in funding_records:
    pname = fr.get('Project_Name', '')
    pname_l = pname.lower()
    for comp in completed_list:
        comp_l = comp.lower()
        comp_l_clean = re.sub(r"\s+updates:.*$", '', comp_l)
        if comp_l_clean in pname_l or pname_l in comp_l_clean:
            try:
                amt_int = int(fr.get('Amount') if fr.get('Amount') is not None else 0)
            except:
                amt_int = 0
            matched_funding.append({
                'Funding_ID': int(fr.get('Funding_ID')) if fr.get('Funding_ID') is not None else None,
                'Project_Name': fr.get('Project_Name'),
                'Funding_Source': fr.get('Funding_Source'),
                'Amount': amt_int
            })
            break

total = sum(r['Amount'] for r in matched_funding)

output = {
    'completed_2022_park_projects': completed_list,
    'matched_funding_records': matched_funding,
    'total_funding': total
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_sy1V1coTcc1dbPbkKC4k3sSv': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}], 'var_call_jYgQTTfjJYxhQRc6W9DPmgOy': [], 'var_call_Ixgpfr8RgziZMmYhLXToKoEa': ['civic_docs'], 'var_call_r892hONIdSNhSOVoSwLtYDDb': 'file_storage/call_r892hONIdSNhSOVoSwLtYDDb.json'}

exec(code, env_args)
