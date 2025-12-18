code = """import json
import pandas as pd

with open(locals()['var_function-call-6439696821773378279'], 'r') as f:
    publication_data = json.load(f)

# Prepare to store data for citing patents and their CPCs
citing_patent_info = []

for record in publication_data:
    patent_info = record.get('Patents_info', '')
    citations = json.loads(record.get('citation', '[]')) # citation is a string, needs to be loaded as JSON
    cpc_codes = json.loads(record.get('cpc', '[]')) # cpc is a string, needs to be loaded as JSON

    # Check if this patent is assigned to UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in patent_info:
        for citation in citations:
            cited_publication_number = citation.get('publication_number')
            # We need to find patents that cite 'UNIV CALIFORNIA' patents, so the current record should be a cited patent
            # and the citation itself is a patent *citing* this UNIV CALIFORNIA patent. 
            # We need to find the assignee of the *citing* patent.
            # This means we need to query for the assignee of the cited_publication_number.
            # This is a bit convoluted. Let's re-think the approach.
            # The query asks for 'assignees ... have cited patents assigned to UNIV CALIFORNIA'.
            # So, we first need to identify all publication numbers for patents assigned to 'UNIV CALIFORNIA'.
            # Then, for each of these publication numbers, we need to find other patents that cite them.
            # Finally, for those citing patents, we need to extract their assignees and CPCs. 

# Let's extract all publication numbers and their assignees from the initial data.
# And also, extract all citations from the initial data, to build a map of citing patents to cited patents.

univ_california_patent_numbers = set()
patent_citations = [] # (citing_pub_number, cited_pub_number)
patent_assignees = {}
patent_cpcs = {}

for record in publication_data:
    patent_info = record.get('Patents_info', '')
    citations = json.loads(record.get('citation', '[]'))
    cpc_codes_list = json.loads(record.get('cpc', '[]'))

    # Extract publication number and assignee for the current patent
    pub_num_start = patent_info.find('pub. number ') + len('pub. number ')
    pub_num_end = patent_info.find('.', pub_num_start)
    publication_number = patent_info[pub_num_start:pub_num_end].strip() if pub_num_start != -1 and pub_num_end != -1 else None

    assignee_start = patent_info.find('assigned to ') + len('assigned to ')
    assignee_end = patent_info.find(' and has', assignee_start)
    if assignee_end == -1:
        assignee_end = patent_info.find(', with', assignee_start)
    if assignee_end == -1:
        assignee_end = patent_info.find(' holds', assignee_start)
    assignee_harmonized = patent_info[assignee_start:assignee_end].strip() if assignee_start != -1 and assignee_end != -1 else None

    if publication_number and assignee_harmonized:
        patent_assignees[publication_number] = assignee_harmonized
        if 'UNIV CALIFORNIA' in assignee_harmonized:
            univ_california_patent_numbers.add(publication_number)
        
    if publication_number:
        primary_cpc_codes = [cpc['code'] for cpc in cpc_codes_list if cpc.get('first') == True]
        if primary_cpc_codes:
            patent_cpcs[publication_number] = primary_cpc_codes

    # Extract citations from this patent
    for citation_entry in citations:
        cited_pub_num = citation_entry.get('publication_number')
        if publication_number and cited_pub_num:
            patent_citations.append({'citing_patent_number': publication_number, 'cited_patent_number': cited_pub_num})

# Now, identify patents that cite 'UNIV CALIFORNIA' patents, excluding 'UNIV CALIFORNIA' itself
citing_assignees_and_cpcs = []

for citation_pair in patent_citations:
    citing_pub_num = citation_pair['citing_patent_number']
    cited_pub_num = citation_pair['cited_patent_number']

    if cited_pub_num in univ_california_patent_numbers: # This citation is to a UNIV CALIFORNIA patent
        citing_assignee = patent_assignees.get(citing_pub_num)
        if citing_assignee and 'UNIV CALIFORNIA' not in citing_assignee: # Exclude UNIV CALIFORNIA itself
            citing_cpc_codes = patent_cpcs.get(citing_pub_num, [])
            for cpc_code in citing_cpc_codes:
                citing_assignees_and_cpcs.append({'assignee': citing_assignee, 'cpc_code': cpc_code})


# Get unique CPC codes for definition lookup
unique_cpc_codes = list(set([item['cpc_code'] for item in citing_assignees_and_cpcs]))

print('__RESULT__:')
print(json.dumps({'citing_assignees_and_cpcs': citing_assignees_and_cpcs, 'unique_cpc_codes': unique_cpc_codes}))"""

env_args = {'var_function-call-4989284733204990727': ['publicationinfo'], 'var_function-call-6439696821773378279': 'file_storage/function-call-6439696821773378279.json'}

exec(code, env_args)
