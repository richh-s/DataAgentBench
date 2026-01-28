code = """import json
import re

# Load all patents to examine citation patterns more carefully
all_patents_file = locals()['var_functions.query_db:22']
if isinstance(all_patents_file, str) and '.json' in all_patents_file:
    with open(all_patents_file, 'r') as f:
        all_patents = json.load(f)
else:
    all_patents = all_patents_file

# Let's examine citation field more carefully
citation_samples = []
for i, patent in enumerate(all_patents[:50]):
    info = patent.get('Patents_info', '')
    citations = patent.get('citation', '')
    
    if citations and citations != '[]':
        try:
            cites = json.loads(citations)
            # Count citation types
            app_cites = len([c for c in cites if c.get('category') == 'APP'])
            sea_cites = len([c for c in cites if c.get('category') == 'SEA'])
            
            citation_samples.append({
                'index': i,
                'info_preview': info[:100],
                'total_citations': len(cites),
                'app_citations': app_cites,
                'sea_citations': sea_cites,
                'sample_cites': [c.get('publication_number', '') for c in cites[:3]]
            })
        except:
            pass

print('__RESULT__:')
print(json.dumps(citation_samples[:20]))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.execute_python:16': {'total_patents': 100, 'sample_assignees': ['UNIV CALIFORNIA', 'the TW patent filing (app', 'UNIV CALIFORNIA', 'the AU patent application (no', 'the US patent application (no', 'UNIV CALIFORNIA', 'UNIV CALIFORNIA', 'the EP patent application (ID EP-00992018-A)', 'UNIV CALIFORNIA AT SAN DIEGO', 'the US patent application (number US-55161904-A)']}, 'var_functions.query_db:18': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}, {'Patents_info': 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.'}, {'Patents_info': 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.'}, {'Patents_info': 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.'}, {'Patents_info': 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'EAGLE TECH LLC holds the US patent filing (application no. US-201916510650-A), with publication number US-11018783-B2.'}, {'Patents_info': 'LUTRON TECH CO LLC holds the US patent application (no. US-201916557179-A), with pub. number US-10904976-B2.'}, {'Patents_info': 'ALLISON TRANSM INC holds the US application (no. US-201916558689-A), with publication number US-10704655-B2.'}], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'total_california_patents': 32, 'sample_pub_numbers': ['US-11421276-B2', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'US-2019169580-A1', 'US-2020283856-A1']}, 'var_functions.execute_python:30': {'total_california_patents': 32, 'total_citing_patents': 0, 'unique_assignees': 0, 'top_assignees': [], 'sample_results': []}, 'var_functions.execute_python:38': {'uc_patents': 32, 'citing_patents': 0, 'unique_assignees': 0, 'top_assignees': [], 'samples': []}}

exec(code, env_args)
