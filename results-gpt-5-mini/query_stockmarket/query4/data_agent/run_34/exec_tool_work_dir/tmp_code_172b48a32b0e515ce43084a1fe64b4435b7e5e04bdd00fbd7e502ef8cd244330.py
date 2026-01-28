code = """import json, math, os
# Prepare list of var_call keys
all_keys = list(globals().keys())
var_keys = [k for k in all_keys if k.startswith('var_call_')]
# Load stockinfo mapping
stock_map = {}
stockinfo_key = 'var_call_HEKveFApzB5OJoibVOo3FeNG'
if stockinfo_key in globals():
    path = globals()[stockinfo_key]
    if isinstance(path, str) and os.path.exists(path):
        with open(path, 'r') as f:
            stockinfo = json.load(f)
        for rec in stockinfo:
            sym = rec.get('Symbol')
            desc = rec.get('Company Description')
            if sym:
                stock_map[sym] = desc

records = []
for key in var_keys:
    if key in (stockinfo_key, 'var_call_bB4AdaDG75rQ4lJcrmnQ5gCQ'):
        continue
    v = globals()[key]
    # If v is a path to a file, load it
    if isinstance(v, str) and os.path.exists(v):
        try:
            with open(v, 'r') as f:
                v = json.load(f)
        except Exception:
            # try to parse as json string
            try:
                v = json.loads(v)
            except Exception:
                continue
    # If v is a string containing JSON-like list, try parse
    if isinstance(v, str):
        try:
            vv = json.loads(v)
            v = vv
        except Exception:
            # skip non-json strings
            continue
    # Now if v is a list of dicts
    if isinstance(v, list):
        for rec in v:
            if not isinstance(rec, dict):
                continue
            if 'symbol' not in rec:
                continue
            sym = rec.get('symbol')
            up = rec.get('up_days')
            down = rec.get('down_days')
            # convert to float
            try:
                up_n = float(up)
            except Exception:
                up_n = float('nan')
            try:
                down_n = float(down)
            except Exception:
                down_n = float('nan')
            records.append({'symbol': sym, 'up': up_n, 'down': down_n})

# Filter valid where up and down are numbers and up > down
valid = [r for r in records if (not math.isnan(r['up'])) and (not math.isnan(r['down'])) and (r['up'] > r['down'])]
# Remove duplicates keeping max up if duplicates
best = {}
for r in valid:
    s = r['symbol']
    if s not in best or r['up'] > best[s]['up']:
        best[s] = r
valid_unique = list(best.values())
# Sort by up descending, then by symbol
valid_sorted = sorted(valid_unique, key=lambda x: (-x['up'], x['symbol']))
# Take top 5
top5 = valid_sorted[:5]
# Map to company names
result_names = []
for r in top5:
    sym = r['symbol']
    name = stock_map.get(sym)
    if name is None:
        name = sym
    result_names.append(name)

print('__RESULT__:')
print(json.dumps(result_names))"""

