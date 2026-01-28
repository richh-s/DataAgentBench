code = """import json, math, os
# List of known result variable names from previous query_db calls
var_names = [
'var_call_ndlpHdiA1gJWv7ljpoASmWHi','var_call_FbYpINOJBzzThbPhZZsE2KdW','var_call_sp7gxNkZdMYFq5MLBbCRzBfA',
'var_call_1rxp3i06lwxU5B4r7iWc82V6','var_call_JuHJ4Bbq3xX9rG2NHSnpw6Ey','var_call_Hhc4rgo5Zy9bUTCx3qonV3Sm',
'var_call_EhSsDdX70ukJWrVJ5jroteoj','var_call_seEVZyjwDwBrqw69yAYTS3FU','var_call_EXetEEm8TgSiYRo1DniOSntx',
'var_call_7AHuB8ApHFLmXnuvKDN0fV8j','var_call_9TDYTVWhsuTvuib2Qsll2E34','var_call_FPFC1cgv4jpd3uZ6z2dgEJ4l',
'var_call_2wiumcsZDU6t8YdQ79Ur3W3j','var_call_CoK99UM5v61z24E3VXNvwZMq','var_call_HTcXVhqgdv1YI9TSteSRRrQt',
'var_call_kTKDPMzPLOzDP00xIodimspy','var_call_pqi2pKWK7ub1TC4hCteKkrav','var_call_srx61Aoo5FDbbwelTrQ1XLE1',
'var_call_wSwDKqzLHBc493fOmVctz2rq','var_call_UvZjHi4RWni0LnkOSZdnoIrN','var_call_ZNn4MQpdFjZs9l21wcYQr8r8',
'var_call_y04ERKAdqhj7SUC8czYpEhQ7','var_call_DUzX6k80NQvzi2lg51Mx0kCQ','var_call_xuwynXibFcKw2CKgI4lXUHLK',
'var_call_OxcsTk42Ayav4Bp6y2yzon7v','var_call_QfP7UHhWdRL0ezqdOZ5NMKPn','var_call_jaRdmnHwJsjRXZlvy87j512w',
'var_call_TrcSL9l7V8m8yeo7TQsEXrLg','var_call_SZP0ANkr8nI231Y2yFMluuLB','var_call_DDKPcKSnEPgClOD9fZGPe2HU',
'var_call_LhCRYK5erJTY2HncJZpPjq1b','var_call_Rd66fY0206xmDRAf11gr8JwL','var_call_3ie1aTGL4yODP1nYKJAkE91J',
'var_call_dYzgR9ttydbtATHyEenlbXow','var_call_dHXqzdo2ZcCuAb78j6iBhyCu','var_call_kR8dRJSH4ACE6365vUQH9guq'
]
# Also include mapping variable from earlier execute_python which contains symbols and sym2desc
map_var = 'var_call_wcdrTGvraMvb3WJXAUedBSw6'
# helper to load variable content
results = []
for vn in var_names:
    if vn in globals():
        v = globals()[vn]
        # if it's a string and looks like JSON filepath
        if isinstance(v, str) and os.path.exists(v):
            with open(v,'r') as f:
                content = json.load(f)
        else:
            content = v
        # content expected to be a list of dicts
        if isinstance(content, list):
            results.extend(content)
# load mapping
sym2desc = {}
if map_var in globals():
    mv = globals()[map_var]
    if isinstance(mv, str) and os.path.exists(mv):
        with open(mv,'r') as f:
            m = json.load(f)
    else:
        m = mv
    # m is dict with 'symbols' and 'sym2desc'
    if isinstance(m, dict) and 'sym2desc' in m:
        sym2desc = m['sym2desc']
# process results
rows = []
for r in results:
    try:
        sym = r.get('symbol')
        up = r.get('up_count')
        down = r.get('down_count')
        # convert to float if possible
        upf = None
        downf = None
        if up is None or down is None:
            continue
        # handle strings like 'nan'
        try:
            upf = float(up)
            downf = float(down)
        except:
            continue
        if math.isnan(upf) or math.isnan(downf):
            continue
        rows.append({'symbol': sym, 'up': int(upf), 'down': int(downf)})
    except Exception:
        continue
# filter up>down
wins = [r for r in rows if r['up']>r['down']]
# sort by up desc
wins_sorted = sorted(wins, key=lambda x: x['up'], reverse=True)
# take top 5
top5 = wins_sorted[:5]
# map to company names using sym2desc, fallback to symbol
result_names = []
for r in top5:
    name = sym2desc.get(r['symbol'], r['symbol'])
    # If company description field contains both name and description, extract first part before ' is ' or comma
    if isinstance(name, str):
        # try split at ' is ' or ' Inc' etc. But user wants names (not symbol). We'll output company description as-is.
        out_name = name
    else:
        out_name = r['symbol']
    result_names.append(out_name)
print('__RESULT__:')
print(json.dumps(result_names))"""

