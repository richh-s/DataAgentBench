code = """import json, re, pandas as pd

# Load variables from tool storage
civic_docs_path = var_call_r892hONIdSNhSOVoSwLtYDDb  # file path to large civic_docs query result
funding_records = var_call_sy1V1coTcc1dbPbkKC4k3sSv  # list of funding records (park-related)

# Read civic docs JSON file
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

completed_2022_parks = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Split into lines for heuristic parsing
    lines = text.splitlines()
    for i, line in enumerate(lines):
        l = line.strip()
        if not l:
            continue
        # Consider lines that look like project titles containing 'park'
        if 'park' in l.lower() and len(l) < 150:
            # Look ahead few lines for 'completed' and '2022'
            look_ahead = ' '.join(lines[i+1:i+12]).lower()
            if 'completed' in look_ahead and '2022' in look_ahead:
                # Clean up title: remove trailing punctuation
                title = re.sub(r"\s+\(cid:.*$", "", l)  # remove (cid: markers
                title = title.strip(' -:\t')
                completed_2022_parks.add(title)

# Additionally, search for patterns where the project title and 'Construction was completed' are separated
# Sometimes the project title might be followed by '\n\n(cid:190) Updates:' before the 'Construction was completed' mention
# The above lookahead should catch those.

completed_list = sorted(completed_2022_parks)

# Now match funding records. Use substring matching (case-insensitive)
matched_funding = []
for fr in funding_records:
    pname = fr.get('Project_Name', '').lower()
    for comp in completed_list:
        comp_l = comp.lower()
        if comp_l in pname or pname in comp_l:
            matched_funding.append({
                'Funding_ID': int(fr.get('Funding_ID')) if fr.get('Funding_ID') is not None else None,
                'Project_Name': fr.get('Project_Name'),
                'Funding_Source': fr.get('Funding_Source'),
                'Amount': int(fr.get('Amount')) if fr.get('Amount') not in (None, '') else 0
            })
            break

# Compute total
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
