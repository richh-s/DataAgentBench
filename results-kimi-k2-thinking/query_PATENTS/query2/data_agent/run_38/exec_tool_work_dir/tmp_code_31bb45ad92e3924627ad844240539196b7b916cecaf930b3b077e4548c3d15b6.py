code = """import json
import re
from collections import defaultdict

# Load the patents data
result_file = locals()['var_functions.query_db:28']
with open(result_file, 'r') as f:
    patents_data = json.load(f)

# Function to parse grant date
def parse_grant_date(date_str):
    if not date_str:
        return None, None
    # Extract year
    year_match = re.search(r'(20\d{2})', str(date_str))
    if year_match:
        year = int(year_match.group(1))
    else:
        return None, None
    
    # Extract month
    month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', str(date_str), re.IGNORECASE)
    if month_match:
        month_name = month_match.group(1).lower()
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        month = month_map.get(month_name, 0)
    else:
        month = 0
    
    return year, month

# Extract CPC counts by year for German patents
cpc_by_year = defaultdict(lambda: defaultdict(int))
total_by_year = defaultdict(int)

for patent in patents_data:
    year, month = parse_grant_date(patent.get('grant_date', ''))
    
    if year in [2017, 2018, 2019]:
        total_by_year[year] += 1
        
        # Check if it's second half for 2019
        if year == 2019 and month < 7:
            continue
            
        cpc_field = patent.get('cpc', '[]')
        if cpc_field:
            try:
                cpc_list = json.loads(cpc_field)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code and '/' in code:
                        cpc_by_year[year][code] += 1
            except:
                continue

print('__RESULT__:')
print(json.dumps({
    'total_by_year': dict(total_by_year),
    'cpc_codes_2017': len(cpc_by_year[2017]),
    'cpc_codes_2018': len(cpc_by_year[2018]),
    'cpc_codes_2019': len(cpc_by_year[2019]),
    'sample_cpcs': list(cpc_by_year[2019].keys())[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'total_records': 68, 'sample_cpc_codes': ['H02J1/10', 'H02J7/34', 'H02J7/007182', 'H02J1/10', 'H02J7/34', 'H02J7/007182'], 'sample_grant_date': '14th Aug 2019'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_records': 68, 'first_few': [{'Patents_info': 'Patent application (ID DE-102009033309-A) from DE, assigned to CONTINENTAL AUTOMOTIVE GMBH, with pub. number DE-102009033309-B4.', 'grant_date': '14th Aug 2019', 'cpc': '[\n  {\n    "code": "H02J1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/007182",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H02J1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/007182",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_de_2019': 68, 'second_half_2019': 34, 'sample_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:22': {'total_cpc_groups': 201, 'top_10_cpc': [{'cpc_code': 'F02D41/20', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W72/21', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W72/56', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W52/0261', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W52/0216', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W52/0229', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W72/0446', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W52/0251', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'F24B5/023', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'F23L15/04', 'year': 2019, 'count': 3, 'ema': 3}], 'all_cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00', 'F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02M59/102', 'F02M55/04', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'G01D11/24', 'B23K1/0016', 'B63B21/50', 'H04W72/21', 'H04W72/56', 'H04L5/0037', 'H04L1/1614']}, 'var_functions.query_db:24': [], 'var_functions.query_db:26': [{'symbol': 'F24B5/023', 'titleFull': 'Supply of primary air for combustion'}, {'symbol': 'F02D41/20', 'titleFull': 'Output circuits, e.g. for controlling currents in command coils'}, {'symbol': 'F23L15/04', 'titleFull': 'Arrangements of recuperators'}, {'symbol': 'H04W72/0446', 'titleFull': 'Resources in time domain, e.g. slots or frames'}, {'symbol': 'H04W52/0261', 'titleFull': 'Power saving arrangements in terminal devices managing power supply demand, e.g. depending on battery level'}, {'symbol': 'H04W52/0251', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of local events, e.g. events related to user activity'}, {'symbol': 'H04W52/0216', 'titleFull': 'Power saving arrangements in terminal devices managed by the network, e.g. network or access point is master and terminal is slave using a pre-established activity schedule, e.g. traffic indication frame'}, {'symbol': 'H04W52/0229', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of external events, e.g. the presence of a signal where the received signal is a wanted signal'}, {'symbol': 'H04W72/21', 'titleFull': 'Control channels or signalling for resource management in the uplink direction of a wireless link, i.e. towards the network'}, {'symbol': 'H04W72/56', 'titleFull': 'Allocation or scheduling criteria for wireless resources based on priority criteria'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
