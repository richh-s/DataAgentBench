code = """import json
import re

# Access storage variable
california_data = locals()['var_functions.query_db:6']

# Load data if it's a file path
if isinstance(california_data, str) and '.json' in california_data:
    with open(california_data, 'r') as f:
        california_patents = json.load(f)
else:
    california_patents = california_data

# Extract California patents and their publication numbers
california_pub_nums = []
for patent in california_patents:
    info_str = patent.get('Patents_info', '')
    
    # Check if this is actually a UNIV CALIFORNIA patent
    if 'UNIV CALIFORNIA' in info_str:
        # Extract publication number
        pub_match = re.search(r'pub(?:lication)?\s*number\s*([A-Z0-9\-]+)', info_str, re.IGNORECASE)
        if pub_match:
            pub_num = pub_match.group(1)
            california_pub_nums.append(pub_num)

result = {
    'total_california_patents': len(california_pub_nums),
    'sample_pub_numbers': california_pub_nums[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.execute_python:16': {'total_patents': 100, 'sample_assignees': ['UNIV CALIFORNIA', 'the TW patent filing (app', 'UNIV CALIFORNIA', 'the AU patent application (no', 'the US patent application (no', 'UNIV CALIFORNIA', 'UNIV CALIFORNIA', 'the EP patent application (ID EP-00992018-A)', 'UNIV CALIFORNIA AT SAN DIEGO', 'the US patent application (number US-55161904-A)']}, 'var_functions.query_db:18': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}, {'Patents_info': 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.'}, {'Patents_info': 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.'}, {'Patents_info': 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.'}, {'Patents_info': 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'EAGLE TECH LLC holds the US patent filing (application no. US-201916510650-A), with publication number US-11018783-B2.'}, {'Patents_info': 'LUTRON TECH CO LLC holds the US patent application (no. US-201916557179-A), with pub. number US-10904976-B2.'}, {'Patents_info': 'ALLISON TRANSM INC holds the US application (no. US-201916558689-A), with publication number US-10704655-B2.'}], 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
