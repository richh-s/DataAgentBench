code = """import json
import re

civic_file = open('/tmp/tmpyq7d3x4g.json', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

funding_file = open('/tmp/tmp8j8x8g9f.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

spring_2022_projects = set()

# First pass: find Spring 2022 mentions
for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    pos = 0
    while True:
        pos = lower_text.find('spring 2022', pos)
        if pos == -1:
            break
        # Get context before this mention
        start = max(0, pos - 500)
        context = text[start:pos]
        # Find project name in context
        sections = context.split('\n\n')
        for section in reversed(sections):
            lines = section.strip().split('\n')
            for line in reversed(lines):
                proj = line.strip()
                if proj and len(proj) > 10 and not proj.startswith('(') and 'Page' not in proj:
                    if 'Capital Improvement' not in proj and 'Project Schedule' not in proj:
                        if not proj.startswith('cid:') and 'Project Description' not in proj:
                            spring_2022_projects.add(proj)
                            break
        pos += 1

# Match with funding data
total_funding = 0
matched = 0

for project in spring_2022_projects:
    p_lower = project.lower()
    for f in funding_data:
        f_lower = f['Project_Name'].lower()
        if p_lower in f_lower or f_lower in p_lower:
            total_funding += int(f['Amount'])
            matched += 1
            break

result = {'spring_2022_count': len(spring_2022_projects), 'matched_with_funding': matched, 'total_funding': total_funding}
print('__RESULT__:');
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
