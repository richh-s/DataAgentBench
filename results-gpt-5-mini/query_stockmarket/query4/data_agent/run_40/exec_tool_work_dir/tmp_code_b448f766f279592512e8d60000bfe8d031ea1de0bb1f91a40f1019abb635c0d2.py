code = """import json, os, math
# Collect all variables from storage that start with var_call_
vars_dict = {k: globals().get(k) for k in list(globals().keys()) if k.startswith('var_call_')}
# Function to load value if it's a filepath
def load_val(v):
    if isinstance(v, str) and os.path.exists(v):
        try:
            return json.load(open(v, 'r'))
        except Exception:
            return v
    return v

all_data = []
for k,v in vars_dict.items():
    val = load_val(v)
    # val might be list of records (from query_db) or dict
    if isinstance(val, list):
        # extend
        all_data.append((k, val))
    else:
        all_data.append((k, val))

# Find stockinfo data (from initial stockinfo query)
stockinfo_key = None
for k,val in all_data:
    if isinstance(val, list) and len(val)>0 and 'Symbol' in val[0]:
        stockinfo_key = k
        stockinfo = val
        break
# Build symbol->company description map
sym_to_name = {}
if stockinfo_key:
    for r in stockinfo:
        sym = r.get('Symbol')
        desc = r.get('Company Description')
        if sym:
            sym_to_name[sym] = desc

# Collect symbol up/down results from query_db outputs
rows = []
for k,val in all_data:
    if isinstance(val, list) and len(val)>0:
        rec = val[0]
        if isinstance(rec, dict) and 'symbol' in rec and 'up' in rec and 'down' in rec:
            sym = rec.get('symbol')
            up = rec.get('up')
            down = rec.get('down')
            # convert to number if possible
            def to_num(x):
                if x is None:
                    return None
                if isinstance(x, (int,float)):
                    return x
                try:
                    if isinstance(x, str) and x.lower()=='nan':
                        return None
                    return float(x)
                except Exception:
                    return None
            upn = to_num(up)
            downn = to_num(down)
            rows.append({'symbol': sym, 'up': upn, 'down': downn})

# Deduplicate by symbol preferring non-None up
by_sym = {}
for r in rows:
    s = r['symbol']
    if s not in by_sym:
        by_sym[s]=r
    else:
        # if existing has None and new has value, replace
        existing = by_sym[s]
        if (existing['up'] is None or math.isnan(existing['up'])) and (r['up'] is not None and not math.isnan(r['up'])):
            by_sym[s]=r

# Build list and filter to symbols present in stockinfo (non-ETF NYSE list)
candidates = []
for s,r in by_sym.items():
    if s in sym_to_name:
        up = r['up']
        down = r['down']
        if up is None or down is None:
            continue
        # consider more up days than down days
        if up>down:
            candidates.append({'symbol': s, 'up': int(up), 'down': int(down), 'name': sym_to_name.get(s)})

# Sort by up desc, take top 5
candidates_sorted = sorted(candidates, key=lambda x: x['up'], reverse=True)
top5 = candidates_sorted[:5]
# Prepare output: names only
names = [ (r['name'] if r['name'] is not None else r['symbol']) for r in top5 ]
print("__RESULT__:")
print(json.dumps(names))"""

