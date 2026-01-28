code = """import json
import re
from collections import defaultdict

# Load UNIV CALIFORNIA patents
uni_cal_file = str(locals()['var_functions.query_db:18'])
with open(uni_cal_file, 'r') as f:
    uni_cal_patents = json.load(f)

print("Loading UNIV CALIFORNIA patents...")
uni_cal_pub_nums = []
uni_cal_cpc = defaultdict(set)

for patent in uni_cal_patents:
    patents_info = patent['Patents_info']
    pub_match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if not pub_match:
        pub_match = re.search(r'publication\s+no\.\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if not pub_match:
        pub_match = re.search(r'publication\s+number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    
    if pub_match:
        pub_num = pub_match.group(1)
        uni_cal_pub_nums.append(pub_num)
        
        if patent['cpc']:
            try:
                cpc_list = json.loads(patent['cpc'])
                for cpc_entry in cpc_list:
                    if cpc_entry.get('code'):
                        subclass = cpc_entry['code'][:4]
                        uni_cal_cpc[pub_num].add(subclass)
            except:
                pass

uni_cal_set = set(uni_cal_pub_nums)
print("Found", len(uni_cal_set), "UNIV CALIFORNIA publication numbers")

# Load all patent records to find citations
all_patents_file = str(locals()['var_functions.query_db:22'])
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

print("Scanning", len(all_patents), "patents for citations to UNIV CALIFORNIA...")

# Find citing patents
citations_data = []
for patent in all_patents:
    if patent['citation']:
        try:
            citations = json.loads(patent['citation'])
            for citation in citations:
                cited_pub = citation.get('publication_number', '')
                if cited_pub and cited_pub in uni_cal_set:
                    # Found a citation! Get the citing patent's assignee
                    patents_info = patent['Patents_info']
                    citations_data.append({
                        'cited_pub': cited_pub,
                        'citing_info': patents_info,
                        'citation': citation
                    })
        except:
            pass

print("Found", len(citations_data), "citations to UNIV CALIFORNIA patents")

# Process the citations to extract assignees
assignee_citations = defaultdict(lambda: defaultdict(set))

for entry in citations_data:
    citing_info = entry['citing_info']
    cited_pub = entry['cited_pub']
    
    # Extract assignee from citing patent info
    # Try different patterns to extract the assignee name
    patterns = [
        r'^(.+?)(?:\s+(?:hold|holds|is|from|belonging to|assigned to))?\s+(?:holds?|is|from|belonging to|assigned to)\s+(?:the\s+)?(?:[A-Z]{2})\s+(?:patent|application)',
        r'^(.+?)(?:\s+holds?)\s+(?:the\s+)?(?:[A-Z]{2})\s+(?:patent|application)',
        r'^(.+?)\s+holds?',  # Simple case
    ]
    
    assignee = "UNKNOWN"
    for pattern in patterns:
        match = re.search(pattern, citing_info, re.IGNORECASE)
        if match:
            possible_assignee = match.group(1).strip()
            if possible_assignee and len(possible_assignee) < 100:  # Sanity check
                assignee = possible_assignee
                break
    
    # Skip UNIV CALIFORNIA itself
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Get CPC codes for the cited UNIV CALIFORNIA patent
    cpc_codes = uni_cal_cpc.get(cited_pub, [])
    for cpc in cpc_codes:
        assignee_citations[assignee][cpc].add(cited_pub)

# Get unique assignees and their CPC codes
citing_assignees_cpcs = {}
for assignee, cpc_dict in assignee_citations.items():
    citing_assignees_cpcs[assignee] = list(cpc_dict.keys())

print("Unique citing assignees (excluding UNIV CALIFORNIA):", len(citing_assignees_cpcs))
print("Sample assignees and their CPCs:")
for assignee, cpcs in list(citing_assignees_cpcs.items())[:5]:
    print(f"  {assignee}: {cpcs}")

print("__RESULT__:")
print(json.dumps({
    'num_citing_assignees': len(citing_assignees_cpcs),
    'sample_assignees': dict(list(citing_assignees_cpcs.items())[:10]),
    'cpc_codes_needed': sorted(list(set(cpc for cpcs in citing_assignees_cpcs.values() for cpc in cpcs)))
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'total': 5, 'uni_california': 0}, 'var_functions.query_db:16': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_uni_cal_patents': 169, 'sample_pubs': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017194630-A1', 'JP-S6163700-A', 'US-2017281687-A1', 'EP-1224461-B1', 'AU-2003247814-A1', 'AU-2017356943-A1'], 'sample_cpc': {'US-2022074631-A1': ['F28D', 'Y02B', 'F25B'], 'TW-201925402-A': ['C08K', 'B82Y', 'C09D', 'C09J']}}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.list_db:24': ['cpc_definition']}

exec(code, env_args)
