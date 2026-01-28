code = """import json
import os

# Find the variables we need
all_vars = list(locals().keys())
tradeable_var_name = None
company_info_path = None

for var in all_vars:
    if 'execute_python' in var and ':38' in var:
        tradeable_var_name = var
    elif 'query_db:44' in var:
        company_info_path = locals()[var]

if tradeable_var_name and company_info_path:
    tradeable_symbols = locals()[tradeable_var_name]['symbols']
    print(f"Processing {len(tradeable_symbols)} symbols for 2019 volatility...")
    
    # Read company info
    with open(company_info_path, 'r') as f:
        company_data = json.load(f)
    
    # Create mapping of symbol to company name
    symbol_to_company = {}
    for item in company_data:
        symbol = item['Symbol']
        desc = item['Company Description']
        # Extract company name (usually first part before "specializes" or other verbs)
        company_name = desc.split(' specializes')[0].split(' is a')[0].split(' operates')[0].split(' provides')[0].strip()
        symbol_to_company[symbol] = company_name
    
    # We'll query each symbol to count high volatility days in 2019
    results = []
    
    # For now, let's create the queries we need to run
    # We'll process them one by one due to query limitations
    queries = []
    for symbol in tradeable_symbols:
        query = f"""SELECT COUNT(*) as count FROM "{symbol}" 
                 WHERE Date >= '2019-01-01' 
                 AND Date <= '2019-12-31' 
                 AND (\"High\" - \"Low\") > (0.20 * \"Low\")"""
        queries.append((symbol, query))
    
    print(f"Generated {len(queries)} queries")
    print(f"Company mappings created for {len(symbol_to_company)} symbols")
    
    result = {
        'symbol_to_company': symbol_to_company,
        'queries': queries,
        'total_symbols': len(tradeable_symbols)
    }
    
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'Variables not found'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:18': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}], 'var_functions.query_db:24': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:34': {'tradeable_symbols': ['IDEX', 'BLFS', 'CFFA', 'XBIOW', 'BWEN', 'CBAT', 'SES', 'HRTX', 'PECK', 'OTEL', 'VTIQW', 'POPE', 'BIOC', 'CUBA', 'OPOF', 'ELSE', 'ALACU', 'ORSNU', 'FNCB', 'MNPR', 'PLIN', 'TGLS', 'ITI', 'OPTT', 'GDYN', 'ORGO', 'BOTJ', 'EXPC', 'FSBW', 'VVPR', 'MMAC', 'FTFT', 'VRRM', 'LACQ', 'WHLR', 'TMSR', 'NXTD', 'PBTS', 'CLRB', 'HQI', 'EYEG', 'GTEC', 'IGIC', 'CDMOP', 'BHAT', 'CPAH', 'WHLM', 'MBCN', 'BKYI', 'DZSI', 'GLG', 'SSNT', 'CFBK', 'MCEP', 'STKS', 'VERB', 'BCLI', 'PCSB', 'CORV', 'CEMI', 'ISNS', 'SNSS', 'XPEL', 'SHSP', 'MNCLU', 'AMHC', 'AGMH', 'CPAAU', 'PFIE', 'MBNKP', 'APEX', 'HNNA', 'IOTS', 'MLND', 'GRNVU', 'BOSC', 'FAMI', 'CVV', 'ANDA', 'CCCL', 'PEIX', 'NVEE', 'VMD', 'QRHC', 'PBFS', 'HCCOU'], 'count': 86}, 'var_functions.execute_python:38': {'count': 86, 'symbols': ['IDEX', 'BLFS', 'CFFA', 'XBIOW', 'BWEN', 'CBAT', 'SES', 'HRTX', 'PECK', 'OTEL', 'VTIQW', 'POPE', 'BIOC', 'CUBA', 'OPOF', 'ELSE', 'ALACU', 'ORSNU', 'FNCB', 'MNPR', 'PLIN', 'TGLS', 'ITI', 'OPTT', 'GDYN', 'ORGO', 'BOTJ', 'EXPC', 'FSBW', 'VVPR', 'MMAC', 'FTFT', 'VRRM', 'LACQ', 'WHLR', 'TMSR', 'NXTD', 'PBTS', 'CLRB', 'HQI', 'EYEG', 'GTEC', 'IGIC', 'CDMOP', 'BHAT', 'CPAH', 'WHLM', 'MBCN', 'BKYI', 'DZSI', 'GLG', 'SSNT', 'CFBK', 'MCEP', 'STKS', 'VERB', 'BCLI', 'PCSB', 'CORV', 'CEMI', 'ISNS', 'SNSS', 'XPEL', 'SHSP', 'MNCLU', 'AMHC', 'AGMH', 'CPAAU', 'PFIE', 'MBNKP', 'APEX', 'HNNA', 'IOTS', 'MLND', 'GRNVU', 'BOSC', 'FAMI', 'CVV', 'ANDA', 'CCCL', 'PEIX', 'NVEE', 'VMD', 'QRHC', 'PBFS', 'HCCOU'], 'symbols_for_query': "IDEX','BLFS','CFFA','XBIOW','BWEN','CBAT','SES','HRTX','PECK','OTEL','VTIQW','POPE','BIOC','CUBA','OPOF','ELSE','ALACU','ORSNU','FNCB','MNPR','PLIN','TGLS','ITI','OPTT','GDYN','ORGO','BOTJ','EXPC','FSBW','VVPR','MMAC','FTFT','VRRM','LACQ','WHLR','TMSR','NXTD','PBTS','CLRB','HQI','EYEG','GTEC','IGIC','CDMOP','BHAT','CPAH','WHLM','MBCN','BKYI','DZSI','GLG','SSNT','CFBK','MCEP','STKS','VERB','BCLI','PCSB','CORV','CEMI','ISNS','SNSS','XPEL','SHSP','MNCLU','AMHC','AGMH','CPAAU','PFIE','MBNKP','APEX','HNNA','IOTS','MLND','GRNVU','BOSC','FAMI','CVV','ANDA','CCCL','PEIX','NVEE','VMD','QRHC','PBFS','HCCOU"}, 'var_functions.query_db:40': [{'high_volatility_days': '15'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
