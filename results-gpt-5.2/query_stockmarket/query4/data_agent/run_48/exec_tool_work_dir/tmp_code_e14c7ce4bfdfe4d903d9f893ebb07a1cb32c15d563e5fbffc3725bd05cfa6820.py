code = """import json, pandas as pd

# Gather computed up/down for candidates we queried
rows = []
for v in [
    var_call_EQdJjVaB7pTJAiCE8fJquOhK,
    var_call_Iq2DDjdXHYILQP9KTlkiDT8h,
    var_call_SZD67EsQMHJNjkHMoQy76kjJ,
    var_call_ZFmpGAwlJ13C9kEayoExiYL8,
    var_call_uI9YuCnhUX5GF0xet3FiQ6Zf,
    var_call_JuXuWmw1DfCMwxw3AuSqSm8Y
]:
    rows.extend(v)

df = pd.DataFrame(rows)
df['up_days'] = pd.to_numeric(df['up_days'])
df['down_days'] = pd.to_numeric(df['down_days'])
df['diff'] = df['up_days'] - df['down_days']
df = df.sort_values(['diff','up_days','symbol'], ascending=[False,False,True]).head(5)

# Map to company names
src = var_call_QTlIzelgD7c9YCeCM1DsmgUt
if isinstance(src, str):
    with open(src, 'r') as f:
        info = json.load(f)
else:
    info = src
info_df = pd.DataFrame(info)
res = df.merge(info_df, left_on='symbol', right_on='Symbol', how='left')
ans = res['company_name'].tolist()
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_QTlIzelgD7c9YCeCM1DsmgUt': 'file_storage/call_QTlIzelgD7c9YCeCM1DsmgUt.json', 'var_call_AceQkdmru6bj7QFVvVXiKhbC': 'file_storage/call_AceQkdmru6bj7QFVvVXiKhbC.json', 'var_call_ptXhpFZ8BINMPs4Fg32qM4rU': {'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'n_symbols': 234}, 'var_call_K4j5SnBNfZsmlZK9Whv71wF6': [{'symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}], 'var_call_mVVLGm5KWOKFT8CK6fa77gZf': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_rt1qWiijNKqzHHnVO71bPVZv': [{'n': '0'}], 'var_call_fl7yx1dYGhU50ilRBAag9uOG': [{'min_date': '2019-10-24', 'max_date': '2020-04-01', 'n': '110'}], 'var_call_FRdBbf31YaYaeAAoScu0SEdk': [{'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'CVX'}, {'Symbol': 'GD'}, {'Symbol': 'IBM'}, {'Symbol': 'IRM'}, {'Symbol': 'IT'}, {'Symbol': 'JNPR'}, {'Symbol': 'KMB'}, {'Symbol': 'KNX'}, {'Symbol': 'LB'}, {'Symbol': 'LDOS'}, {'Symbol': 'LHC'}, {'Symbol': 'LHX'}, {'Symbol': 'MKC'}, {'Symbol': 'MS'}, {'Symbol': 'NUE'}, {'Symbol': 'ORCL'}, {'Symbol': 'PFE'}, {'Symbol': 'PGR'}, {'Symbol': 'PMT'}, {'Symbol': 'PPG'}, {'Symbol': 'ROG'}, {'Symbol': 'ROL'}, {'Symbol': 'RPM'}, {'Symbol': 'TRV'}], 'var_call_xk0z2Pkt7q79c4XSXZY43A4p': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], 'var_call_YNHHqwJaSAcX4slcbLJl4NCt': [{'symbol': 'AIN', 'n_2017': '251'}], 'var_call_EQdJjVaB7pTJAiCE8fJquOhK': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_87UWUkSBiH6jm5E8KhMsMz4l': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_ZhNOX3xGjYu9z7dQ7QsjiNsH': [{'symbol': 'AIZP', 'n': '0'}], 'var_call_02el0zhJ1fO6zkMjVk119iEQ': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_Iq2DDjdXHYILQP9KTlkiDT8h': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_SZD67EsQMHJNjkHMoQy76kjJ': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_ZFmpGAwlJ13C9kEayoExiYL8': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_uI9YuCnhUX5GF0xet3FiQ6Zf': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_jWAoHlqAdowQsxphZP9oF2BS': [{'symbol': 'ARD', 'n': '204'}], 'var_call_izLomEHxeLMtt04F9Cfmc1Fe': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_uPqazduhDgcxA1K3WpyiVuU7': [{'symbol': 'ARGD', 'n': '251'}], 'var_call_JuXuWmw1DfCMwxw3AuSqSm8Y': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}]}

exec(code, env_args)
