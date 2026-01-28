code = """import json, math, os, re
# list of storage keys that likely contain query_db results and other data
keys = [
    'var_call_RTQBbDkWPELjIO5FP4rkeZY2','var_call_09LdLcgAY8tG44YYClxlgY5J','var_call_n9MoeGESKA45AnzQfMXwAFVG',
    'var_call_8hg4Iziok321nJL1Xe79kfkY','var_call_1Au5ugNQtZbAn8TcgIQjXgyk','var_call_gyVsCgSQNXMdRy8bgpolQQne',
    'var_call_QAiSVhx1oDd6W2oDh3nN43Mf','var_call_dGCbiCZQrsWlVXurJytMWPds','var_call_GHUFp2al78VsJKY1aqL9oTN7',
    'var_call_NmF31sPPZhD8nZ61K5YifkNF','var_call_l0KrHcWUw6yphIc1Ymdu4XZX','var_call_2ImRcGCNewWpVEepT8OmvPk1',
    'var_call_ljVPfIkmj4BDZng86dacxRPT','var_call_YOGWz0S7IUBIq2v94rTvRuxX','var_call_kWbqEfwNMMdLuHPxff7ZzKRg',
    'var_call_TD1olBBJGadRePNiRUaitqwh','var_call_Txduw21UxAyaI5yCMKA2Eq9Z','var_call_scoujjm2kklYe75BcSA6Xhxo',
    'var_call_HEhAFt7Vw9FXMIyzpb4oCRM5','var_call_FyD1MtMrKw930pYTVnViTYfX','var_call_mLhBcANnksoYFMxFJ203dfAg',
    'var_call_Q6QaUog25H4c6PqV3YL7euSr','var_call_t73D5Wz5Bophh3ex7fbcLVnS','var_call_T3E4tkdgZ5vfuu670iDZYcjt',
    'var_call_sYAFM2YooyrYg7090qjFZGyN','var_call_jz2X2gqxy3izTI4CCR9nONs0','var_call_fjpCfkAoaxbAr0uf0ExDOEyM',
    'var_call_zvO8R9JMEzZBj57AbeWXpJac','var_call_mpttCgt3o8zdDD9j5hSBMVn6','var_call_T3gjZH4glFFz0pxytnb6A8QH',
    'var_call_YCE8fzxxdCiMSigrAEBhKs4E','var_call_ZppGqK2unkeQdr0GKNsRcKCH','var_call_f20XTJ56oxo8AfHrEA2P89Cs',
    'var_call_7Eak6C7v4eH0cfpgPuLtnsHh','var_call_pkwqlc4GX9mz2R2PQZhHEeHc','var_call_kzwZ5umb5c0SgcKFkWtFa8kk'
]
records = []
for k in keys:
    if k in globals():
        v = globals()[k]
        # if v is a list of records
        if isinstance(v, list):
            records.extend(v)
        elif isinstance(v, str):
            # if points to a file
            if os.path.exists(v):
                try:
                    with open(v, 'r') as f:
                        data = json.load(f)
                    if isinstance(data, list):
                        records.extend(data)
                except Exception:
                    pass
            else:
                # try to extract JSON array from string
                try:
                    data = json.loads(v)
                    if isinstance(data, list):
                        records.extend(data)
                except Exception:
                    # try to find a JSON-like substring
                    m = re.search(r'(\[\{.*\}\])', v)
                    if m:
                        try:
                            data = json.loads(m.group(1))
                            if isinstance(data, list):
                                records.extend(data)
                        except Exception:
                            pass
# Now normalize records to symbol, up_days, down_days
normalized = []
for r in records:
    if not isinstance(r, dict):
        continue
    sym = r.get('symbol') or r.get('Symbol') or r.get('symbol')
    up = r.get('up_days')
    down = r.get('down_days')
    if sym is None or up is None or down is None:
        continue
    # convert to float if possible
    try:
        upv = float(up)
    except Exception:
        upv = None
    try:
        downv = float(down)
    except Exception:
        downv = None
    if upv is None or downv is None or math.isnan(upv) or math.isnan(downv):
        continue
    normalized.append({'symbol': sym, 'up_days': upv, 'down_days': downv})
# filter up>down
filtered = [r for r in normalized if r['up_days']>r['down_days']]
# sort by up_days desc
filtered_sorted = sorted(filtered, key=lambda x: x['up_days'], reverse=True)
top5 = filtered_sorted[:5]
# load stockinfo mapping
stockinfo = []
if 'var_call_RTQBbDkWPELjIO5FP4rkeZY2' in globals():
    stockinfo = globals()['var_call_RTQBbDkWPELjIO5FP4rkeZY2']
sym_to_name = {}
for item in stockinfo:
    if isinstance(item, dict):
        sym = item.get('Symbol')
        name = item.get('Company Description')
        if sym and name:
            sym_to_name[sym] = name
# map top5 symbols to names
result_names = []
for it in top5:
    name = sym_to_name.get(it['symbol'], it['symbol'])
    result_names.append(name)
print("__RESULT__:")
print(json.dumps(result_names))"""

