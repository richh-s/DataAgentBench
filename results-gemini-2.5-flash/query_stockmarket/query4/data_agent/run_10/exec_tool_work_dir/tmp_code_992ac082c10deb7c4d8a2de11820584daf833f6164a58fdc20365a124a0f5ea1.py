code = """import json
import pandas as pd

company_descriptions = json.loads(open(locals()['var_function-call-5283719638804300270'], 'r').read())
all_stock_metrics = locals()['var_function-call-10293984484642375117']

# AMT metrics
amt_data = json.loads(open(locals()['var_function-call-8914714034803056839'], 'r').read())
if amt_data:
    df_amt = pd.DataFrame(amt_data)
    df_amt['Open'] = pd.to_numeric(df_amt['Open'])
    df_amt['Close'] = pd.to_numeric(df_amt['Close'])
    up_days_amt = int((df_amt['Close'] > df_amt['Open']).sum())
    down_days_amt = int((df_amt['Close'] < df_amt['Open']).sum())
    all_stock_metrics.append({
        'Symbol': 'AMT',
        'CompanyName': company_descriptions.get('AMT', ''),
        'UpDays': up_days_amt,
        'DownDays': down_days_amt,
        'Difference': up_days_amt - down_days_amt
    })

# ARD metrics
ard_data = json.loads(open(locals()['var_function-call-287717800431114967'], 'r').read())
if ard_data:
    df_ard = pd.DataFrame(ard_data)
    df_ard['Open'] = pd.to_numeric(df_ard['Open'])
    df_ard['Close'] = pd.to_numeric(df_ard['Close'])
    up_days_ard = int((df_ard['Close'] > df_ard['Open']).sum())
    down_days_ard = int((df_ard['Close'] < df_ard['Open']).sum())
    all_stock_metrics.append({
        'Symbol': 'ARD',
        'CompanyName': company_descriptions.get('ARD', ''),
        'UpDays': up_days_ard,
        'DownDays': down_days_ard,
        'Difference': up_days_ard - down_days_ard
    })

# Sort the results by 'Difference' in descending order
sorted_stocks = sorted(all_stock_metrics, key=lambda x: x['Difference'], reverse=True)

# Get the top 5 stocks
top_5_stocks = sorted_stocks[:5]

# Extract only the company names for the final answer
final_answer = [stock['CompanyName'] for stock in top_5_stocks]

print("__RESULT__:")
print(json.dumps(final_answer))"""

env_args = {'var_function-call-11172199451937018748': 'file_storage/function-call-11172199451937018748.json', 'var_function-call-17905251415240036896': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_function-call-882953285913068802': 'file_storage/function-call-882953285913068802.json', 'var_function-call-4411113967099580380': [], 'var_function-call-4127579461008071104': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_function-call-17166464458016291226': [], 'var_function-call-11732842960606041636': [], 'var_function-call-5794986562977301765': [], 'var_function-call-15885306565752454339': [], 'var_function-call-93036555456939424': 'file_storage/function-call-93036555456939424.json', 'var_function-call-5283719638804300270': 'file_storage/function-call-5283719638804300270.json', 'var_function-call-8376040961081475196': [], 'var_function-call-14052189794834845418': {'Symbol': 'AIN', 'UpDays': 143, 'DownDays': 101, 'Difference': 42}, 'var_function-call-8731803415882000974': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], 'var_function-call-11455793764559058493': 'file_storage/function-call-11455793764559058493.json', 'var_function-call-14765135681916210135': {'Symbol': 'AIV', 'UpDays': 118, 'DownDays': 128, 'Difference': -10}, 'var_function-call-5735656636022699616': [], 'var_function-call-13897785943647784714': 'file_storage/function-call-13897785943647784714.json', 'var_function-call-7155618970726079343': {'Symbol': 'AJRD', 'UpDays': 123, 'DownDays': 123, 'Difference': 0}, 'var_function-call-11621031147563018972': 'file_storage/function-call-11621031147563018972.json', 'var_function-call-1354431990670212571': {'Symbol': 'AL', 'UpDays': 131, 'DownDays': 117, 'Difference': 14}, 'var_function-call-3077134290963933169': 'file_storage/function-call-3077134290963933169.json', 'var_function-call-4415555747010191233': 'file_storage/function-call-4415555747010191233.json', 'var_function-call-10293984484642375117': [{'Symbol': 'AIN', 'CompanyName': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'UpDays': 143, 'DownDays': 101, 'Difference': 42}, {'Symbol': 'AIV', 'CompanyName': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'UpDays': 118, 'DownDays': 128, 'Difference': -10}, {'Symbol': 'AJRD', 'CompanyName': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.', 'UpDays': 123, 'DownDays': 123, 'Difference': 0}, {'Symbol': 'AL', 'CompanyName': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.', 'UpDays': 131, 'DownDays': 117, 'Difference': 14}, {'Symbol': 'AMN', 'CompanyName': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.', 'UpDays': 134, 'DownDays': 111, 'Difference': 23}, {'Symbol': 'AMP', 'CompanyName': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.', 'UpDays': 141, 'DownDays': 110, 'Difference': 31}], 'var_function-call-8914714034803056839': 'file_storage/function-call-8914714034803056839.json', 'var_function-call-287717800431114967': 'file_storage/function-call-287717800431114967.json'}

exec(code, env_args)
