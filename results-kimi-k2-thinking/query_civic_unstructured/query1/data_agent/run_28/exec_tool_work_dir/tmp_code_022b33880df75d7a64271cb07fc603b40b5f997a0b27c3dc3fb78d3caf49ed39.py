code = """import json
import re

funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8']

funding = json.load(open(funding_path))
docs = json.load(open(civic_docs_path))

def extract_projects(docs):
    projects = []
    for doc in docs:
        txt = doc['text']
        pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects \(|$)'
        m = re.search(pattern, txt, re.DOTALL)
        if m:
            section = m.group(1)
            for line in section.splitlines():
                line = line.strip()
                # Filter for likely project names
                if (line and len(line) > 10 and not line.startswith(('(', 'cid', '•', '-', 'Page', 'Agenda')) 
                    and not line.endswith(':') and not any(x in line for x in ['Updates:', 'Schedule:', 'Complete Design', 'Advertise:'])):
                    # Check if it looks like a project name (contains capitalized words, project/improvement terms)
                    proj_terms = ['Project', 'Improvement', 'Repair', 'Road', 'Park', 'Drain', 'Bridge', 'Walkway', 'Study', 'Infrastructure']
                    has_proj_term = any(term in line for term in proj_terms)
                    has_capitalized = sum(1 for word in line.split() if word and word[0].isupper()) >= 2
                    
                    if has_proj_term or has_capitalized:
                        clean = re.sub(r'\s*-\s*', '', line)
                        clean = re.sub(r'\(.*?\)$', '', clean).strip()
                        clean = re.sub(r'^\d+\.\s*', '', clean)
                        if clean and len(clean) < 150:  # Reasonable length
                            projects.append({'Project_Name': clean, 'status': 'design', 'type': 'capital'})
    return projects

extracted = extract_projects(docs)
unique = list({p['Project_Name']: p for p in extracted}.values())

# Match with funding > $50,000
large_funding = [f for f in funding if int(f['Amount']) > 50000]
funding_names = {f['Project_Name'].lower().strip() for f in large_funding}

# Check which design projects have funding > $50k
design_with_funding = []
for proj in unique:
    proj_name = proj['Project_Name'].lower().strip()
    # Direct match
    if proj_name in funding_names:
        design_with_funding.append(proj)
    else:
        # Try fuzzy matching - check if project name is contained in any funding name
        for fund_name in funding_names:
            if proj_name in fund_name or fund_name in proj_name:
                design_with_funding.append(proj)
                break

print('__RESULT__:')
print(json.dumps({
    'design_projects': len(unique),
    'large_funding_projects': len(funding_names),
    'design_with_large_funding': len(design_with_funding),
    'matching_projects': design_with_funding[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:32': {'funding_count': 276, 'civic_docs_count': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.execute_python:42': {'extracted_count': 211, 'unique_count': 137, 'sample': [{'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'status': 'design', 'type': 'capital'}, {'Project_Name': 'project and will submit to the County for review.', 'status': 'design', 'type': 'capital'}, {'Project_Name': 'PCH Median Improvements Project', 'status': 'design', 'type': 'capital'}, {'Project_Name': 'and rejected all bids due to a budget shortfall', 'status': 'design', 'type': 'capital'}, {'Project_Name': 'or phasing out the project', 'status': 'design', 'type': 'capital'}, {'Project_Name': 'Page 1 of 6', 'status': 'design', 'type': 'capital'}, {'Project_Name': 'Agenda Item # 4.B.', 'status': 'design', 'type': 'capital'}, {'Project_Name': 'Westward Beach Road Repair Project', 'status': 'design', 'type': 'capital'}]}}

exec(code, env_args)
