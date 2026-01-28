code = """import json
import pandas as pd

file_path_key = 'var_functions.query_db:2'
if isinstance(globals().get(file_path_key), str):
    with open(globals()[file_path_key], 'r') as f:
        patents_data = json.load(f)
else:
    patents_data = globals().get(file_path_key, [])

print('Data type:', type(patents_data))
print('Length of data:', len(patents_data) if isinstance(patents_data, list) else 'Not a list')

# Parse CPC codes and filter for Germany patents
valid_patents = []
for record in patents_data:
    if not record:
        continue
    
    patents_info = record.get('Patents_info', '')
    if not patents_info or 'DE-' not in str(patents_info):
        continue
    
    grant_date = record.get('grant_date', '')
    if not grant_date or '2019' not in str(grant_date):
        continue
    
    cpc_field = record.get('cpc', '')
    if not cpc_field:
        continue
    
    valid_patents.append(record)

print('Germany 2019 patents found:', len(valid_patents))

# Now extract CPC codes and grant months
cpc_count_by_month = {}
for patent in valid_patents:
    grant_date = patent.get('grant_date', '')
    cpc_data = patent.get('cpc', '')
    
    # Extract month from grant date
    month_num = None
    date_str = str(grant_date).lower()
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for i, month in enumerate(months, 1):
        if month in date_str:
            month_num = i
            break
    
    if month_num is None or month_num < 7:
        continue
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code:
                code_level4 = code[:7] if len(code) >= 7 else code
                if month_num not in cpc_count_by_month:
                    cpc_count_by_month[month_num] = {}
                cpc_count_by_month[month_num][code_level4] = cpc_count_by_month[month_num].get(code_level4, 0) + 1
    except:
        pass

print('Patents by month:')
for month in range(7, 13):
    total = sum(cpc_count_by_month.get(month, {}).values())
    print(f'  Month {month}: {total} patents')

result = {
    'total_germany_2019_second_half': sum(sum(month_counts.values()) for month_counts in cpc_count_by_month.values()),
    'months_with_data': list(cpc_count_by_month.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
