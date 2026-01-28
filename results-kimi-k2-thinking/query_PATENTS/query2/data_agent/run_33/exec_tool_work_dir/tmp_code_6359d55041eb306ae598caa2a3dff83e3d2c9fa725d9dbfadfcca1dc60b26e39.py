code = """import json

# Load the final results from the previous step
result_file = 'german_cpc_ema_final.json'
if not os.path.exists(result_file):
    print('ERROR: Results file not found')
    exit()

with open(result_file, 'r') as f:
    results = json.load(f)

# Format the results for display
formatted_results = []
for item in results:
    formatted_results.append({
        'cpc_group_code': item['cpc_group_code'],
        'full_title': item['full_title'],
        'best_year': item['best_year'],
        'exponential_moving_average': item['exponential_moving_average']
    })

# Display all results sorted by EMA
print('CPC Technology Areas in Germany (Patents Granted in 2nd Half 2019)')
print('=' * 80)
print()

for i, item in enumerate(formatted_results, 1):
    print(f"{i}. {item['cpc_group_code']}")
    print(f"   Title: {item['full_title']}")
    print(f"   Best Year: {item['best_year']}")
    print(f"   Exponential Moving Average: {item['exponential_moving_average']}")
    print()

# Save formatted results
with open('final_german_cpc_results.json', 'w') as f:
    json.dump(formatted_results, f, indent=2)

result_summary = {
    'status': 'success',
    'total_groups': len(formatted_results),
    'results': formatted_results
}

print('__RESULT__:')
print(json.dumps(result_summary, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': {'status': 'check_complete'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['cpc_definition'], 'var_functions.execute_python:28': {'status': 'error', 'message': 'Could not find result file'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'status': 'success', 'cpc_groups': 11, 'total_patents': 6, 'sample_groups': ['B41F', 'B66C', 'E02F', 'B60S', 'F02D']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'status': 'success', 'cpc_groups': 564, 'total_patents': 11644, 'year_range': {'min': 1882, 'max': 2024}}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': {'status': 'success', 'total_cpc_groups': 11, 'top_groups': 11}, 'var_functions.execute_python:50': {'status': 'success', 'top_cpc_groups': [{'cpc_group_code': 'C04B', 'full_title': 'Title not available', 'best_year': 2015, 'exponential_moving_average': 4.5, 'total_patents_in_dataset': 45}, {'cpc_group_code': 'B29C', 'full_title': 'Title not available', 'best_year': 2007, 'exponential_moving_average': 1.5, 'total_patents_in_dataset': 15}, {'cpc_group_code': 'E02F', 'full_title': 'Title not available', 'best_year': 2012, 'exponential_moving_average': 0.5, 'total_patents_in_dataset': 6}, {'cpc_group_code': 'B41F', 'full_title': 'Title not available', 'best_year': 2007, 'exponential_moving_average': 0.3, 'total_patents_in_dataset': 3}, {'cpc_group_code': 'F02D', 'full_title': 'Title not available', 'best_year': 2018, 'exponential_moving_average': 0.3, 'total_patents_in_dataset': 3}, {'cpc_group_code': 'C09K', 'full_title': 'Title not available', 'best_year': 2015, 'exponential_moving_average': 0.2, 'total_patents_in_dataset': 2}, {'cpc_group_code': 'F42B', 'full_title': 'Title not available', 'best_year': 2012, 'exponential_moving_average': 0.2, 'total_patents_in_dataset': 2}, {'cpc_group_code': 'F41H', 'full_title': 'Title not available', 'best_year': 2012, 'exponential_moving_average': 0.2, 'total_patents_in_dataset': 2}, {'cpc_group_code': 'B66C', 'full_title': 'Title not available', 'best_year': 2016, 'exponential_moving_average': 0.1, 'total_patents_in_dataset': 1}, {'cpc_group_code': 'B60S', 'full_title': 'Title not available', 'best_year': 2016, 'exponential_moving_average': 0.1, 'total_patents_in_dataset': 1}, {'cpc_group_code': 'Y02T', 'full_title': 'Title not available', 'best_year': 2018, 'exponential_moving_average': 0.1, 'total_patents_in_dataset': 1}]}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:54': {'status': 'success', 'total_cpc_groups': 11, 'top_groups': [{'cpc_group_code': 'C04B', 'full_title': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE', 'best_year': 2015, 'exponential_moving_average': 4.5, 'total_patents': 45}, {'cpc_group_code': 'B29C', 'full_title': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING', 'best_year': 2007, 'exponential_moving_average': 1.5, 'total_patents': 15}, {'cpc_group_code': 'E02F', 'full_title': 'DREDGING; SOIL-SHIFTING', 'best_year': 2012, 'exponential_moving_average': 0.5, 'total_patents': 6}, {'cpc_group_code': 'B41F', 'full_title': 'PRINTING MACHINES OR PRESSES', 'best_year': 2007, 'exponential_moving_average': 0.3, 'total_patents': 3}, {'cpc_group_code': 'F02D', 'full_title': 'CONTROLLING COMBUSTION ENGINES', 'best_year': 2018, 'exponential_moving_average': 0.3, 'total_patents': 3}, {'cpc_group_code': 'C09K', 'full_title': 'MATERIALS FOR MISCELLANEOUS APPLICATIONS, NOT PROVIDED FOR ELSEWHERE', 'best_year': 2015, 'exponential_moving_average': 0.2, 'total_patents': 2}, {'cpc_group_code': 'F42B', 'full_title': 'EXPLOSIVE CHARGES, e.g. FOR BLASTING, FIREWORKS, AMMUNITION', 'best_year': 2012, 'exponential_moving_average': 0.2, 'total_patents': 2}, {'cpc_group_code': 'F41H', 'full_title': 'ARMOUR; ARMOURED TURRETS; ARMOURED OR ARMED VEHICLES; MEANS OF ATTACK OR DEFENCE, e.g. CAMOUFLAGE, IN GENERAL', 'best_year': 2012, 'exponential_moving_average': 0.2, 'total_patents': 2}, {'cpc_group_code': 'B66C', 'full_title': 'CRANES; LOAD-ENGAGING ELEMENTS OR DEVICES FOR CRANES, CAPSTANS, WINCHES, OR TACKLES', 'best_year': 2016, 'exponential_moving_average': 0.1, 'total_patents': 1}, {'cpc_group_code': 'B60S', 'full_title': 'SERVICING, CLEANING, REPAIRING, SUPPORTING, LIFTING, OR MANOEUVRING OF VEHICLES, NOT OTHERWISE PROVIDED FOR', 'best_year': 2016, 'exponential_moving_average': 0.1, 'total_patents': 1}]}}

exec(code, env_args)