env_args = {'var_call_RTQBbDkWPELjIO5FP4rkeZY2': 'file_storage/call_RTQBbDkWPELjIO5FP4rkeZY2.json', 'var_call_09LdLcgAY8tG44YYClxlgY5J': 'file_storage/call_09LdLcgAY8tG44YYClxlgY5J.json', 'var_call_n9MoeGESKA45AnzQfMXwAFVG': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_8hg4Iziok321nJL1Xe79kfkY': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_1Au5ugNQtZbAn8TcgIQjXgyk': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_gyVsCgSQNXMdRy8bgpolQQne': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_QAiSVhx1oDd6W2oDh3nN43Mf': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_dGCbiCZQrsWlVXurJytMWPds': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_GHUFp2al78VsJKY1aqL9oTN7': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_NmF31sPPZhD8nZ61K5YifkNF': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_l0KrHcWUw6yphIc1Ymdu4XZX': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_2ImRcGCNewWpVEepT8OmvPk1': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_ljVPfIkmj4BDZng86dacxRPT': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_YOGWz0S7IUBIq2v94rTvRuxX': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}], 'var_call_kWbqEfwNMMdLuHPxff7ZzKRg': [{'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_TD1olBBJGadRePNiRUaitqwh': [{'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}], 'var_call_Txduw21UxAyaI5yCMKA2Eq9Z': [{'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_scoujjm2kklYe75BcSA6Xhxo': [{'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}], 'var_call_HEhAFt7Vw9FXMIyzpb4oCRM5': [{'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}], 'var_call_FyD1MtMrKw930pYTVnViTYfX': [{'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}], 'var_call_mLhBcANnksoYFMxFJ203dfAg': [{'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}], 'var_call_Q6QaUog25H4c6PqV3YL7euSr': [{'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}], 'var_call_t73D5Wz5Bophh3ex7fbcLVnS': [{'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}], 'var_call_T3E4tkdgZ5vfuu670iDZYcjt': [{'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}], 'var_call_sYAFM2YooyrYg7090qjFZGyN': [{'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}], 'var_call_jz2X2gqxy3izTI4CCR9nONs0': [{'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_fjpCfkAoaxbAr0uf0ExDOEyM': [{'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_zvO8R9JMEzZBj57AbeWXpJac': [{'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}], 'var_call_mpttCgt3o8zdDD9j5hSBMVn6': [{'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}], 'var_call_T3gjZH4glFFz0pxytnb6A8QH': [{'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}], 'var_call_YCE8fzxxdCiMSigrAEBhKs4E': [{'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}], 'var_call_ZppGqK2unkeQdr0GKNsRcKCH': [{'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_f20XTJ56oxo8AfHrEA2P89Cs': [{'symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}], 'var_call_7Eak6C7v4eH0cfpgPuLtnsHh': [{'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}], 'var_call_pkwqlc4GX9mz2R2PQZhHEeHc': [{'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}], 'var_call_kzwZ5umb5c0SgcKFkWtFa8kk': [{'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}]}

exec(code, env_args)
