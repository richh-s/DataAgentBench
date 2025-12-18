code = """import json
import re
import pandas as pd

# Load the full result from the file
with open(locals()[\'var_function-call-8448093354361830252\'], \'r\') as f:
    publication_data = json.load(f)

# Step 1: Parse and structure all relevant data from the raw records once
processed_records = []
for record in publication_data:
    patents_info = record.get(\'Patents_info\', \'\')
    assignee = None
    pub_number = None
    cpc_codes_list = []
    citation_list = []

    # Extract assignee
    match_assignee = re.search(r\'(.*?)\\\\s+holds the US patent\', patents_info)
    if match_assignee:
        assignee = match_assignee.group(1).strip()
    
    # Extract publication number
    match_pub_number = re.search(r\'publication number ([A-Z0-9-]+)\', patents_info)
    if match_pub_number:
        pub_number = match_pub_number.group(1).replace(\'-\', \'\')

    # Parse CPC codes
    try:
        cpc_codes_list = [cpc_entry[\'code\'] for cpc_entry in json.loads(record.get(\'cpc\', \'[]\')) if cpc_entry.get(\'code\')]
    except (json.JSONDecodeError, TypeError):\
        pass

    # Parse citations
    try:
        citation_list = [c[\'publication_number\'].replace(\'-\', \'\') for c in json.loads(record.get(\'citation\', \'[]\')) if c.get(\'publication_number\')]
    except (json.JSONDecodeError, TypeError):\
        pass

    processed_records.append({\n        \'assignee\': assignee,\n        \'publication_number\': pub_number,\n        \'cpc_codes\': cpc_codes_list,\n        \'citations\': citation_list\n    })\n\n# Convert to DataFrame for easier filtering and manipulation\ndf_publications = pd.DataFrame(processed_records)\n\n# Filter out rows with None in critical columns early\ndf_publications = df_publications.dropna(subset=[\'assignee\', \'publication_number\'])\n\n# Step 2: Identify UNIV CALIFORNIA patents\nuniv_california_assignee_keywords = [\'UNIV CALIFORNIA\', \'UNIVERSITY OF CALIFORNIA\']\nis_unif_california = df_publications[\'assignee\'].apply(lambda x: any(keyword.lower() in x.lower() for keyword in univ_california_assignee_keywords))\n\nuniv_california_pub_numbers = set(df_publications[is_unif_california][\'publication_number\'].tolist())\n\n# Step 3: Find citing assignees and their primary CPC subclasses\nrelevant_citations_set = set() # Use a set of tuples for efficient duplicate removal\n\n# Iterate through publications that are NOT assigned to UNIV CALIFORNIA\nfor index, row in df_publications[~is_unif_california].iterrows():\n    citing_assignee = row[\'assignee\']\n    \n    # Check if this patent cites any of the UNIV CALIFORNIA patents\n    if set(row[\'citations\']).intersection(unif_california_pub_numbers):\n        # Extract the primary CPC subclass (first available code)\n        if row[\'cpc_codes\']:\n            primary_cpc_subclass = row[\'cpc_codes\'][0].split(\'/\')[0]\n            relevant_citations_set.add((citing_assignee, primary_cpc_subclass))\n\n# Convert the set of tuples back to a list of dictionaries\nunique_relevant_citations = [{\'assignee\': assignee, \'cpc_subclass\': cpc} for assignee, cpc in relevant_citations_set]\n\n# Extract unique CPC subclass symbols to query for their full titles\nunique_cpc_subclass_symbols = list(set([item[\'cpc_subclass\'] for item in unique_relevant_citations]))\n\nprint(\'__RESULT__:\')\nprint(json.dumps({\'unique_relevant_citations\': unique_relevant_citations, \'unique_cpc_subclass_symbols\': unique_cpc_subclass_symbols}))\n"""

env_args = {'var_function-call-8448093354361830252': 'file_storage/function-call-8448093354361830252.json', 'var_function-call-14330967010767219437': []}

exec(code, env_args)
