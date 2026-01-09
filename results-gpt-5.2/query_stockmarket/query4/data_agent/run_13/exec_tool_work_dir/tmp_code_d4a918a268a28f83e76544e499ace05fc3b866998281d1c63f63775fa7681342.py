code = """import json
import pandas as pd

counts = pd.DataFrame(var_call_QXbYxmbhi5oKDho7ltRL1y0F)
info = pd.DataFrame(var_call_FNK6e5QbaxN7EKrM8AkPiKre)

# Extract name as text before ' specializes' or ' is ' or first comma
names=[]
for desc in info['company_name']:
    d=str(desc)
    for sep in [' specializes', ' is ', ' operates', ', commonly']:
        if sep in d:
            d=d.split(sep)[0]
            break
    if ',' in d:
        d=d.split(',')[0]
    names.append(d.strip())
info['name']=names

merged = counts.merge(info[['Symbol','name']], on='Symbol', how='left')
merged['up_days']=merged['up_days'].astype(float).astype(int)
merged['down_days']=merged['down_days'].astype(float).astype(int)
merged = merged.sort_values(['up_days'], ascending=False)

answer_lines = [f"{row['name']}" for _,row in merged.iterrows()]
print('__RESULT__:')
print(json.dumps(answer_lines))"""

env_args = {'var_call_XSjSsb8GS4EPwnO4lroyRna5': ['stockinfo'], 'var_call_kNZOFIAS7l658Bla0yhEzoVR': 'file_storage/call_kNZOFIAS7l658Bla0yhEzoVR.json', 'var_call_JQeLNUauzOkn7Bn3RHEafsPk': 'file_storage/call_JQeLNUauzOkn7Bn3RHEafsPk.json', 'var_call_Ol5eKKR6EQ8lu5KDu1vjEJeq': {'symbols_count': 234, 'chunks': 3, 'first_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_QXbYxmbhi5oKDho7ltRL1y0F': [{'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_FNK6e5QbaxN7EKrM8AkPiKre': [{'Symbol': 'AIN', 'company_name': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AL', 'company_name': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.'}, {'Symbol': 'AMN', 'company_name': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.'}, {'Symbol': 'AMP', 'company_name': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.'}, {'Symbol': 'AMT', 'company_name': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.'}]}

exec(code, env_args)
