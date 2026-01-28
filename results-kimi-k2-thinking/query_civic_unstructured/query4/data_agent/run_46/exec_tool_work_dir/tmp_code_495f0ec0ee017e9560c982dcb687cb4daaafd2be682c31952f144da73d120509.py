code = """import json

civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding = json.load(f)

# Debug: Print document structure info
doc_count = len(civic_docs)
funding_count = len(funding)

# Quick content analysis - check for Spring 2022 mentions
spring_mentions = 0
project_names = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if '2022' in text and ('spring' in text or 'mar' in text or 'apr' in text or 'may' in text):
        spring_mentions += 1
        
        # Extract potential project names from text
        # Look for uppercase titles/headings that don't start with bullets
        lines = doc.get('text', '').split('\n')
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            if (line_stripped and line_stripped[0].isupper() and 
                not line_stripped.startswith('cid:') and 
                not line_stripped.startswith('TO:') and
                10 < len(line_stripped) < 150 and
                'agenda' not in line_stripped.lower() and
                'report' not in line_stripped.lower()):
                project_names.append(line_stripped)

# Remove obvious non-project entries
filtered_names = [name for name in project_names if not any(x in name.lower() for x in ['public works', 'commission meeting', 'capital improvement projects', 'not started', 'construction', 'design'])]
unique_names = list(dict.fromkeys(filtered_names))[:20]

result = {
    'doc_count': doc_count,
    'funding_count': funding_count,
    'spring_mentions': spring_mentions,
    'sample_project_names': unique_names,
    'first_doc_preview': civic_docs[0].get('text', '')[:500]
}

print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
