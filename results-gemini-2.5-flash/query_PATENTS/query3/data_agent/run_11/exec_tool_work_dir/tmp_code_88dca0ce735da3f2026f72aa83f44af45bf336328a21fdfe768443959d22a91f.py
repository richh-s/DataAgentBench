code = """import json
import re

with open(locals()['var_function-call-7476042936698487296'], 'r') as f:
    publication_data = json.load(f)

univ_california_publication_numbers = set()
citing_patents_info = []

for record in publication_data:
    # Extract assignee_harmonized and publication_number for current patent
    patent_info_str = record['Patents_info']
    assignee_match = re.search(r'^(.*?)(?: holds the US patent application| is the assignee)', patent_info_str)
    current_assignee = assignee_match.group(1).strip() if assignee_match else "UNKNOWN"

    pub_number_match = re.search(r'publication number ([A-Z0-9-]+)', patent_info_str)
    current_publication_number = pub_number_match.group(1).strip() if pub_number_match else None

    # Step 1: Identify patents assigned to "UNIV CALIFORNIA"
    if "UNIV CALIFORNIA" in current_assignee.upper() and current_publication_number:
        univ_california_publication_numbers.add(current_publication_number)

    # Step 2: Find patents that cite "UNIV CALIFORNIA" patents
    citations = json.loads(record['citation']) if record['citation'] else []
    
    # Check if this patent cites any UNIV CALIFORNIA patent
    cites_univ_california = False
    for citation in citations:
        if citation.get('publication_number') in univ_california_publication_numbers:
            cites_univ_california = True
            break
    
    if cites_univ_california and "UNIV CALIFORNIA" not in current_assignee.upper():
        primary_cpc = None
        cpc_codes = json.loads(record['cpc']) if record['cpc'] else []
        for cpc_entry in cpc_codes:
            if cpc_entry.get('first'):
                primary_cpc = cpc_entry.get('code')
                break
        
        if primary_cpc:
            citing_patents_info.append({
                "citing_assignee": current_assignee,
                "primary_cpc_subclass": primary_cpc
            })

result = json.dumps(citing_patents_info)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-7476042936698487296': 'file_storage/function-call-7476042936698487296.json'}

exec(code, env_args)
