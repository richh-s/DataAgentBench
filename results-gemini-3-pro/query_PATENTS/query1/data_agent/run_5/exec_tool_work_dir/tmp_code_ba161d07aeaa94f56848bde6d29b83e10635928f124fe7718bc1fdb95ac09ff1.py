code = """import json
import re

# Load publication info
with open(locals()['var_function-call-3342335174744796923'], 'r') as f:
    pub_data = json.load(f)

print("Type:", type(pub_data))
print("Length:", len(pub_data))
if len(pub_data) > 0:
    print("First item:", pub_data[0])
    date_val = pub_data[0].get('filing_date')
    print("Filing date val:", date_val)
    print("Type of date:", type(date_val))
    
    match = re.search(r'\b(19|20)\d{2}\b', str(date_val))
    print("Regex match:", match)

# Check specifically for 2022
count_2022 = 0
for entry in pub_data:
    d = str(entry.get('filing_date'))
    if '2022' in d:
        count_2022 += 1

print("Count with '2022' substring:", count_2022)

print("__RESULT__:")
print("DEBUG_DONE")"""

env_args = {'var_function-call-6966994197956776721': 'file_storage/function-call-6966994197956776721.json', 'var_function-call-6966994197956777598': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-7852690627219261662': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}, {'symbol': 'A01B1/02', 'level': '8.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-14140994627699433809': [{'count(*)': '277813'}], 'var_function-call-5220002852052879670': 'file_storage/function-call-5220002852052879670.json', 'var_function-call-3342335174744796923': 'file_storage/function-call-3342335174744796923.json', 'var_function-call-7004644481195674653': [], 'var_function-call-1960842569152316207': [{'filing_date': '24th Jan 2020'}, {'filing_date': 'January 29th, 2020'}, {'filing_date': 'on January 31st, 2020'}, {'filing_date': '10th February 2020'}, {'filing_date': '14th of February, 2020'}, {'filing_date': 'on February 28th, 2020'}, {'filing_date': 'Feb 28th, 2020'}, {'filing_date': 'dated 2nd March 2020'}, {'filing_date': '5th of March, 2020'}, {'filing_date': 'dated 11th March 2020'}], 'var_function-call-5274327421915137173': {'year_counts': {}, 'examples_2022': []}}

exec(code, env_args)
