code = """import json
import pandas as pd

company_descriptions = json.loads(open(locals()['var_function-call-5283719638804300270'], 'r').read())
all_stock_metrics = []

# AIN metrics
ain_data = json.loads(open(locals()['var_function-call-93036555456939424'], 'r').read())
if ain_data:
    df_ain = pd.DataFrame(ain_data)
    df_ain['Open'] = pd.to_numeric(df_ain['Open'])
    df_ain['Close'] = pd.to_numeric(df_ain['Close'])
    up_days_ain = int((df_ain['Close'] > df_ain['Open']).sum())
    down_days_ain = int((df_ain['Close'] < df_ain['Open']).sum())
    all_stock_metrics.append({
        'Symbol': 'AIN',
        'CompanyName': company_descriptions.get('AIN', ''),
        'UpDays': up_days_ain,
        'DownDays': down_days_ain,
        'Difference': up_days_ain - down_days_ain
    })

# AIV metrics
aiv_data = json.loads(open(locals()['var_function-call-11455793764559058493'], 'r').read())
if aiv_data:
    df_aiv = pd.DataFrame(aiv_data)
    df_aiv['Open'] = pd.to_numeric(df_aiv['Open'])
    df_aiv['Close'] = pd.to_numeric(df_aiv['Close'])
    up_days_aiv = int((df_aiv['Close'] > df_aiv['Open']).sum())
    down_days_aiv = int((df_aiv['Close'] < df_aiv['Open']).sum())
    all_stock_metrics.append({
        'Symbol': 'AIV',
        'CompanyName': company_descriptions.get('AIV', ''),
        'UpDays': up_days_aiv,
        'DownDays': down_days_aiv,
        'Difference': up_days_aiv - down_days_aiv
    })

# AJRD metrics
ajrd_data = json.loads(open(locals()['var_function-call-13897785943647784714'], 'r').read())
if ajrd_data:
    df_ajrd = pd.DataFrame(ajrd_data)
    df_ajrd['Open'] = pd.to_numeric(df_ajrd['Open'])
    df_ajrd['Close'] = pd.to_numeric(df_ajrd['Close'])
    up_days_ajrd = int((df_ajrd['Close'] > df_ajrd['Open']).sum())
    down_days_ajrd = int((df_ajrd['Close'] < df_ajrd['Open']).sum())
    all_stock_metrics.append({
        'Symbol': 'AJRD',
        'CompanyName': company_descriptions.get('AJRD', ''),
        'UpDays': up_days_ajrd,
        'DownDays': down_days_ajrd,
        'Difference': up_days_ajrd - down_days_ajrd
    })

# AL metrics
al_data = json.loads(open(locals()['var_function-call-11621031147563018972'], 'r').read())
if al_data:
    df_al = pd.DataFrame(al_data)
    df_al['Open'] = pd.to_numeric(df_al['Open'])
    df_al['Close'] = pd.to_numeric(df_al['Close'])
    up_days_al = int((df_al['Close'] > df_al['Open']).sum())
    down_days_al = int((df_al['Close'] < df_al['Open']).sum())
    all_stock_metrics.append({
        'Symbol': 'AL',
        'CompanyName': company_descriptions.get('AL', ''),
        'UpDays': up_days_al,
        'DownDays': down_days_al,
        'Difference': up_days_al - down_days_al
    })

# AMN metrics
amn_data = json.loads(open(locals()['var_function-call-3077134290963933169'], 'r').read())
if amn_data:
    df_amn = pd.DataFrame(amn_data)
    df_amn['Open'] = pd.to_numeric(df_amn['Open'])
    df_amn['Close'] = pd.to_numeric(df_amn['Close'])
    up_days_amn = int((df_amn['Close'] > df_amn['Open']).sum())
    down_days_amn = int((df_amn['Close'] < df_amn['Open']).sum())
    all_stock_metrics.append({
        'Symbol': 'AMN',
        'CompanyName': company_descriptions.get('AMN', ''),
        'UpDays': up_days_amn,
        'DownDays': down_days_amn,
        'Difference': up_days_amn - down_days_amn
    })

# AMP metrics
amp_data = json.loads(open(locals()['var_function-call-4415555747010191233'], 'r').read())
if amp_data:
    df_amp = pd.DataFrame(amp_data)
    df_amp['Open'] = pd.to_numeric(df_amp['Open'])
    df_amp['Close'] = pd.to_numeric(df_amp['Close'])
    up_days_amp = int((df_amp['Close'] > df_amp['Open']).sum())
    down_days_amp = int((df_amp['Close'] < df_amp['Open']).sum())
    all_stock_metrics.append({
        'Symbol': 'AMP',
        'CompanyName': company_descriptions.get('AMP', ''),
        'UpDays': up_days_amp,
        'DownDays': down_days_amp,
        'Difference': up_days_amp - down_days_amp
    })

print("__RESULT__:")
print(json.dumps(all_stock_metrics))"""

env_args = {'var_function-call-11172199451937018748': 'file_storage/function-call-11172199451937018748.json', 'var_function-call-17905251415240036896': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_function-call-882953285913068802': 'file_storage/function-call-882953285913068802.json', 'var_function-call-4411113967099580380': [], 'var_function-call-4127579461008071104': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_function-call-17166464458016291226': [], 'var_function-call-11732842960606041636': [], 'var_function-call-5794986562977301765': [], 'var_function-call-15885306565752454339': [], 'var_function-call-93036555456939424': 'file_storage/function-call-93036555456939424.json', 'var_function-call-5283719638804300270': 'file_storage/function-call-5283719638804300270.json', 'var_function-call-8376040961081475196': [], 'var_function-call-14052189794834845418': {'Symbol': 'AIN', 'UpDays': 143, 'DownDays': 101, 'Difference': 42}, 'var_function-call-8731803415882000974': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], 'var_function-call-11455793764559058493': 'file_storage/function-call-11455793764559058493.json', 'var_function-call-14765135681916210135': {'Symbol': 'AIV', 'UpDays': 118, 'DownDays': 128, 'Difference': -10}, 'var_function-call-5735656636022699616': [], 'var_function-call-13897785943647784714': 'file_storage/function-call-13897785943647784714.json', 'var_function-call-7155618970726079343': {'Symbol': 'AJRD', 'UpDays': 123, 'DownDays': 123, 'Difference': 0}, 'var_function-call-11621031147563018972': 'file_storage/function-call-11621031147563018972.json', 'var_function-call-1354431990670212571': {'Symbol': 'AL', 'UpDays': 131, 'DownDays': 117, 'Difference': 14}, 'var_function-call-3077134290963933169': 'file_storage/function-call-3077134290963933169.json', 'var_function-call-4415555747010191233': 'file_storage/function-call-4415555747010191233.json'}

exec(code, env_args)
