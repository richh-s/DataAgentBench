code = """import json
import re
from collections import defaultdict

# Get the UNIV CALIFORNIA patents data from storage
uc_patents = var_functions.query_db:8

print(f"Total UNIV CALIFORNIA patents loaded: {len(uc_patents)}")

# Extract publication numbers from UNIV CALIFORNIA patents
uc_pub_numbers = []
uc_patents_dict = {}  # Map pub number to patent data

for patent in uc_patents:
    patents_info = patent['Patents_info']
    # Extract publication number using regex
    match = re.search(r'pub\. number ([^\.]+)', patents_info)
    if match:
        pub_num = match.group(1).strip()
        uc_pub_numbers.append(pub_num)
        uc_patents_dict[pub_num] = patent

print(f"Extracted {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")
print(f"Sample: {uc_pub_numbers[:5]}")

# Now find all patents that cite these UNIV CALIFORNIA patents
# First, let's get a sample of all patents with citations
print('__RESULT__:')
print(json.dumps({
    "total_uc_patents": len(uc_patents),
    "uc_pub_numbers_count": len(uc_pub_numbers),
    "sample_uc_pub_numbers": uc_pub_numbers[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
