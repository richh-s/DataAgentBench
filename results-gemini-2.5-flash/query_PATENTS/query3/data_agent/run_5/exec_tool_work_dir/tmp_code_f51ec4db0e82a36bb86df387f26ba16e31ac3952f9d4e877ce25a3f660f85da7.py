code = """import json
import re

univ_california_publication_numbers = locals()['var_function-call-10059552934646644970']

file_path = locals()['var_function-call-15593298384675158215']
with open(file_path, 'r') as f:
    citations_data = json.load(f)

citing_assignees_info = []

for record in citations_data:
    patents_info = record['Patents_info']
    citation_list = json.loads(record['citation'])
    cpc_list = json.loads(record['cpc'])

    citing_assignee_match = re.search(r'assignee_harmonized: ([^,]+)', patents_info)
    citing_assignee = citing_assignee_match.group(1).strip() if citing_assignee_match else 'UNKNOWN'

    if citing_assignee == 'UNIV CALIFORNIA':
        continue

    cites_univ_california = False
    for citation in citation_list:
        cited_pub_number = citation.get('publication_number')
        if cited_pub_number in univ_california_publication_numbers:
            cites_univ_california = True
            break

    if cites_univ_california:
        primary_cpc_codes = []
        for cpc_entry in cpc_list:
            if cpc_entry.get('first') == True:
                primary_cpc_codes.append(cpc_entry['code'])
        
        # If no primary CPC found, consider the first one as a fallback or skip if strict primary is required
        # For this query, let's take all 'first: true' CPCs, and if none, the first available CPC.
        if not primary_cpc_codes and cpc_list:
            primary_cpc_codes.append(cpc_list[0]['code'])

        for cpc_code in primary_cpc_codes:
            citing_assignees_info.append({
                'assignee': citing_assignee,
                'cpc_code': cpc_code
            })

print('__RESULT__:')
print(json.dumps(citing_assignees_info))"""

env_args = {'var_function-call-13930125777228040085': ['publicationinfo'], 'var_function-call-1621381890062432431': [], 'var_function-call-10802364016398363406': [], 'var_function-call-13532911310427381018': 'file_storage/function-call-13532911310427381018.json', 'var_function-call-10059552934646644970': ['US-6767662-B2', 'US-9061071-B2', 'US-11376346-B2', 'US-6750960-B2', 'US-11546022-B2', 'US-11667770-B2'], 'var_function-call-15593298384675158215': 'file_storage/function-call-15593298384675158215.json'}

exec(code, env_args)
