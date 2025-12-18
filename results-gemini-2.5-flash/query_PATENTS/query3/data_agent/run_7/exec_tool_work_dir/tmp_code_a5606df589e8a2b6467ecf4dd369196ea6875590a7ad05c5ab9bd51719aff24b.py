code = """import json
import re
import pandas as pd

# Load the full result from the file
with open(locals()['var_function-call-8448093354361830252'], 'r') as f:
    publication_data = json.load(f)

# Pre-parse all necessary fields and store them in a more accessible format
parsed_records = []
for record in publication_data:
    assignee = None
    pub_number = None
    cpc_codes = []
    citations = []

    patents_info = record.get('Patents_info', '')
    
    match_assignee = re.search(r'(.*?)\\s+holds the US patent', patents_info)
    if match_assignee:
        assignee = match_assignee.group(1).strip()
    
    match_pub_number = re.search(r'publication number ([A-Z0-9-]+)', patents_info)
    if match_pub_number:
        pub_number = match_pub_number.group(1).replace('-', '')

    try:
        cpc_codes = json.loads(record.get('cpc', '[]'))
    except (json.JSONDecodeError, TypeError):
        pass # cpc_codes remains empty list

    try:
        citations = json.loads(record.get('citation', '[]'))
    except (json.JSONDecodeError, TypeError):
        pass # citations remains empty list

    parsed_records.append({
        'assignee': assignee,
        'publication_number': pub_number,
        'cpc_codes': cpc_codes,
        'citations': citations
    })

# Identify UNIV CALIFORNIA patents and their publication numbers
univ_california_assignee_keywords = ['UNIV CALIFORNIA', 'UNIVERSITY OF CALIFORNIA']
univ_california_publication_numbers = set()

for record in parsed_records:
    if record['assignee'] and any(keyword.lower() in record['assignee'].lower() for keyword in univ_california_assignee_keywords):
        if record['publication_number']:
            univ_california_publication_numbers.add(record['publication_number'])

# Find citing assignees and their primary CPC subclasses in a single pass
relevant_citations = []
processed_citing_patents = set() # To avoid redundant processing of the same citing patent

for record in parsed_records:
    citing_assignee = record['assignee']
    current_patent_pub_number = record['publication_number']

    if citing_assignee and not any(keyword.lower() in citing_assignee.lower() for keyword in univ_california_assignee_keywords):
        # Prevent processing the same citing patent multiple times if it cites multiple UC patents
        if current_patent_pub_number in processed_citing_patents:
            continue
        
        is_citing_uc_patent = False
        for citation in record['citations']:
            cited_pub_num = citation.get('publication_number')
            if cited_pub_num:
                cleaned_cited_pub_num = cited_pub_num.replace('-', '')
                if cleaned_cited_pub_num in univ_california_publication_numbers:
                    is_citing_uc_patent = True
                    break
        
        if is_citing_uc_patent:
            primary_cpc_subclass = None
            for cpc_entry in record['cpc_codes']:
                if cpc_entry.get('code'):
                    primary_cpc_subclass = cpc_entry['code'].split('/')[0]
                    break # Take the first available CPC code as primary
            
            if primary_cpc_subclass:
                relevant_citations.append({'assignee': citing_assignee, 'cpc_subclass': primary_cpc_subclass})
                processed_citing_patents.add(current_patent_pub_number) # Mark this patent as processed

# Remove duplicate (assignee, cpc_subclass) pairs
if relevant_citations:
    unique_relevant_citations_df = pd.DataFrame(relevant_citations).drop_duplicates()
    unique_relevant_citations = unique_relevant_citations_df.to_dict(orient='records')
else:
    unique_relevant_citations = []

# Extract unique CPC subclass symbols to query for their full titles
unique_cpc_subclass_symbols = list(set([item['cpc_subclass'] for item in unique_relevant_citations]))

print('__RESULT__:')
print(json.dumps({'unique_relevant_citations': unique_relevant_citations, 'unique_cpc_subclass_symbols': unique_cpc_subclass_symbols}))"""

env_args = {'var_function-call-8448093354361830252': 'file_storage/function-call-8448093354361830252.json', 'var_function-call-14330967010767219437': []}

exec(code, env_args)
