code = """import json, os, math
# load stockinfo result and many query results available in storage
stockinfo_var = var_call_ybrJiY7qN1q4Ht1Y8kc0VNaz

# list of query result variable names collected
keys = [
 'var_call_QlRkJgjDUJyd07WWLIb4AxGc','var_call_8PY6ySQE4MLdcfZo3bMStQ1f','var_call_EWgel0ztRhiAFfczT7CzRnqn',
 'var_call_8nmlhhngt0PoNOMYDc6i7eYc','var_call_mZAddzfTuuC4N62xsAEMYG95','var_call_PrDUKviKGjLVIv8dWnalBpM6',
 'var_call_bGLUXPwMB6PbQUtDpqOlN9ln','var_call_ru9a5cKsk8zXcV3Qw5WNMDR2','var_call_SYFnnTpFCXupcKJv3irRofzL',
 'var_call_cQgyHehcgFg7vCIqxpQbqSb8','var_call_7aQk9YPOWYPB3OIL0dXLs2Fh','var_call_b25s2ricgge5npFsGIYl2I0P',
 'var_call_giGEgA1O05fJPBMJDDPR5djJ','var_call_X8r50mvfKBxKIz0oOhFbGY2n','var_call_dLeW6xfy9d06DGr8EDb1KDql',
 'var_call_qf0FPov5WBzxorR1xKKJ8MSN','var_call_0t1bp065WDzkJH8cHN3vWZaj','var_call_aPJ4f3L5CdXO5I5qvReqaPfa',
 'var_call_NQ1ohzwVDp0yMM6HJoQnKpSC','var_call_iBIPW7yDLJP2wRfz4ByPW0kd','var_call_Is27gwRcnvtoR0qPfRJhegs7',
 'var_call_mgEO9fzs2JzRddBkOcqjLdhy','var_call_TUlkKpFiOBPDZWRQka6egjOj','var_call_2tfFxGlVk0rzWvCq6EjDULYj',
 'var_call_96BxyZyQ28D3dH7tX0Ii8E8M','var_call_Ctq6H9ymBXj5RphYEhnUlejV','var_call_6EzM2HWBXT6J7IsZJ10s4HFB',
 'var_call_bIxTKre4ai2zCYXjrUhkdnzw','var_call_RuhQlAFrjCto0en7hUMpsEAl','var_call_rnsNaPqZ1IKsLCzl9AaiOZKh',
 'var_call_CMMj0pOOz0ewknuwLDZfnPF5','var_call_cSR216S0mzuOqaxagf7A7eAR','var_call_eAxvO6epZnrW1bDDoFklwIS1',
 'var_call_uxvxPIcQdpHUt5XVS8RKeXsi','var_call_Hl7T3MNIYonFLtuacYTshsJZ','var_call_zJm8t8VRhcOuDwYfcsaS9HUk',
 'var_call_QgyXEqfuCE1Uc7nop2kpreGW','var_call_rnNjtO9RAgcUM67MTa83UIMr','var_call_duQ5nf9oxdQzqDiCtvh420SM',
 'var_call_ObgHnbJoeAXL95Vjc6mD8ZM6','var_call_WKIoD0wKK641ilGQvcHhKb3z','var_call_LM9p79fXPQz9vKh6UIn2iJ6H',
 'var_call_4tq3fGT2Tv4b0eNnyNNF6vJn','var_call_3wzH1qbE0uuNPJihKnunVztv','var_call_7OeraRK4j0B9WJVD24YOw8Yv',
 'var_call_181tn6Cg71gwsH3H5S94waKA','var_call_6GkAVPkgg0tG7CkqmRGmdRI8','var_call_Zdmt4nCRccBQdvRRdM0o14k4'
]

# helper to load potential file or var
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

stockinfo = load_var(stockinfo_var)

# build symbol -> company description
mapping = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    exch = rec.get('Listing Exchange')
    etf = rec.get('ETF')
    if sym and exch == 'N' and (etf is None or etf != 'Y'):
        mapping[sym] = rec.get('Company Description')

# collect results
results = []
for k in keys:
    if k not in globals():
        continue
    val = globals()[k]
    data = load_var(val)
    if not isinstance(data, list) or len(data)==0:
        continue
    rec = data[0]
    sym = rec.get('symbol')
    up = rec.get('up_count')
    down = rec.get('down_count')
    def to_num(x):
        if x is None:
            return None
        if isinstance(x, (int,float)):
            return int(x)
        xs = str(x)
        if xs.lower()=='nan':
            return None
        try:
            f = float(xs)
            if math.isnan(f):
                return None
            return int(f)
        except:
            return None
    upn = to_num(up)
    downn = to_num(down)
    results.append({'symbol':sym,'up':upn,'down':downn})

# filter where up>down
filtered = [r for r in results if r['up'] is not None and r['down'] is not None and r['up']>r['down']]
# sort by up desc
filtered.sort(key=lambda x: x['up'], reverse=True)
# take top 5
top5 = filtered[:5]
# map to company names
output = []
for r in top5:
    name = mapping.get(r['symbol'], r['symbol'])
    output.append({'symbol':r['symbol'],'company_name':name,'up':r['up'],'down':r['down']})

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ybrJiY7qN1q4Ht1Y8kc0VNaz': 'file_storage/call_ybrJiY7qN1q4Ht1Y8kc0VNaz.json', 'var_call_oD1ck6ZNbrCkc79DewGoacXv': 'file_storage/call_oD1ck6ZNbrCkc79DewGoacXv.json', 'var_call_uvBsGUqPZ0nfKhogw7GU92nj': {'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'symbols_count': 234}, 'var_call_QlRkJgjDUJyd07WWLIb4AxGc': [{'symbol': 'AEFC', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_8PY6ySQE4MLdcfZo3bMStQ1f': [{'symbol': 'AIN', 'up_count': '143.0', 'down_count': '101.0'}], 'var_call_EWgel0ztRhiAFfczT7CzRnqn': [{'symbol': 'AIV', 'up_count': '118.0', 'down_count': '128.0'}], 'var_call_8nmlhhngt0PoNOMYDc6i7eYc': [{'symbol': 'AIZP', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_mZAddzfTuuC4N62xsAEMYG95': [{'symbol': 'AJRD', 'up_count': '123.0', 'down_count': '123.0'}], 'var_call_PrDUKviKGjLVIv8dWnalBpM6': [{'symbol': 'AL', 'up_count': '131.0', 'down_count': '117.0'}], 'var_call_bGLUXPwMB6PbQUtDpqOlN9ln': [{'symbol': 'AMN', 'up_count': '134.0', 'down_count': '111.0'}], 'var_call_ru9a5cKsk8zXcV3Qw5WNMDR2': [{'symbol': 'AMP', 'up_count': '141.0', 'down_count': '110.0'}], 'var_call_SYFnnTpFCXupcKJv3irRofzL': [{'symbol': 'AMT', 'up_count': '128.0', 'down_count': '123.0'}], 'var_call_cQgyHehcgFg7vCIqxpQbqSb8': [{'symbol': 'ARD', 'up_count': '80.0', 'down_count': '119.0'}], 'var_call_7aQk9YPOWYPB3OIL0dXLs2Fh': [{'symbol': 'ARGD', 'up_count': '133.0', 'down_count': '82.0'}], 'var_call_b25s2ricgge5npFsGIYl2I0P': [{'symbol': 'ARLO', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_giGEgA1O05fJPBMJDDPR5djJ': [{'symbol': 'ASG', 'up_count': '110.0', 'down_count': '110.0'}], 'var_call_X8r50mvfKBxKIz0oOhFbGY2n': [{'symbol': 'AVA', 'up_count': '134.0', 'down_count': '112.0'}], 'var_call_dLeW6xfy9d06DGr8EDb1KDql': [{'symbol': 'BANC', 'up_count': '108.0', 'down_count': '119.0'}], 'var_call_qf0FPov5WBzxorR1xKKJ8MSN': [{'symbol': 'BBU', 'up_count': '129.0', 'down_count': '120.0'}], 'var_call_0t1bp065WDzkJH8cHN3vWZaj': [{'symbol': 'BBVA', 'up_count': '126.0', 'down_count': '104.0'}], 'var_call_aPJ4f3L5CdXO5I5qvReqaPfa': [{'symbol': 'BDXA', 'up_count': '83.0', 'down_count': '77.0'}], 'var_call_NQ1ohzwVDp0yMM6HJoQnKpSC': [{'symbol': 'BKH', 'up_count': '134.0', 'down_count': '115.0'}], 'var_call_iBIPW7yDLJP2wRfz4ByPW0kd': [{'symbol': 'BKT', 'up_count': '105.0', 'down_count': '97.0'}], 'var_call_Is27gwRcnvtoR0qPfRJhegs7': [{'symbol': 'BLD', 'up_count': '131.0', 'down_count': '120.0'}], 'var_call_mgEO9fzs2JzRddBkOcqjLdhy': [{'symbol': 'BNS', 'up_count': '132.0', 'down_count': '117.0'}], 'var_call_TUlkKpFiOBPDZWRQka6egjOj': [{'symbol': 'BV', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_2tfFxGlVk0rzWvCq6EjDULYj': [{'symbol': 'BZH', 'up_count': '127.0', 'down_count': '123.0'}], 'var_call_96BxyZyQ28D3dH7tX0Ii8E8M': [{'symbol': 'CADE', 'up_count': '88.0', 'down_count': '83.0'}], 'var_call_Ctq6H9ymBXj5RphYEhnUlejV': [{'symbol': 'CAE', 'up_count': '122.0', 'down_count': '117.0'}], 'var_call_6EzM2HWBXT6J7IsZJ10s4HFB': [{'symbol': 'CAF', 'up_count': '131.0', 'down_count': '113.0'}], 'var_call_bIxTKre4ai2zCYXjrUhkdnzw': [{'symbol': 'CBT', 'up_count': '128.0', 'down_count': '122.0'}], 'var_call_RuhQlAFrjCto0en7hUMpsEAl': [{'symbol': 'CCC', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_rnsNaPqZ1IKsLCzl9AaiOZKh': [{'symbol': 'CCZ', 'up_count': '17.0', 'down_count': '10.0'}], 'var_call_CMMj0pOOz0ewknuwLDZfnPF5': [{'symbol': 'CHAP', 'up_count': '34.0', 'down_count': '23.0'}], 'var_call_cSR216S0mzuOqaxagf7A7eAR': [{'symbol': 'CIA', 'up_count': '130.0', 'down_count': '112.0'}], 'var_call_eAxvO6epZnrW1bDDoFklwIS1': [{'symbol': 'CMA', 'up_count': '124.0', 'down_count': '124.0'}], 'var_call_uxvxPIcQdpHUt5XVS8RKeXsi': [{'symbol': 'CMI', 'up_count': '127.0', 'down_count': '123.0'}], 'var_call_Hl7T3MNIYonFLtuacYTshsJZ': [{'symbol': 'CMSA', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_zJm8t8VRhcOuDwYfcsaS9HUk': [{'symbol': 'CNK', 'up_count': '128.0', 'down_count': '122.0'}], 'var_call_QgyXEqfuCE1Uc7nop2kpreGW': [{'symbol': 'COTY', 'up_count': '124.0', 'down_count': '123.0'}], 'var_call_rnNjtO9RAgcUM67MTa83UIMr': [{'symbol': 'CRC', 'up_count': '121.0', 'down_count': '128.0'}], 'var_call_duQ5nf9oxdQzqDiCtvh420SM': [{'symbol': 'CRM', 'up_count': '137.0', 'down_count': '113.0'}], 'var_call_ObgHnbJoeAXL95Vjc6mD8ZM6': [{'symbol': 'CRS', 'up_count': '121.0', 'down_count': '128.0'}], 'var_call_WKIoD0wKK641ilGQvcHhKb3z': [{'symbol': 'CSL', 'up_count': '131.0', 'down_count': '119.0'}], 'var_call_LM9p79fXPQz9vKh6UIn2iJ6H': [{'symbol': 'CTS', 'up_count': '113.0', 'down_count': '122.0'}], 'var_call_4tq3fGT2Tv4b0eNnyNNF6vJn': [{'symbol': 'CUBE', 'up_count': '133.0', 'down_count': '113.0'}], 'var_call_3wzH1qbE0uuNPJihKnunVztv': [{'symbol': 'CURO', 'up_count': '9.0', 'down_count': '7.0'}], 'var_call_7OeraRK4j0B9WJVD24YOw8Yv': [{'symbol': 'CVIA', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_181tn6Cg71gwsH3H5S94waKA': [{'symbol': 'CVX', 'up_count': '118.0', 'down_count': '132.0'}], 'var_call_6GkAVPkgg0tG7CkqmRGmdRI8': [{'symbol': 'CXH', 'up_count': '126.0', 'down_count': '91.0'}], 'var_call_Zdmt4nCRccBQdvRRdM0o14k4': [{'symbol': 'DAC', 'up_count': '66.0', 'down_count': '115.0'}]}

exec(code, env_args)
