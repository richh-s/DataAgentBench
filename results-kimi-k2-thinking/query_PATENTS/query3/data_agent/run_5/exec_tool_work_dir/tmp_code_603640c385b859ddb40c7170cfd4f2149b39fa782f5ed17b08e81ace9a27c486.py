code = """import json
import re

# Load UNIV CALIFORNIA data to get CPC codes for their patents
uc_file_path = locals()['var_functions.query_db:6']
with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Get UC publication numbers and their CPC codes
uc_cpc_codes = {}
for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc = patent.get('cpc', '[]')
    
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        pub_num = pub_match.group(1)
        
        try:
            cpc_data = json.loads(cpc)
            cpc_codes_list = [item['code'] for item in cpc_data if 'code' in item]
            uc_cpc_codes[pub_num] = list(set(cpc_codes_list))
        except:
            uc_cpc_codes[pub_num] = []

print("Loading all patent data...")
# Load all patents to search for UC citations
all_patents_file = locals()['var_functions.query_db:24']
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

print(f"Total patents loaded: {len(all_patents)}")

# Create UC publication number set for fast lookup
uc_pub_set = set(uc_cpc_codes.keys())
print(f"UC publication numbers: {len(uc_pub_set)}")
print(f"Sample UC pubs: {list(uc_pub_set)[:10]}")

# Search for citations to UC patents
citation_map = {}  # Maps citing patent info to cited UC patents
uc_cited_by_assignee = {}  # Maps UC patent to list of citing assignees

for patent in all_patents:
    patents_info = patent['Patents_info']
    citation = patent.get('citation', '[]')
    patent_cpc = patent.get('cpc', '[]')
    
    # Skip UNIV CALIFORNIA patents
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    try:
        citation_list = json.loads(citation)
        for cite in citation_list:
            cited_pub = cite.get('publication_number', '')
            if not cited_pub:
                continue
                
            # Flexible matching for UC publication numbers
            for uc_pub in uc_pub_set:
                uc_parts = uc_pub.split('-')
                if len(uc_parts) < 3:
                    continue
                
                uc_country, uc_number, uc_kind = uc_parts[0], uc_parts[1], uc_parts[2]
                
                # Check various matching patterns
                matches = (
                    uc_pub == cited_pub or  # Exact match
                    uc_pub.replace('-', '') in cited_pub.replace('-', '') or  # Dashless match
                    (uc_country in cited_pub and uc_number in cited_pub) or  # Country and number
                    (uc_number in cited_pub and uc_kind in cited_pub)  # Number and kind
                )
                
                if matches:
                    # Extract assignee
                    assignee_match = re.search(r'^([A-Z][A-Z0-9\s&.,-]+?)\s+(holds|hold|is|assigned)', patents_info)
                    if not assignee_match:
                        assignee_match = re.search(r'^(In [A-Z]{2},\s+)?([A-Z][A-Z0-9\s&.,-]+?)\s+(holds|hold|is owned by|is assigned to)', patents_info)
                        assignee = assignee_match.group(2).strip() if assignee_match else "UNKNOWN"
                    else:
                        assignee = assignee_match.group(1).strip()
                    
                    assignee = re.sub(r'^In [A-Z]{2},\s*', '', assignee)
                    
                    if assignee and 'UNIV CALIFORNIA' not in assignee:
                        # Record this citation
                        citation_key = f"{assignee}|{patents_info[:200]}"
                        if citation_key not in citation_map:
                            citation_map[citation_key] = {
                                'assignee': assignee,
                                'cited_uc_pubs': set(),
                                'citing_cpc_codes': set(),
                                'cited_cpc_codes': set()
                            }
                        
                        citation_map[citation_key]['cited_uc_pubs'].add(uc_pub)
                        
                        # Add CPC codes from the cited UC patent
                        citation_map[citation_key]['cited_cpc_codes'].update(uc_cpc_codes.get(uc_pub, []))
                        
                        # Add CPC codes from the citing patent
                        try:
                            citing_cpc_data = json.loads(patent_cpc)
                            citing_cpc_list = [item['code'] for item in citing_cpc_data if 'code' in item]
                            citation_map[citation_key]['citing_cpc_codes'].update(citing_cpc_list)
                        except:
                            pass
                        
                        # Track UC patent being cited
                        if uc_pub not in uc_cited_by_assignee:
                            uc_cited_by_assignee[uc_pub] = []
                        uc_cited_by_assignee[uc_pub].append(assignee)
                        
    except:
        continue

# Convert sets to lists for JSON serialization
processed_citations = []
for key, data in citation_map.items():
    processed_citations.append({
        'assignee': data['assignee'],
        'cited_uc_pubs': list(data['cited_uc_pubs']),
        'cited_cpc_codes': list(data['cited_cpc_codes']),
        'citing_cpc_codes': list(data['citing_cpc_codes']),
        'total_cited': len(data['cited_uc_pubs']),
        'total_cpc_codes': len(data['cited_cpc_codes']) + len(data['citing_cpc_codes'])
    })

# Sort by number of citations
processed_citations.sort(key=lambda x: x['total_cited'], reverse=True)

print(f"Found {len(processed_citations)} unique assignee/citation patterns")
print(f"UC patents cited by others: {len(uc_cited_by_assignee)}/{len(uc_pub_set)}")

# Show top results
print("\nTop citing assignees:")
for i, citation in enumerate(processed_citations[:10]):
    print(f"{i+1}. {citation['assignee']}: cites {citation['total_cited']} UC patents, has {len(citation['citing_cpc_codes'])} CPC codes")

print('__RESULT__:')
print(json.dumps({
    'citing_assignees_found': len(processed_citations),
    'uc_patents_cited': len(uc_cited_by_assignee),
    'top_citations': processed_citations[:20],  # Top 20
    'uc_cpc_codes': uc_cpc_codes  # All UC CPC codes for reference
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'uc_patents_count': 114, 'sample_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'sample_cpc_codes': ['A61K38/16', 'A61K39/4611', 'B64C39/02', 'C12Q1/485', 'C12N15/1044', 'C07D409/08', 'H01M8/0232', 'C09J11/04', 'B01L2300/0883', 'C07B59/001']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'uc_publication_numbers_count': 114, 'sample_uc_pub_numbers': ['US-6980295-B2', 'US-9061071-B2', 'AU-2008349842-A1', 'CN-102584712-A', 'AU-2007297661-A1', 'US-7052856-B2', 'EP-4284234-A1', 'WO-2018067976-A1', 'KR-20160119166-A', 'IL-274176-A']}, 'var_functions.execute_python:20': {'uc_pub_count': 114, 'sample_pub_numbers': ['WO-2017214343-A1', 'US-2004115131-A1', 'AU-2409401-A', 'US-2021039104-A1', 'CA-2562038-C', 'KR-20050085437-A', 'AU-2015364602-B2', 'IL-274176-A', 'AU-2010214112-B2', 'US-2017281687-A1', 'CA-2718348-C', 'WO-2012158833-A3', 'US-2019209590-A1', 'CA-3161617-A1', 'JP-S6163700-A', 'US-6980295-B2', 'US-11376346-B2', 'WO-2010045542-A3', 'AU-5938296-A', 'WO-2020055916-A9']}, 'var_functions.execute_python:22': {'checking': 'test'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_citing_patents_found': 0, 'unique_citing_assignees': 0, 'top_citing_assignees': []}, 'var_functions.execute_python:28': {'total_citations_found': 0, 'unique_citing_assignees': 0, 'citing_assignees': [], 'sample_cpc_codes': []}, 'var_functions.execute_python:30': {'uc_pub_count': 114, 'citation_pub_count': 289279, 'overlap_count': 0, 'sample_uc_pub': ['AU-2008349842-A1', 'WO-2023225482-A3', 'US-11667770-B2', 'JP-2014224156-A', 'US-2005234013-A1', 'US-5547866-A', 'US-10359432-B2', 'CN-101584047-A', 'US-2019169580-A1', 'US-9061071-B2', 'PT-2970346-T', 'JP-S6163700-A', 'CA-2718348-C', 'WO-2010045542-A3', 'US-2006292670-A1', 'US-2017145219-A1', 'ID-23426-A', 'WO-2012162563-A2', 'AU-5938296-A', 'CA-2562038-C'], 'sample_citation_pub': ['DE-2744547-A1', 'US-6978890-B2', 'US-2009200494-A1', 'US-5661134-A', 'KR-20020047199-A', 'US-2018363019-A1', 'KR-100853216-B1', 'US-2003231140-A1', 'DE-10323239-A1', 'US-6468685-B1']}, 'var_functions.execute_python:32': {'total_citation_matches': 0, 'unique_citing_assignees': 0, 'top_10_assignees': []}, 'var_functions.execute_python:36': {'uc_patents': 114, 'citation_numbers': 289279, 'exact_matches': 0, 'partial_matches_found': 0}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
