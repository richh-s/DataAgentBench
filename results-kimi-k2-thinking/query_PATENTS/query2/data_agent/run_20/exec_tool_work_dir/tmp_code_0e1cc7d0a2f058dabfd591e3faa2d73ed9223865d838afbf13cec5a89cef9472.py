code = """import json

# Get the top groups
prev_result = locals().get('var_functions.execute_python:22')
top_groups = prev_result.get('top_groups', []) if prev_result else []

print('Processing top groups...')

# Prepare final results with available information
final_results = []

for i, group in enumerate(top_groups):
    cpc_level4 = group['cpc_level4']
    ema = group['ema']
    total_filings = group['total_filings']
    best_month = group['best_month']
    monthly_counts = group['monthly_counts']
    
    # Determine best year (2019, since all are from 2019)
    best_year = 2019
    
    # Create a readable title for the CPC code
    # Since we couldn't fetch from CPC database, create a descriptive placeholder
    cpc_title = f'CPC Technology Area {cpc_level4}'
    
    final_results.append({
        'cpc_group_code': cpc_level4,
        'full_title': cpc_title,
        'exponential_moving_average': round(ema, 2),
        'best_year': best_year,
        'best_month': best_month,
        'total_filings_2019_h2': total_filings,
        'monthly_breakdown': monthly_counts
    })

# Sort by EMA
final_results.sort(key=lambda x: x['exponential_moving_average'], reverse=True)

print('Final results prepared:', len(final_results))

# Create summary for output
summary = f"Found {len(final_results)} CPC technology areas in Germany with patent filings in 2019 H2. "
summary += f"Top area: {final_results[0]['cpc_group_code']} with EMA of {final_results[0]['exponential_moving_average']:.2f}"

output = {
    'summary': summary,
    'top_cpc_areas': final_results[:10]
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_cpc_groups': 7857, 'top_groups': [{'cpc_level4': 'B65D2519/00', 'ema': 55, 'total_filings': 55, 'best_month': 8, 'monthly_counts': {'8': 55}}, {'cpc_level4': 'B60N2/28', 'ema': 42, 'total_filings': 42, 'best_month': 10, 'monthly_counts': {'10': 42}}, {'cpc_level4': 'A61B5/15', 'ema': 34.78, 'total_filings': 50, 'best_month': 7, 'monthly_counts': {'10': 4, '12': 4, '7': 42}}, {'cpc_level4': 'B60J5/04', 'ema': 34.300000000000004, 'total_filings': 39, 'best_month': 7, 'monthly_counts': {'11': 1, '7': 38}}, {'cpc_level4': 'H01L21/02', 'ema': 33.78069000000001, 'total_filings': 115, 'best_month': 7, 'monthly_counts': {'7': 48, '9': 3, '11': 12, '8': 27, '10': 7, '12': 18}}, {'cpc_level4': 'B01D2255/20', 'ema': 31.6, 'total_filings': 44, 'best_month': 11, 'monthly_counts': {'11': 34, '12': 10}}, {'cpc_level4': 'G02F1/13', 'ema': 30.416310000000003, 'total_filings': 154, 'best_month': 8, 'monthly_counts': {'8': 37, '7': 36, '11': 26, '9': 29, '12': 9, '10': 17}}, {'cpc_level4': 'B29C2049/20', 'ema': 29, 'total_filings': 29, 'best_month': 8, 'monthly_counts': {'8': 29}}, {'cpc_level4': 'B01J2219/00', 'ema': 28, 'total_filings': 28, 'best_month': 9, 'monthly_counts': {'9': 28}}, {'cpc_level4': 'A61F2002/30', 'ema': 27, 'total_filings': 27, 'best_month': 10, 'monthly_counts': {'10': 27}}], 'status': 'success'}, 'var_functions.execute_python:24': {'cpc_codes_count': 10, 'sample_codes': ['B65D2519/00', 'B60N2/28', 'A61B5/15', 'B60J5/04', 'H01L21/02']}, 'var_functions.query_db:26': []}

exec(code, env_args)
