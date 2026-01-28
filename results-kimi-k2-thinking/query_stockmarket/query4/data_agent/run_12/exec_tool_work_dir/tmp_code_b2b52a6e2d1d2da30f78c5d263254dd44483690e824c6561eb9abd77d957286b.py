code = """import json

# Load the first batch results - they should be lists
def load_result(key):
    result = locals()[key]
    if isinstance(result, str) and result.endswith('.json'):
        with open(result, 'r') as f:
            return json.load(f)
    else:
        return result

batch1_data = load_result('var_functions.query_db:36')
batch2_data = load_result('var_functions.query_db:38')

# Combine results
all_results = batch1_data + batch2_data

# Count stocks with more up days than down days
stocks_with_more_up_days = []
for result in all_results:
    up_days = float(result.get('up_days', 0))
    down_days = float(result.get('down_days', 0))
    symbol = result.get('Symbol', '')
    
    if up_days > down_days:
        stocks_with_more_up_days.append({
            'symbol': symbol,
            'up_days': up_days,
            'down_days': down_days,
            'difference': up_days - down_days
        })

# Sort by difference (largest positive difference first)
stocks_with_more_up_days.sort(key=lambda x: x['difference'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_analyzed': len(all_results),
    'stocks_with_more_up_days': len(stocks_with_more_up_days),
    'top_5_by_difference': stocks_with_more_up_days[:5],
    'all_up_day_stocks': stocks_with_more_up_days
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'stockinfo_count': 234, 'tables_count': 2753, 'sample_stockinfo': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}], 'sample_tables': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}]}, 'var_functions.execute_python:14': {'nyse_non_etf_count': 234, 'trade_tables_count': 2753, 'common_symbols_count': 234, 'sample_common': ['VKQ', 'JHY', 'VRT', 'MFO', 'DAC', 'AEFC', 'AL', 'LHX', 'EARN', 'MTD']}, 'var_functions.query_db:16': [{'Date': '2017-01-03', 'Open': '45.68999862670898', 'High': '45.72999954223633', 'Low': '44.66999816894531', 'Close': '44.93999862670898', 'Adj Close': '40.33967971801758', 'Volume': '770100'}, {'Date': '2017-01-04', 'Open': '45.09999847412109', 'High': '45.52000045776367', 'Low': '44.79999923706055', 'Close': '45.36000061035156', 'Adj Close': '40.716678619384766', 'Volume': '1089400'}, {'Date': '2017-01-05', 'Open': '45.09999847412109', 'High': '45.650001525878906', 'Low': '44.650001525878906', 'Close': '45.45000076293945', 'Adj Close': '40.7974739074707', 'Volume': '833400'}, {'Date': '2017-01-06', 'Open': '45.29999923706055', 'High': '45.560001373291016', 'Low': '44.97999954223633', 'Close': '45.45000076293945', 'Adj Close': '40.7974739074707', 'Volume': '1299300'}, {'Date': '2017-01-09', 'Open': '45.540000915527344', 'High': '45.61000061035156', 'Low': '44.91999816894531', 'Close': '44.959999084472656', 'Adj Close': '40.35763168334961', 'Volume': '697700'}], 'var_functions.execute_python:20': {'total_stocks': 234, 'sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}, 'var_functions.execute_python:22': {'symbols_to_analyze': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:24': [{'total_days': '251', 'up_days': '118.0', 'down_days': '128.0', 'neutral_days': '5.0'}], 'var_functions.execute_python:28': {'message': 'Loaded 234 NYSE non-ETF stocks for analysis', 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:30': {'status': 'ready_to_analyze', 'symbol_count': 234, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT']}, 'var_functions.query_db:32': [{'count': '251'}], 'var_functions.execute_python:34': {'test_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'sample_company': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, 'var_functions.query_db:36': [{'Symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'Symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'Symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'Symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'Symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'Symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'Symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'Symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'Symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'Symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_functions.query_db:38': [{'Symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'Symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'Symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}, {'Symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'Symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'Symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}, {'Symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'Symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'Symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'Symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'Symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'Symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'Symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'Symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'Symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}]}

exec(code, env_args)
