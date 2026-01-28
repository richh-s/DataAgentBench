code = """import json
import re

# Load data from storage using string keys
all_patents_key = 'var_functions.query_db:22'
california_patents_key = 'var_functions.query_db:6'

# Get all patents
all_patents_data = locals()[all_patents_key]
if isinstance(all_patents_data, str) and '.json' in all_patents_data:
    with open(all_patents_data, 'r') as f:
        all_patents = json.load(f)
else:
    all_patents = all_patents_data

# Get California patents
california_patents_data = locals()[california_patents_key]
if isinstance(california_patents_data, str) and '.json' in california_patents_data:
    with open(california_patents_data, 'r') as f:
        california_patents = json.load(f)
else:
    california_patents = california_patents_data

# Extract California publication numbers into a set
california_pub_set = set()
for patent in california_patents:
    info_str = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in info_str:
        pub_match = re.search(r'pub(?:lication)?\s*number\s*([A-Z0-9\-]+)', info_str, re.IGNORECASE)
        if pub_match:
            pub_num = pub_match.group(1)
            california_pub_set.add(pub_num)

# Find patents that cite California patents
results = []
for patent in all_patents:
    info_str = patent.get('Patents_info', '')
    citations = patent.get('citation', '')
    
    if not citations or citations == '[]':
        continue
    
    try:
        citation_list = json.loads(citations)
        citing_pubs = [c.get('publication_number', '') for c in citation_list]
        
        # Check if any citation is a California patent
        for cite_pub in citing_pubs:
            if cite_pub and any(cal_pub in cite_pub for cal_pub in california_pub_set):
                # Extract assignee from the citing patent
                assignee_match = re.search(r'^(\b[A-Z][A-Z0-9\&\.\s\-\,]+?)(?:\s+(?:holds|owns|is assigned|is owned by|holds the)|\b)', info_str)
                if assignee_match:
                    assignee = assignee_match.group(1).strip()
                    # Exclude UNIV CALIFORNIA itself
                    if 'UNIV CALIFORNIA' not in assignee:
                        results.append({
                            'citing_assignee': assignee,
                            'cited_california_patent': cite_pub,
                            'citing_patent_info': info_str
                        })
                break
    except:
        pass

# Count assignees
from collections import Counter
assignee_counts = Counter([r['citing_assignee'] for r in results])

print('__RESULT__:')
print(json.dumps({
    'total_california_patents': len(california_pub_set),
    'total_citing_patents': len(results),
    'unique_assignees': len(assignee_counts),
    'top_assignees': assignee_counts.most_common(10),
    'sample_results': results[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.execute_python:16': {'total_patents': 100, 'sample_assignees': ['UNIV CALIFORNIA', 'the TW patent filing (app', 'UNIV CALIFORNIA', 'the AU patent application (no', 'the US patent application (no', 'UNIV CALIFORNIA', 'UNIV CALIFORNIA', 'the EP patent application (ID EP-00992018-A)', 'UNIV CALIFORNIA AT SAN DIEGO', 'the US patent application (number US-55161904-A)']}, 'var_functions.query_db:18': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}, {'Patents_info': 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.'}, {'Patents_info': 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.'}, {'Patents_info': 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.'}, {'Patents_info': 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'EAGLE TECH LLC holds the US patent filing (application no. US-201916510650-A), with publication number US-11018783-B2.'}, {'Patents_info': 'LUTRON TECH CO LLC holds the US patent application (no. US-201916557179-A), with pub. number US-10904976-B2.'}, {'Patents_info': 'ALLISON TRANSM INC holds the US application (no. US-201916558689-A), with publication number US-10704655-B2.'}], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'total_california_patents': 32, 'sample_pub_numbers': ['US-11421276-B2', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'US-2019169580-A1', 'US-2020283856-A1']}}

exec(code, env_args)
