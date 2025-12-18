code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-17345096948690760045']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

pub_to_assignee = {}
univ_california_pubs = set()

for index, row in df.iterrows():
    patents_info = row['Patents_info']
    
    assignee_match = re.search(r'assignee_harmonized: ([^,;.]+)', patents_info)
    publication_number_match = re.search(r'publication number ([A-Z0-9-]+)', patents_info)
    
    assignee = assignee_match.group(1).strip() if assignee_match else None
    publication_number = publication_number_match.group(1).strip() if publication_number_match else None
    
    if publication_number and assignee:
        pub_to_assignee[publication_number] = assignee
        if assignee == 'UNIV CALIFORNIA':
            univ_california_pubs.add(publication_number)

citing_assignees_cpc_info = []
unique_cpc_codes = set()

for index, row in df.iterrows():
    citation_str = row['citation']
    citations = json.loads(citation_str) if citation_str else []
    
    cites_univ_california = False
    for citation in citations:
        cited_pub_number = citation.get('publication_number')
        if cited_pub_number in univ_california_pubs:
            cites_univ_california = True
            break
            
    if cites_univ_california:
        patents_info = row['Patents_info']
        citing_assignee_match = re.search(r'assignee_harmonized: ([^,;.]+)', patents_info)
        citing_assignee = citing_assignee_match.group(1).strip() if citing_assignee_match else None
        
        if citing_assignee and citing_assignee != 'UNIV CALIFORNIA':
            cpc_str = row['cpc']
            cpc_codes = json.loads(cpc_str) if cpc_str else []
            primary_cpc = None
            for cpc_item in cpc_codes:
                if cpc_item.get('first'):
                    primary_cpc = cpc_item.get('code')
                    break
            
            if primary_cpc:
                citing_assignees_cpc_info.append({
                    'citing_assignee': citing_assignee,
                    'primary_cpc': primary_cpc
                })
                unique_cpc_codes.add(primary_cpc)


result = {
    'citing_info': citing_assignees_cpc_info,
    'unique_cpc_codes': list(unique_cpc_codes)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-6464706059766972960': [], 'var_function-call-17345096948690760045': 'file_storage/function-call-17345096948690760045.json', 'var_function-call-6766413519393345432': []}

exec(code, env_args)
