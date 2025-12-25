code = """import json
import re

with open(locals()['var_function-call-7476042936698487296'], 'r') as f:
    publication_data = json.load(f)

univ_california_publication_numbers = set()
publication_to_assignee = {}

for record in publication_data:
    patent_info_str = record['Patents_info']
    
    current_publication_number = None
    # Try to extract publication number, checking for both "publication number" and "ID"
    pub_number_match = re.search(r'(?:publication number|ID) ([A-Z0-9-]+)', patent_info_str)
    if pub_number_match:
        current_publication_number = pub_number_match.group(1).strip()

    current_assignee = "UNKNOWN"
    # Extract assignee by taking the part before common phrases
    assignee_parts = re.split(r' holds the US patent application| is the assignee| - US Patent|: US Patent|\(', patent_info_str, 1)
    current_assignee = assignee_parts[0].strip()

    # Further refinement for assignee
    if current_assignee.endswith(','):
        current_assignee = current_assignee[:-1].strip()

    if current_publication_number:
        publication_to_assignee[current_publication_number] = current_assignee
        # Check for variations of "UNIV CALIFORNIA"
        if "UNIV CALIFORNIA" in current_assignee.upper() or \
           "UNIVERSITY OF CALIFORNIA" in current_assignee.upper() or \
           "REGENTS OF THE UNIVERSITY OF CALIFORNIA" in current_assignee.upper():
            univ_california_publication_numbers.add(current_publication_number)

citing_patents_details = []

for record in publication_data:
    patent_info_str = record['Patents_info']

    current_patent_assignee = "UNKNOWN"
    assignee_parts = re.split(r' holds the US patent application| is the assignee| - US Patent|: US Patent|\(', patent_info_str, 1)
    current_patent_assignee = assignee_parts[0].strip()

    if current_patent_assignee.endswith(','):
        current_patent_assignee = current_patent_assignee[:-1].strip()

    # Exclude UNIV CALIFORNIA itself as a citing assignee
    if "UNIV CALIFORNIA" in current_patent_assignee.upper() or \
       "UNIVERSITY OF CALIFORNIA" in current_patent_assignee.upper() or \
       "REGENTS OF THE UNIVERSITY OF CALIFORNIA" in current_patent_assignee.upper():
        continue

    citations = json.loads(record['citation']) if record['citation'] else []
    
    cites_univ_california = False
    for citation in citations:
        cited_pub_number = citation.get('publication_number')
        if cited_pub_number and cited_pub_number in univ_california_publication_numbers:
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
            citing_patents_details.append({
                "citing_assignee": current_patent_assignee,
                "primary_cpc_code": primary_cpc
            })

result = json.dumps(citing_patents_details)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-7476042936698487296': 'file_storage/function-call-7476042936698487296.json', 'var_function-call-8596662436659277732': [], 'var_function-call-9703979398989705124': ['cpc_definition'], 'var_function-call-1782199739990948902': [], 'var_function-call-12802302354754268019': []}

exec(code, env_args)
