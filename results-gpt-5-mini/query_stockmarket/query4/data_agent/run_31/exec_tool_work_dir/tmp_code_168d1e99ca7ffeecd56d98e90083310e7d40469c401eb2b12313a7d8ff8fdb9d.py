code = """import json
nyse_var = var_call_K63MgEF0ck5Q3hnmXh8jEFw7
if isinstance(nyse_var, str):
    with open(nyse_var, 'r') as f:
        nyse_list = json.load(f)
else:
    nyse_list = nyse_var

symbols = [rec['Symbol'] for rec in nyse_list if rec.get('Symbol')]
print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_call_PMBN6E9T7eI2X9WsQ47LDLpM': 'file_storage/call_PMBN6E9T7eI2X9WsQ47LDLpM.json', 'var_call_KmfEKriY70zObdxCudPoIzlv': 'file_storage/call_KmfEKriY70zObdxCudPoIzlv.json', 'var_call_K63MgEF0ck5Q3hnmXh8jEFw7': 'file_storage/call_K63MgEF0ck5Q3hnmXh8jEFw7.json', 'var_call_9MsHHwZylGcelvizXCzgiZN0': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT']}

exec(code, env_args)
