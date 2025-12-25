code = """import json
import re
import pandas as pd

# Load the full result from the file
with open(locals()['var_function-call-8448093354361830252'], 'r') as f:
    publication_data = json.load(f)

df = pd.DataFrame(publication_data)

# Function to extract assignee from Patents_info
def extract_assignee_robust(patents_info):
    # Prioritize extracting assignee from the beginning of the string or before 'holds'
    match_holds = re.search(r'(.*?)\s+holds the US patent', patents_info)
    if match_holds:
        return match_holds.group(1).strip()
    
    # Fallback to extracting the first significant capitalized phrase that looks like an organization name
    # This is a heuristic and might need further refinement based on actual data patterns
    match_start = re.match(r'^([A-Z0-9][A-Z0-9\s&.-]+?(?:CO|LTD|INC|UNIV|UNIVERSITY|CORP|LLC|GMBH|SAS|AG|SA|PLC|NV|BV))\b', patents_info)
    if match_start:
        return match_start.group(1).strip()
        
    return None

# Apply the function to create a new 'assignee' column
df['assignee'] = df['Patents_info'].apply(extract_assignee_robust)

# Filter patents assigned to UNIV CALIFORNIA (case-insensitive and partial match)
univ_california_patents = df[df['assignee'].str.contains('UNIV CALIFORNIA', na=False, case=False)]

# Extract publication numbers of UNIV CALIFORNIA patents
univ_california_publication_numbers = set()
for index, row in univ_california_patents.iterrows():
    match = re.search(r'publication number ([A-Z0-9-]+)', row['Patents_info'])
    if match:
        pub_num = match.group(1).replace('-', '') # Remove hyphens for consistent comparison
        univ_california_publication_numbers.add(pub_num)

# Initialize a list to store unique (citing assignee, primary CPC subclass) pairs
relevant_citations = []

# Iterate through all patents to find those citing UNIV CALIFORNIA patents
for index, row in df.iterrows():
    citing_assignee = row['assignee']
    if citing_assignee and 'UNIV CALIFORNIA' not in citing_assignee.upper(): # Exclude UNIV CALIFORNIA itself
        try:
            citations = json.loads(row['citation'])
            for citation in citations:
                cited_pub_num = citation.get('publication_number')
                if cited_pub_num:
                    cited_pub_num_cleaned = cited_pub_num.replace('-', '')
                    if cited_pub_num_cleaned in univ_california_publication_numbers:
                        # Extract primary CPC subclass
                        cpc_codes = json.loads(row['cpc'])
                        primary_cpc_subclass = None
                        for cpc_entry in cpc_codes:
                            if cpc_entry.get('code'):
                                primary_cpc_subclass = cpc_entry['code'].split('/')[0] # Get the subclass part
                                break # Take the first available CPC code as primary if no 'first' or 'inventive' is explicitly marked as such
                        
                        if primary_cpc_subclass:
                            relevant_citations.append({'assignee': citing_assignee, 'cpc_subclass': primary_cpc_subclass})
                        break # Move to the next citing patent once one relevant citation is found
        except json.JSONDecodeError:
            continue

# Remove duplicate (assignee, cpc_subclass) pairs
unique_relevant_citations = pd.DataFrame(relevant_citations).drop_duplicates().to_dict(orient='records')

# Extract unique CPC subclass symbols to query for their full titles
unique_cpc_subclass_symbols = list(set([item['cpc_subclass'] for item in unique_relevant_citations]))

print('__RESULT__:')
print(json.dumps({'unique_relevant_citations': unique_relevant_citations, 'unique_cpc_subclass_symbols': unique_cpc_subclass_symbols}))"""

env_args = {'var_function-call-8448093354361830252': 'file_storage/function-call-8448093354361830252.json', 'var_function-call-14330967010767219437': []}

exec(code, env_args)
