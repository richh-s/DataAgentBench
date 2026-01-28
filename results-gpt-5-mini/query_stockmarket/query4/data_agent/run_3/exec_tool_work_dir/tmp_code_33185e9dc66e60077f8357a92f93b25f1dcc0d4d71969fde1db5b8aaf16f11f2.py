code = """import json
# Load specific stored query results by known keys from earlier calls
keys = [
    'var_call_gjbCKfbmD3lXXIhLRmrgyHgr', 'var_call_kgVwUMufOhehk2wUxNM0dd2R', 'var_call_JXhrA4SimuFuX9llo9BwGFHH',
    'var_call_IoI66mIKno166JbAcGDDHzaZ', 'var_call_0FFsvUFihbWdmICSmCaciOkz', 'var_call_TgehQT5PgohuFGEAhUsANJz2',
    'var_call_cjhS63VXiuLtWblOFIb94uKF', 'var_call_42p5TV1QTYShq8MLhfATgdY3', 'var_call_G50LzqgSlZu2SYWbB02ms78Y',
    'var_call_JdEKT6QNN6HTUXHCDfRV3N7O', 'var_call_xxC6AyTBuGMoIviMET5s38aF', 'var_call_WbrANemlXHFaNKMTNIYZPK17',
    'var_call_SpgVvSjnVK0fu435RMBDhEaY', 'var_call_SpgVvSjnVK0fu435RMBDhEaY', 'var_call_SpgVvSjnVK0fu435RMBDhEaY'
]
records = []
for k in keys:
    if k in globals():
        v = globals()[k]
        # if it's a string containing JSON, try parse
        try:
            data = json.loads(v)
        except Exception:
            # maybe it's a path
            try:
                with open(v,'r') as f:
                    data = json.load(f)
            except Exception:
                data = v
        if isinstance(data,list):
            records.extend(data)

print('__RESULT__:')
print(json.dumps({'count': len(records), 'sample': records[:10]}))"""

env_args = {'var_call_30Q4bH3inArkxlM7dvrMi1ha': 'file_storage/call_30Q4bH3inArkxlM7dvrMi1ha.json', 'var_call_u7zNvvdRWah3dEIyubxloJSI': 'file_storage/call_u7zNvvdRWah3dEIyubxloJSI.json', 'var_call_ju2RRLLOikKW3RxjWPt7duns': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_zzmUMXZsH2jlNBEHumFraywb': 'file_storage/call_zzmUMXZsH2jlNBEHumFraywb.json', 'var_call_gjbCKfbmD3lXXIhLRmrgyHgr': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_kgVwUMufOhehk2wUxNM0dd2R': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_JXhrA4SimuFuX9llo9BwGFHH': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_IoI66mIKno166JbAcGDDHzaZ': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_0FFsvUFihbWdmICSmCaciOkz': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_TgehQT5PgohuFGEAhUsANJz2': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_cjhS63VXiuLtWblOFIb94uKF': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_42p5TV1QTYShq8MLhfATgdY3': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_G50LzqgSlZu2SYWbB02ms78Y': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_JdEKT6QNN6HTUXHCDfRV3N7O': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_xxC6AyTBuGMoIviMET5s38aF': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}], 'var_call_WbrANemlXHFaNKMTNIYZPK17': [{'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_SpgVvSjnVK0fu435RMBDhEaY': [{'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}], 'var_call_w2elXrr4Z40zFLQyg1GkHVcj': [{'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_5cdyplEO6AZ9dp8aTSdMUMLJ': [{'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}], 'var_call_hzM3JsHGT5vevGoDdATQ0J2h': [{'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}], 'var_call_GIyquGrLcxRlPzF8oBX0eXDC': [{'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}], 'var_call_0O73iZk0Wp6WQkxFKuFgpZht': [{'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}], 'var_call_600NviKeS6uWFEW0kuwv3rXN': [{'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}]}

exec(code, env_args)
