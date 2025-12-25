code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-17345096948690760045']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

pub_to_assignee = {}
pub_to_cpc = {}

for index, row in df.iterrows():
    patents_info = row['Patents_info']
    citation_str = row['citation']
    cpc_str = row['cpc']

    assignee = None
    publication_number = None
    primary_cpc = None

    # Extract assignee and publication number from Patents_info
    assignee_match = re.search(r'assignee_harmonized: ([^,;.]+)', patents_info)
    if assignee_match:
        assignee = assignee_match.group(1).strip()

    publication_number_match = re.search(r'publication number ([A-Z0-9-]+)', patents_info)
    if publication_number_match:
        publication_number = publication_number_match.group(1).strip()

    if publication_number and assignee:
        pub_to_assignee[publication_number] = assignee
    
    # Extract primary CPC code
    if cpc_str:
        cpc_codes = json.loads(cpc_str)
        for cpc_item in cpc_codes:
            if cpc_item.get('first'):
                primary_cpc = cpc_item.get('code')
                break
    if publication_number and primary_cpc:
        pub_to_cpc[publication_number] = primary_cpc

univ_california_pubs = {pub for pub, assgn in pub_to_assignee.items() if assgn == 'UNIV CALIFORNIA'}

citing_assignees_cpc_info = []
unique_cpc_codes = set()

for index, row in df.iterrows():
    citation_str = row['citation']
    current_patent_info = row['Patents_info']

    current_assignee_match = re.search(r'assignee_harmonized: ([^,;.]+)', current_patent_info)
    current_assignee = current_assignee_match.group(1).strip() if current_assignee_match else None

    if current_assignee and current_assignee != 'UNIV CALIFORNIA' and citation_str:
        citations = json.loads(citation_str)
        for citation in citations:
            cited_pub_number = citation.get('publication_number')
            if cited_pub_number in univ_california_pubs:
                # This is a citing patent by an assignee other than UNIV CALIFORNIA
                current_pub_number_match = re.search(r'publication number ([A-Z0-9-]+)', current_patent_info)
                current_publication_number = current_pub_number_match.group(1).strip() if current_publication_number_match else None

                if current_publication_number and current_publication_number in pub_to_cpc:
                    primary_cpc_for_citing_patent = pub_to_cpc[current_publication_number]
                    citing_assignees_cpc_info.append({
                        'citing_assignee': current_assignee,
                        'primary_cpc': primary_cpc_for_citing_patent
                    })
                    unique_cpc_codes.add(primary_cpc_for_citing_patent)
                break # Found a citation to UNIV CALIFORNIA, no need to check other citations for this patent

result = {
    'citing_info': citing_assignees_cpc_info,
    'unique_cpc_codes': list(unique_cpc_codes)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-6464706059766972960': [], 'var_function-call-17345096948690760045': 'file_storage/function-call-17345096948690760045.json', 'var_function-call-6766413519393345432': [], 'var_function-call-8146522725027344362': {'citing_info': [], 'unique_cpc_codes': []}}

exec(code, env_args)
