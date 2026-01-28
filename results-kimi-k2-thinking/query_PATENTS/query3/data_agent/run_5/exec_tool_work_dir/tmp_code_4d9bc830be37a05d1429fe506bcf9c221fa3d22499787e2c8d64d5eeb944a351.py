code = """import json
import re

# Load UNIV CALIFORNIA data
uc_file_path = locals()['var_functions.query_db:6']
with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Get UC publication numbers and their CPC codes
uc_pub_numbers = set()
uc_cpc_codes = {}  # Map pub number to list of CPC codes

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc = patent.get('cpc', '[]')
    
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        pub_num = pub_match.group(1)
        uc_pub_numbers.add(pub_num)
        
        # Parse CPC codes
        try:
            cpc_data = json.loads(cpc)
            cpc_codes_list = [item['code'] for item in cpc_data if 'code' in item]
            # Get unique CPC codes
            unique_cpc = list(set(cpc_codes_list))
            uc_cpc_codes[pub_num] = unique_cpc
        except:
            uc_cpc_codes[pub_num] = []

print('UC publication numbers found:', len(uc_pub_numbers))
print('Sample UC patents:')
for i, pub in enumerate(list(uc_pub_numbers)[:10]):
    print(f"  {pub}: {uc_cpc_codes.get(pub, [])[:3]}...")

# Load all patents and search for citations to UC patents
all_patents_file = locals()['var_functions.query_db:24']
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# The key insight: We need to match the publication numbers as they appear in citations
# Let me extract ALL citation publication numbers to see the format diversity
all_citation_nums = set()
for patent in all_patents:
    citation = patent.get('citation', '[]')
    try:
        citation_list = json.loads(citation)
        for cite in citation_list:
            pub_num = cite.get('publication_number', '')
            if pub_num:
                all_citation_nums.add(pub_num)
    except:
        continue

print('\\nTotal unique citation publication numbers:', len(all_citation_nums))
print('Sample citation numbers:')
for i, num in enumerate(list(all_citation_nums)[:15]):
    print(f"  {num}")

# Check if there's ANY overlap (exact match)
exact_overlap = uc_pub_numbers.intersection(all_citation_nums)
print('\\nExact matches (UC patents cited by others):', len(exact_overlap))

if len(exact_overlap) == 0:
    print('No exact matches found. Let\'s try partial matching...')
    
    # Create simplified UC numbers for matching (remove dashes, extract core numbers)
    uc_core_numbers = {}
    for uc_pub in uc_pub_numbers:
        parts = uc_pub.split('-')
        if len(parts) >= 2:
            country = parts[0]
            number = parts[1]
            kind = parts[2] if len(parts) > 2 else ''
            
            # Different matching strategies
            uc_core_numbers[uc_pub] = {
                'full': uc_pub,
                'country_number': f"{country}{number}",
                'just_number': number,
                'with_kind': f"{country}{number}{kind}",
                'dashed_pattern': uc_pub.replace('-', '')
            }
    
    # Check for partial matches
    partial_matches = []
    for uc_pub, formats in uc_core_numbers.items():
        for cite_num in all_citation_nums:
            if (formats['full'] == cite_num or
                formats['country_number'] == cite_num or
                formats['dashed_pattern'] == cite_num or
                formats['with_kind'] == cite_num or
                (formats['country_number'] in cite_num and len(cite_num) <= len(formats['country_number']) + 2)):
                partial_matches.append((uc_pub, cite_num))
    
    print('Partial matches found:', len(partial_matches))
    for i, (uc_pub, cite_num) in enumerate(partial_matches[:10]):
        print(f"  UC: {uc_pub}  Cited as: {cite_num}")

print('__RESULT__:')
print(json.dumps({
    'uc_pub_count': len(uc_pub_numbers),
    'citation_pub_count': len(all_citation_nums),
    'exact_matches': len(exact_overlap),
    'partial_matches': len(partial_matches) if 'partial_matches' in locals() else 0,
    'sample_uc_pub_numbers': list(uc_pub_numbers)[:20],
    'sample_citation_numbers': list(all_citation_nums)[:20]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'uc_patents_count': 114, 'sample_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'sample_cpc_codes': ['A61K38/16', 'A61K39/4611', 'B64C39/02', 'C12Q1/485', 'C12N15/1044', 'C07D409/08', 'H01M8/0232', 'C09J11/04', 'B01L2300/0883', 'C07B59/001']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'uc_publication_numbers_count': 114, 'sample_uc_pub_numbers': ['US-6980295-B2', 'US-9061071-B2', 'AU-2008349842-A1', 'CN-102584712-A', 'AU-2007297661-A1', 'US-7052856-B2', 'EP-4284234-A1', 'WO-2018067976-A1', 'KR-20160119166-A', 'IL-274176-A']}, 'var_functions.execute_python:20': {'uc_pub_count': 114, 'sample_pub_numbers': ['WO-2017214343-A1', 'US-2004115131-A1', 'AU-2409401-A', 'US-2021039104-A1', 'CA-2562038-C', 'KR-20050085437-A', 'AU-2015364602-B2', 'IL-274176-A', 'AU-2010214112-B2', 'US-2017281687-A1', 'CA-2718348-C', 'WO-2012158833-A3', 'US-2019209590-A1', 'CA-3161617-A1', 'JP-S6163700-A', 'US-6980295-B2', 'US-11376346-B2', 'WO-2010045542-A3', 'AU-5938296-A', 'WO-2020055916-A9']}, 'var_functions.execute_python:22': {'checking': 'test'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_citing_patents_found': 0, 'unique_citing_assignees': 0, 'top_citing_assignees': []}, 'var_functions.execute_python:28': {'total_citations_found': 0, 'unique_citing_assignees': 0, 'citing_assignees': [], 'sample_cpc_codes': []}, 'var_functions.execute_python:30': {'uc_pub_count': 114, 'citation_pub_count': 289279, 'overlap_count': 0, 'sample_uc_pub': ['AU-2008349842-A1', 'WO-2023225482-A3', 'US-11667770-B2', 'JP-2014224156-A', 'US-2005234013-A1', 'US-5547866-A', 'US-10359432-B2', 'CN-101584047-A', 'US-2019169580-A1', 'US-9061071-B2', 'PT-2970346-T', 'JP-S6163700-A', 'CA-2718348-C', 'WO-2010045542-A3', 'US-2006292670-A1', 'US-2017145219-A1', 'ID-23426-A', 'WO-2012162563-A2', 'AU-5938296-A', 'CA-2562038-C'], 'sample_citation_pub': ['DE-2744547-A1', 'US-6978890-B2', 'US-2009200494-A1', 'US-5661134-A', 'KR-20020047199-A', 'US-2018363019-A1', 'KR-100853216-B1', 'US-2003231140-A1', 'DE-10323239-A1', 'US-6468685-B1']}, 'var_functions.execute_python:32': {'total_citation_matches': 0, 'unique_citing_assignees': 0, 'top_10_assignees': []}}

exec(code, env_args)
