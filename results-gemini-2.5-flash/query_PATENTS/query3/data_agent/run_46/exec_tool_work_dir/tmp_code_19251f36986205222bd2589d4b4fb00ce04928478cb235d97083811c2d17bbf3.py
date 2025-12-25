code = """import json
import pandas as pd
import re

# Load the data from the file
with open(locals()['var_function-call-886299632864564984'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

univ_california_patents_info = {}

# More robust regex for assignee, trying to capture names around 'assignee_harmonized:' or other keywords
assignee_pattern = re.compile(r'(?:assignee_harmonized: |owned by |holds the |is assigned to |assigned to )([A-Z0-9\\s&\\.,-]+?)(?: and has pub\\. number| with publication number| has pub\\. number| patent filing \\(app\\. number| patent application \\(no\\.|\\. number| application \\(number| the US patent application \\(ID| and has publication number| \\(number|\\. |$)', re.IGNORECASE)
pub_num_pattern = re.compile(r'(?:pub\\.? number|publication number|ID) ([A-Z0-9-]+)')

for index, row in df.iterrows():
    patents_info = row['Patents_info']
    current_assignee = None
    
    # Attempt to extract assignee using the general pattern
    assignee_match = assignee_pattern.search(patents_info)
    if assignee_match:
        current_assignee = assignee_match.group(1).strip().replace('\\n', '')
    
    # Further check and normalize for 'UNIV CALIFORNIA'
    if current_assignee and 'UNIV CALIFORNIA' in current_assignee.upper():
        current_assignee = 'UNIV CALIFORNIA' # Standardize the name
    else:
        current_assignee = None

    if current_assignee == 'UNIV CALIFORNIA':
        pub_num_match = pub_num_pattern.search(patents_info)
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

# Store the intermediate result to inspect
print('__RESULT__:')
print(json.dumps(list(univ_california_patents_info.items())))"""

env_args = {'var_function-call-11763644540560458459': [], 'var_function-call-3342722278808768487': 'file_storage/function-call-3342722278808768487.json', 'var_function-call-8212725183868192279': [], 'var_function-call-17671957491941840990': 'file_storage/function-call-17671957491941840990.json', 'var_function-call-18160213982380891272': [], 'var_function-call-886299632864564984': 'file_storage/function-call-886299632864564984.json', 'var_function-call-8140757829065748700': [], 'var_function-call-16974150656813884896': [], 'var_function-call-14807397755304369764': [], 'var_function-call-18053632019672920162': [], 'var_function-call-543755377448319006': [], 'var_function-call-13829192013951973503': [], 'var_function-call-6992365713272503397': [], 'var_function-call-13413364122417469166': [], 'var_function-call-12648170104299062999': [], 'var_function-call-4828962983335102307': []}

exec(code, env_args)
