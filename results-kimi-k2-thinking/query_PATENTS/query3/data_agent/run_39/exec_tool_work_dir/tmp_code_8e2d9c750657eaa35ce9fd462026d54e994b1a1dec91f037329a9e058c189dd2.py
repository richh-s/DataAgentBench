code = """import json
import re

# Load UNIV CALIFORNIA patents data and extract CPC codes
uc_file = locals()['var_functions.query_db:50']
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

# Extract all unique CPC codes from UNIV CALIFORNIA patents
uc_cpc_codes = set()
for patent in uc_patents:
    cpc_data_str = patent.get('cpc', '[]')
    try:
        cpc_data = json.loads(cpc_data_str)
        for cpc_entry in cpc_data:
            code = cpc_entry.get('code', '')
            if code:
                # Extract main subclass (first part before /)
                if '/' in code:
                    main_class = code.split('/')[0]
                    uc_cpc_codes.add(main_class)
                else:
                    uc_cpc_codes.add(code)
    except:
        # Skip malformed entries
        continue

print(f"Found {len(uc_cpc_codes)} unique CPC codes from UNIV CALIFORNIA patents")
print("First 20 CPC codes:", list(uc_cpc_codes)[:20])

# Query CPC definitions for these codes
cpc_codes_list = list(uc_cpc_codes)
result = {
    'total_cpc_codes': len(cpc_codes_list),
    'cpc_codes': cpc_codes_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'uc_pub_to_cpc': {}, 'uc_pub_numbers': []}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': 'file_storage/functions.execute_python:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'uc_pub_count': 54, 'citation_count': 0, 'citations': []}, 'var_functions.query_db:44': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.execute_python:46': {'uc_pub_numbers': ['CN-103687626-A', 'AU-2003297741-A1', 'US-2017281687-A1', 'US-2019209590-A1', 'US-6750960-B2', 'WO-2024112568-A1', 'US-2020025859-A1', 'US-2021039104-A1', 'HK-1250569-A1', 'IL-274176-A', 'US-2005234013-A1', 'EP-0826155-A4', 'EP-3668487-A4', 'AU-6535890-A', 'WO-2020055916-A9', 'AU-2005269556-A1', 'CA-2283629-C', 'MX-2013002850-A', 'ID-23426-A', 'US-5304932-A', 'WO-2010045542-A3', 'EP-2210307-A4', 'US-2010025717-A1', 'US-7745569-B2', 'WO-2017214343-A1', 'AU-2409401-A', 'US-2021282642-A1', 'US-2003112494-A1', 'WO-2017136335-A1', 'US-7052856-B2', 'US-2018243924-A1', 'WO-2012158833-A3', 'KR-20110004413-A', 'EP-4284234-A1', 'CA-2550552-A1', 'WO-2024044766-A3', 'CA-2718348-C', 'WO-2023212447-A2', 'KR-20050085437-A', 'US-2017145219-A1', 'AU-2017356943-A1', 'AU-5938296-A', 'US-11421276-B2', 'HK-1052178-A1', 'US-2019328740-A1', 'US-2022074631-A1', 'AU-2010214112-B2', 'WO-2023239670-A1', 'AU-2898989-A', 'AU-2019275518-B2', 'EP-1212462-A1', 'WO-2023225482-A3', 'US-2022018060-A1', 'CA-3161617-A1', 'CA-2562038-C', 'US-6767662-B2', 'PE-20130764-A1', 'CN-102584712-A', 'US-11546022-B2', 'AU-2004253879-A1', 'KR-20160119166-A', 'WO-2018026404-A3', 'US-2020283856-A1', 'IL-244029-A0', 'US-10744347-B2', 'CN-100339724-C', 'US-2021000566-A1', 'JP-2014224156-A', 'US-2021101879-A1', 'CN-102067370-B', 'US-2019169580-A1', 'US-9061071-B2', 'AU-2008349842-A1', 'US-2004115131-A1', 'RO-70061-A', 'AU-2003247814-A1', 'WO-2012162563-A2', 'US-2023155090-A1', 'US-2021002329-A1', 'US-5547866-A', 'AU-2015364602-B2', 'US-11014955-B2', 'CA-2298540-A1', 'US-2021181673-A1', 'WO-2019067860-A1', 'TW-201925402-A', 'US-10359432-B2', 'US-2006051790-A1', 'KR-20200041324-A', 'CN-103189548-A', 'JP-2005104983-A', 'US-11072681-B2', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2006292670-A1', 'CN-101584047-A', 'WO-2021102420-A1', 'AU-3353000-A', 'US-2023321419-A1', 'US-6980295-B2', 'US-2009031436-A1', 'US-11376346-B2', 'WO-2019173834-A1', 'US-6237292-B1', 'US-12025581-B2', 'US-2017087258-A1', 'WO-2014152660-A1', 'PT-2970346-T', 'US-11667770-B2', 'JP-2009260386-A', 'AU-2007297661-A1', 'WO-2018067976-A1'], 'sample_search_patterns': ['%CN-103687626-A%', '%AU-2003297741-A1%', '%US-2017281687-A1%', '%US-2019209590-A1%', '%US-6750960-B2%', '%WO-2024112568-A1%', '%US-2020025859-A1%', '%US-2021039104-A1%', '%HK-1250569-A1%', '%IL-274176-A%']}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
