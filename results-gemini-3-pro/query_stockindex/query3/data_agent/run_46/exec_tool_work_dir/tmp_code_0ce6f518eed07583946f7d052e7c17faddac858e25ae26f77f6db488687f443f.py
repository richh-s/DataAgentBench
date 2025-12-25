code = """import json
import pandas as pd

try:
    file_path = locals()['var_function-call-5900596531419111934']
    with open(file_path, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    
    # Check date format
    # The preview showed "2000-01-04 00:00:00", which works with standard parser
    # But to be safe against mixed formats
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
    df = df.dropna(subset=['Date'])
    
    df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
    df = df.dropna(subset=['Adj Close'])
    
    df = df.sort_values(['Index', 'Date'])

    results = []

    for index_name, group in df.groupby('Index'):
        if group.empty:
            continue
            
        group = group.copy()
        group['YearMonth'] = group['Date'].dt.to_period('M')
        
        # Monthly investment on first available day
        monthly_investments = group.drop_duplicates(subset=['YearMonth'], keep='first')
        
        # Invest 1 unit each month
        # Units = Investment / Price
        monthly_investments['Units_Bought'] = 1 / monthly_investments['Adj Close']
        
        total_units = monthly_investments['Units_Bought'].sum()
        total_invested = len(monthly_investments) # Total amount invested
        
        if total_invested == 0:
            continue
            
        # Final value
        last_price = group.iloc[-1]['Adj Close']
        final_value = total_units * last_price
        
        roi = (final_value - total_invested) / total_invested
        
        results.append({
            'Index': index_name,
            'ROI': roi,
            'ROI_Percent': roi * 100,
            'Total_Invested': total_invested,
            'Final_Value': final_value
        })

    results_df = pd.DataFrame(results).sort_values('ROI', ascending=False)
    
    print("__RESULT__:")
    print(results_df.head(5).to_json(orient='records'))

except Exception as e:
    print(f"Error: {e}")"""

env_args = {'var_function-call-13501008299029343830': ['index_info'], 'var_function-call-13501008299029341129': ['index_trade'], 'var_function-call-17345393264304504446': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-17345393264304504609': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-5900596531419111934': 'file_storage/function-call-5900596531419111934.json'}

exec(code, env_args)
