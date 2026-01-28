code = """import json

# Debug: show all locals
all_locals = list(locals().keys())
print('Available variables:', all_locals[:20])  # Show first 20

# Try to find our data
univ_california_key = 'var_functions.query_db:12'
publications_key = 'var_functions.query_db:28'

if univ_california_key in locals():
    print('Found UNIV CALIFORNIA data')
    univ_data = locals()[univ_california_key]
    print('Type:', type(univ_data))
    if isinstance(univ_data, str) and '.json' in univ_data:
        print('Loading from file:', univ_data)
        with open(univ_data, 'r') as f:
            univ_data = json.load(f)
    print('Records:', len(univ_data))
else:
    print('UNIV CALIFORNIA key not found')

if publications_key in locals():
    print('Found publications data')
    pub_data = locals()[publications_key]
    print('Type:', type(pub_data))
    if isinstance(pub_data, str) and '.json' in pub_data:
        print('Loading from file:', pub_data)
        with open(pub_data, 'r') as f:
            pub_data = json.load(f)
    print('Records:', len(pub_data))
else:
    print('Publications key not found')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': 'Test output', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
