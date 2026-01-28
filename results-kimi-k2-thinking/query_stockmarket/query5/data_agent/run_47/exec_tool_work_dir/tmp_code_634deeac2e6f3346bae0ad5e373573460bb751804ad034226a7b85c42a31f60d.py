code = """import json

# Load 2019 data for AGMH and count high volatility days
with open('file_storage/functions.query_db:16.json', 'r') as f:
    agmh_data = json.load(f)

high_vol_count = 0
high_vol_days = []

for row in agmh_data:
    high = float(row['High'])
    low = float(row['Low'])
    
    if low > 0:  # Avoid division by zero
        range_pct = (high - low) / low
        if range_pct > 0.20:
            high_vol_count += 1
            high_vol_days.append({
                'Date': row['Date'],
                'High': high,
                'Low': low,
                'Range_Pct': range_pct
            })

print('__RESULT__:')
print(json.dumps({
    'symbol': 'AGMH',
    'total_days': len(agmh_data),
    'high_vol_days': high_vol_count,
    'sample_vol_days': high_vol_days[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'file_path': 'file_storage/functions.query_db:0.json', 'status': 'file_path_retrieved'}, 'var_functions.execute_python:6': {'total_stocks': 86, 'sample_records': [{'Symbol': 'AGMH', 'Market Category': 'S', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Listing Exchange': 'Q'}, {'Symbol': 'ALACU', 'Market Category': 'S', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.', 'Listing Exchange': 'Q'}, {'Symbol': 'AMHC', 'Market Category': 'S', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.', 'Listing Exchange': 'Q'}], 'symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': {'total_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.execute_python:12': {'total_existent': 86, 'existent_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.query_db:14': [{'Date': '2018-04-18', 'Open': '5.75', 'High': '7.5', 'Low': '5.010000228881836', 'Close': '6.300000190734863', 'Adj Close': '6.300000190734863', 'Volume': '291800'}, {'Date': '2018-04-19', 'Open': '6.800000190734863', 'High': '8.859999656677246', 'Low': '6.684000015258789', 'Close': '8.479999542236328', 'Adj Close': '8.479999542236328', 'Volume': '299600'}, {'Date': '2018-04-20', 'Open': '13.260000228881836', 'High': '14.989999771118164', 'Low': '7.590000152587891', 'Close': '7.788000106811523', 'Adj Close': '7.788000106811523', 'Volume': '830400'}, {'Date': '2018-04-23', 'Open': '7.5', 'High': '8.579999923706055', 'Low': '7.010000228881836', 'Close': '8.399999618530273', 'Adj Close': '8.399999618530273', 'Volume': '102600'}, {'Date': '2018-04-24', 'Open': '8.119999885559082', 'High': '8.640000343322754', 'Low': '7.28000020980835', 'Close': '8.449999809265137', 'Adj Close': '8.449999809265137', 'Volume': '87600'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
