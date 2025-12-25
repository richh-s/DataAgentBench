code = """import json
import re

# Load the full JSON data from the file
with open(locals()['var_function-call-17586866852388310109'], 'r') as f:
    patents_data_uc = json.load(f)

univ_california_patent_info = {}
for patent in patents_data_uc:
    patents_info = patent.get('Patents_info', '')
    cpc_codes_str = patent.get('cpc', '[]')

    # Extract publication number
    pub_number_match = re.search(r'pub\. number ([A-Z0-9\-]+)', patents_info)
    publication_number = pub_number_match.group(1) if pub_number_match else None

    # Extract first CPC code
    cpc_codes = json.loads(cpc_codes_str)
    first_cpc_code = cpc_codes[0]['code'] if cpc_codes and cpc_codes[0]['code'] else None

    if publication_number and first_cpc_code:
        univ_california_patent_info[publication_number] = first_cpc_code

print("__RESULT__:")
print(json.dumps(univ_california_patent_info))"""

env_args = {'var_function-call-9991954280777560525': ['publicationinfo'], 'var_function-call-17198847221600567673': [], 'var_function-call-10301112809646823471': 'file_storage/function-call-10301112809646823471.json', 'var_function-call-4997015473653672400': [], 'var_function-call-10862841933274024202': 'file_storage/function-call-10862841933274024202.json', 'var_function-call-7620258214686575354': 'file_storage/function-call-7620258214686575354.json', 'var_function-call-17586866852388310109': 'file_storage/function-call-17586866852388310109.json'}

exec(code, env_args)
