code = """import pandas as pd
import re
import json
with open(var_call_yKwxD3BzqBIdp2DoNjV7uBjL, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
funding_records = var_call_5TdYcEy68NdBahVf6yGc16Me
projects_2022 = set()
pattern_completed = re.compile(r'(completed|accepted as complete|project.* complete)', re.IGNORECASE)
pattern_year = re.compile(r'2022')
park_keywords = ['park']
for doc in civic_docs:
    text = doc.get('text', '')
    for segment in text.split('\n\n'):
        if any(pk in segment.lower() for pk in park_keywords):
            if pattern_completed.search(segment):
                if pattern_year.search(segment):
                    m = re.search(r'(?:Project Name:|Project:|Project Description:)\s*([A-Za-z0-9\- ,]+)', segment)
                    if m:
                        name = m.group(1).strip()
                        projects_2022.add(name)
                    else:
                        m2 = re.search(r'([A-Z][a-zA-Z0-9\- \/]+Park[a-zA-Z0-9\- ]*)', segment)
                        if m2:
                            name = m2.group(1).strip()
                            projects_2022.add(name)
funding_total = 0
matched_projects = set()
for record in funding_records:
    fname = record['Project_Name']
    if any(pn.lower() in fname.lower() or fname.lower() in pn.lower() for pn in projects_2022):
        try:
            amt = int(record['Amount'])
            funding_total += amt
            matched_projects.add(fname)
        except:
            continue
result_json = {
    'total_funding': funding_total,
    'matched_projects': list(matched_projects),
    'completed_parks_2022': list(projects_2022)
}
print('__RESULT__:')
print(json.dumps(result_json))"""

env_args = {'var_call_yKwxD3BzqBIdp2DoNjV7uBjL': 'file_storage/call_yKwxD3BzqBIdp2DoNjV7uBjL.json', 'var_call_5TdYcEy68NdBahVf6yGc16Me': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}]}

exec(code, env_args)
