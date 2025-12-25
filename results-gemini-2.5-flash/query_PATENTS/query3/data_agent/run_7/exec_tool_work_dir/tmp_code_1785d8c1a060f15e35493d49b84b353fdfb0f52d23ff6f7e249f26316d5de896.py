code = """import json
import re
# No pandas for core logic to avoid potential overhead given previous timeouts

# Load the full result from the file
with open(locals()['var_function-call-8448093354361830252'], 'r') as f:
    publication_data = json.load(f)

# Step 1: Parse and structure all relevant data from the raw records once
processed_records = []
for record in publication_data:
    patents_info = record.get('Patents_info', '')
    assignee = None
    pub_number = None
    cpc_codes_list = []
    citation_list = []

    # Extract assignee from Patents_info
    match_assignee = re.search(r'(.*?)\\s+holds the US patent', patents_info)
    if match_assignee:
        assignee = match_assignee.group(1).strip()
    
    # Extract publication number from Patents_info
    match_pub_number = re.search(r'publication number ([A-Z0-9-]+)', patents_info)
    if match_pub_number:
        pub_number = match_pub_number.group(1).replace('-', '') # Clean publication number

    # Parse CPC codes. Handle potential JSON errors or empty lists.
    try:
        cpc_codes_list = [cpc_entry['code'] for cpc_entry in json.loads(record.get('cpc', '[]')) if cpc_entry.get('code')]
    except (json.JSONDecodeError, TypeError):
        pass # cpc_codes_list remains empty

    # Parse citations. Handle potential JSON errors or empty lists.
    try:
        citation_list = [c['publication_number'].replace('-', '') for c in json.loads(record.get('citation', '[]')) if c.get('publication_number')]
    except (json.JSONDecodeError, TypeError):
        pass # citation_list remains empty

    # Only include records that have a valid assignee and publication number for further processing
    if assignee and pub_number:
        processed_records.append({
            'assignee': assignee,
            'publication_number': pub_number,
            'cpc_codes': cpc_codes_list,
            'citations': citation_list
        })

# Step 2: Identify UNIV CALIFORNIA patents and their publication numbers
univ_california_assignee_keywords = ['UNIV CALIFORNIA', 'UNIVERSITY OF CALIFORNIA']
univ_california_publication_numbers = set()

for record in processed_records:
    # Case-insensitive check for UNIV CALIFORNIA or UNIVERSITY OF CALIFORNIA in assignee name
    if record['assignee'] and any(keyword.lower() in record['assignee'].lower() for keyword in univ_california_assignee_keywords):
        univ_california_publication_numbers.add(record['publication_number'])

# Step 3: Find citing assignees and their primary CPC subclasses
relevant_citations_set = set() # Use a set of tuples (assignee, cpc_subclass) for efficient duplicate removal

for record in processed_records:
    citing_assignee = record['assignee']
    
    # Exclude UNIV CALIFORNIA itself from citing assignees
    if citing_assignee and not any(keyword.lower() in citing_assignee.lower() for keyword in univ_california_assignee_keywords):
        
        # Check if this patent cites any of the UNIV CALIFORNIA patents using set intersection for efficiency
        if set(record['citations']).intersection(univ_california_publication_numbers):
            
            # Extract the primary CPC subclass (the first available CPC code, split by '/')
            if record['cpc_codes']:
                first_cpc_code = record['cpc_codes'][0]
                primary_cpc_subclass = first_cpc_code.split('/')[0] if '/' in first_cpc_code else first_cpc_code
                relevant_citations_set.add((citing_assignee, primary_cpc_subclass))

# Convert the set of tuples back to a list of dictionaries for output
unique_relevant_citations = [{'assignee': assignee, 'cpc_subclass': cpc} for assignee, cpc in relevant_citations_set]

# Extract unique CPC subclass symbols to query for their full titles from CPCDefinition_database
unique_cpc_subclass_symbols = list(set([item['cpc_subclass'] for item in unique_relevant_citations]))

print('__RESULT__:')
print(json.dumps({'unique_relevant_citations': unique_relevant_citations, 'unique_cpc_subclass_symbols': unique_cpc_subclass_symbols}))"""

env_args = {'var_function-call-8448093354361830252': 'file_storage/function-call-8448093354361830252.json', 'var_function-call-14330967010767219437': []}

exec(code, env_args)
