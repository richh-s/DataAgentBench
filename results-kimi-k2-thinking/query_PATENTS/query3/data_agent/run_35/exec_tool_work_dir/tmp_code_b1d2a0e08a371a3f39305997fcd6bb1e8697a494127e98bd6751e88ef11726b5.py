code = """import json, os, re

# Load the data
uc_data_file = 'var_functions.query_db:58'
with open(uc_data_file, 'r') as f:
    uc_data = json.load(f)

print('Loaded', len(uc_data), 'UC California patents')

# Extract cited patents and CPC codes
cited_pub_numbers = set()
cpc_codes = set()

for record in uc_data:
    # Parse citations using regex
    cit_str = record.get('citation', '')
    if cit_str and cit_str != '[]':
        pub_matches = re.findall(r'"publication_number":\s*"([^"]+)"', cit_str)
        cited_pub_numbers.update(pub_matches)
    
    # Parse CPC codes
    cpc_str = record.get('cpc_str', '') or record.get('cpc', '')
    if cpc_str and cpc_str != '[]':
        cpc_matches = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
        cpc_codes.update(cpc_matches)

print('Unique cited patents:', len(cited_pub_numbers))
print('Unique CPC codes:', len(cpc_codes))

result = {
    'total_uc_patents': len(uc_data),
    'cited_patents': list(cited_pub_numbers),
    'cpc_codes': list(cpc_codes)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:20': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}], 'var_functions.query_db:22': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}, {'Patents_info': 'Patent filing (application number US-201916399064-A) from US, held by INTEL CORP, with pub. number US-10853219-B2.'}, {'Patents_info': 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.'}, {'Patents_info': 'In US, the patent filing (application number US-201916412428-A) is belonging to INNOLUX CORP and has publication no. US-11076136-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.'}, {'Patents_info': 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.'}, {'Patents_info': 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.'}, {'Patents_info': 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'Patent application (number US-201916445265-A) from US, belonging to MURATA MANUFACTURING CO, with publication number US-11601114-B2.'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:30': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:38': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:56': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
