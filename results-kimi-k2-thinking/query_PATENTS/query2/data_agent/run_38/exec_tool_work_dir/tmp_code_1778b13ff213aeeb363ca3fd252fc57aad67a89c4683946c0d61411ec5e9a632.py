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
    year_match = re.search(r'(20\d{2})', str(date_str))
    year = int(year_match.group(1)) if year_match else None
    
    month_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', str(date_str), re.IGNORECASE)
    month = 0
    if month_match:
        month_name = month_match.group(1).lower()
        month_map = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
        month = month_map.get(month_name, 0)
    
    return year, month

# Extract CPC codes for second half of each year (July-December)
cpc_counts = defaultdict(lambda: {2017: 0, 2018: 0, 2019: 0})
yearly_totals = {2017: 0, 2018: 0, 2019: 0}

for patent in patents_data:
    year, month = parse_grant_date(patent.get('grant_date', ''))
    
    if year in [2017, 2018, 2019] and month >= 7:  # Second half only
        yearly_totals[year] += 1
        
        cpc_field = patent.get('cpc', '[]')
        if cpc_field:
            try:
                cpc_list = json.loads(cpc_field)
                for cpc_item in cpc_list:
                    code = cpc_item.get('code', '')
                    if code and '/' in code:
                        cpc_counts[code][year] += 1
            except:
                continue

# Calculate exponential moving average (EMA) for each CPC code
# Formula: EMA_t = alpha * value_t + (1-alpha) * EMA_{t-1}
# For first period, EMA = value
alpha = 0.1

cpc_ema_results = []
for code, year_counts in cpc_counts.items():
    # For each CPC code, calculate EMA across years 2017-2019
    sorted_years = sorted(year_counts.keys())
    ema_values = {}
    prev_ema = None
    
    for year in [2017, 2018, 2019]:
        count = year_counts[year]
        if prev_ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * prev_ema
        
        ema_values[year] = {
            'count': count,
            'ema': ema
        }
        prev_ema = ema
    
    # Find the year with highest EMA
    best_year = max(ema_values.keys(), key=lambda y: ema_values[y]['ema'])
    
    cpc_ema_results.append({
        'cpc_code': code,
        'best_year': best_year,
        'best_year_ema': ema_values[best_year]['ema'],
        'ema_2017': ema_values[2017]['ema'],
        'ema_2018': ema_values[2018]['ema'],
        'ema_2019': ema_values[2019]['ema'],
        'counts': year_counts
    })

