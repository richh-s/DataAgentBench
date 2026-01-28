code = """import json
import re
# Load funding records from previous query (var_call_NamOwbygOgO52u2nyGSu5Xlo)
funding_records = var_call_NamOwbygOgO52u2nyGSu5Xlo

# Load civic docs full result from JSON file path (var_call_u18siW6N5DiPkAf5w8RQGnu1)
with open(var_call_u18siW6N5DiPkAf5w8RQGnu1, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and prepare results
for fr in funding_records:
    # Convert Amount to int
    try:
        fr['Amount'] = int(fr['Amount'])
    except:
        # remove non-digit characters
        amt = re.sub(r"[^0-9]", "", fr.get('Amount', '0'))
        fr['Amount'] = int(amt) if amt else 0

# Function to detect if a project is completed in 2022 within civic docs
def is_completed_in_2022(project_name, docs):
    pn = project_name.lower()
    for doc in docs:
        text = doc.get('text', '')
        text_lower = text.lower()
        if pn in text_lower:
            # find all occurrences
            start = 0
            while True:
                idx = text_lower.find(pn, start)
                if idx == -1:
                    break
                # window around occurrence
                wstart = max(0, idx - 400)
                wend = min(len(text_lower), idx + len(pn) + 400)
                window = text_lower[wstart:wend]
                # look for completion indicators and year 2022
                if ('completed' in window or 'complete construction' in window or 'complete construction:' in window or 'complete construction' in window or 'complete:' in window) and '2022' in window:
                    return True
                # also check lines following the occurrence up to 3 lines
                following = '\n'.join(text_lower[idx:idx+1000].splitlines()[:3])
                if ('completed' in following or 'complete construction' in following or 'complete:' in following) and '2022' in following:
                    return True
                start = idx + 1
    return False

# Identify funding records whose project was completed in 2022
completed_ids = []
completed_records = []
for fr in funding_records:
    pname = fr['Project_Name']
    if is_completed_in_2022(pname, civic_docs):
        completed_ids.append(fr['Funding_ID'])
        completed_records.append(fr)

# Sum amounts
total = sum(r['Amount'] for r in completed_records)

# Prepare result dict
result = {
    'total_funding': total,
    'currency': 'USD',
    'total_formatted': f"${total:,}",
    'num_records': len(completed_records),
    'funding_ids': completed_ids,
    'matched_projects': [r['Project_Name'] for r in completed_records]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NamOwbygOgO52u2nyGSu5Xlo': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}], 'var_call_u0Pzf6H2nKCMiEZ3EfSvYKwz': ['civic_docs'], 'var_call_u18siW6N5DiPkAf5w8RQGnu1': 'file_storage/call_u18siW6N5DiPkAf5w8RQGnu1.json'}

exec(code, env_args)
