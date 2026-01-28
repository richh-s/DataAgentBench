code = """import json
import pandas as pd

# Define the function to count volatility days for a single stock
def count_volatility_days(db_query_func, symbol):
    """Count days in 2019 where (High - Low) / Low > 0.20"""
    try:
        query = f'SELECT Date, High, Low FROM "{symbol}" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\''
        result = db_query_func('stocktrade_database', query)
        
        if not result or len(result) == 0:
            return 0, 0
        
        df = pd.DataFrame(result)
        if df.empty or 'High' not in df.columns or 'Low' not in df.columns:
            return 0, 0
        
        # Convert to numeric, handling potential string values
        df['High'] = pd.to_numeric(df['High'], errors='coerce')
        df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
        
        # Remove rows with missing values
        df = df.dropna(subset=['High', 'Low'])
        
        if df.empty:
            return 0, 0
        
        # Calculate volatility condition: (High - Low) / Low > 0.20
        df['volatility_ratio'] = (df['High'] - df['Low']) / df['Low']
        volatile_days = (df['volatility_ratio'] > 0.20).sum()
        total_days = len(df)
        
        return volatile_days, total_days
    except Exception as e:
        print(f"Error processing {symbol}: {e}")
        return 0, 0

# For testing, let's process a few stocks first

# Get symbols
nasdaq_cap_file_path = locals()['var_functions.query_db:22']
with open(nasdaq_cap_file_path, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]

# Test with a few symbols
test_symbols = symbols[:5]
print('__RESULT__:')
print(f"Testing with symbols: {test_symbols}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': 'file_storage/functions.list_db:4.json', 'var_functions.execute_python:14': {'file_path': 'file_storage/functions.query_db:0.json', 'count': 86, 'symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.execute_python:16': {'nasdaq_cap_count': 86, 'trade_db_count': 2753, 'intersection_count': 86, 'existing_symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.query_db:18': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'count': 86, 'sample': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.']]}, 'var_functions.execute_python:26': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
