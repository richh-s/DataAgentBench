code = """import json

def load_data_from_storage(var_key):
    data = locals().get(var_key)
    if isinstance(data, dict) and 'results' in data:
        return data['results']
    elif isinstance(data, str) and data.endswith('.json'):
        with open(data, 'r') as f:
            return json.load(f)
    return [] # Return an empty list if data is not found or in an unexpected format

# Load the map of symbols to company names from the stockinfo_database query result
stock_info_full = load_data_from_storage('var_function-call-12569103376830388847')
company_names = {d['Symbol']: d['Company Description'] for d in stock_info_full}

processed_stocks_data = []

# List of (symbol, var_key) tuples for processing the available stock data
stock_data_keys = [
    ('AEFC', 'var_function-call-1980294828156932039'),
    ('AIN', 'var_function-call-11239077458938920857'),
    ('AIV', 'var_function-call-14000946303462645799'),
    ('AIZP', 'var_function-call-3225285148180011713'),
    ('AJRD', 'var_function-call-8962430770534129849'),
    ('AL', 'var_function-call-1169396377710212234'),
    ('AMN', 'var_function-call-16825786640932626777'),
    ('AMP', 'var_function-call-1075379290820917676'),
    ('AMT', 'var_function-call-2245022596143109378'),
    ('ARD', 'var_function-call-12524401120981646008'),
    ('ARGD', 'var_function-call-2577122950510130847'),
    ('ARLO', 'var_function-call-6689745659516594189'),
    ('ASG', 'var_function-call-9952656554784577183'),
    ('AVA', 'var_function-call-16920902625881462391'),
    ('BANC', 'var_function-call-7004080807362656796'),
]

for symbol, var_key in stock_data_keys:
    data = load_data_from_storage(var_key)
    if data:
        up_days = sum(1 for d in data if float(d['Close']) > float(d['Open']))
        down_days = sum(1 for d in data if float(d['Close']) < float(d['Open']))
        # Only add if there are actual trading days to avoid including stocks with no data
        if (up_days + down_days) > 0: # Ensure there was some trading activity
            processed_stocks_data.append({
                'symbol': symbol,
                'company_name': company_names.get(symbol, 'N/A'),
                'day_difference': up_days - down_days
            })

# Filter for stocks with more up days than down days and sort
qualified_stocks = [s for s in processed_stocks_data if s['day_difference'] > 0]
qualified_stocks.sort(key=lambda x: x['day_difference'], reverse=True)

# Get top 5 names
top_5_names = [s['company_name'] for s in qualified_stocks[:5]]

print("__RESULT__:")
print(json.dumps(top_5_names))"""