# Sort by EMA in best year descending
cpc_ema_results_sorted = sorted(cpc_ema_results, key=lambda x: x['best_year_ema'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'yearly_totals_second_half': yearly_totals,
    'total_cpc_codes_second_half': len(cpc_ema_results),
    'top_20_cpc_ema': cpc_ema_results_sorted[:20],
    'sample_cpc_data': cpc_ema_results_sorted[0] if cpc_ema_results_sorted else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'total_records': 68, 'sample_cpc_codes': ['H02J1/10', 'H02J7/34', 'H02J7/007182', 'H02J1/10', 'H02J7/34', 'H02J7/007182'], 'sample_grant_date': '14th Aug 2019'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_records': 68, 'first_few': [{'Patents_info': 'Patent application (ID DE-102009033309-A) from DE, assigned to CONTINENTAL AUTOMOTIVE GMBH, with pub. number DE-102009033309-B4.', 'grant_date': '14th Aug 2019', 'cpc': '[\n  {\n    "code": "H02J1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/007182",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H02J1/10",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/34",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H02J7/007182",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019', 'cpc': '[\n  {\n    "code": "B63B21/50",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_de_2019': 68, 'second_half_2019': 34, 'sample_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:22': {'total_cpc_groups': 201, 'top_10_cpc': [{'cpc_code': 'F02D41/20', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W72/21', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W72/56', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W52/0261', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W52/0216', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W52/0229', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W72/0446', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'H04W52/0251', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'F24B5/023', 'year': 2019, 'count': 3, 'ema': 3}, {'cpc_code': 'F23L15/04', 'year': 2019, 'count': 3, 'ema': 3}], 'all_cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00', 'F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02M59/102', 'F02M55/04', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'G01D11/24', 'B23K1/0016', 'B63B21/50', 'H04W72/21', 'H04W72/56', 'H04L5/0037', 'H04L1/1614']}, 'var_functions.query_db:24': [], 'var_functions.query_db:26': [{'symbol': 'F24B5/023', 'titleFull': 'Supply of primary air for combustion'}, {'symbol': 'F02D41/20', 'titleFull': 'Output circuits, e.g. for controlling currents in command coils'}, {'symbol': 'F23L15/04', 'titleFull': 'Arrangements of recuperators'}, {'symbol': 'H04W72/0446', 'titleFull': 'Resources in time domain, e.g. slots or frames'}, {'symbol': 'H04W52/0261', 'titleFull': 'Power saving arrangements in terminal devices managing power supply demand, e.g. depending on battery level'}, {'symbol': 'H04W52/0251', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of local events, e.g. events related to user activity'}, {'symbol': 'H04W52/0216', 'titleFull': 'Power saving arrangements in terminal devices managed by the network, e.g. network or access point is master and terminal is slave using a pre-established activity schedule, e.g. traffic indication frame'}, {'symbol': 'H04W52/0229', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of external events, e.g. the presence of a signal where the received signal is a wanted signal'}, {'symbol': 'H04W72/21', 'titleFull': 'Control channels or signalling for resource management in the uplink direction of a wireless link, i.e. towards the network'}, {'symbol': 'H04W72/56', 'titleFull': 'Allocation or scheduling criteria for wireless resources based on priority criteria'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_by_year': {'2017': 48, '2019': 68, '2018': 56}, 'cpc_codes_2017': 280, 'cpc_codes_2018': 321, 'cpc_codes_2019': 201, 'sample_cpcs': ['B41F21/102', 'B41F22/00', 'B41F21/00', 'F02D41/3005', 'F02D41/20']}, 'var_functions.query_db:32': [], 'var_functions.query_db:34': [{'symbol': 'F24B5/023', 'titleFull': 'Supply of primary air for combustion', 'level': '10.0'}, {'symbol': 'H04W72/0446', 'titleFull': 'Resources in time domain, e.g. slots or frames', 'level': '10.0'}, {'symbol': 'H04W52/0216', 'titleFull': 'Power saving arrangements in terminal devices managed by the network, e.g. network or access point is master and terminal is slave using a pre-established activity schedule, e.g. traffic indication frame', 'level': '11.0'}, {'symbol': 'H04W52/0229', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of external events, e.g. the presence of a signal where the received signal is a wanted signal', 'level': '11.0'}, {'symbol': 'F02D41/00', 'titleFull': 'Electrical control of supply of combustible mixture or its constituents', 'level': '7.0'}, {'symbol': 'F02M65/005', 'titleFull': 'Measuring or detecting injection-valve lift, e.g. to determine injection timing', 'level': '8.0'}, {'symbol': 'F02D41/3005', 'titleFull': 'Details not otherwise provided for', 'level': '9.0'}, {'symbol': 'H04W72/21', 'titleFull': 'Control channels or signalling for resource management in the uplink direction of a wireless link, i.e. towards the network', 'level': '9.0'}, {'symbol': 'H04W72/56', 'titleFull': 'Allocation or scheduling criteria for wireless resources based on priority criteria', 'level': '9.0'}, {'symbol': 'F02M59/102', 'titleFull': 'Mechanical drive, e.g. tappets or cams', 'level': '10.0'}, {'symbol': 'H04W52/0261', 'titleFull': 'Power saving arrangements in terminal devices managing power supply demand, e.g. depending on battery level', 'level': '10.0'}, {'symbol': 'H04W52/0251', 'titleFull': 'Power saving arrangements in terminal devices using monitoring of local events, e.g. events related to user activity', 'level': '10.0'}, {'symbol': 'F02D41/20', 'titleFull': 'Output circuits, e.g. for controlling currents in command coils', 'level': '8.0'}, {'symbol': 'F23L15/04', 'titleFull': 'Arrangements of recuperators', 'level': '8.0'}, {'symbol': 'B41F21/102', 'titleFull': 'Combinations of transfer drums and grippers with pneumatic means', 'level': '9.0'}, {'symbol': 'B41F22/00', 'titleFull': 'Means preventing smudging of machine parts or printed articles', 'level': '7.0'}, {'symbol': 'B41F21/00', 'titleFull': 'Devices for conveying sheets through printing apparatus or machines', 'level': '7.0'}, {'symbol': 'F02M55/04', 'titleFull': 'Means for damping vibrations or pressure fluctuations in injection pump inlets or outlets', 'level': '8.0'}], 'var_functions.execute_python:36': {'total_patents': {'2017': 48, '2019': 68, '2018': 56}, 'total_cpc_codes': 791, 'sample_cpc_data': {'H01L29/1095': {'2017': 0, '2018': 2, '2019': 0}, 'B64C1/064': {'2017': 0, '2018': 3, '2019': 0}, 'G03B21/28': {'2017': 0, '2018': 1, '2019': 0}, 'H01L29/66734': {'2017': 0, '2018': 2, '2019': 0}, 'F02M59/462': {'2017': 0, '2018': 2, '2019': 0}}}, 'var_functions.execute_python:38': {'second_half_total_by_year': {'2017': 25, '2018': 27, '2019': 34}, 'second_half_2017_cpc_count': 152, 'second_half_2018_cpc_count': 129, 'second_half_2019_cpc_count': 201}}

exec(code, env_args)
