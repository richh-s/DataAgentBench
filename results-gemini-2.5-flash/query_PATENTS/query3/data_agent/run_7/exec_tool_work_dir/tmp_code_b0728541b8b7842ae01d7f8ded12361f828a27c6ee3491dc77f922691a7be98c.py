code = """import json
import re
import pandas as pd

# Load the full result from the file
with open(locals()['var_function-call-8448093354361830252'], 'r') as f:
    publication_data = json.load(f)

# Pre-process all patents to extract necessary information efficiently
processed_patents = []
for record in publication_data:
    patents_info = record.get('Patents_info', '')
    assignee = None
    pub_number = None

    match_assignee = re.search(r'(.*?)\s+holds the US patent', patents_info)
    if match_assignee:
        assignee = match_assignee.group(1).strip()

    match_pub_number = re.search(r'publication number ([A-Z0-9-]+)', patents_info)
    if match_pub_number:
        pub_number = match_pub_number.group(1).replace('-', '')
    
    processed_patents.append({
        'assignee': assignee,
        'publication_number': pub_number,
        'cpc_raw': record.get('cpc'),
        'citation_raw': record.get('citation')
    })

# Identify UNIV CALIFORNIA patents
univ_california_assignee_keywords = ['UNIV CALIFORNIA', 'UNIVERSITY OF CALIFORNIA']

univ_california_publication_numbers = set()
for patent in processed_patents:
    if patent['assignee'] and any(keyword.lower() in patent['assignee'].lower() for keyword in univ_california_assignee_keywords):
        if patent['publication_number']:
            univ_california_publication_numbers.add(patent['publication_number'])

# Find citing assignees and their primary CPC subclasses
relevant_citations = []

for patent in processed_patents:
    citing_assignee = patent['assignee']
    
    if citing_assignee and not any(keyword.lower() in citing_assignee.lower() for keyword in univ_california_assignee_keywords):
        try:
            citations = json.loads(patent['citation_raw'])
            for citation in citations:
                cited_pub_num = citation.get('publication_number')
                if cited_pub_num:
                    cleaned_cited_pub_num = cited_pub_num.replace('-', '')
                    if cleaned_cited_pub_num in univ_california_publication_numbers:
                        # Found a patent citing UNIV CALIFORNIA and not assigned to UNIV CALIFORNIA
                        try:
                            cpc_codes = json.loads(patent['cpc_raw'])
                            primary_cpc_subclass = None
                            for cpc_entry in cpc_codes:
                                if cpc_entry.get('code'):
                                    primary_cpc_subclass = cpc_entry['code'].split('/')[0]
                                    break # Take the first available CPC code as primary
                            
                            if primary_cpc_subclass:
                                relevant_citations.append({'assignee': citing_assignee, 'cpc_subclass': primary_cpc_subclass})
                        except (json.JSONDecodeError, TypeError):
                            pass # Handle cases where cpc field might be malformed or None
                        break # Move to the next citing patent once one relevant citation is found
        except (json.JSONDecodeError, TypeError):
            pass # Handle cases where citation field might be malformed or None

# Remove duplicate (assignee, cpc_subclass) pairs
# Using a DataFrame for easy dropping of duplicates
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
