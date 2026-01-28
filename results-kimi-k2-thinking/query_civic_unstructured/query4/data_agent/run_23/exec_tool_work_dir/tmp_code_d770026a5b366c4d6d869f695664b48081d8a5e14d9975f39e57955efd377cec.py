code = """import json
import re

# Access data
civic_docs_file = locals()['var_functions.query_db:16']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Search for mentions of Spring 2022 in all documents
spring_2022_mentions = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check if this document mentions Spring 2022 in any context
    if '2022' in text and ('spring' in text or 'march' in text or 'april' in text or 'may' in text):
        # Find lines mentioning both 2022 and spring/months
        lines = text.split('\n')
        relevant_lines = []
        for line in lines:
            line_lower = line.lower()
            if '2022' in line_lower:
                if any(month in line_lower for month in ['spring', 'march', 'april', 'may']):
                    relevant_lines.append(line.strip())
        
        if relevant_lines:
            spring_2022_mentions.append({
                'doc_id': doc.get('_id'),
                'filename': doc.get('filename'),
                'mentions': relevant_lines[:5]  # First 5 mentions
            })

print('__RESULT__:')
print(json.dumps({
    'docs_with_2022_spring_refs': len(spring_2022_mentions),
    'sample_references': spring_2022_mentions[:3]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:22': {'civic_docs_count': 5, 'funding_count': 500, 'sample_civic_doc_filename': 'malibucity_agenda_03222023-2060.txt', 'total_funding_available': 28094000}}

exec(code, env_args)
