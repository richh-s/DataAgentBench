code = """import json
# The stored vars are likely plain Python lists already (from earlier query_db). Let's inspect their types by printing first 200 chars
print('__RESULT__:')
res = {
    'var1_type': str(type(var_call_01xeWJ6DlbUF6ExjEiN0knj3))[:200],
    'var2_type': str(type(var_call_k22XZZZHlqzT8CA5vvfK2jqG))[:200],
}
print(json.dumps(res))"""

env_args = {'var_call_JgVdZ5lPpvNbcr53P85FVhko': 'file_storage/call_JgVdZ5lPpvNbcr53P85FVhko.json', 'var_call_pg5PrTVxGV9a7THHNxzy7odL': 'file_storage/call_pg5PrTVxGV9a7THHNxzy7odL.json', 'var_call_3CdQj3Q6YQ8u0U19WMxZbALc': 'file_storage/call_3CdQj3Q6YQ8u0U19WMxZbALc.json', 'var_call_QV8UTH7arKnVHjxz3ksLPxOA': {'count': 234, 'symbols_sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA']}, 'var_call_01xeWJ6DlbUF6ExjEiN0knj3': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_k22XZZZHlqzT8CA5vvfK2jqG': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_Jy1o2iezClzd7PwE5VvdoNGN': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_8Y9dYxhK3RBbQxgW2fcVch3u': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_CukME8smKID93D9ATGgNoNJ5': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}]}

exec(code, env_args)
