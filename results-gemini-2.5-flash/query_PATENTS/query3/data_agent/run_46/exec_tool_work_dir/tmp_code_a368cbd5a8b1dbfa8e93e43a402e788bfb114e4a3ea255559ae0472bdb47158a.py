code = """import json
import pandas as pd
import re

# Load the data from the file
with open(locals()['var_function-call-886299632864564984'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

univ_california_patents_info = {}

# Regex for extracting publication numbers (more robust to variations)
pub_num_pattern = r'(?:pub\\.? number|publication number|ID) ([A-Z0-9-]+)'

# Regex for extracting assignee names
# Prioritize 'assignee_harmonized:' as it's often cleaner
assignee_pattern_harmonized = r'assignee_harmonized: ([A-Z0-9\\s&\\.,-]+)'
# General pattern for assignee that looks for common preceding phrases
# and captures the assignee name until a known separator or end of string.
assignee_pattern_general = r'(?:owned by|holds the|is assigned to|assigned to) ([A-Z0-9\\s&\\.,-]+?)(?: and has| with| patent| the|\\. number|\\(|\\s*app\\.? number|$|\\.)'

# First pass: Identify UNIV CALIFORNIA patents and their primary CPCs
for index, row in df.iterrows():
    patents_info = row['Patents_info']
    
    current_assignee = None
    
    # Try harmonized pattern first
    assignee_match = re.search(assignee_pattern_harmonized, patents_info, re.IGNORECASE)
    if assignee_match:
        current_assignee = assignee_match.group(1).strip().replace('\n', '')
    
    # If not found, try the general pattern
    if not current_assignee:
        assignee_match = re.search(assignee_pattern_general, patents_info, re.IGNORECASE)
        if assignee_match:
            current_assignee = assignee_match.group(1).strip().replace('\n', '')

    # Normalize assignee name for comparison and filter for UNIV CALIFORNIA
    if current_assignee and 'UNIV CALIFORNIA' in current_assignee.upper():
        current_assignee = 'UNIV CALIFORNIA'
    else:
        current_assignee = None

    if current_assignee == 'UNIV CALIFORNIA':
        pub_num_match = re.search(pub_num_pattern, patents_info)
        if pub_num_match:
            publication_number = pub_num_match.group(1)
            
            cpc_codes = json.loads(row['cpc']) if isinstance(row['cpc'], str) else row['cpc']
            primary_cpc = None
            for cpc_entry in cpc_codes:
                if cpc_entry.get('first'): 
                    primary_cpc = cpc_entry['code']
                    break
            
            if primary_cpc: 
                if publication_number not in univ_california_patents_info:
                    univ_california_patents_info[publication_number] = primary_cpc

# Initialize a set to store unique (citing assignee, CPC symbol) pairs
citing_assignees_and_cpc_symbols = set()

# Second pass: Find patents that cite UNIV CALIFORNIA patents
for index, row in df.iterrows():
    citations = json.loads(row['citation']) if isinstance(row['citation'], str) else row['citation']
    if citations:
        for citation in citations:
            cited_publication_number = citation.get('publication_number')
            
            if cited_publication_number in univ_california_patents_info:
                # This patent cites a UNIV CALIFORNIA patent
                citing_patents_info = row['Patents_info']
                
                citing_assignee = None
                # Try to extract assignee for the citing patent, prioritizing harmonized pattern
                citing_assignee_match = re.search(assignee_pattern_harmonized, citing_patents_info, re.IGNORECASE)
                if citing_assignee_match:
                    citing_assignee = citing_assignee_match.group(1).strip().replace('\n', '')
                
                if not citing_assignee:
                    citing_assignee_match = re.search(assignee_pattern_general, citing_patents_info, re.IGNORECASE)
                    if citing_assignee_match:
                        citing_assignee = citing_assignee_match.group(1).strip().replace('\n', '')

                # Check if citing assignee exists and is not 'UNIV CALIFORNIA'
                if citing_assignee and 'UNIV CALIFORNIA' not in citing_assignee.upper():
                    primary_cpc_of_cited_patent = univ_california_patents_info[cited_publication_number]
                    citing_assignees_and_cpc_symbols.add((citing_assignee, primary_cpc_of_cited_patent))

# Convert set to a list of dictionaries for easier downstream processing
result_list = [{'assignee': item[0], 'cpc_symbol': item[1]} for item in citing_assignees_and_cpc_symbols]

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_function-call-11763644540560458459': [], 'var_function-call-3342722278808768487': 'file_storage/function-call-3342722278808768487.json', 'var_function-call-8212725183868192279': [], 'var_function-call-17671957491941840990': 'file_storage/function-call-17671957491941840990.json', 'var_function-call-18160213982380891272': [], 'var_function-call-886299632864564984': 'file_storage/function-call-886299632864564984.json', 'var_function-call-8140757829065748700': [], 'var_function-call-16974150656813884896': [], 'var_function-call-14807397755304369764': [], 'var_function-call-18053632019672920162': [], 'var_function-call-543755377448319006': [], 'var_function-call-13829192013951973503': [], 'var_function-call-6992365713272503397': [], 'var_function-call-13413364122417469166': []}

exec(code, env_args)
