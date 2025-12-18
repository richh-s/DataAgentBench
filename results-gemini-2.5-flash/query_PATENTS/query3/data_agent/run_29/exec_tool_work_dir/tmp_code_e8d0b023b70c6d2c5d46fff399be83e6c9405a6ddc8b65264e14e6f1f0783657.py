code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-17345096948690760045']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

pub_data = {}

for index, row in df.iterrows():
    patents_info = row['Patents_info']
    cpc_str = row['cpc']

    publication_number = None
    assignee = None
    primary_cpc = None

    # Extract publication number
    pub_num_match = re.search(r'publication number ([A-Z0-9-]+)', patents_info)
    if pub_num_match:
        publication_number = pub_num_match.group(1).strip()

    # Extract assignee_harmonized
    assignee_match = re.search(r'assignee_harmonized: ([^,;.]+)', patents_info)
    if assignee_match:
        assignee = assignee_match.group(1).strip()

    # Extract primary CPC
    if cpc_str:
        cpc_list = json.loads(cpc_str)
        for cpc_item in cpc_list:
            if cpc_item.get('first'):
                primary_cpc = cpc_item.get('code')
                break
    
    if publication_number:
        pub_data[publication_number] = {
            'assignee': assignee,
            'primary_cpc': primary_cpc,
            'citations': json.loads(row['citation']) if row['citation'] else []
        }

univ_california_pubs = {pub_num for pub_num, info in pub_data.items() if info['assignee'] == 'UNIV CALIFORNIA'}

citing_info_list = []
unique_cpc_codes_to_fetch = set()

for pub_num, info in pub_data.items():
    citing_assignee = info['assignee']
    if citing_assignee and citing_assignee != 'UNIV CALIFORNIA':
        for citation in info['citations']:
            cited_pub_number = citation.get('publication_number')
            if cited_pub_number in univ_california_pubs:
                if info['primary_cpc']:
                    citing_info_list.append({
                        'citing_assignee': citing_assignee,
                        'primary_cpc': info['primary_cpc']
                    })
                    unique_cpc_codes_to_fetch.add(info['primary_cpc'])
                break # Move to the next citing patent once a UNIV CALIFORNIA citation is found

result = {
    'citing_details': citing_info_list,
    'cpc_codes_for_lookup': list(unique_cpc_codes_to_fetch)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-6464706059766972960': [], 'var_function-call-17345096948690760045': 'file_storage/function-call-17345096948690760045.json', 'var_function-call-6766413519393345432': [], 'var_function-call-8146522725027344362': {'citing_info': [], 'unique_cpc_codes': []}, 'var_function-call-14898240996228576662': {'citing_info': [], 'unique_cpc_codes': []}}

exec(code, env_args)
