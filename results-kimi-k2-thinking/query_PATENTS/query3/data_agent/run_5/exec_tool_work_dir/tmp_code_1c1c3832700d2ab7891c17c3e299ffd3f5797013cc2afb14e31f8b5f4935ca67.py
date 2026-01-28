code = """import json
import re

# Load UNIV CALIFORNIA publication numbers
uc_file_path = locals()['var_functions.query_db:6']
with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Create a normalized mapping for UC publication numbers
uc_pub_map = {}  # Maps various formats to standard format
uc_cpc_map = {}

for patent in uc_patents:
    patents_info = patent['Patents_info']
    cpc = patent.get('cpc', '[]')
    
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        standard_pub_num = pub_match.group(1)
        # Create normalized versions
        parts = standard_pub_num.split('-')
        if len(parts) >= 3:
            country = parts[0]
            number = parts[1]
            kind = parts[2]
            
            # Create alternative formats
            normalized = f"{country}{number}{kind}"
            minimal = number
            
            uc_pub_map[standard_pub_num] = {
                'standard': standard_pub_num,
                'normalized': normalized,
                'minimal': minimal,
                'country': country
            }
            
            # Store CPC codes
            try:
                cpc_codes = json.loads(cpc)
                cpc_list = [code['code'] for code in cpc_codes]
                uc_cpc_map[standard_pub_num] = cpc_list
            except:
                uc_cpc_map[standard_pub_num] = []

print('UC publication numbers map size:', len(uc_pub_map))

# Load all patents to find citations with flexible matching
all_patents_file = locals()['var_functions.query_db:24']
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

# Test: Look for citations that might match a known UC patent
known_uc_patent = list(uc_pub_map.keys())[0]
print('Testing with UC patent:', known_uc_patent)
print('UC CPC codes for this patent:', uc_cpc_map.get(known_uc_patent, []))

# Check a few patents that cite this (if any exist)
citing_examples = []
for patent in all_patents[:1000]:  # Check first 1000 for examples
    citation = patent.get('citation', '[]')
    patents_info = patent.get('Patents_info', '')
    
    # Skip UC patents
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    try:
        citation_list = json.loads(citation)
        for cite in citation_list:
            cited_pub = cite.get('publication_number', '')
            if known_uc_patent in cited_pub or (known_uc_patent.split('-')[1] in cited_pub and known_uc_patent.split('-')[0] in cited_pub):
                citing_examples.append({
                    'citing_patent': patents_info[:100],
                    'cited_as': cited_pub,
                    'standard_uc': known_uc_patent
                })
    except:
        continue

print('Direct matches found:', len(citing_examples))
for ex in citing_examples[:3]:
    print(ex)

# Now do broader matching to find actual citations
citation_matches = []
matched_uc_pubs = set()

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    citation = patent.get('citation', '[]')
    patent_cpc = patent.get('cpc', '[]')
    
    # Skip UNIV CALIFORNIA patents and unknown assignees
    if 'UNIV CALIFORNIA' in patents_info:
        continue
    
    # Extract assignee more carefully
    assignee = "UNKNOWN"
    # Pattern 1: "ASSIGNEE holds/is/assigned..."
    am1 = re.search(r'^([A-Z][A-Z0-9\s&.,-]+?)\s+(holds|hold|is|assigned|owns)', patents_info)
    # Pattern 2: "In XX, ASSIGNEE..."
    am2 = re.search(r'^(In [A-Z]{2},\s+)([A-Z][A-Z0-9\s&.,-]+?)\s+(holds|hold|is owned by|is assigned to|owns)', patents_info)
    # Pattern 3: application number then assignee
    am3 = re.search(r'\)\s*is\s*(owned by|assigned to)\s+([A-Z][A-Z0-9\s&.,-]+)', patents_info)
    
    if am1:
        assignee = am1.group(1).strip()
    elif am2:
        assignee = am2.group(2).strip()
    elif am3:
        assignee = am3.group(2).strip()
    
    assignee = re.sub(r'^In [A-Z]{2},\s*', '', assignee)
    if not assignee or len(assignee) < 3:
        continue
    
    # Check if this patent cites any UC patent
    try:
        citation_list = json.loads(citation)
        for cite in citation_list:
            cited_pub = cite.get('publication_number', '')
            
            # Compare with each UC publication number
            for uc_pub, uc_formats in uc_pub_map.items():
                # Various matching strategies
                if (uc_pub in cited_pub or  # Standard format
                    uc_formats['normalized'] in cited_pub or  # Without dashes
                    (uc_formats['country'] in cited_pub and uc_formats['minimal'] in cited_pub) or  # Country + number
                    uc_formats['minimal'] == cited_pub.replace('-', '')):  # Just the number
                    
                    citation_matches.append({
                        'citing_assignee': assignee,
                        'cited_uc_pub': uc_pub,
                        'cited_as': cited_pub
                    })
                    matched_uc_pubs.add(uc_pub)
                    break
    except:
        continue

print('\\nFlexible matching found', len(citation_matches), 'citations')
print('Matched UC patents:', len(matched_uc_pubs))

# Get unique assignees and their citation counts
assignee_stats = {}
for match in citation_matches:
    assignee = match['citing_assignee']
    if assignee not in assignee_stats:
        assignee_stats[assignee] = set()
    assignee_stats[assignee].add(match['cited_uc_pub'])

# Sort and prepare final list
assignee_list = [{'assignee': k, 'cited_uc_pubs': list(v), 'count': len(v)} 
                 for k, v in assignee_stats.items() if 'UNIV CALIFORNIA' not in k]
assignee_list.sort(key=lambda x: x['count'], reverse=True)

print('\\nUnique citing assignees (excluding UC):', len(assignee_list))
print('Top assignees:')
for a in assignee_list[:10]:
    print(f"  {a['assignee']}: {a['count']} UC patents cited")

print('__RESULT__:')
print(json.dumps({
    'total_citation_matches': len(citation_matches),
    'unique_citing_assignees': len(assignee_list),
    'top_10_assignees': assignee_list[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'uc_patents_count': 114, 'sample_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'sample_cpc_codes': ['A61K38/16', 'A61K39/4611', 'B64C39/02', 'C12Q1/485', 'C12N15/1044', 'C07D409/08', 'H01M8/0232', 'C09J11/04', 'B01L2300/0883', 'C07B59/001']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'uc_publication_numbers_count': 114, 'sample_uc_pub_numbers': ['US-6980295-B2', 'US-9061071-B2', 'AU-2008349842-A1', 'CN-102584712-A', 'AU-2007297661-A1', 'US-7052856-B2', 'EP-4284234-A1', 'WO-2018067976-A1', 'KR-20160119166-A', 'IL-274176-A']}, 'var_functions.execute_python:20': {'uc_pub_count': 114, 'sample_pub_numbers': ['WO-2017214343-A1', 'US-2004115131-A1', 'AU-2409401-A', 'US-2021039104-A1', 'CA-2562038-C', 'KR-20050085437-A', 'AU-2015364602-B2', 'IL-274176-A', 'AU-2010214112-B2', 'US-2017281687-A1', 'CA-2718348-C', 'WO-2012158833-A3', 'US-2019209590-A1', 'CA-3161617-A1', 'JP-S6163700-A', 'US-6980295-B2', 'US-11376346-B2', 'WO-2010045542-A3', 'AU-5938296-A', 'WO-2020055916-A9']}, 'var_functions.execute_python:22': {'checking': 'test'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_citing_patents_found': 0, 'unique_citing_assignees': 0, 'top_citing_assignees': []}, 'var_functions.execute_python:28': {'total_citations_found': 0, 'unique_citing_assignees': 0, 'citing_assignees': [], 'sample_cpc_codes': []}, 'var_functions.execute_python:30': {'uc_pub_count': 114, 'citation_pub_count': 289279, 'overlap_count': 0, 'sample_uc_pub': ['AU-2008349842-A1', 'WO-2023225482-A3', 'US-11667770-B2', 'JP-2014224156-A', 'US-2005234013-A1', 'US-5547866-A', 'US-10359432-B2', 'CN-101584047-A', 'US-2019169580-A1', 'US-9061071-B2', 'PT-2970346-T', 'JP-S6163700-A', 'CA-2718348-C', 'WO-2010045542-A3', 'US-2006292670-A1', 'US-2017145219-A1', 'ID-23426-A', 'WO-2012162563-A2', 'AU-5938296-A', 'CA-2562038-C'], 'sample_citation_pub': ['DE-2744547-A1', 'US-6978890-B2', 'US-2009200494-A1', 'US-5661134-A', 'KR-20020047199-A', 'US-2018363019-A1', 'KR-100853216-B1', 'US-2003231140-A1', 'DE-10323239-A1', 'US-6468685-B1']}}

exec(code, env_args)
