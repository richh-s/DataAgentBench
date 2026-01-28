code = """import json, pandas as pd

# load trade counts result
r = var_call_lb4xNIc7NCOzS7FDFSirtQPV
if isinstance(r,str):
    with open(r,'r') as f:
        r=json.load(f)
df=pd.DataFrame(r)

# load info
info = var_call_8SQH7HGO9zXTat5DBZ5KCOLp
if isinstance(info,str):
    with open(info,'r') as f:
        info=json.load(f)
info_df=pd.DataFrame(info)

# coerce numeric
for c in ['up_days','down_days']:
    df[c]=pd.to_numeric(df[c], errors='coerce')

# drop rows with NaN counts (no 2017 data)
df=df.dropna(subset=['up_days','down_days'])

# filter more up than down
df=df[df['up_days']>df['down_days']].copy()

# rank by (up_days - down_days) desc, then up_days desc

df['diff']=df['up_days']-df['down_days']
df=df.sort_values(['diff','up_days','Symbol'], ascending=[False,False,True]).head(5)

out=pd.merge(df, info_df, on='Symbol', how='left')
answer_list=out['company_name'].tolist()

print('__RESULT__:')
print(json.dumps({'top5_company_names': answer_list, 'details': out[['Symbol','company_name','up_days','down_days','diff']].to_dict(orient='records')}))"""

env_args = {'var_call_6eMnvquPseEJWBPYIuXkBczW': ['stockinfo'], 'var_call_8SQH7HGO9zXTat5DBZ5KCOLp': 'file_storage/call_8SQH7HGO9zXTat5DBZ5KCOLp.json', 'var_call_KtI05COHj2GeVxPnUriejCD4': 'file_storage/call_KtI05COHj2GeVxPnUriejCD4.json', 'var_call_b4DWohrCNtLwUeeUmUgHamqx': 'file_storage/call_b4DWohrCNtLwUeeUmUgHamqx.json', 'var_call_dHD5rxh9vR2TTbVC3xXFAsqa': {'n_symbols': 234, 'EIX_included': False, 'query_len': 49903, 'first20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'contains_EIX_substring': False}, 'var_call_L4q9xkZVw50qF6avt7Tk89YC': {'n_info': 234, 'n_trade': 2753, 'n_missing': 0, 'missing_sample': []}, 'var_call_z8xed14PSfHWo0Q111DUdc7e': {'IVZ_in_info': False, 'IVZ_in_trade': False}, 'var_call_LOkh8YoVXUx7oprA4QWHAw9H': {'n_symbols': 234, 'EIX_included': False, 'query_len': 49903, 'first20': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'contains_EIX_substring': False}, 'var_call_4PWuSxTt3Y1Z5z0y9eua27eD': {'I_symbols_sample': ['IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT'], 'count_I_symbols': 6}, 'var_call_e9XiVEOQZcvsYWJLPT1cztbj': [{'Symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}, {'Symbol': 'IGR', 'up_days': '126.0', 'down_days': '101.0'}, {'Symbol': 'IHC', 'up_days': '98.0', 'down_days': '134.0'}, {'Symbol': 'IPG', 'up_days': '129.0', 'down_days': '116.0'}, {'Symbol': 'IRM', 'up_days': '131.0', 'down_days': '116.0'}, {'Symbol': 'IT', 'up_days': '125.0', 'down_days': '125.0'}], 'var_call_9VdpkkKq3LFRBX2FJIioI1CZ': {'ok': True}, 'var_call_BVv7Uy9ukpo0EKeJW1GX6jTm': {'sym': 'AEFC', 'q': 'SELECT \'{}\' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM "AEFC" WHERE Date >= \'2017-01-01\' AND Date < \'2018-01-01\''}, 'var_call_Jw6m4ITOTfXXpfsjuLkX0jQO': {'n_symbols': 234, 'query_len': 50335, 'query_preview': "SELECT 'AEFC' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM  + s +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AIN' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM  + s +  WHERE Date >= '2017-01-01' AND Date < '2018-01-01' UNION ALL SELECT 'AIV' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END)"}, 'var_call_GLkKBVTMwXZoVqAIvwcTpbHz': {'query_len': 49903, 'preview': 'SELECT \'AEFC\' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM "AEFC" WHERE Date >= \'2017-01-01\' AND Date < \'2018-01'}, 'var_call_lb4xNIc7NCOzS7FDFSirtQPV': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'Symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'Symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'Symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'Symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'Symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'Symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'Symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'Symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'Symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'Symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'Symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'Symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'Symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'Symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'Symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'Symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}, {'Symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'Symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'Symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'Symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'Symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'Symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'Symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'Symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'Symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'Symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}, {'Symbol': 'CXH', 'up_days': '126.0', 'down_days': '91.0'}, {'Symbol': 'DAC', 'up_days': '66.0', 'down_days': '115.0'}, {'Symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}, {'Symbol': 'IGR', 'up_days': '126.0', 'down_days': '101.0'}, {'Symbol': 'IHC', 'up_days': '98.0', 'down_days': '134.0'}, {'Symbol': 'IPG', 'up_days': '129.0', 'down_days': '116.0'}, {'Symbol': 'IRM', 'up_days': '131.0', 'down_days': '116.0'}, {'Symbol': 'IT', 'up_days': '125.0', 'down_days': '125.0'}]}

exec(code, env_args)
