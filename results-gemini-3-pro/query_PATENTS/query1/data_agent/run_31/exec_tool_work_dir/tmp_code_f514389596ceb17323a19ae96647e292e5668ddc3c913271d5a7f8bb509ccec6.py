code = """import json
import re

with open(locals()['var_function-call-15653579714414806466'], 'r') as f:
    patent_data = json.load(f)

max_year = 0
for entry in patent_data:
    d = str(entry.get('filing_date'))
    match = re.search(r'(19|20)\d{2}', d)
    if match:
        y = int(match.group(0))
        if y > max_year:
            max_year = y

print("__RESULT__:")
print(max_year)"""

env_args = {'var_function-call-8605716924548816221': 'file_storage/function-call-8605716924548816221.json', 'var_function-call-3390649654093091550': [{'COUNT(*)': '277813'}], 'var_function-call-15653579714414806466': 'file_storage/function-call-15653579714414806466.json', 'var_function-call-3948899147405893627': [], 'var_function-call-6555282486067486608': {'sample_years': [], 'min_year': None, 'max_year': None, 'codes_found_sample': ['F41H', 'H02J', 'D06B', 'B25D', 'Y02E', 'F28D', 'G05D', 'G11B', 'F41C', 'G04F'], 'level5_sample': ['F41H', 'H02J', 'D06B', 'B25D', 'F22D', 'Y02E', 'F28D', 'C08H', 'G05D', 'G11B']}, 'var_function-call-17022073147038242497': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-17189268383737464155': [None, None, None], 'var_function-call-11122473221756250122': ["'dated 5th March 2019'", "'March the 18th, 2019'"], 'var_function-call-8771736156658332328': ['A23J', 'A23P', 'A24F', 'A41H', 'A44D', 'A61G', 'A62C', 'A63K', 'B02C', 'B03C', 'B04B', 'B05B', 'B07B', 'B08B', 'B09B', 'B09C', 'B21B', 'B21C', 'B21H', 'B22D', 'B22F', 'B25D', 'B27C', 'B27G', 'B27M', 'B33Y', 'B60D', 'B60L', 'B60P', 'B63C', 'B63G', 'B65G', 'B66F', 'C01D', 'C01F', 'C01G', 'C01P', 'C07B', 'C21B', 'C21C', 'C21D', 'C22B', 'D03J', 'D06H', 'E01C', 'E01D', 'E02D', 'E03B', 'E03D', 'E03F', 'E04B', 'E04G', 'E21F', 'F02K', 'F04F', 'F16M', 'F16N', 'F17B', 'F23N', 'F25J', 'F41C', 'F42C', 'G01D', 'G01H', 'G01K', 'G01L', 'G01P', 'G01S', 'G04F', 'G06J', 'G06N', 'G06Q', 'G06T', 'G06V', 'G08B', 'G09F', 'G10L', 'G16B', 'G16H', 'G16Y', 'G21F', 'G21G', 'H01M', 'H02B', 'H02G', 'H02J', 'H03H', 'H04S', 'Y02B', 'Y02E', 'Y02T', 'Y04S']}

exec(code, env_args)
