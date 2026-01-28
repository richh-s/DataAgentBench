code = """import json

# Let's first see what variables are available
available_vars = list(vars().keys())
print('Available variables:', available_vars)

# Now let's check the actual variable values
univ_california_data = None
publications_data = None
citations_data = None

for key, value in vars().items():
    if 'query_db_12' in str(key):
        print(f'Found UNIV CALIFORNIA data variable: {key}')
        univ_california_data = value
    elif 'query_db_8' in str(key):
        print(f'Found publications data variable: {key}')
        publications_data = value
    elif 'query_db_6' in str(key):
        print(f'Found citations data variable: {key}')
        citations_data = value

print('\nData types:')
print('UNIV CALIFORNIA:', type(univ_california_data))
print('Publications:', type(publications_data))
print('Citations:', type(citations_data))

# Check if they are file paths
if isinstance(univ_california_data, str) and '.json' in univ_california_data:
    print('UNIV CALIFORNIA data is in file:', univ_california_data)
    with open(univ_california_data, 'r') as f:
        univ_california_data = json.load(f)

if isinstance(publications_data, str) and '.json' in publications_data:
    print('Publications data is in file:', publications_data)
    with open(publications_data, 'r') as f:
        publications_data = json.load(f)

if isinstance(citations_data, str) and '.json' in citations_data:
    print('Citations data is in file:', citations_data)
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

print('\nAfter loading:')
print('UNIV CALIFORNIA records:', len(univ_california_data) if univ_california_data else 0)
print('Publications records:', len(publications_data) if publications_data else 0)
print('Citations records:', len(citations_data) if citations_data else 0)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
