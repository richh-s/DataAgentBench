code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-17345096948690760045']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

pub_details = {}

# First pass: Extract all relevant details (publication number, assignee, primary CPC, citations)
for index, row in df.iterrows():
    patents_info = str(row['Patents_info'])
    cpc_str = row['cpc']
    citation_str = row['citation']

    publication_number = None
    assignee = None
    primary_cpc = None

    # Extract assignee: prioritize assignee_harmonized, then try other patterns
    assignee_harmonized_match = re.search(r'assignee_harmonized:\s*([^,;.]+)', patents_info)
    if assignee_harmonized_match:
        assignee = assignee_harmonized_match.group(1).strip()
    else:
        # Try finding assignee at the beginning or after keywords
        assignee_match_start = re.match(r'^(.+?)(?: holds the US patent| is owned by| is assigned to| belonging to| US patent| application| from [A-Z]{2}, held by)', patents_info)
        if assignee_match_start:
            assignee = assignee_match_start.group(1).strip()
        else:
            assignee_match_keywords = re.search(r'(?:owned by|assigned to|belonging to|held by)\s*([^,;.]+)', patents_info, re.IGNORECASE)
            if assignee_match_keywords:
                assignee = assignee_match_keywords.group(1).strip()

    # Extract publication number: handle variations like "pub. number", "publication number", "publication no."
    pub_num_match = re.search(r'(?:publication\s*number|pub\.\s*number|publication\s*no\.|pub\.\s*no\.)\s*([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_num_match:
        publication_number = pub_num_match.group(1).strip()

    # Extract primary CPC
    if cpc_str:
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_item in cpc_list:
                if cpc_item.get('first'):
                    primary_cpc = cpc_item.get('code')
                    break
        except json.JSONDecodeError:
            pass # Handle malformed JSON gracefully
    
    if publication_number:
        pub_details[publication_number] = {
            'assignee': assignee,
            'primary_cpc': primary_cpc,
            'citations': json.loads(citation_str) if citation_str else []
        }

# Identify publication numbers assigned to 'UNIV CALIFORNIA'
univ_california_pubs = {pub_num for pub_num, details in pub_details.items() if details['assignee'] == 'UNIV CALIFORNIA'}

citing_assignees_cpc_info = []
unique_cpc_codes_to_lookup = set()

# Second pass: Find patents that cite UNIV CALIFORNIA patents
for pub_num, details in pub_details.items():
    citing_assignee = details['assignee']
    
    # Only consider citing assignees that are not UNIV CALIFORNIA
    if citing_assignee and citing_assignee != 'UNIV CALIFORNIA':
        for citation in details['citations']:
            cited_pub_number = citation.get('publication_number')
            
            # If this patent cites a UNIV CALIFORNIA patent
            if cited_pub_number in univ_california_pubs:
                # Record the citing assignee and its primary CPC
                if details['primary_cpc']:
                    citing_assignees_cpc_info.append({
                        'citing_assignee': citing_assignee,
                        'primary_cpc_code': details['primary_cpc']
                    })
                    unique_cpc_codes_to_lookup.add(details['primary_cpc'])
                break # Move to the next citing patent once a UNIV CALIFORNIA citation is found for efficiency

result = {
    'citing_data': citing_assignees_cpc_info,
    'cpc_codes_for_title_lookup': list(unique_cpc_codes_to_lookup)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-6464706059766972960': [], 'var_function-call-17345096948690760045': 'file_storage/function-call-17345096948690760045.json', 'var_function-call-6766413519393345432': [], 'var_function-call-8146522725027344362': {'citing_info': [], 'unique_cpc_codes': []}, 'var_function-call-14898240996228576662': {'citing_info': [], 'unique_cpc_codes': []}, 'var_function-call-1968237375525755243': {'citing_details': [], 'cpc_codes_for_lookup': []}, 'var_function-call-1389845607898337217': {'citing_data': [], 'cpc_codes_for_title_lookup': []}, 'var_function-call-5611834866437857616': {'citing_data': [], 'cpc_codes_for_title_lookup': []}, 'var_function-call-7002475197602620142': {'citing_data': [], 'cpc_codes_for_title_lookup': []}, 'var_function-call-5439960736756727231': {'citing_data': [], 'cpc_codes_for_title_lookup': []}, 'var_function-call-13097895891798860154': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_function-call-3094318534147400678': {'citing_data': [], 'cpc_codes_for_title_lookup': []}}

exec(code, env_args)
