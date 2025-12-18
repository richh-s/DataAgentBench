code = """import json
import pandas as pd
import re

# Load the data from the file
with open(locals()['var_function-call-886299632864564984'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

univ_california_patents_info = {}

# Regex to extract publication number
pub_num_pattern = r'(?:pub\\.? number|publication number|ID) ([A-Z0-9-]+)'

# Regex to extract assignee
# This pattern attempts to capture the assignee name more broadly, looking for common introductory phrases
assignee_pattern = r'(?:owned by|holds the|is assigned to|assignee_harmonized:|assigned to) ([A-Z0-9\\s&\\.,-]+?)(?: and has pub\\. number| with publication number| has pub\\. number| patent filing \\(app\\. number| patent application \\(no\\.|\\. number| application \\(number| the US patent application \\(ID| and has publication number| \\(number|\\. |$)'

# First pass: Identify UNIV CALIFORNIA patents and their primary CPCs
for index, row in df.iterrows():
    patents_info = row['Patents_info']
    
    current_assignee = None
    assignee_match = re.search(assignee_pattern, patents_info)
    if assignee_match:
        current_assignee = assignee_match.group(1).strip().replace('\\n', '')
    
    # If the first regex didn't find an assignee, try a simpler one for 'assignee_harmonized:'
    if not current_assignee:
        assignee_harmonized_match = re.search(r'assignee_harmonized: ([A-Z0-9\\s&\\.-]+)', patents_info)
        if assignee_harmonized_match:
            current_assignee = assignee_harmonized_match.group(1).strip().replace('\\n', '')

    if current_assignee == 'UNIV CALIFORNIA':
        pub_num_match = re.search(pub_num_pattern, patents_info)
        if pub_num_match:
            publication_number = pub_num_match.group(1)
            
            cpc_codes = json.loads(row['cpc']) if isinstance(row['cpc'], str) else row['cpc']
            primary_cpc = None
            for cpc_entry in cpc_codes:
                if cpc_entry.get('first'): # Assuming 'first' indicates the primary CPC
                    primary_cpc = cpc_entry['code']
                    break
            
            if primary_cpc: # Only store if primary_cpc is found
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
                citing_assignee_match = re.search(assignee_pattern, citing_patents_info)
                if citing_assignee_match:
                    citing_assignee = citing_assignee_match.group(1).strip().replace('\\n', '')
                
                # If the first regex didn't find an assignee for the citing patent, try a simpler one
                if not citing_assignee:
                    citing_assignee_harmonized_match = re.search(r'assignee_harmonized: ([A-Z0-9\\s&\\.-]+)', citing_patents_info)
                    if citing_assignee_harmonized_match:
                        citing_assignee = citing_assignee_harmonized_match.group(1).strip().replace('\\n', '')

                if citing_assignee and citing_assignee != 'UNIV CALIFORNIA':
                    primary_cpc_of_cited_patent = univ_california_patents_info[cited_publication_number]
                    citing_assignees_and_cpc_symbols.add((citing_assignee, primary_cpc_of_cited_patent))

# Convert set to a list of dictionaries for easier downstream processing
result_list = [{'assignee': item[0], 'cpc_symbol': item[1]} for item in citing_assignees_and_cpc_symbols]

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_function-call-11763644540560458459': [], 'var_function-call-3342722278808768487': 'file_storage/function-call-3342722278808768487.json', 'var_function-call-8212725183868192279': [], 'var_function-call-17671957491941840990': 'file_storage/function-call-17671957491941840990.json', 'var_function-call-18160213982380891272': [], 'var_function-call-886299632864564984': 'file_storage/function-call-886299632864564984.json', 'var_function-call-8140757829065748700': [], 'var_function-call-16974150656813884896': [], 'var_function-call-14807397755304369764': [], 'var_function-call-18053632019672920162': []}

exec(code, env_args)
