code = """import json
import pandas as pd

# Load the full list of NYSE non-ETF stocks and their names
file_path_names = locals()['var_function-call-10853579971891121046']
with open(file_path_names, 'r') as f:
    nyse_stocks_info = json.load(f)

nyse_symbols_and_names = {symbol: info for symbol, info in nyse_stocks_info.items()}

# Process AIN data
ain_data_path = locals()['var_function-call-16625541470645651839']
with open(ain_data_path, 'r') as f:
    ain_data = json.load(f)

up_days_ain = 0
down_days_ain = 0
for record in ain_data:
    if record['Close'] > record['Open']:
        up_days_ain += 1
    elif record['Close'] < record['Open']:
        down_days_ain += 1

result_ain = {
    "Symbol": "AIN",
    "Company Name": nyse_symbols_and_names["AIN"],
    "Up Days": up_days_ain,
    "Down Days": down_days_ain,
    "Difference": up_days_ain - down_days_ain
}

# Process AIV data
aiv_data_path = locals()['var_function-call-9344154709759001343']
with open(aiv_data_path, 'r') as f:
    aiv_data = json.load(f)

up_days_aiv = 0
down_days_aiv = 0
for record in aiv_data:
    if record['Close'] > record['Open']:
        up_days_aiv += 1
    elif record['Close'] < record['Open']:
        down_days_aiv += 1

result_aiv = {
    "Symbol": "AIV",
    "Company Name": nyse_symbols_and_names["AIV"],
    "Up Days": up_days_aiv,
    "Down Days": down_days_aiv,
    "Difference": up_days_aiv - down_days_aiv
}

# AEFC data was empty, so up_days and down_days will be 0. It won't be in top 5.

# Aggregate results and print
results_list = [result_ain, result_aiv]
results_list = sorted(results_list, key=lambda x: x['Difference'], reverse=True)

print("__RESULT__:")
print(json.dumps(results_list))"""

env_args = {'var_function-call-17305754365419409781': 'file_storage/function-call-17305754365419409781.json', 'var_function-call-96436201150395967': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD'], 'var_function-call-10853579971891121046': 'file_storage/function-call-10853579971891121046.json', 'var_function-call-13167300087875100134': [], 'var_function-call-10241209635430852053': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_function-call-16625541470645651839': 'file_storage/function-call-16625541470645651839.json', 'var_function-call-9344154709759001343': 'file_storage/function-call-9344154709759001343.json'}

exec(code, env_args)
