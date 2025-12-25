code = """import json
import re
import collections

# Load publication info
with open(locals()['var_function-call-3342335174744796923'], 'r') as f:
    pub_data = json.load(f)

# Helper to extract year
def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(19|20)\d{2}\b', date_str)
    if match:
        return int(match.group(0))
    return None

year_counts = collections.Counter()
examples_2022 = []

for entry in pub_data:
    d = entry.get('filing_date', '')
    y = extract_year(d)
    if y:
        year_counts[y] += 1
        if y == 2022 and len(examples_2022) < 5:
            examples_2022.append(d)

print("__RESULT__:")
print(json.dumps({"year_counts": year_counts, "examples_2022": examples_2022}))"""

env_args = {'var_function-call-6966994197956776721': 'file_storage/function-call-6966994197956776721.json', 'var_function-call-6966994197956777598': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-7852690627219261662': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-14140994627699433809': [{'count(*)': '277813'}], 'var_function-call-5220002852052879670': 'file_storage/function-call-5220002852052879670.json', 'var_function-call-3342335174744796923': 'file_storage/function-call-3342335174744796923.json', 'var_function-call-7004644481195674653': [], 'var_function-call-1960842569152316207': [{'filing_date': '24th Jan 2020'}, {'filing_date': 'January 29th, 2020'}, {'filing_date': 'on January 31st, 2020'}, {'filing_date': '10th February 2020'}, {'filing_date': '14th of February, 2020'}, {'filing_date': 'on February 28th, 2020'}, {'filing_date': 'Feb 28th, 2020'}, {'filing_date': 'dated 2nd March 2020'}, {'filing_date': '5th of March, 2020'}, {'filing_date': 'dated 11th March 2020'}]}

exec(code, env_args)
