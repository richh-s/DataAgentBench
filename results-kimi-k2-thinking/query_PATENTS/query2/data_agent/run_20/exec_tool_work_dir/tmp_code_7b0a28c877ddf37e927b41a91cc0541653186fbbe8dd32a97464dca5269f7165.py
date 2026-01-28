code = """import json

# Get the top CPC groups from previous analysis
prev_result_key = 'var_functions.execute_python:22'
prev_result = locals().get(prev_result_key)

if not prev_result:
    print('Previous result not found')
    top_groups = []
else:
    top_groups = prev_result.get('top_groups', [])

print('Top groups to get titles for:', len(top_groups))

cpc_codes = [group['cpc_level4'] for group in top_groups]
print('CPC codes to query:', cpc_codes[:10])

# Format as a list for SQL IN clause
cpc_list_str = ', '.join([f"'{code}'" for code in cpc_codes[:100]])  # Limit to avoid too long query
print('First few CPC codes for query:', cpc_list_str[:200])

result = {'cpc_codes_count': len(cpc_codes), 'sample_codes': cpc_codes[:5]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_cpc_groups': 7857, 'top_groups': [{'cpc_level4': 'B65D2519/00', 'ema': 55, 'total_filings': 55, 'best_month': 8, 'monthly_counts': {'8': 55}}, {'cpc_level4': 'B60N2/28', 'ema': 42, 'total_filings': 42, 'best_month': 10, 'monthly_counts': {'10': 42}}, {'cpc_level4': 'A61B5/15', 'ema': 34.78, 'total_filings': 50, 'best_month': 7, 'monthly_counts': {'10': 4, '12': 4, '7': 42}}, {'cpc_level4': 'B60J5/04', 'ema': 34.300000000000004, 'total_filings': 39, 'best_month': 7, 'monthly_counts': {'11': 1, '7': 38}}, {'cpc_level4': 'H01L21/02', 'ema': 33.78069000000001, 'total_filings': 115, 'best_month': 7, 'monthly_counts': {'7': 48, '9': 3, '11': 12, '8': 27, '10': 7, '12': 18}}, {'cpc_level4': 'B01D2255/20', 'ema': 31.6, 'total_filings': 44, 'best_month': 11, 'monthly_counts': {'11': 34, '12': 10}}, {'cpc_level4': 'G02F1/13', 'ema': 30.416310000000003, 'total_filings': 154, 'best_month': 8, 'monthly_counts': {'8': 37, '7': 36, '11': 26, '9': 29, '12': 9, '10': 17}}, {'cpc_level4': 'B29C2049/20', 'ema': 29, 'total_filings': 29, 'best_month': 8, 'monthly_counts': {'8': 29}}, {'cpc_level4': 'B01J2219/00', 'ema': 28, 'total_filings': 28, 'best_month': 9, 'monthly_counts': {'9': 28}}, {'cpc_level4': 'A61F2002/30', 'ema': 27, 'total_filings': 27, 'best_month': 10, 'monthly_counts': {'10': 27}}], 'status': 'success'}}

exec(code, env_args)
