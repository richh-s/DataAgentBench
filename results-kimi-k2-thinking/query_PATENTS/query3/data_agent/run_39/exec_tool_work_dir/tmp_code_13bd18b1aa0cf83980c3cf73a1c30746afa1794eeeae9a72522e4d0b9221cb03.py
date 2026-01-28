code = """import json
import re

# Load data from previous queries
uc_data_file = locals()['var_functions.query_db:30']
with open(uc_data_file, 'r') as f:
    uc_patents = json.load(f)

# Load citing patents data
citing_data_file = locals()['var_functions.query_db:40']
with open(citing_data_file, 'r') as f:
    citing_patents = json.load(f)

print(f"UNIV CALIFORNIA patents: {len(uc_patents)}")
print(f"Citing patents (sample): {len(citing_patents)}")

# Extract UNIV CALIFORNIA publication numbers and their CPC codes
uc_pub_to_cpc = {}
uc_pub_numbers = set()

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc_data = patent.get('cpc', '[]')
    
    # Extract publication number
    match = re.search(r'(?:pub\.|publication|pub\s+no|publication\s+no|pub\s+number|has\s+publication\s+no|has\s+pub\.|with\s+pub\.)\s+(?:[A-Z]+-)?([A-Z]{2}-\d+-[A-Z]\d*)', patents_info, re.IGNORECASE)
    if not match:
        match = re.search(r'publication\s+number\s+([A-Z]{2}-\d+-[A-Z]\d*)', patents_info, re.IGNORECASE)
    
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.add(pub_num)
        uc_pub_to_cpc[pub_num] = cpc_data

print(f"Extracted {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")

# Now scan through citing patents to find those that cite UNIV CALIFORNIA patents
citations_found = []

for patent in citing_patents:
    patents_info = patent['Patents_info']
    citation_data = patent.get('citation', '[]')
    cpc_data = patent.get('cpc', '[]')
    
    # Skip if this is also a UNIV CALIFORNIA patent
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Parse citation JSON
    try:
        citations = json.loads(citation_data)
    except:
        continue
    
    # Check each citation
    for citation in citations:
        cited_pub_num = citation.get('publication_number', '')
        if cited_pub_num in uc_pub_numbers:
            # Extract assignee from citing patent
            assignee_match = re.search(r'^([A-Z][A-Z\s&\-]+)(?:holds|hold the|is|hold|assigned to|owned by|belonging to)', patents_info)
            if assignee_match:
                assignee = assignee_match.group(1).strip()
                # Exclude UNIV CALIFORNIA variants
                if 'UNIV CALIFORNIA' not in assignee:
                    citations_found.append({
                        'citing_assignee': assignee,
                        'cited_pub_num': cited_pub_num,
                        'citing_patent': patents_info,
                        'cited_cpc': uc_pub_to_cpc[cited_pub_num]
                    })

print(f"Found {len(citations_found)} citations from non-UC assignees to UC patents")

# Show sample results
if citations_found:
    print("Sample citation:")
    print(json.dumps(citations_found[0], indent=2))

result = {
    'uc_pub_count': len(uc_pub_numbers),
    'citation_count': len(citations_found),
    'citations': citations_found[:100]  # Limit for now
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'uc_pub_to_cpc': {}, 'uc_pub_numbers': []}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': 'file_storage/functions.execute_python:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
