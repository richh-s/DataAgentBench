code = """import json
import re

pub_file = locals()['var_function-call-17751803970902191593']
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

year_pattern = re.compile(r'\b(19|20)\d{2}\b')
years = []
for r in pub_data:
    fd = r.get('filing_date')
    if fd:
        m = year_pattern.search(fd)
        if m:
            years.append(int(m.group(0)))

if years:
    print("__RESULT__:")
    print(json.dumps({"min": min(years), "max": max(years), "count_2022": years.count(2022)}))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "No years found"}))"""

env_args = {'var_function-call-9665950342090287602': 'file_storage/function-call-9665950342090287602.json', 'var_function-call-9665950342090285761': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-16928258735931206764': [{'COUNT(*)': '277813'}], 'var_function-call-13650408886884758128': 'file_storage/function-call-13650408886884758128.json', 'var_function-call-17751803970902191593': 'file_storage/function-call-17751803970902191593.json', 'var_function-call-2714896827906959896': [], 'var_function-call-15280219420561285810': {'level5_sample': ['G07D', 'B68C', 'F41C', 'B60F', 'B27D'], 'level5_lengths': [4], 'years_found': [], 'symbols_matched_count': 0}, 'var_function-call-9633243674128522724': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-16820435960730373528': []}

exec(code, env_args)
