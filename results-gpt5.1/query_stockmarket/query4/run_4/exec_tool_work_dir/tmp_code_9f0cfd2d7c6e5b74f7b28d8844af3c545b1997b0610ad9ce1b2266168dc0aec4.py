code = """import json
from pathlib import Path

files = {
 'IBM': var_call_StsXVck9NXWqFPWQkV2Vefb5,
 'MS': var_call_yzMgJSSKRPAqR6HtXMlTpt6w,
 'ORCL': var_call_A15jcpySmQDOBYGSO3T499mp,
 'PFE': var_call_T9oKm52b7oYnBXATWsThQWos,
 'TRV': var_call_FPxWlEb0OG3gGyFxij4mFtU4,
}

summary = {}
for sym, path in files.items():
    data = json.loads(Path(path).read_text())
    up = sum(1 for d in data if float(d['Close']) > float(d['Open']))
    down = sum(1 for d in data if float(d['Close']) < float(d['Open']))
    summary[sym] = {'up': up, 'down': down}

print("__RESULT__:")
print(json.dumps(summary))"""

env_args = {'var_call_z3w05wE5Ypxfbtq7ucO6JvyI': 'file_storage/call_z3w05wE5Ypxfbtq7ucO6JvyI.json', 'var_call_MWllCGhgDvLPK7utbFrlPQzp': 'file_storage/call_MWllCGhgDvLPK7utbFrlPQzp.json', 'var_call_L21RBjxbdpdjmXKi1A5TMTG3': 'file_storage/call_L21RBjxbdpdjmXKi1A5TMTG3.json', 'var_call_Zm9i5CC05CBbvxIflAwSLvuR': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_StsXVck9NXWqFPWQkV2Vefb5': 'file_storage/call_StsXVck9NXWqFPWQkV2Vefb5.json', 'var_call_yzMgJSSKRPAqR6HtXMlTpt6w': 'file_storage/call_yzMgJSSKRPAqR6HtXMlTpt6w.json', 'var_call_A15jcpySmQDOBYGSO3T499mp': 'file_storage/call_A15jcpySmQDOBYGSO3T499mp.json', 'var_call_T9oKm52b7oYnBXATWsThQWos': 'file_storage/call_T9oKm52b7oYnBXATWsThQWos.json', 'var_call_FPxWlEb0OG3gGyFxij4mFtU4': 'file_storage/call_FPxWlEb0OG3gGyFxij4mFtU4.json'}

exec(code, env_args)
