code = """import json
import re

# Access the full result from the previous query
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    publications = json.load(f)

print(f"Total publications found: {len(publications)}")

# Extract UNIV CALIFORNIA patents and their publication numbers
uc_patents = []
for pub in publications:
    patents_info = pub.get('Patents_info', '')
    # Extract publication number
    match = re.search(r'(US|WO|EP|JP|CN|TW|KR|DE|GB|FR)-[A-Z0-9-]+-A[0-9]*', patents_info)
    if match:
        pub_num = match.group(0)
        uc_patents.append({
            'pub_num': pub_num,
            'patents_info': patents_info,
            'citation': pub.get('citation', '[]'),
            'cpc': pub.get('cpc', '[]')
        })

print(f"\nTotal UNIV CALIFORNIA patents identified: {len(uc_patents)}")
print("\nSample publications:")
for i, patent in enumerate(uc_patents[:5]):
    print(f"{i+1}. {patent['pub_num']}")
    print(f"   Info: {patent['patents_info'][:100]}...")
    
# Show how citations look
if uc_patents:
    print(f"\nSample citation data:")
    citations = json.loads(uc_patents[0]['citation'])
    print(f"Number of citations in first patent: {len(citations)}")
    if citations:
        print(f"Sample citation: {citations[0]}")

# Show how CPC codes look
print(f"\nSample CPC data:")
cpc_codes = json.loads(uc_patents[0]['cpc'])
print(f"Number of CPC codes in first patent: {len(cpc_codes)}")
if cpc_codes:
    print(f"Sample CPC: {cpc_codes[0]}")

print('__RESULT__:')
print(json.dumps({'total_publications': len(publications), 'uc_patents': len(uc_patents)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
