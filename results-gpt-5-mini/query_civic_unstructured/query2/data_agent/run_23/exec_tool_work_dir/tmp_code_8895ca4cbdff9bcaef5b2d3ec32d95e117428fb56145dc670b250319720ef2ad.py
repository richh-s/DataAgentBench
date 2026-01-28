code = """import json
import re
# Load funding records
funding_records = var_call_NamOwbygOgO52u2nyGSu5Xlo

# Load civic docs from file path
with open(var_call_u18siW6N5DiPkAf5w8RQGnu1, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize amounts
for fr in funding_records:
    try:
        fr['Amount'] = int(fr.get('Amount', 0))
    except:
        s = re.sub(r"[^0-9]", "", str(fr.get('Amount', '0')))
        fr['Amount'] = int(s) if s else 0

def completed_in_2022(pname, docs):
    pn = pname.lower()
    for doc in docs:
        text = doc.get('text', '')
        text_lower = text.lower()
        if pn in text_lower:
            start = 0
            while True:
                idx = text_lower.find(pn, start)
                if idx == -1:
                    break
                wstart = max(0, idx - 400)
                wend = min(len(text_lower), idx + len(pn) + 400)
                window = text_lower[wstart:wend]
                if '2022' in window and ("completed" in window or "complete construction" in window or "notice of completion" in window or "complete:" in window or "complete construction:" in window):
                    return True
                start = idx + 1
    return False

matched = []
for fr in funding_records:
    if completed_in_2022(fr['Project_Name'], civic_docs):
        matched.append(fr)

total = sum(x['Amount'] for x in matched)
result = {
    'total_funding': total,
    'currency': 'USD',
    'total_formatted': f"${total:,}",
    'num_records': len(matched),
    'funding_ids': [x['Funding_ID'] for x in matched],
    'matched_projects': [x['Project_Name'] for x in matched]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NamOwbygOgO52u2nyGSu5Xlo': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}], 'var_call_u0Pzf6H2nKCMiEZ3EfSvYKwz': ['civic_docs'], 'var_call_u18siW6N5DiPkAf5w8RQGnu1': 'file_storage/call_u18siW6N5DiPkAf5w8RQGnu1.json'}

exec(code, env_args)
