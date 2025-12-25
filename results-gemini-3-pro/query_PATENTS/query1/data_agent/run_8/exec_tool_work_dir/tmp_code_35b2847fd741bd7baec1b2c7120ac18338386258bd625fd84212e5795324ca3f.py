code = """import re
import json

dates = ["dated 5th March 2019", "March the 18th, 2019", "29th March 2019", "on March 29th, 2019", "2nd April 2019"]
pattern = re.compile(r'\d{4}')

results = {}
for d in dates:
    matches = pattern.findall(d)
    results[d] = matches

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-18281922881261155290': ['publicationinfo'], 'var_function-call-18281922881261156991': ['cpc_definition'], 'var_function-call-3853867713196752715': 'file_storage/function-call-3853867713196752715.json', 'var_function-call-3853867713196752716': [{'count': '277813'}], 'var_function-call-3853867713196752717': [{'count': '677'}], 'var_function-call-4744927068419664464': 'file_storage/function-call-4744927068419664464.json', 'var_function-call-4744927068419665303': 'file_storage/function-call-4744927068419665303.json', 'var_function-call-4885472280726247165': [], 'var_function-call-11578580308570018388': {'min_year': None, 'max_year': None, 'total_records': 277813, 'records_with_date_match': 0, 'unique_cpcs_found': 0, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'sample_cpcs': [], 'sample_level5': ['C22F', 'C09K', 'C09B', 'B81B', 'F16F', 'B62B', 'F27D', 'B02B', 'A61Q', 'F41G'], 'sample_counts': {}}}

exec(code, env_args)
