code = """import json, re

civic_path = var_call_DH1giSqKz0Pu46jMd2vreK5q
funding = var_call_sy1V1coTcc1dbPbkKC4k3sSv

with open(civic_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found = set()
for d in docs:
    text = d.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'park' in line.lower():
            look = ' '.join(lines[i:i+12]).lower()
            if 'completed' in look and '2022' in look:
                title = re.sub(r"\s*\(cid:\d+\)", '', line).strip()
                title = re.sub(r'[^\x00-\x7F]+', ' ', title).strip(' -:\t')
                if title:
                    found.add(title)

found_list = sorted(found)

matched = []
for rec in funding:
    pname = rec.get('Project_Name', '')
    pname_l = pname.lower()
    for ftitle in found_list:
        fl = ftitle.lower()
        if fl in pname_l or pname_l in fl:
            try:
                amt = int(rec.get('Amount') if rec.get('Amount') is not None else 0)
            except:
                amt = 0
            matched.append({'Funding_ID': int(rec.get('Funding_ID')) if rec.get('Funding_ID') is not None else None,
                            'Project_Name': rec.get('Project_Name'),
                            'Funding_Source': rec.get('Funding_Source'),
                            'Amount': amt})
            break

total = sum(r['Amount'] for r in matched)

output = {'completed_2022_park_projects': found_list, 'matched_funding_records': matched, 'total_funding': total}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_sy1V1coTcc1dbPbkKC4k3sSv': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}], 'var_call_jYgQTTfjJYxhQRc6W9DPmgOy': [], 'var_call_Ixgpfr8RgziZMmYhLXToKoEa': ['civic_docs'], 'var_call_r892hONIdSNhSOVoSwLtYDDb': 'file_storage/call_r892hONIdSNhSOVoSwLtYDDb.json', 'var_call_DH1giSqKz0Pu46jMd2vreK5q': 'file_storage/call_DH1giSqKz0Pu46jMd2vreK5q.json'}

exec(code, env_args)
