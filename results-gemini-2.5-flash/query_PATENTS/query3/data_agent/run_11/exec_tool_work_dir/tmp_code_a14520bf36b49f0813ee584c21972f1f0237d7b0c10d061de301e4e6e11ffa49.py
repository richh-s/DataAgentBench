code = """import json
import re

with open(locals()['var_function-call-7476042936698487296'], 'r') as f:
    publication_data = json.load(f)

# Step 1: Create a mapping of publication_number to assignee and identify UNIV CALIFORNIA patents
publication_to_assignee = {}
univ_california_publication_numbers = set()

for record in publication_data:
    patent_info_str = record['Patents_info']
    
    # Extract assignee - more robustly
    assignee_match = re.match(r'^(.*?)(?: holds the US patent application| is the assignee| - US Patent)', patent_info_str)
    current_assignee = assignee_match.group(1).strip() if assignee_match else "UNKNOWN"

    # Extract publication number
    pub_number_match = re.search(r'publication number ([A-Z0-9-]+)', patent_info_str)
    current_publication_number = pub_number_match.group(1).strip() if pub_number_match else None

    if current_publication_number:
        publication_to_assignee[current_publication_number] = current_assignee
        if "UNIV CALIFORNIA" in current_assignee.upper() or "UNIVERSITY OF CALIFORNIA" in current_assignee.upper():
            univ_california_publication_numbers.add(current_publication_number)

# Step 2: Find patents that cite UNIV CALIFORNIA patents and collect their assignees and primary CPCs
citing_assignees_and_cpcs = []

for record in publication_data:
    patent_info_str = record['Patents_info']
    
    # Extract current patent's assignee
    assignee_match = re.match(r'^(.*?)(?: holds the US patent application| is the assignee| - US Patent)', patent_info_str)
    current_patent_assignee = assignee_match.group(1).strip() if assignee_match else "UNKNOWN"

    if "UNIV CALIFORNIA" in current_patent_assignee.upper() or "UNIVERSITY OF CALIFORNIA" in current_patent_assignee.upper():
        continue # Exclude UNIV CALIFORNIA itself from being a citing assignee

    citations = json.loads(record['citation']) if record['citation'] else []
    
    cites_univ_california = False
    for citation in citations:
        cited_pub_number = citation.get('publication_number')
        if cited_pub_number in univ_california_publication_numbers:
            cites_univ_california = True
            break
    
    if cites_univ_california:
        primary_cpc = None
        cpc_codes = json.loads(record['cpc']) if record['cpc'] else []
        for cpc_entry in cpc_codes:
            if cpc_entry.get('first'): # "primary CPC subclasses" are those with "first": true
                primary_cpc = cpc_entry.get('code')
                break
        
        if primary_cpc:
            citing_assignees_and_cpcs.append({
                "citing_assignee": current_patent_assignee,
                "primary_cpc_code": primary_cpc
            })

result = json.dumps(citing_assignees_and_cpcs)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-7476042936698487296': 'file_storage/function-call-7476042936698487296.json', 'var_function-call-8596662436659277732': [], 'var_function-call-9703979398989705124': ['cpc_definition']}

exec(code, env_args)
