code = """import json
import re

with open(locals()['var_function-call-7542188176596272141'], 'r') as f:
    pub_data = json.load(f)

year_pattern = re.compile(r'(19|20)\d{2}')
years = set()

for entry in pub_data:
    f_date = entry.get('filing_date')
    if f_date:
        match = year_pattern.search(f_date)
        if match:
            years.add(int(match.group(0)))

print("__RESULT__:")
print(json.dumps({"min": min(years), "max": max(years)}))"""

env_args = {'var_function-call-18438039698466275985': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-11425610840667422492': 'file_storage/function-call-11425610840667422492.json', 'var_function-call-15261515319027993325': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-3988956739634739314': [{'symbol': 'A01H', 'level': '5.0'}], 'var_function-call-16646390810544569620': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-3646825604830857458': 'file_storage/function-call-3646825604830857458.json', 'var_function-call-7247946529193589936': [{'COUNT(*)': '277813'}], 'var_function-call-7542188176596272141': 'file_storage/function-call-7542188176596272141.json', 'var_function-call-2924045124924059341': [], 'var_function-call-14784814548662281515': {'error': 'No years found'}, 'var_function-call-7127365575876393656': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019'], 'var_function-call-2295869064512019575': [{'date': 'dated 5th March 2019', 'match': None}, {'date': 'March the 18th, 2019', 'match': None}, {'date': '29th March 2019', 'match': None}, {'date': 'on March 29th, 2019', 'match': None}, {'date': '2nd April 2019', 'match': None}, {'date': 'on April 8th, 2019', 'match': None}, {'date': '15th April 2019', 'match': None}, {'date': 'April 19th, 2019', 'match': None}, {'date': '2019, April 24th', 'match': None}, {'date': 'April 26th, 2019', 'match': None}], 'var_function-call-15990137332791724935': [{'date': 'dated 5th March 2019', 'match': '2019'}, {'date': 'March the 18th, 2019', 'match': '2019'}, {'date': '29th March 2019', 'match': '2019'}, {'date': 'on March 29th, 2019', 'match': '2019'}, {'date': '2nd April 2019', 'match': '2019'}, {'date': 'on April 8th, 2019', 'match': '2019'}, {'date': '15th April 2019', 'match': '2019'}, {'date': 'April 19th, 2019', 'match': '2019'}, {'date': '2019, April 24th', 'match': '2019'}, {'date': 'April 26th, 2019', 'match': '2019'}]}

exec(code, env_args)
