code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-17345096948690760045']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

pub_details = {}

for index, row in df.iterrows():
    patents_info = row['Patents_info']
    cpc_str = row['cpc']
    citation_str = row['citation']

    publication_number = None
    assignee = None
    primary_cpc = None

    # Extract publication number using a more general pattern
    pub_num_match = re.search(r'publication number\s*([A-Z0-9-]+)', patents_info)
    if pub_num_match:
        publication_number = pub_num_match.group(1).strip()

    # Extract assignee using a more flexible pattern, prioritizing assignee_harmonized
    assignee_match = re.search(r'assignee_harmonized:\s*([^,;.]+)', patents_info)
    if assignee_match:
        assignee = assignee_match.group(1).strip()
    else:
        # Fallback to general assignee extraction if assignee_harmonized is not present
        assignee_match = re.match(r'^([^,;]+?) holds the US patent', patents_info)
        if assignee_match:
            assignee = assignee_match.group(1).strip()
        else:
            # Another fallback for just a name at the beginning
            assignee_match = re.match(r'^([A-Z0-9 .&/-]+?)(?: US patent| holds the US patent| application)', patents_info)
            if assignee_match:
                assignee = assignee_match.group(1).strip()

    # Extract primary CPC
    if cpc_str:
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_item in cpc_list:
                if cpc_item.get('first'):
                    primary_cpc = cpc_item.get('code')
                    break
        except json.JSONDecodeError:
            primary_cpc = None # Handle malformed JSON
    
    if publication_number:
        pub_details[publication_number] = {
            'assignee': assignee,
            'primary_cpc': primary_cpc,
            'citations': json.loads(citation_str) if citation_str else []
        }

# Identify all publication numbers assigned to UNIV CALIFORNIA
univ_california_pubs = {pub_num for pub_num, details in pub_details.items() if details['assignee'] == 'UNIV CALIFORNIA'}

citing_assignees_cpc_info = []
unique_cpc_codes_to_lookup = set()

# Second pass to find citing patents
for pub_num, details in pub_details.items():
    citing_assignee = details['assignee']
    if citing_assignee and citing_assignee != 'UNIV CALIFORNIA':
        for citation in details['citations']:
            cited_pub_number = citation.get('publication_number')
            if cited_pub_number in univ_california_pubs:
                if details['primary_cpc']:
                    citing_assignees_cpc_info.append({
                        'citing_assignee': citing_assignee,
                        'primary_cpc_code': details['primary_cpc']
                    })
                    unique_cpc_codes_to_lookup.add(details['primary_cpc'])
                break # Move to the next citing patent once a UNIV CALIFORNIA citation is found

result = {
    'citing_data': citing_assignees_cpc_info,
    'cpc_codes_for_title_lookup': list(unique_cpc_codes_to_lookup)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-6464706059766972960': [], 'var_function-call-17345096948690760045': 'file_storage/function-call-17345096948690760045.json', 'var_function-call-6766413519393345432': [], 'var_function-call-8146522725027344362': {'citing_info': [], 'unique_cpc_codes': []}, 'var_function-call-14898240996228576662': {'citing_info': [], 'unique_cpc_codes': []}, 'var_function-call-1968237375525755243': {'citing_details': [], 'cpc_codes_for_lookup': []}, 'var_function-call-1389845607898337217': {'citing_data': [], 'cpc_codes_for_title_lookup': []}, 'var_function-call-5611834866437857616': {'citing_data': [], 'cpc_codes_for_title_lookup': []}}

exec(code, env_args)