env_args = {'var_call_HEKveFApzB5OJoibVOo3FeNG': 'file_storage/call_HEKveFApzB5OJoibVOo3FeNG.json', 'var_call_bB4AdaDG75rQ4lJcrmnQ5gCQ': 'file_storage/call_bB4AdaDG75rQ4lJcrmnQ5gCQ.json', 'var_call_d6QGcNKKvqyuOrhcmw1Y50gS': {'candidates': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_4WIpkbtLaRsLyQ4B4LV5F1WN': {'count': 234}, 'var_call_5FousGiPVzvLRjxp4bPjeMs6': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_A0Q1gEdhybYVRDhwxIyDNKkf': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_nfpCuhTGWQsFNhXuJggtV9Xd': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_KBj1kNprPSxtHHIsrrW0O9cp': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_nCrnCBdQJWpp7M5C5fmTwbCG': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_5Nv2FUXjrBqoUyPrQmo5Eg1w': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_E8Hzc3UmGNmiVZX5V7vEW3k6': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_PK2Z0ICkoj66aRKhyCY3RitB': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_XUNlGwSVLyVmDqvPQPG1vAb2': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_pUsD44ui3K9YLIHJt4cSPJTt': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_Y1wADHS220GwZx0Xy8kbDiaq': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}], 'var_call_KAJBsTvMbm4EPesLwq00fYSa': [{'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_990EzL0EeqcBcim3N76E18E7': [{'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}], 'var_call_JTeK5BbCtmr3DHSj9lPHU8Ib': [{'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_xvqstKG32jYBLjKqAXMinG0X': [{'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}], 'var_call_Z99mNv3OMLGq5vcfLlJS5mFO': [{'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}], 'var_call_1RFZrL7TJ2cDy6aW872d3UL5': [{'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}], 'var_call_4WtdxanFNbiShHkJnvKPOf4M': [{'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}], 'var_call_alcfbMQHtVQonLP6xodrov3Y': [{'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}], 'var_call_RxGiu9F09AAZkeCqEFrfuJzY': [{'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}], 'var_call_LYvmp2fk2FCH2pkDGMiqstHe': [{'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}], 'var_call_ZlSHOgKdHTm8cfoCfHPaztyX': [{'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}], 'var_call_dSDaQh50fKBvqq9Kt4IPzA9M': [{'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_BFpb8Y6kNvZhHRaAmuNSWkE1': [{'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_hI4JNWnnWBFHZZI9MN6oqDGx': [{'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}], 'var_call_cXSMGtQgIFsgMIVR5RXdl17i': [{'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}], 'var_call_TtTiEcu2gokIRIwafRxli5d9': [{'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}], 'var_call_6nniA47BLXYPhdCgWwjws3yA': [{'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}], 'var_call_4LrZuo3EgFUmSCQBUrEBUTlY': [{'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_zKHJDbdyzcFgqjDSN0RTpilg': [{'symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}], 'var_call_c7tyDNGD55nay8sa0eCDycHi': [{'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}], 'var_call_5VfP80nQUWkKhbT02IgrByeW': [{'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}], 'var_call_fZjQxdr7zVUdkNBNoVfi7ZPn': [{'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}], 'var_call_g0HFYW4BbrlT903nhGfCTWWR': [{'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_Eatae84m4E2mvKFj3PEqBJAJ': [{'symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_iq3xfXTWQUhg7eEOOg9KxRWm': [{'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}], 'var_call_9X24BOjWPUqGREB9YTTcbb37': [{'symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}], 'var_call_ktnlFInhzWuR5ktuIznqhYaW': [{'symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}], 'var_call_V6QmpPRlYMTMnQYHf2Md61W4': [{'symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}], 'var_call_R4aHmBQErzRw8UrtZIDUUHEB': [{'symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}], 'var_call_AnqQ7iT73oDfY0228rLV42K6': [{'symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}], 'var_call_ojOi08AImbBwE7nh2pWiPcu3': [{'symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}], 'var_call_9fPEa4NJdfjnDETm4UqXbfpf': [{'symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}], 'var_call_HdhRLLUueGprqTTEf77VBxFI': [{'symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}], 'var_call_U7xuzI4wStK5u4dgCVtm0Iag': [{'symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_0c0A8cYDwvqZOlzkp9L1iWnQ': [{'symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}], 'var_call_FrbjfMpyHEMHLgf45Hm3EZUn': [{'symbol': 'CXH', 'up_days': '126.0', 'down_days': '91.0'}], 'var_call_gbdRefUlXtkcgINCAmZZFiRe': [{'symbol': 'DAC', 'up_days': '66.0', 'down_days': '115.0'}], 'var_call_vepvZLnj8940zPt3EYStXDpk': [{'symbol': 'DDS', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_QPTIB5Y5day4evJfeUErLPuH': [{'symbol': 'DDT', 'up_days': '118.0', 'down_days': '119.0'}], 'var_call_cxiribIwqyNo2oYMVpRqkgcR': [{'symbol': 'DEO', 'up_days': '131.0', 'down_days': '120.0'}], 'var_call_pHRbF2q5WufFEv4E2dEugcxQ': [{'symbol': 'DGX', 'up_days': '129.0', 'down_days': '121.0'}], 'var_call_gxgQfYSTzwoieplGjT7C7POZ': [{'symbol': 'DMB', 'up_days': '132.0', 'down_days': '95.0'}], 'var_call_93Ucs84JLyIEVT4ivb62InSj': [{'symbol': 'DTQ', 'up_days': '139.0', 'down_days': '98.0'}], 'var_call_eW5UROs0HSIeBq0i2Mwd8nro': [{'symbol': 'DXC', 'up_days': '133.0', 'down_days': '116.0'}], 'var_call_ZL1F9LSuQej9Ptcr01xoXFTU': [{'symbol': 'EARN', 'up_days': '114.0', 'down_days': '124.0'}], 'var_call_Hn0xlK4aa4dfmDqYb61wQAv2': [{'symbol': 'EBS', 'up_days': '133.0', 'down_days': '115.0'}], 'var_call_3RogrZYVV2xlSvY1wSnRJwTY': [{'symbol': 'EGO', 'up_days': '108.0', 'down_days': '123.0'}], 'var_call_5ueGqMzizHZxDE3gNq3Qgti1': [{'symbol': 'EGY', 'up_days': '100.0', 'down_days': '128.0'}], 'var_call_fSOLFtoWkcgbUHUFuudIyR1C': [{'symbol': 'EIG', 'up_days': '125.0', 'down_days': '116.0'}], 'var_call_j8rtD30g5ULShGUs5jZ6FNnE': [{'symbol': 'ELF', 'up_days': '121.0', 'down_days': '129.0'}], 'var_call_SZCT1kQTJ4HGmBla8Djgakax': [{'symbol': 'EMP', 'up_days': '74.0', 'down_days': '100.0'}], 'var_call_b1SX5JTQ0Ivk9POqXVK7jDWb': [{'symbol': 'ENLC', 'up_days': '107.0', 'down_days': '124.0'}], 'var_call_6NjPavp12SeRpGr2PkPP96SB': [{'symbol': 'EPR', 'up_days': '132.0', 'down_days': '117.0'}], 'var_call_aMSKwoOBN5xyvtxONeDPUhyO': [{'symbol': 'EPRT', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_iNYuHFmYmn9gwLtQRDDi0ZQf': [{'symbol': 'ES', 'up_days': '132.0', 'down_days': '117.0'}], 'var_call_RvPhHoBEv8BlZwFG2SeCn1hp': [{'symbol': 'ESRT', 'up_days': '124.0', 'down_days': '125.0'}], 'var_call_2bjP5fzPtZfbwdjuy0VhZ87D': [{'symbol': 'ESS', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_vdW641R58iB1f0j9aSCheuYU': [{'symbol': 'ETM', 'up_days': '97.0', 'down_days': '140.0'}], 'var_call_0L3NhBlOqxjshtaxIM4L3wJx': [{'symbol': 'EV', 'up_days': '139.0', 'down_days': '112.0'}], 'var_call_vKGoafWEWxr49iqR37nKUCr5': [{'symbol': 'EVT', 'up_days': '131.0', 'down_days': '109.0'}], 'var_call_dLOn7ZW91K20NJbvJvp58RLQ': [{'symbol': 'EXP', 'up_days': '127.0', 'down_days': '124.0'}], 'var_call_WqmS2s5jY8nPS4MB72AZVwgZ': [{'symbol': 'FMN', 'up_days': '119.0', 'down_days': '106.0'}], 'var_call_IzzWoDhg5VW33JK2j2UDwAbJ': [{'symbol': 'FPAC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_Q6dUfsI9EjhLWPvAp47h9usl': [{'symbol': 'FSM', 'up_days': '113.0', 'down_days': '132.0'}], 'var_call_MuEDje3X9auTCbxuND4oM65K': [{'symbol': 'GCO', 'up_days': '119.0', 'down_days': '126.0'}], 'var_call_foKYLtpT8buVwAcpoN0kTJTd': [{'symbol': 'GD', 'up_days': '134.0', 'down_days': '117.0'}], 'var_call_cQNvUmQNWkC3drZyChtIOhmN': [{'symbol': 'GDL', 'up_days': '122.0', 'down_days': '97.0'}], 'var_call_MkmTcFMvS6Y7FqQY4PyC6mCV': [{'symbol': 'GDV', 'up_days': '126.0', 'down_days': '110.0'}], 'var_call_dnALrJwJGkhRIDX4JQraXj7P': [{'symbol': 'GEL', 'up_days': '103.0', 'down_days': '144.0'}], 'var_call_KlSM5iUy3eMRUk5KXNOELlMt': [{'symbol': 'GJP', 'up_days': '25.0', 'down_days': '23.0'}], 'var_call_X40S2ussL46mKD7i9HdtOBak': [{'symbol': 'GLOB', 'up_days': '126.0', 'down_days': '123.0'}], 'var_call_FDPjT6tSsdxO7iG4rHowVlO7': [{'symbol': 'GLT', 'up_days': '117.0', 'down_days': '130.0'}], 'var_call_dAxdjQO0kPpGPTluCEdgKJVH': [{'symbol': 'GOL', 'up_days': '116.0', 'down_days': '133.0'}], 'var_call_XpAv2IlsRuXze5HMrZJbC6jL': [{'symbol': 'GSLD', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_yYEPhIzF9LM9B7FjAzcuMM0w': [{'symbol': 'GTY', 'up_days': '143.0', 'down_days': '104.0'}], 'var_call_8HoEOUC08tsH2aovAfX2PFPu': [{'symbol': 'GVA', 'up_days': '120.0', 'down_days': '131.0'}], 'var_call_N5vZuQeQgH4lOm3WRz9J29UR': [{'symbol': 'GWB', 'up_days': '119.0', 'down_days': '130.0'}], 'var_call_cCC24ieO3cZM5m4We9rD4xR1': [{'symbol': 'H', 'up_days': '135.0', 'down_days': '115.0'}], 'var_call_TCzVbYvKYNahv3Nl5euMGwMk': [{'symbol': 'HBI', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_D4jppK4yO1uodQ16JwcrJ1oR': [{'symbol': 'HDB', 'up_days': '146.0', 'down_days': '102.0'}], 'var_call_2P0FYnJIE6BjGxhAiHkoPgwq': [{'symbol': 'HEP', 'up_days': '117.0', 'down_days': '133.0'}], 'var_call_1jec5WoAtR3lb6N1jjSQX14a': [{'symbol': 'HIL', 'up_days': '101.0', 'down_days': '96.0'}], 'var_call_cu9mvbKCcJhUyztOHfEvCvVd': [{'symbol': 'HIO', 'up_days': '121.0', 'down_days': '92.0'}], 'var_call_CEMKD1W2MEnZtvcjZr9GknZG': [{'symbol': 'HIX', 'up_days': '113.0', 'down_days': '100.0'}], 'var_call_7UmY7BbA7jFESvu5qgQPxGYw': [{'symbol': 'HLF', 'up_days': '140.0', 'down_days': '110.0'}], 'var_call_TunoDNdlvlSrpanYZL1ei07I': [{'symbol': 'HLT', 'up_days': '129.0', 'down_days': '119.0'}], 'var_call_ZVvGgxqQ71PCkIZQe3WTQz9m': [{'symbol': 'HNI', 'up_days': '130.0', 'down_days': '120.0'}], 'var_call_xSjqczR0Q9ZB7gmbCIp5EthN': [{'symbol': 'HRB', 'up_days': '135.0', 'down_days': '111.0'}], 'var_call_muVRYyT2EW0B4auCxZXXogkO': [{'symbol': 'HTFA', 'up_days': '13.0', 'down_days': '35.0'}], 'var_call_qA2s2G2JzqeysPewKrmOeoX9': [{'symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}], 'var_call_2Xe0c4jWv89ibxEbc2SPyS7E': [{'symbol': 'IGR', 'up_days': '126.0', 'down_days': '101.0'}], 'var_call_VSZiannSOy6FIwkdtwu0U4Z4': [{'symbol': 'IHC', 'up_days': '98.0', 'down_days': '134.0'}], 'var_call_O1YVfkpJbk4dTpYha0qRgdPS': [{'symbol': 'IPG', 'up_days': '129.0', 'down_days': '116.0'}], 'var_call_20iPO5uGl5Oiq4mWGTOb8kK6': [{'symbol': 'IRM', 'up_days': '131.0', 'down_days': '116.0'}], 'var_call_fgKIylYAW6aiJUmFDmM1Pm1N': [{'symbol': 'IT', 'up_days': '125.0', 'down_days': '125.0'}], 'var_call_1CeNolRO5zycfAxvo6hULzHa': [{'symbol': 'JGH', 'up_days': '105.0', 'down_days': '133.0'}]}

exec(code, env_args)