env_args = {'var_call_dXlfw7PBbNWvRB8DrF5zCYoo': 'file_storage/call_dXlfw7PBbNWvRB8DrF5zCYoo.json', 'var_call_7bDFcW723n8AK6WYWmUMLAlr': 'file_storage/call_7bDFcW723n8AK6WYWmUMLAlr.json', 'var_call_wcdrTGvraMvb3WJXAUedBSw6': 'file_storage/call_wcdrTGvraMvb3WJXAUedBSw6.json', 'var_call_IiSYKzGVqrCTvGYbEoqrJWU8': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_ndlpHdiA1gJWv7ljpoASmWHi': [{'symbol': 'AEFC', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_FbYpINOJBzzThbPhZZsE2KdW': [{'symbol': 'AIN', 'up_count': '143.0', 'down_count': '101.0'}], 'var_call_sp7gxNkZdMYFq5MLBbCRzBfA': [{'symbol': 'AIV', 'up_count': '118.0', 'down_count': '128.0'}], 'var_call_1rxp3i06lwxU5B4r7iWc82V6': [{'symbol': 'AIZP', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_JuHJ4Bbq3xX9rG2NHSnpw6Ey': [{'symbol': 'AJRD', 'up_count': '123.0', 'down_count': '123.0'}], 'var_call_Hhc4rgo5Zy9bUTCx3qonV3Sm': [{'symbol': 'AL', 'up_count': '131.0', 'down_count': '117.0'}], 'var_call_EhSsDdX70ukJWrVJ5jroteoj': [{'symbol': 'AMN', 'up_count': '134.0', 'down_count': '111.0'}], 'var_call_seEVZyjwDwBrqw69yAYTS3FU': [{'symbol': 'AMP', 'up_count': '141.0', 'down_count': '110.0'}], 'var_call_EXetEEm8TgSiYRo1DniOSntx': [{'symbol': 'AMT', 'up_count': '128.0', 'down_count': '123.0'}], 'var_call_7AHuB8ApHFLmXnuvKDN0fV8j': [{'symbol': 'ARD', 'up_count': '80.0', 'down_count': '119.0'}], 'var_call_9TDYTVWhsuTvuib2Qsll2E34': [{'symbol': 'ARGD', 'up_count': '133.0', 'down_count': '82.0'}], 'var_call_FPFC1cgv4jpd3uZ6z2dgEJ4l': [{'symbol': 'ARLO', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_2wiumcsZDU6t8YdQ79Ur3W3j': [{'symbol': 'ASG', 'up_count': '110.0', 'down_count': '110.0'}], 'var_call_CoK99UM5v61z24E3VXNvwZMq': [{'symbol': 'AVA', 'up_count': '134.0', 'down_count': '112.0'}], 'var_call_HTcXVhqgdv1YI9TSteSRRrQt': [{'symbol': 'BANC', 'up_count': '108.0', 'down_count': '119.0'}], 'var_call_kTKDPMzPLOzDP00xIodimspy': [{'symbol': 'BBU', 'up_count': '129.0', 'down_count': '120.0'}], 'var_call_pqi2pKWK7ub1TC4hCteKkrav': [{'symbol': 'BBVA', 'up_count': '126.0', 'down_count': '104.0'}], 'var_call_srx61Aoo5FDbbwelTrQ1XLE1': [{'symbol': 'BDXA', 'up_count': '83.0', 'down_count': '77.0'}], 'var_call_wSwDKqzLHBc493fOmVctz2rq': [{'symbol': 'BKH', 'up_count': '134.0', 'down_count': '115.0'}], 'var_call_UvZjHi4RWni0LnkOSZdnoIrN': [{'symbol': 'BKT', 'up_count': '105.0', 'down_count': '97.0'}], 'var_call_ZNn4MQpdFjZs9l21wcYQr8r8': [{'symbol': 'BLD', 'up_count': '131.0', 'down_count': '120.0'}], 'var_call_y04ERKAdqhj7SUC8czYpEhQ7': [{'symbol': 'BNS', 'up_count': '132.0', 'down_count': '117.0'}], 'var_call_DUzX6k80NQvzi2lg51Mx0kCQ': [{'symbol': 'BV', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_xuwynXibFcKw2CKgI4lXUHLK': [{'symbol': 'BZH', 'up_count': '127.0', 'down_count': '123.0'}], 'var_call_OxcsTk42Ayav4Bp6y2yzon7v': [{'symbol': 'CADE', 'up_count': '88.0', 'down_count': '83.0'}], 'var_call_QfP7UHhWdRL0ezqdOZ5NMKPn': [{'symbol': 'CAE', 'up_count': '122.0', 'down_count': '117.0'}], 'var_call_jaRdmnHwJsjRXZlvy87j512w': [{'symbol': 'CAF', 'up_count': '131.0', 'down_count': '113.0'}], 'var_call_TrcSL9l7V8m8yeo7TQsEXrLg': [{'symbol': 'CBT', 'up_count': '128.0', 'down_count': '122.0'}], 'var_call_SZP0ANkr8nI231Y2yFMluuLB': [{'symbol': 'CCC', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_DDKPcKSnEPgClOD9fZGPe2HU': [{'symbol': 'CCZ', 'up_count': '17.0', 'down_count': '10.0'}], 'var_call_LhCRYK5erJTY2HncJZpPjq1b': [{'symbol': 'CHAP', 'up_count': '34.0', 'down_count': '23.0'}], 'var_call_Rd66fY0206xmDRAf11gr8JwL': [{'symbol': 'CIA', 'up_count': '130.0', 'down_count': '112.0'}], 'var_call_3ie1aTGL4yODP1nYKJAkE91J': [{'symbol': 'CMA', 'up_count': '124.0', 'down_count': '124.0'}], 'var_call_dYzgR9ttydbtATHyEenlbXow': [{'symbol': 'CMI', 'up_count': '127.0', 'down_count': '123.0'}], 'var_call_dHXqzdo2ZcCuAb78j6iBhyCu': [{'symbol': 'CMSA', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_kR8dRJSH4ACE6365vUQH9guq': [{'symbol': 'CNK', 'up_count': '128.0', 'down_count': '122.0'}]}

exec(code, env_args)
