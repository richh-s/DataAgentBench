code = """import json
import pandas as pd

# Load the full JSON data from the file
with open(locals()['var_function-call-10301112809646823471'], 'r') as f:
    patents_data = json.load(f)

univ_california_patents = []
for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    citations = json.loads(patent.get('citation', '[]'))
    cpc_codes = json.loads(patent.get('cpc', '[]'))

    # Extract assignee from Patents_info
    assignee_start = patents_info.find('assignee_harmonized': ') + len('assignee_harmonized': ')
    assignee_end = patents_info.find(',', assignee_start)
    if assignee_end == -1:
        assignee_end = patents_info.find('.', assignee_start)
    assignee = patents_info[assignee_start:assignee_end].strip()

    publication_number_start = patents_info.find('pub. number ') + len('pub. number ')
    publication_number_end = patents_info.find('.', publication_number_start)
    publication_number = patents_info[publication_number_start:publication_number_end].strip()

    if "UNIV CALIFORNIA" in patents_info:
        for citation in citations:
            cited_pub_number = citation.get('publication_number')
            if cited_pub_number:
                # For now, let's just store the cited patents and their CPCs for UNIV CALIFORNIA
                # We will process citing patents later.
                first_cpc_code = cpc_codes[0]['code'] if cpc_codes and cpc_codes[0]['code'] else None
                if first_cpc_code:
                    univ_california_patents.append({'publication_number': publication_number, 'first_cpc_code': first_cpc_code})

# Now, we need to find who cited these UNIV CALIFORNIA patents.
# This requires another query to find patents that cite the publication_numbers we just extracted.

# Extract all publication numbers for patents assigned to UNIV CALIFORNIA
univ_california_pub_numbers = [p['publication_number'] for p in univ_california_patents]

# This step needs to be done in SQL, so we will pass the pub numbers to the next query.
# Let's prepare the list of publication numbers to be used in the next SQL query.
# Since we cannot directly query based on list in SQL LIKE, we will construct multiple LIKE clauses.
# For now, let's just extract the unique cited publication numbers to query for their assignees and CPCs later.

# We need to find patents that cite UNIV CALIFORNIA patents. So we need to iterate through all patents,
# find the ones that have UNIV CALIFORNIA patents in their `citation` field.

# Let's get all patents and their citations.
# This step is incorrect. I already have all patents from UNIV CALIFORNIA.
# I need to find patents that *cite* these patents.
# The current approach is looking for citations *within* UNIV CALIFORNIA patents.
# I need to find patents where `citation` field contains a publication_number from `univ_california_pub_numbers`.

# This means I need to query the entire publication_database for citations.

# This is a two step process:
# 1. Get all patents from UNIV CALIFORNIA and their publication numbers (done in first query, need to refine extraction).
# 2. Query all patents in publication_database, and for each patent, check if any of its citations matches a UNIV CALIFORNIA patent.
# 3. If a match is found, extract the assignee of the citing patent and the primary CPC subclass of the *cited* UNIV CALIFORNIA patent.

# Let's refine step 1: Extract UNIV CALIFORNIA patent numbers and their primary CPCs.

univ_california_cited_patent_info = {}
for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    if "UNIV CALIFORNIA" in patents_info:
        publication_number_start = patents_info.find('pub. number ') + len('pub. number ')
        publication_number_end = patents_info.find('.', publication_number_start)
        publication_number = patents_info[publication_number_start:publication_number_end].strip()
        
        cpc_codes = json.loads(patent.get('cpc', '[]'))
        first_cpc_code = cpc_codes[0]['code'] if cpc_codes and cpc_codes[0]['code'] else None
        
        if publication_number and first_cpc_code:
            univ_california_cited_patent_info[publication_number] = first_cpc_code


print("__RESULT__:")
print(json.dumps(univ_california_cited_patent_info))"""

env_args = {'var_function-call-9991954280777560525': ['publicationinfo'], 'var_function-call-17198847221600567673': [], 'var_function-call-10301112809646823471': 'file_storage/function-call-10301112809646823471.json'}

exec(code, env_args)
