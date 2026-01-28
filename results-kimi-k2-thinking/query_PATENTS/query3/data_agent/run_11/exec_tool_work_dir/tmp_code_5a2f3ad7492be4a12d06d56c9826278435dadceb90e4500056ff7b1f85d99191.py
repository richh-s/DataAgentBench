code = """import json
import re

# Load the full results from the previous query
result_file = locals()['var_functions.query_db:5']
with open(result_file, 'r') as f:
    ucs_patents = json.load(f)

print(f"Total records loaded: {len(ucs_patents)}")

# Parse UNIV CALIFORNIA patents to extract publication numbers
uc_pub_numbers = []
uc_patents_with_citations = []

for patent in ucs_patents:
    patents_info = patent.get('Patents_info', '')
    
    # Check if this is actually assigned to UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in patents_info.upper():
        # Extract publication number from Patents_info
        # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
        pub_match = re.search(r'(?:pub\. number|publication number|number)\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
        if pub_match:
            pub_num = pub_match.group(1)
            uc_pub_numbers.append(pub_num)
            
            # Also store citation info if it exists
            citations = patent.get('citation', '[]')
            if citations and citations != '[]':
                try:
                    citation_list = json.loads(citations)
                    if citation_list:
                        uc_patents_with_citations.append({
                            'publication_number': pub_num,
                            'citations': citation_list
                        })
                except:
                    pass

print(f"Found {len(uc_pub_numbers)} UNIV CALIFORNIA patents")
print(f"Sample UNIV CALIFORNIA pub numbers: {uc_pub_numbers[:5]}")
print(f"Sample patents with citations loaded: {len(uc_patents_with_citations)}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