env_args = {'var_call_Z1LS9TfnT11V5aMqhG55TyCL': 'file_storage/call_Z1LS9TfnT11V5aMqhG55TyCL.json', 'var_call_s3uNzaz6ShglCpABRigHiCQR': {'count': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_I2w2b6tM7HA6SwmLOflp4Vzk': [{'symbol': 'AEFC', 'up': 'nan', 'down': 'nan'}], 'var_call_mfzQ8soJ48OG3DlRaGaXVVRD': [{'symbol': 'AIN', 'up': '143.0', 'down': '101.0'}], 'var_call_LfuQb0M0bf7SycAZ0YdYqRhX': [{'symbol': 'AIV', 'up': '118.0', 'down': '128.0'}], 'var_call_bZxnVadsGpJPtD7RUxYOYxgM': [{'symbol': 'AIZP', 'up': 'nan', 'down': 'nan'}], 'var_call_zM3wGAw9WTimAu9reFR6iPTF': [{'symbol': 'AJRD', 'up': '123.0', 'down': '123.0'}], 'var_call_c1eC5Ae6li9LHfon3L7j3hih': [{'symbol': 'AL', 'up': '131.0', 'down': '117.0'}], 'var_call_ZtnczWPhpBnzgsuKNOOJ83ux': [{'symbol': 'AMN', 'up': '134.0', 'down': '111.0'}], 'var_call_Pf11hNJkBcGZyabfWDcUSiMX': [{'symbol': 'AMP', 'up': '141.0', 'down': '110.0'}], 'var_call_hgl9OgY2eGTMbZ6nFIg95ZsL': [{'symbol': 'AMT', 'up': '128.0', 'down': '123.0'}], 'var_call_n9Ar8NTIFscRhyIITjistuVs': [{'symbol': 'ARD', 'up': '80.0', 'down': '119.0'}], 'var_call_ChwE51tTmFYn27y6PszJ3SqJ': [{'symbol': 'ARGD', 'up': '133.0', 'down': '82.0'}], 'var_call_L7IquCBRl75ibgHiOxv7WShz': [{'symbol': 'ARLO', 'up': 'nan', 'down': 'nan'}], 'var_call_bFCv90faNoByeMrQW8AXt0ZP': [{'symbol': 'ASG', 'up': '110.0', 'down': '110.0'}], 'var_call_KCcS0DUSG1HmmNqg7LernHhP': [{'symbol': 'AVA', 'up': '134.0', 'down': '112.0'}], 'var_call_PnZ2OFooN4l5yYK62GV60OuE': [{'symbol': 'BANC', 'up': '108.0', 'down': '119.0'}], 'var_call_Ydk9bvh1anuOyZ857POFIEtz': [{'symbol': 'BBU', 'up': '129.0', 'down': '120.0'}], 'var_call_zOjuIIAb9URRG5Je46POu3Pl': [{'symbol': 'BBVA', 'up': '126.0', 'down': '104.0'}], 'var_call_YbLfUx7Fy2ArSReT4P8rfIkF': [{'symbol': 'BDXA', 'up': '83.0', 'down': '77.0'}], 'var_call_zhZv6CDJfDMxLA2sE0sECvUg': [{'symbol': 'BKH', 'up': '134.0', 'down': '115.0'}], 'var_call_cTHs384K7B2xl4K8Eniyi4Yk': [{'symbol': 'BKT', 'up': '105.0', 'down': '97.0'}], 'var_call_n1NKQzjPTdC9ZNAlR5MUuuHZ': [{'symbol': 'BLD', 'up': '131.0', 'down': '120.0'}], 'var_call_yoSnyUXVHTL0d6PBgrjMQDX1': [{'symbol': 'BNS', 'up': '132.0', 'down': '117.0'}], 'var_call_uO5m8aqM7OIay7jOMHqcKl70': [{'symbol': 'BV', 'up': 'nan', 'down': 'nan'}], 'var_call_GcNTIsUhK8UCsJvkapkFJ4gC': [{'symbol': 'BZH', 'up': '127.0', 'down': '123.0'}], 'var_call_pxlacaXCfuj4C3ZvkXK0OIwT': [{'symbol': 'CADE', 'up': '88.0', 'down': '83.0'}], 'var_call_EcWGl6gYAV74ezQZkucmPgly': [{'symbol': 'CAE', 'up': '122.0', 'down': '117.0'}], 'var_call_1mGWu525BEAJdM2l9HBpzcSw': [{'symbol': 'CAF', 'up': '131.0', 'down': '113.0'}], 'var_call_Wdjfc6zSq3DPRbU0PfslaPOe': [{'symbol': 'CBT', 'up': '128.0', 'down': '122.0'}], 'var_call_fHh4DZGgYBz2UB9fqXL8h7eq': [{'symbol': 'CCC', 'up': 'nan', 'down': 'nan'}], 'var_call_Q7KEZCbJbKndZU7tsBAi3Q2s': [{'symbol': 'CCZ', 'up': '17.0', 'down': '10.0'}], 'var_call_oYh6uDFYkk5Sl0NRTF8BJryR': [{'symbol': 'CHAP', 'up': '34.0', 'down': '23.0'}], 'var_call_BcMD8mxiMogOoTQ3Zi3xtfOP': [{'symbol': 'AEFC', 'up': 'nan', 'down': 'nan'}], 'var_call_Y8oMNFW5f7lUoh4UbVC9TtFC': [{'symbol': 'AIN', 'up': '143.0', 'down': '101.0'}], 'var_call_LyyvfaE0iD5R8Czn7iymfuvR': [{'symbol': 'AIV', 'up': '118.0', 'down': '128.0'}], 'var_call_tRKTpsRVYolaZU5sXS6sRKsv': [{'symbol': 'AIZP', 'up': 'nan', 'down': 'nan'}], 'var_call_HacJ7CtqvBql0UqQNzD9Xtj7': [{'symbol': 'AJRD', 'up': '123.0', 'down': '123.0'}], 'var_call_OPH7x3jmZmAHCH2of8ADBfZj': [{'symbol': 'AL', 'up': '131.0', 'down': '117.0'}], 'var_call_bItsYpancDDizGQCMF99AMez': [{'symbol': 'AMN', 'up': '134.0', 'down': '111.0'}], 'var_call_UQJyNmdp52KVLQ8qruohiXMs': [{'symbol': 'AMP', 'up': '141.0', 'down': '110.0'}], 'var_call_wQQlMrrEtI2UNx2vOcturaYG': [{'symbol': 'AMT', 'up': '128.0', 'down': '123.0'}], 'var_call_tbRMH2G6uSugh5tcEvrD8wPl': [{'symbol': 'ARD', 'up': '80.0', 'down': '119.0'}], 'var_call_mbuEIsYofM2lx5aHJYey9hZQ': [{'symbol': 'ARGD', 'up': '133.0', 'down': '82.0'}], 'var_call_EcJE5J92ILYbfAmQsTF7BYvX': [{'symbol': 'ARLO', 'up': 'nan', 'down': 'nan'}], 'var_call_F4madjZIOsytLMWVCgfcvgxF': [{'symbol': 'ASG', 'up': '110.0', 'down': '110.0'}], 'var_call_NgRXjcBOAitcpwXNA1Wtrgo0': [{'symbol': 'AVA', 'up': '134.0', 'down': '112.0'}], 'var_call_Yp7bM692XAHcJcHf2J02dmsF': [{'symbol': 'BANC', 'up': '108.0', 'down': '119.0'}], 'var_call_PFIE8UsYDbqtYy9KN9WFlJGJ': [{'symbol': 'BBU', 'up': '129.0', 'down': '120.0'}], 'var_call_VdLT4IROIOZDhjZFNoucApUb': [{'symbol': 'BBVA', 'up': '126.0', 'down': '104.0'}], 'var_call_BfW1ZGW64dqNY3z4t2cuVRBv': [{'symbol': 'BDXA', 'up': '83.0', 'down': '77.0'}], 'var_call_23gGvKDWIuU4qNc1RyXaWldO': [{'symbol': 'BKH', 'up': '134.0', 'down': '115.0'}], 'var_call_my1fn4F2X12qEvPSn9YjVVKQ': [{'symbol': 'BKT', 'up': '105.0', 'down': '97.0'}], 'var_call_lhEjVwNztNL4c9chyuIe2GRM': [{'symbol': 'BLD', 'up': '131.0', 'down': '120.0'}], 'var_call_BZiyuU4c4uSwjstOOCYaXXaI': [{'symbol': 'BNS', 'up': '132.0', 'down': '117.0'}], 'var_call_Y9ha0QpY98KyhyBAxFtZvioJ': [{'symbol': 'BV', 'up': 'nan', 'down': 'nan'}], 'var_call_LveHgnqWvLMvl4K9SwSGN4hR': [{'symbol': 'BZH', 'up': '127.0', 'down': '123.0'}], 'var_call_Tp09LixFl2hkzNzJF4Q3qfpC': [{'symbol': 'CADE', 'up': '88.0', 'down': '83.0'}], 'var_call_2ct7QCbiBCkFYJDptSi1oWUh': [{'symbol': 'CAE', 'up': '122.0', 'down': '117.0'}], 'var_call_TLbWRwdTAvsx43orAmB6w4vh': [{'symbol': 'CAF', 'up': '131.0', 'down': '113.0'}], 'var_call_1jwSCTivmnKzHEzFmzeM0K8m': [{'symbol': 'CBT', 'up': '128.0', 'down': '122.0'}], 'var_call_QnfgbgDUmcVr1JVHcWoCgDtb': [{'symbol': 'CCC', 'up': 'nan', 'down': 'nan'}], 'var_call_e94Q15auLrgb5yOBBCrJOBYL': [{'symbol': 'CCZ', 'up': '17.0', 'down': '10.0'}], 'var_call_Gwp8mBYxfcuFygN3yHoWTVTr': [{'symbol': 'CHAP', 'up': '34.0', 'down': '23.0'}], 'var_call_um8KyxF2VFZbsSLeC4DDS5PQ': [{'symbol': 'CIA', 'up': '130.0', 'down': '112.0'}], 'var_call_W8eZAN9NK3Qd3O9XuWdqyRS6': [{'symbol': 'CMA', 'up': '124.0', 'down': '124.0'}], 'var_call_KDGYGo5VsSgp0Oxvhrfu4Wrq': [{'symbol': 'CMI', 'up': '127.0', 'down': '123.0'}], 'var_call_I9eynHmEgJ3ahizxZsIj9A1F': [{'symbol': 'CMSA', 'up': 'nan', 'down': 'nan'}], 'var_call_79qiqWvKXv8wxtTIIfpUGZ70': [{'symbol': 'CNK', 'up': '128.0', 'down': '122.0'}], 'var_call_BgqvkhB0sLDqw9hOPNpmxzCn': [{'symbol': 'COTY', 'up': '124.0', 'down': '123.0'}], 'var_call_wcjBetHhI9gocJWiM7GG9jK5': [{'symbol': 'CRC', 'up': '121.0', 'down': '128.0'}], 'var_call_xfz6FUssP87bWQFOwJOsQFuV': [{'symbol': 'CRM', 'up': '137.0', 'down': '113.0'}], 'var_call_XuePJIKo2cQMehAauMaHwRwu': [{'symbol': 'CRS', 'up': '121.0', 'down': '128.0'}], 'var_call_VWSxtU2TTCQ8958mhGMRtDrd': [{'symbol': 'CSL', 'up': '131.0', 'down': '119.0'}], 'var_call_cVYOZiMVoAgxb4tjVIhouHyN': [{'symbol': 'CTS', 'up': '113.0', 'down': '122.0'}], 'var_call_QazxVnnyACBTprC1fwtpnmq2': 'file_storage/call_QazxVnnyACBTprC1fwtpnmq2.json', 'var_call_DVRWDjcyC5va2zsJdpUovHE1': [{'symbol': 'AEFC', 'up': 'nan', 'down': 'nan'}], 'var_call_9TN4GkL29I8i63wcUUF0nR2B': [{'symbol': 'AIN', 'up': '143.0', 'down': '101.0'}], 'var_call_igr2VTRM0y73nwZNMlnRQbNr': [{'symbol': 'AIV', 'up': '118.0', 'down': '128.0'}], 'var_call_2MedkF9cCEInprVA156AgEPB': [{'symbol': 'AIZP', 'up': 'nan', 'down': 'nan'}], 'var_call_ZrxigcUqNXqYTVfufS6KpHNl': [{'symbol': 'AJRD', 'up': '123.0', 'down': '123.0'}], 'var_call_dWVqDbem6IZunqstL60QODRF': [{'symbol': 'AL', 'up': '131.0', 'down': '117.0'}], 'var_call_Phi9c8ITd1yhlTOlEEXo0VKH': [{'symbol': 'AMN', 'up': '134.0', 'down': '111.0'}], 'var_call_t6sMS8CvU1iUcMhie3zI9y19': [{'symbol': 'AMP', 'up': '141.0', 'down': '110.0'}], 'var_call_aC6Y0RECgE92bgtXyQ5RKQ52': [{'symbol': 'AMT', 'up': '128.0', 'down': '123.0'}], 'var_call_Xf8XG1EZuA2yHeTMPCHsQRo9': [{'symbol': 'ARD', 'up': '80.0', 'down': '119.0'}], 'var_call_n3ckUBL3DPFiV4eZ1qHJA9lh': [{'symbol': 'ARGD', 'up': '133.0', 'down': '82.0'}], 'var_call_6G5kMFVVLkvapPYl3K4yD4mB': [{'symbol': 'ARLO', 'up': 'nan', 'down': 'nan'}], 'var_call_A1ZPs6aGyRIqpjNCDppy8RB3': [{'symbol': 'ASG', 'up': '110.0', 'down': '110.0'}], 'var_call_aL9wZOL5iwzsLjbOurLMpTvV': [{'symbol': 'AVA', 'up': '134.0', 'down': '112.0'}], 'var_call_sWwUM7DznL3alDqzf5z5VbqW': [{'symbol': 'BANC', 'up': '108.0', 'down': '119.0'}], 'var_call_66FiT7frhuhtBn4fkTxYxO29': [{'symbol': 'BBU', 'up': '129.0', 'down': '120.0'}], 'var_call_zeaSp1yS5C54nhkycjtiZjEJ': [{'symbol': 'BBVA', 'up': '126.0', 'down': '104.0'}], 'var_call_WDpVWq09uxQWm44zNYNxrSlo': [{'symbol': 'BDXA', 'up': '83.0', 'down': '77.0'}], 'var_call_EQrsKwGe9xD0hbLvIPwlSmJW': [{'symbol': 'BKH', 'up': '134.0', 'down': '115.0'}], 'var_call_xDsvL0URSHiVGuh2JZhovYcE': [{'symbol': 'BKT', 'up': '105.0', 'down': '97.0'}], 'var_call_9YfWVRX83TqML8R41SP5ZBoE': [{'symbol': 'BLD', 'up': '131.0', 'down': '120.0'}], 'var_call_fv9og42SgZrjntqZqaibWM7Z': [{'symbol': 'BNS', 'up': '132.0', 'down': '117.0'}], 'var_call_PQERBdhcEJ7WxD5R1NtIaBxP': [{'symbol': 'BV', 'up': 'nan', 'down': 'nan'}], 'var_call_G6JsJDB9zUIUuKCMSR6LavGV': [{'symbol': 'BZH', 'up': '127.0', 'down': '123.0'}], 'var_call_demM3HTsPZZNresCX0gaZM1s': [{'symbol': 'CADE', 'up': '88.0', 'down': '83.0'}], 'var_call_eQ2t2j5Yra3lbtsuGkUQapdp': [{'symbol': 'CAE', 'up': '122.0', 'down': '117.0'}], 'var_call_nZrAvdCLcruv3V5LMZ4WT1dL': [{'symbol': 'CAF', 'up': '131.0', 'down': '113.0'}], 'var_call_wtkjtqYNEQ086OyfskZabWM0': [{'symbol': 'CBT', 'up': '128.0', 'down': '122.0'}]}

exec(code, env_args)