env_args = {'var_function-call-1817325595551073581': 'file_storage/function-call-1817325595551073581.json', 'var_function-call-17537764033768390306': 'file_storage/function-call-17537764033768390306.json', 'var_function-call-15459508532790814433': [{'symbol': 'AEFC', 'error': "name 'default_api' is not defined"}, {'symbol': 'AIN', 'error': "name 'default_api' is not defined"}, {'symbol': 'AIV', 'error': "name 'default_api' is not defined"}, {'symbol': 'AIZP', 'error': "name 'default_api' is not defined"}, {'symbol': 'AJRD', 'error': "name 'default_api' is not defined"}, {'symbol': 'AL', 'error': "name 'default_api' is not defined"}, {'symbol': 'AMN', 'error': "name 'default_api' is not defined"}, {'symbol': 'AMP', 'error': "name 'default_api' is not defined"}, {'symbol': 'AMT', 'error': "name 'default_api' is not defined"}, {'symbol': 'ARD', 'error': "name 'default_api' is not defined"}, {'symbol': 'ARGD', 'error': "name 'default_api' is not defined"}, {'symbol': 'ARLO', 'error': "name 'default_api' is not defined"}, {'symbol': 'ASG', 'error': "name 'default_api' is not defined"}, {'symbol': 'AVA', 'error': "name 'default_api' is not defined"}, {'symbol': 'BANC', 'error': "name 'default_api' is not defined"}, {'symbol': 'BBU', 'error': "name 'default_api' is not defined"}, {'symbol': 'BBVA', 'error': "name 'default_api' is not defined"}, {'symbol': 'BDXA', 'error': "name 'default_api' is not defined"}, {'symbol': 'BKH', 'error': "name 'default_api' is not defined"}, {'symbol': 'BKT', 'error': "name 'default_api' is not defined"}, {'symbol': 'BLD', 'error': "name 'default_api' is not defined"}, {'symbol': 'BNS', 'error': "name 'default_api' is not defined"}, {'symbol': 'BV', 'error': "name 'default_api' is not defined"}, {'symbol': 'BZH', 'error': "name 'default_api' is not defined"}, {'symbol': 'CADE', 'error': "name 'default_api' is not defined"}, {'symbol': 'CAE', 'error': "name 'default_api' is not defined"}, {'symbol': 'CAF', 'error': "name 'default_api' is not defined"}, {'symbol': 'CBT', 'error': "name 'default_api' is not defined"}, {'symbol': 'CCC', 'error': "name 'default_api' is not defined"}, {'symbol': 'CCZ', 'error': "name 'default_api' is not defined"}, {'symbol': 'CHAP', 'error': "name 'default_api' is not defined"}, {'symbol': 'CIA', 'error': "name 'default_api' is not defined"}, {'symbol': 'CMA', 'error': "name 'default_api' is not defined"}, {'symbol': 'CMI', 'error': "name 'default_api' is not defined"}, {'symbol': 'CMSA', 'error': "name 'default_api' is not defined"}, {'symbol': 'CNK', 'error': "name 'default_api' is not defined"}, {'symbol': 'COTY', 'error': "name 'default_api' is not defined"}, {'symbol': 'CRC', 'error': "name 'default_api' is not defined"}, {'symbol': 'CRM', 'error': "name 'default_api' is not defined"}, {'symbol': 'CRS', 'error': "name 'default_api' is not defined"}, {'symbol': 'CSL', 'error': "name 'default_api' is not defined"}, {'symbol': 'CTS', 'error': "name 'default_api' is not defined"}, {'symbol': 'CUBE', 'error': "name 'default_api' is not defined"}, {'symbol': 'CURO', 'error': "name 'default_api' is not defined"}, {'symbol': 'CVIA', 'error': "name 'default_api' is not defined"}, {'symbol': 'CVX', 'error': "name 'default_api' is not defined"}, {'symbol': 'CXH', 'error': "name 'default_api' is not defined"}, {'symbol': 'DAC', 'error': "name 'default_api' is not defined"}, {'symbol': 'DDS', 'error': "name 'default_api' is not defined"}, {'symbol': 'DDT', 'error': "name 'default_api' is not defined"}, {'symbol': 'DEO', 'error': "name 'default_api' is not defined"}, {'symbol': 'DGX', 'error': "name 'default_api' is not defined"}, {'symbol': 'DMB', 'error': "name 'default_api' is not defined"}, {'symbol': 'DTQ', 'error': "name 'default_api' is not defined"}, {'symbol': 'DXC', 'error': "name 'default_api' is not defined"}, {'symbol': 'EARN', 'error': "name 'default_api' is not defined"}, {'symbol': 'EBS', 'error': "name 'default_api' is not defined"}, {'symbol': 'EGO', 'error': "name 'default_api' is not defined"}, {'symbol': 'EGY', 'error': "name 'default_api' is not defined"}, {'symbol': 'EIG', 'error': "name 'default_api' is not defined"}, {'symbol': 'ELF', 'error': "name 'default_api' is not defined"}, {'symbol': 'EMP', 'error': "name 'default_api' is not defined"}, {'symbol': 'ENLC', 'error': "name 'default_api' is not defined"}, {'symbol': 'EPR', 'error': "name 'default_api' is not defined"}, {'symbol': 'EPRT', 'error': "name 'default_api' is not defined"}, {'symbol': 'ES', 'error': "name 'default_api' is not defined"}, {'symbol': 'ESRT', 'error': "name 'default_api' is not defined"}, {'symbol': 'ESS', 'error': "name 'default_api' is not defined"}, {'symbol': 'ETM', 'error': "name 'default_api' is not defined"}, {'symbol': 'EV', 'error': "name 'default_api' is not defined"}, {'symbol': 'EVT', 'error': "name 'default_api' is not defined"}, {'symbol': 'EXP', 'error': "name 'default_api' is not defined"}, {'symbol': 'FMN', 'error': "name 'default_api' is not defined"}, {'symbol': 'FPAC', 'error': "name 'default_api' is not defined"}, {'symbol': 'FSM', 'error': "name 'default_api' is not defined"}, {'symbol': 'GCO', 'error': "name 'default_api' is not defined"}, {'symbol': 'GD', 'error': "name 'default_api' is not defined"}, {'symbol': 'GDL', 'error': "name 'default_api' is not defined"}, {'symbol': 'GDV', 'error': "name 'default_api' is not defined"}, {'symbol': 'GEL', 'error': "name 'default_api' is not defined"}, {'symbol': 'GJP', 'error': "name 'default_api' is not defined"}, {'symbol': 'GLOB', 'error': "name 'default_api' is not defined"}, {'symbol': 'GLT', 'error': "name 'default_api' is not defined"}, {'symbol': 'GOL', 'error': "name 'default_api' is not defined"}, {'symbol': 'GSLD', 'error': "name 'default_api' is not defined"}, {'symbol': 'GTY', 'error': "name 'default_api' is not defined"}, {'symbol': 'GVA', 'error': "name 'default_api' is not defined"}, {'symbol': 'GWB', 'error': "name 'default_api' is not defined"}, {'symbol': 'H', 'error': "name 'default_api' is not defined"}, {'symbol': 'HBI', 'error': "name 'default_api' is not defined"}, {'symbol': 'HDB', 'error': "name 'default_api' is not defined"}, {'symbol': 'HEP', 'error': "name 'default_api' is not defined"}, {'symbol': 'HIL', 'error': "name 'default_api' is not defined"}, {'symbol': 'HIO', 'error': "name 'default_api' is not defined"}, {'symbol': 'HIX', 'error': "name 'default_api' is not defined"}, {'symbol': 'HLF', 'error': "name 'default_api' is not defined"}, {'symbol': 'HLT', 'error': "name 'default_api' is not defined"}, {'symbol': 'HNI', 'error': "name 'default_api' is not defined"}, {'symbol': 'HRB', 'error': "name 'default_api' is not defined"}, {'symbol': 'HTFA', 'error': "name 'default_api' is not defined"}], 'var_function-call-5472831697073455258': 'file_storage/function-call-5472831697073455258.json', 'var_function-call-1980294828156932039': [], 'var_function-call-11239077458938920857': 'file_storage/function-call-11239077458938920857.json', 'var_function-call-14000946303462645799': 'file_storage/function-call-14000946303462645799.json', 'var_function-call-3225285148180011713': [], 'var_function-call-8962430770534129849': 'file_storage/function-call-8962430770534129849.json', 'var_function-call-1169396377710212234': 'file_storage/function-call-1169396377710212234.json', 'var_function-call-16825786640932626777': 'file_storage/function-call-16825786640932626777.json', 'var_function-call-1075379290820917676': 'file_storage/function-call-1075379290820917676.json', 'var_function-call-1196030950791586646': 'file_storage/function-call-1196030950791586646.json', 'var_function-call-14739683218134507378': 'file_storage/function-call-14739683218134507378.json', 'var_function-call-3484533877795082151': 'file_storage/function-call-3484533877795082151.json', 'var_function-call-2245022596143109378': 'file_storage/function-call-2245022596143109378.json', 'var_function-call-12524401120981646008': 'file_storage/function-call-12524401120981646008.json', 'var_function-call-9669330825014345636': 'file_storage/function-call-9669330825014345636.json', 'var_function-call-11019961720335262410': 'file_storage/function-call-11019961720335262410.json', 'var_function-call-2577122950510130847': 'file_storage/function-call-2577122950510130847.json', 'var_function-call-6689745659516594189': [], 'var_function-call-9952656554784577183': 'file_storage/function-call-9952656554784577183.json', 'var_function-call-13108156588146959221': 'file_storage/function-call-13108156588146959221.json', 'var_function-call-4962940301481776363': 'file_storage/function-call-4962940301481776363.json', 'var_function-call-16920902625881462391': 'file_storage/function-call-16920902625881462391.json', 'var_function-call-12569103376830388847': 'file_storage/function-call-12569103376830388847.json', 'var_function-call-7004080807362656796': 'file_storage/function-call-7004080807362656796.json'}

exec(code, env_args)
