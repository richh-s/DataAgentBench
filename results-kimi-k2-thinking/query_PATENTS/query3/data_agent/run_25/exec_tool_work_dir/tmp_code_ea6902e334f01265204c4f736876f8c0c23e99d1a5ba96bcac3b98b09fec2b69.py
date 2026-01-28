code = """import json
import re

# Load all patents data
data = locals()['var_functions.query_db:8']
if isinstance(data, str):
    with open(data, 'r') as f:
        data = json.load(f)

# Step 1: Find all patents assigned to UNIV CALIFORNIA
uc_patents = []
uc_assignee_patterns = [
    r'owned by UNIV CALIFORNIA',
    r'assigned to UNIV CALIFORNIA',
    r'held by UNIV CALIFORNIA',
    r'belonging to UNIV CALIFORNIA',
    r'^UNIV CALIFORNIA holds',
    r'^UNIV CALIFORNIA'
]

for row in data:
    patents_info = row.get('Patents_info', '')
    if any(re.search(pattern, patents_info, re.IGNORECASE) for pattern in uc_assignee_patterns):
        uc_patents.append(row)

# Step 2: Get all publication numbers for UNIV CALIFORNIA patents
uc_pub_numbers = set()
for row in uc_patents:
    patents_info = row['Patents_info']
    # Extract publication number from the text
    pub_match = re.search(r'(?:pub\. number|publication number|publication no\.?)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        uc_pub_numbers.add(pub_match.group(1))

# Step 3: Find all patents that cite UNIV CALIFORNIA patents
citing_patents = []

for row in data:
    # Skip patents assigned to UNIV CALIFORNIA (find others that cite them)
    patents_info = row.get('Patents_info', '')
    is_uc_assigned = any(re.search(pattern, patents_info, re.IGNORECASE) for pattern in uc_assignee_patterns)
    if is_uc_assigned:
        continue
    
    # Check citations
    citation_text = row.get('citation', '')
    if citation_text and citation_text.strip() != '[]':
        try:
            citations = json.loads(citation_text)
            for cite in citations:
                pub_num = cite.get('publication_number', '')
                if pub_num and pub_num in uc_pub_numbers:
                    # This patent cites a UNIV CALIFORNIA patent
                    
                    # Extract assignee from patents_info
                    assignee = None
                    patterns = [
                        r'^(.*?) holds the US',
                        r'In US, the (?:application|patent filing|patent application) (?:\(.*?\) )?(?:is(?: belonging to| assigned to| held by| owned by))? (.+?)(?: and has|,)',
                        r'Application (?:\(.*?\) )?from US, (?:owned by|held by|assigned to|belonging to) (.+?)(?:,| with|$)',
                        r'The US (?:application|patent filing|patent application) (?:\(.*?\) )?(?:is (?:assigned to|owned by|held by|belonging to)) (.+?)(?: and has|,|\. )',
                        r'Patent (?:application|filing) (?:\(.*?\) )?(?:from US, )?(?:assigned to|held by|belonging to) (.+?)(?:,| with|$)'
                    ]
                    
                    for pattern in patterns:
                        match = re.search(pattern, patents_info, re.IGNORECASE)
                        if match:
                            assignee = match.group(1).strip()
                            break
                    
                    if assignee:
                        citing_patents.append({
                            'citing_assignee': assignee,
                            'cited_pub_number': pub_num,
                            'citing_patent_info': patents_info,
                            'cpc_data': row.get('cpc', '[]')
                        })
        except:
            pass

# Step 4: Get unique citation relationships
unique_citations = {}
for cite in citing_patents:
    key = (cite['citing_assignee'], cite['cited_pub_number'])
    if key not in unique_citations:
        unique_citations[key] = {
            'citing_assignee': cite['citing_assignee'],
            'cited_pub_number': cite['cited_pub_number'],
            'cpc_data': cite['cpc_data']
        }

result = list(unique_citations.values())

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'citations_from_other_assignees': len(result),
    'first_10_citations': result[:10]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'sample_patents_info': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.', 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.', 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.', 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.', 'Patent filing (application number US-201916399064-A) from US, held by INTEL CORP, with pub. number US-10853219-B2.', 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.', 'In US, the patent filing (application number US-201916412428-A) is belonging to INNOLUX CORP and has publication no. US-11076136-B2.', 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.', 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.', 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.', 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.', 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'Patent application (number US-201916445265-A) from US, belonging to MURATA MANUFACTURING CO, with publication number US-11601114-B2.'], 'extracted_assignees': ['PANASONIC IP MAN CO LTD', 'GLASSNER RUDOLF', 'COVESTRO LLC', 'HOMOLOGY MEDICINES INC', 'APPLETON GRP LLC', 'MEAD JOHNSON NUTRITION CO', 'WATERS TECHNOLOGIES CORP', 'MODERNATX INC', 'YOBS TECH INC', 'HONDA MOTOR CO LTD', 'INTEL CORP', 'UNIV EMORY', 'INNOLUX CORP', 'LEGACY RES AND DEVELOPMENT GROUP LLC', 'EBAY INC', 'MAHLE INT GMBH', 'RLW VIRTUAL SOLUTIONS LLC', 'BHANDARI RAJNEESH', 'TANDEM DIABETES CARE INC', 'MURATA MANUFACTURING CO']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
