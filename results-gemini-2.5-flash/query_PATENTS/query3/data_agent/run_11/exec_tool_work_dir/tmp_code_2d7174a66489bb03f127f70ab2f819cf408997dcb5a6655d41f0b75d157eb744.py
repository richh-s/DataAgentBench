code = """import json
import re
import pandas as pd

# Load publication data
with open(locals()['var_function-call-7476042936698487296'], 'r') as f:
    publication_data = json.load(f)

# Process publication data to identify UNIV CALIFORNIA patents and all assignees
univ_california_publication_numbers = set()
publication_assignee_map = {}
all_patent_info = []

for record in publication_data:
    patent_info_str = record['Patents_info']
    
    current_assignee = "UNKNOWN"
    assignee_match = re.search(r'^(.*?)(?: holds the US patent application| is the assignee| - US Patent|: US Patent|\.)', patent_info_str)
    if assignee_match:
        current_assignee = assignee_match.group(1).strip()
    
    # Further refinement for assignee
    if current_assignee.endswith(','):
        current_assignee = current_assignee[:-1].strip()
    
    current_publication_number = None
    pub_number_match = re.search(r'(?:publication number|ID) ([A-Z0-9-]+)', patent_info_str)
    if pub_number_match:
        current_publication_number = pub_number_match.group(1).strip()

    if current_publication_number:
        publication_assignee_map[current_publication_number] = current_assignee
        if "UNIV CALIFORNIA" in current_assignee.upper() or \
           "UNIVERSITY OF CALIFORNIA" in current_assignee.upper() or \
           "REGENTS OF THE UNIVERSITY OF CALIFORNIA" in current_assignee.upper():
            univ_california_publication_numbers.add(current_publication_number)
    
    all_patent_info.append({
        "publication_number": current_publication_number,
        "assignee": current_assignee,
        "cpc": record['cpc'],
        "citation": record['citation']
    })

# Find patents that cite UNIV CALIFORNIA patents
citing_patents_details = []

for patent in all_patent_info:
    current_patent_assignee = patent['assignee']
    current_publication_number = patent['publication_number']

    # Exclude UNIV CALIFORNIA itself as a citing assignee
    if "UNIV CALIFORNIA" in current_patent_assignee.upper() or \
       "UNIVERSITY OF CALIFORNIA" in current_patent_assignee.upper() or \
       "REGENTS OF THE UNIVERSITY OF CALIFORNIA" in current_patent_assignee.upper():
        continue
    
    if patent['citation']:
        citations = json.loads(patent['citation'])
        cites_univ_california = False
        for citation in citations:
            cited_pub_number = citation.get('publication_number')
            if cited_pub_number and cited_pub_number in univ_california_publication_numbers:
                cites_univ_california = True
                break
        
        if cites_univ_california:
            primary_cpc = None
            if patent['cpc']:
                cpc_codes = json.loads(patent['cpc'])
                for cpc_entry in cpc_codes:
                    if cpc_entry.get('first'):
                        primary_cpc = cpc_entry.get('code')
                        break
            
            if primary_cpc:
                citing_patents_details.append({
                    "citing_assignee": current_patent_assignee,
                    "primary_cpc_code": primary_cpc
                })

# Load CPC definition data
with open(locals()['var_function-call-14230902140254691529'], 'r') as f:
    cpc_definition_data = json.load(f)

# Create a DataFrame for CPC definitions for easy lookup
cpc_df = pd.DataFrame(cpc_definition_data)
cpc_df_filtered = cpc_df[['symbol', 'titleFull']]

# Create a DataFrame for citing patents details
citing_df = pd.DataFrame(citing_patents_details)

final_result = []
if not citing_df.empty:
    # Join the two dataframes to get the full CPC title
    merged_df = pd.merge(citing_df, cpc_df_filtered, left_on='primary_cpc_code', right_on='symbol', how='left')

    # Format the output
    for index, row in merged_df.iterrows():
        final_result.append({
            "citing_assignee": row['citing_assignee'],
            "primary_cpc_subclass_title": row['titleFull']
        })

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-7476042936698487296': 'file_storage/function-call-7476042936698487296.json', 'var_function-call-8596662436659277732': [], 'var_function-call-9703979398989705124': ['cpc_definition'], 'var_function-call-1782199739990948902': [], 'var_function-call-12802302354754268019': [], 'var_function-call-14333384151158430616': [], 'var_function-call-14230902140254691529': 'file_storage/function-call-14230902140254691529.json'}

exec(code, env_args)
