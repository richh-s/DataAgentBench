code = """# First, let's extract all UNIV CALIFORNIA patents and their publication numbers
import json
import re
import sqlite3
import pandas as pd

# Access the result using locals()
uc_data_file = locals()['var_functions.query_db:12']

with open(uc_data_file, 'r') as f:
    uc_patents = json.load(f)

# Extract publication numbers from UNIV CALIFORNIA patents
uc_pub_numbers = []
for patent in uc_patents:
    patents_info = patent['Patents_info']
    # Extract publication number using regex
    match = re.search(r'(?:pub\. number|publication number|has pub\. number|with publication number|with pub\. number) ([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.append(pub_num)

print('__RESULT__:')
print(json.dumps({
    'total_uc_patents': len(uc_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'sample_pub_numbers': uc_pub_numbers[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:10': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}, {'Patents_info': 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.'}, {'Patents_info': 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.'}, {'Patents_info': 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.'}, {'Patents_info': 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.'}, {'Patents_info': 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.'}, {'Patents_info': 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'}, {'Patents_info': 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.'}, {'Patents_info': 'Patent filing (app. number AU-2898989-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2898989-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the RO patent filing (application no. RO-7944874-A), with pub. number RO-70061-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the WO patent filing (application number US-2017015812-W), with publication number WO-2017136335-A1.'}, {'Patents_info': 'In WO, the patent application (no. US-2019059638-W) is held by UNIV CALIFORNIA and has publication no. WO-2020096950-A1.'}, {'Patents_info': 'The WO patent filing (application no. US-2020061827-W) is assigned to UNIV CALIFORNIA and has pub. number WO-2021102420-A1.'}, {'Patents_info': 'In WO, the patent filing (app. number US-2012039471-W) is belonging to UNIV CALIFORNIA and has pub. number WO-2012162563-A2.'}, {'Patents_info': 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201816612511-A) is assigned to UNIV CALIFORNIA and has pub. number US-11376346-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-201715646074-A), with publication no. US-2017369950-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the KR patent filing (app. number KR-20187008669-A), with publication no. KR-20180041236-A.'}]}

exec(code, env_args)
