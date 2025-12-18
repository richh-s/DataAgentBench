code = """import json
import pandas as pd
import re

# Load the data from the file
with open(locals()['var_function-call-886299632864564984'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

univ_california_patents_info = {}

# Regex for extracting publication numbers
pub_num_pattern = re.compile(r'(?:pub\\.? number|publication number|ID) ([A-Z0-9-]+)')

# Regex for extracting assignee names, prioritizing 'assignee_harmonized:'
assignee_pattern_harmonized = re.compile(r'assignee_harmonized: ([A-Z0-9\\s&\\.,-]+)', re.IGNORECASE)
# General pattern for assignee that looks for common preceding phrases
# and captures the assignee name until the end of the line or a new descriptive keyword.
assignee_pattern_general = re.compile(r'(?:owned by|holds the|is assigned to|assigned to) ([A-Z0-9\\s&\\.,-]+?)(?: and has| with| patent| the|\\. number|\\(|\\s*app\\.? number|$)', re.IGNORECASE)

# Function to extract assignee from Patents_info
def extract_assignee(patents_info):
    assignee = None
    match_harmonized = assignee_pattern_harmonized.search(patents_info)
    if match_harmonized:
        assignee = match_harmonized.group(1).strip().replace('\\n', '')
    else:
        match_general = assignee_pattern_general.search(patents_info)
        if match_general:
            assignee = match_general.group(1).strip().replace('\\n', '')
    return assignee

# First pass: Identify UNIV CALIFORNIA patents and their primary CPCs
for index, row in df.iterrows():
    patents_info = row['Patents_info']
    current_assignee = extract_assignee(patents_info)
    
    # Normalize assignee name for comparison and filter for UNIV CALIFORNIA
    if current_assignee and 'UNIV CALIFORNIA' in current_assignee.upper():
        current_assignee = 'UNIV CALIFORNIA'
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
                citing_assignee = extract_assignee(citing_patents_info)

                # Check if citing assignee exists and is not 'UNIV CALIFORNIA' (case-insensitive)
                if citing_assignee and 'UNIV CALIFORNIA' not in citing_assignee.upper():
                    primary_cpc_of_cited_patent = univ_california_patents_info[cited_publication_number]
                    citing_assignees_and_cpc_symbols.add((citing_assignee, primary_cpc_of_cited_patent))

# Convert set to a list of dictionaries for easier downstream processing
result_list = [{'assignee': item[0], 'cpc_symbol': item[1]} for item in citing_assignees_and_cpc_symbols]

# Extract all CPC symbols to query the definition database
cpc_symbols_to_query = list(set([item[1] for item in citing_assignees_and_cpc_symbols]))

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_function-call-11763644540560458459': [], 'var_function-call-3342722278808768487': 'file_storage/function-call-3342722278808768487.json', 'var_function-call-8212725183868192279': [], 'var_function-call-17671957491941840990': 'file_storage/function-call-17671957491941840990.json', 'var_function-call-18160213982380891272': [], 'var_function-call-886299632864564984': 'file_storage/function-call-886299632864564984.json', 'var_function-call-8140757829065748700': [], 'var_function-call-16974150656813884896': [], 'var_function-call-14807397755304369764': [], 'var_function-call-18053632019672920162': [], 'var_function-call-543755377448319006': [], 'var_function-call-13829192013951973503': [], 'var_function-call-6992365713272503397': [], 'var_function-call-13413364122417469166': [], 'var_function-call-12648170104299062999': [], 'var_function-call-4828962983335102307': [], 'var_function-call-15348511395839215204': [['US-2022074631-A1', 'F25B21/00'], ['US-11421276-B2', 'C12Q1/6883'], ['JP-S6163700-A', 'C07K16/34'], ['US-2017281687-A1', 'A61K35/28'], ['US-11072681-B2', 'C07H21/00'], ['KR-20160119166-A', 'G01N33/5767'], ['US-2019169580-A1', 'C12N9/1029'], ['WO-2021102420-A1', 'A61P35/00'], ['US-201916537416-A', 'C12N15/8255'], ['US-11376346-B2', 'A61L27/58'], ['CN-100339724-C', 'G01V3/12'], ['WO-2019173834-A1', 'A61K31/734'], ['US-202016883515-A', 'A61P25/16'], ['US-2021000566-A1', 'A61F9/009'], ['PT-2970346-T', 'A61K31/675'], ['US-2022016812-W', 'A61K45/06'], ['US-2006292670-A1', 'C07K14/51'], ['US-2023321419-A1', 'A61M37/0015'], ['US-2019209590-A1', 'A61K31/663'], ['US-11667770-B2', 'C08J9/30'], ['CA-3161617-A', 'C07K16/2803'], ['JP-2009260386-A', 'C30B29/403'], ['CA-2562038-C', 'C07K16/2839'], ['EP-2210307-A4', 'H01M8/0232'], ['US-74211203-A', 'H01L21/76838'], ['US-2021039104-A1', 'B01L3/5085'], ['WO-2014152660-A1', 'G01N33/6854'], ['AU-2008349842-A', 'C22C30/02'], ['WO-2018067976-A1', 'G01N27/44791'], ['US-202016952492-A', 'G03H1/0866'], ['US-2018018836-W', 'G01N33/6869'], ['AU-2015364602-B2', 'C12Q1/48'], ['IL-274176-A', 'C07K14/47'], ['JP-2014224156-A', 'A61K38/02'], ['US-2004115131-A1', 'G01N33/58'], ['AU-2010214112-B2', 'C07D473/18'], ['US-2018053351-W', 'A61P17/14'], ['PE-20130764-A1', 'A01N43/90'], ['US-11014955-B2', 'C07H19/16'], ['CN-201210027378-A', 'C07D233/86'], ['CN-103687626-A', 'C12N5/0621'], ['CA-2278751-A', 'H01J37/32192'], ['HK-03104403-A', 'C07D235/02'], ['US-2023155090-A1', 'H10K59/131'], ['EP-3668487-A4', 'A61K48/00'], ['CA-2283629-C', 'G01N33/542'], ['US-2023024482-W', 'A61N1/36021'], ['ID-23426-A', 'A61B17/1214'], ['US-5304932-A', 'G01R33/421'], ['AU-5938296-A', 'A61K9/0075'], ['US-2018243924-A1', 'B25J13/084']]}

exec(code, env_args)
