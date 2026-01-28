code = """import json
with open(var_call_YAmGc7SHT2zMzksFygYdnQRl, 'r') as f:
    stockinfo = json.load(f)
# Map symbols to company description
mapping = {rec['Symbol']: rec.get('Company Description') for rec in stockinfo}
# Selected top 5 symbols based on earlier partial results
selected_symbols = ['AIN','AMP','AMN','AVA','BKH']
# Extract company names (take text before first ' is ' or first ' specializes' or first comma)
names = []
for s in selected_symbols:
    desc = mapping.get(s, '')
    if not desc:
        names.append(None)
        continue
    # Try to extract company name
    # Many descriptions start with company name followed by description. We'll split by ' is ' or ' specializes' or ','
    parts = None
    for sep in [' is ', ' specializes', ',']:
        if sep in desc:
            parts = desc.split(sep)[0]
            break
    if parts is None:
        parts = desc
    # Clean
    name = parts.strip()
    names.append(name)

result = dict(zip(selected_symbols, names))
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_YAmGc7SHT2zMzksFygYdnQRl': 'file_storage/call_YAmGc7SHT2zMzksFygYdnQRl.json', 'var_call_cDQEaKskDLs8TaPk1lEF91pz': 'file_storage/call_cDQEaKskDLs8TaPk1lEF91pz.json', 'var_call_rv7AwKhcaSbLUleltodP8ssN': {'stockinfo_count': 234, 'trade_tables_count': 2753}, 'var_call_ENOYm3MeNoxvEQnLKbkhIigF': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_pKJcLoP3HeEH6paFnoKAUQyH': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_nomYtGovSYnzX3GqnxXjOm8O': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_Uiyq40yDAw33LQHOLnhX85A2': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_weYl6J2oD3dTYG5N1LqZzc0k': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_uXdydAKuvYrkTDFttPsu4Toy': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_LAHhf8SQS9RdcfB56vieHuVP': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_8kIQP0QjQ7OG4gKgOyG28EZi': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_LIqMOCl09cOGfFd1CsuXCBeo': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_uasaihPuuPna88DnKwjmVbVi': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_f8bstCeVe8KyRlMnGX7jcosf': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_4DRW7meDKcOmljIjhUjMdVbI': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}], 'var_call_bbrLMT2vi5jbM2ag6J8POsLd': [{'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_49l99K7KWSITrQBRVqzHZjpG': [{'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}], 'var_call_2G9801s8mFOexc121aMFacKL': [{'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_Drr3IBq1asGilEfsaEc91WXX': [{'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}], 'var_call_DytOvjyMYpujUuW3OJW0GNh1': [{'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}], 'var_call_yE2qiboLI6J8fbJlGKfj2BQ4': [{'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}], 'var_call_7TMlWxX2oKa3vuo8K0v7FjpM': [{'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}], 'var_call_MZWzoBn1Htnxf0VHn8c0PFbD': [{'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}], 'var_call_tHN1ovceZ0S7t1SCunjd1e6i': [{'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}], 'var_call_tH8OH5mB5L6BcaK6hx6FOxK4': [{'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}], 'var_call_DS3SPUt8WpRqem1bYVWlqzji': [{'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}], 'var_call_rOFqmHO7JrVv0xCTI79f5kj2': [{'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_9UmKv3LkqVLTd7HgSVEdGjOI': [{'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_j1aprDCU7uCyPHs8pNpa6at6': [{'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}], 'var_call_5XuVQn95LSQjExlUZQEJTtXK': [{'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}], 'var_call_EKQoOTVPGBL0Nwdm6eYSkcv1': [{'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}], 'var_call_IJHoBi8UTutYbis5nOH3x1GT': [{'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}], 'var_call_AaqVIIiMCZI9jgFayuNsJVMo': [{'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_ljO0uAdb08E45KNBaRxrHoNQ': [{'symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}], 'var_call_9oMVLljRKtVvKwJjrHxNw46P': [{'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}], 'var_call_GM9VTL1jTJ6w3LNgwB5cQsap': [{'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}], 'var_call_5lyETjFrxFTMlLLLae5uk2Pk': [{'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}], 'var_call_bZ8oGYdnWpVvWiXLVu093fh5': [{'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_wb7IjqW4VhWoYM7LIXplTO4K': [{'symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_RjDWVkwXeWjFtmDhlOsdbWkG': [{'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}], 'var_call_MCjQunisc3ln9wu5ps9QvGG0': [{'symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}]}

exec(code, env_args)
