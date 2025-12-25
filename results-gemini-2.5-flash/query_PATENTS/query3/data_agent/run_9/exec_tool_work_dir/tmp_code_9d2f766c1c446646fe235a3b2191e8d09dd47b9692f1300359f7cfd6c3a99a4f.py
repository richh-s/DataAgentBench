code = """import json
import pandas as pd

# Load the publication numbers of patents assigned to UNIV CALIFORNIA
univ_california_publication_numbers = locals()['var_function-call-9732747833126604290']

# Load all patent information
with open(locals()['var_function-call-176660053425290826'], 'r') as f:
    all_patents_info = json.load(f)

citing_patents_info = []

for patent in all_patents_info:
    citation_data = json.loads(patent['citation']) if patent['citation'] else []
    
    cites_univ_california = False
    for citation in citation_data:
        cited_pub_number = citation.get('publication_number', '').replace('-', '').replace('.', '')
        # Extract the country code from the publication number if present and only keep the numeric part
        if len(cited_pub_number) > 2 and not cited_pub_number[:2].isalpha():
            # If the first two characters are not letters, assume no country code prefix
            pass
        elif len(cited_pub_number) > 2 and cited_pub_number[:2].isalpha():
            # If the first two characters are letters, assume it's a country code
            cited_pub_number = cited_pub_number[2:]

        if cited_pub_number in univ_california_publication_numbers:
            cites_univ_california = True
            break
    
    if cites_univ_california:
        # Extract assignee from Patents_info
        assignee = None
        if 'Patents_info' in patent and patent['Patents_info']:
            patent_info_str = patent['Patents_info']
            if "assigned to " in patent_info_str:
                start_index = patent_info_str.find("assigned to ") + len("assigned to ")
                end_index = patent_info_str.find(" and has", start_index)
                if end_index == -1:
                    end_index = patent_info_str.find(" holds", start_index)
                if end_index == -1:
                    end_index = patent_info_str.find(" with publication", start_index)
                if end_index == -1:
                    end_index = patent_info_str.find(" (ID", start_index)
                if end_index == -1:
                    end_index = patent_info_str.find(" (app.", start_index)
                if end_index == -1:
                    end_index = len(patent_info_str) # If no clear end, take till the end

                assignee = patent_info_str[start_index:end_index].strip().replace('.', '')
            elif "owned by " in patent_info_str:
                start_index = patent_info_str.find("owned by ") + len("owned by ")
                end_index = patent_info_str.find(" and has", start_index)
                if end_index == -1:
                    end_index = len(patent_info_str)
                assignee = patent_info_str[start_index:end_index].strip().replace('.', '')
            elif "holds the " in patent_info_str:
                start_index = patent_info_str.find("holds the ")
                end_index = patent_info_str.find(" patent", start_index)
                if end_index != -1:
                    assignee_candidate = patent_info_str[:start_index].strip()
                    if assignee_candidate.isupper(): # heuristic for assignee name
                        assignee = assignee_candidate


        # Exclude UNIV CALIFORNIA as the citing assignee
        if assignee and "UNIV CALIFORNIA" not in assignee.upper():
            # Extract primary CPC subclass
            cpc_data = json.loads(patent['cpc']) if patent['cpc'] else []
            primary_cpc = None
            for cpc_entry in cpc_data:
                if cpc_entry.get('first'):
                    primary_cpc = cpc_entry['code']
                    break
            
            if primary_cpc:
                citing_patents_info.append({
                    'assignee': assignee,
                    'primary_cpc': primary_cpc
                })

print("__RESULT__:")
print(json.dumps(citing_patents_info))"""

env_args = {'var_function-call-11905661168972610564': 'file_storage/function-call-11905661168972610564.json', 'var_function-call-9732747833126604290': ['RO', 'TW', 'EP', 'AU', 'IL', 'US', 'ID', 'CN', 'HK', 'WO', 'KR', 'CA', 'JP', 'MX'], 'var_function-call-4403495635799159949': 'file_storage/function-call-4403495635799159949.json', 'var_function-call-176660053425290826': 'file_storage/function-call-176660053425290826.json'}

exec(code, env_args)
