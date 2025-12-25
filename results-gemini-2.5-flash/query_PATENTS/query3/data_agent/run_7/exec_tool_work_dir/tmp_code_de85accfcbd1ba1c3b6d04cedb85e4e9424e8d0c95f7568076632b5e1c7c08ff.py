code = """import json
import re
import pandas as pd

# Load the full result from the file
with open(locals()['var_function-call-8448093354361830252'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# --- Step 1: Efficiently extract assignee and publication number ---
def parse_patents_info(info_str):
    assignee = None
    pub_number = None
    match_assignee = re.search(r'(.*?)\s+holds the US patent', info_str)
    if match_assignee:
        assignee = match_assignee.group(1).strip()
    match_pub_number = re.search(r'publication number ([A-Z0-9-]+)', info_str)
    if match_pub_number:
        pub_number = match_pub_number.group(1).replace('-', '')
    return assignee, pub_number

df[['assignee', 'publication_number']] = df['Patents_info'].apply(lambda x: pd.Series(parse_patents_info(x)))

# --- Step 2: Identify UNIV CALIFORNIA patents ---
univ_california_assignee_keywords = ['UNIV CALIFORNIA', 'UNIVERSITY OF CALIFORNIA']

univ_california_publication_numbers = set(
    df[(df['assignee'].fillna('').str.contains('UNIV CALIFORNIA', case=False)) & (df['publication_number'].notna())]
    ['publication_number'].tolist()
)

# --- Step 3 & 4: Find citing assignees and their primary CPC subclasses ---
relevant_citations = []

for index, row in df.iterrows():
    citing_assignee = row['assignee']
    current_pub_number = row['publication_number'] # This is the publication number of the citing patent

    if citing_assignee and not any(keyword.lower() in citing_assignee.lower() for keyword in univ_california_assignee_keywords):
        try:
            citations = json.loads(row['citation'])
            for citation in citations:
                cited_pub_num = citation.get('publication_number')
                if cited_pub_num:
                    cleaned_cited_pub_num = cited_pub_num.replace('-', '')
                    if cleaned_cited_pub_num in univ_california_publication_numbers:
                        # Found a patent citing UNIV CALIFORNIA and not assigned to UNIV CALIFORNIA
                        try:
                            cpc_codes = json.loads(row['cpc'])
                            primary_cpc_subclass = None
                            for cpc_entry in cpc_codes:
                                if cpc_entry.get('code'):
                                    primary_cpc_subclass = cpc_entry['code'].split('/')[0]
                                    break # Take the first available CPC code as primary
                            
                            if primary_cpc_subclass:
                                relevant_citations.append({'assignee': citing_assignee, 'cpc_subclass': primary_cpc_subclass})
                        except json.JSONDecodeError:
                            pass # Handle cases where cpc field might be malformed
                        break # Move to the next citing patent once one relevant citation is found
        except json.JSONDecodeError:
            pass # Handle cases where citation field might be malformed

# Remove duplicate (assignee, cpc_subclass) pairs
unique_relevant_citations = pd.DataFrame(relevant_citations).drop_duplicates().to_dict(orient='records')

# Extract unique CPC subclass symbols to query for their full titles
unique_cpc_subclass_symbols = list(set([item['cpc_subclass'] for item in unique_relevant_citations]))

print('__RESULT__:')
print(json.dumps({'unique_relevant_citations': unique_relevant_citations, 'unique_cpc_subclass_symbols': unique_cpc_subclass_symbols}))"""

env_args = {'var_function-call-8448093354361830252': 'file_storage/function-call-8448093354361830252.json', 'var_function-call-14330967010767219437': []}

exec(code, env_args)
