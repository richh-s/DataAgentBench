code = """import json, pandas as pd

def load(x):
    if isinstance(x,str):
        with open(x,'r') as f:
            return json.load(f)
    return x

res = pd.DataFrame(load(var_call_AqJGOVGzA1d3DfkCEUEcWIC4))
# numeric
for c in ['up_days','down_days']:
    res[c] = pd.to_numeric(res[c], errors='coerce')
res = res.dropna(subset=['up_days','down_days'])
res = res[res['up_days'] > res['down_days']].copy()
res['diff'] = res['up_days'] - res['down_days']
res = res.sort_values(['diff','up_days','Symbol'], ascending=[False,False,True]).head(5)
syms = res['Symbol'].tolist()

# get name_map
obj = load(var_call_KlUqdfFJiyV7brNuMalwfAVJ)
name_map = obj['name_map']

names = [name_map.get(s,'') for s in syms]
print('__RESULT__:')
print(json.dumps({'symbols': syms, 'names': names}))"""

env_args = {'var_call_R5Fm9qBHEnIjJw8IdgrwecTb': 'file_storage/call_R5Fm9qBHEnIjJw8IdgrwecTb.json', 'var_call_9KkYakqJdaS1o0ssxYdG90nb': 'file_storage/call_9KkYakqJdaS1o0ssxYdG90nb.json', 'var_call_pSlDq3Iya59P4L94vtKPK8Li': 'file_storage/call_pSlDq3Iya59P4L94vtKPK8Li.json', 'var_call_33fgjpjrXsOxarmSqxpiXVXf': 'file_storage/call_33fgjpjrXsOxarmSqxpiXVXf.json', 'var_call_0XfaOrnx4aN78Mfl2GOtwk4K': 'file_storage/call_0XfaOrnx4aN78Mfl2GOtwk4K.json', 'var_call_eHAlpS6iMI0n4rEjONy1Fv8Q': 'file_storage/call_eHAlpS6iMI0n4rEjONy1Fv8Q.json', 'var_call_KlUqdfFJiyV7brNuMalwfAVJ': 'file_storage/call_KlUqdfFJiyV7brNuMalwfAVJ.json', 'var_call_AqJGOVGzA1d3DfkCEUEcWIC4': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'Symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'Symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'Symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'Symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'Symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'Symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'Symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'Symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'Symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'Symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'Symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'Symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'Symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'Symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'Symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'Symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}, {'Symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'Symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'Symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'Symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'Symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'Symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'Symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'Symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'Symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'Symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}, {'Symbol': 'CXH', 'up_days': '126.0', 'down_days': '91.0'}]}

exec(code, env_args)
