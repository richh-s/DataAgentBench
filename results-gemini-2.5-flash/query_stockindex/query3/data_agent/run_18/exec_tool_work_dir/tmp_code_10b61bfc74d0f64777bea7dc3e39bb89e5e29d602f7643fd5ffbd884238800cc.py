code = """import pandas as pd
import json
import io

df_trade = pd.read_json(locals()['var_function-call-15735413083344890865'])

# For df_info, the result is directly a list, so we need to convert it to a JSON string and then read it
df_info_list = locals()['var_function-call-15933026684059475808']
df_info = pd.read_json(io.StringIO(json.dumps(df_info_list)))

df_trade['Date'] = pd.to_datetime(df_trade['Date'], errors='coerce')
df_trade = df_trade.dropna(subset=['Date', 'CloseUSD'])
df_trade['CloseUSD'] = pd.to_numeric(df_trade['CloseUSD'])
df_trade = df_trade[df_trade['Date'].dt.year >= 2000]

# Sort by Index and Date to easily get the first day of each month
df_trade = df_trade.sort_values(by=['Index', 'Date'])

# Get the first trading day of each month for each index
df_trade['year_month'] = df_trade['Date'].dt.to_period('M')
monthly_data = df_trade.groupby(['Index', 'year_month']).first().reset_index()

# Calculate the return for each index
returns = {}
for index_symbol in monthly_data['Index'].unique():
    index_df = monthly_data[monthly_data['Index'] == index_symbol].copy()
    if len(index_df) > 0:
        # Assuming 1 USD invested each month, so total_invested is the number of months
        # The total value is the sum of CloseUSD at the end of each month
        total_invested = len(index_df)
        total_value = index_df['CloseUSD'].sum()
        overall_return = (total_value - total_invested) / total_invested
        returns[index_symbol] = overall_return

# Sort by return and get the top 5
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices_returns = sorted_returns[:5]

# Map indices to countries - using a more comprehensive mapping and handling potential missing indices
index_to_country = {
    'HSI': 'Hong Kong (China)',
    '000001.SS': 'China',
    'N225': 'Japan',
    '^GSPC': 'USA',
    '399001.SZ': 'China',
    '^DJI': 'USA',
    '^IXIC': 'USA',
    'GDAXI': 'Germany',
    'TSX': 'Canada',
    'KOSPI': 'South Korea',
    '^TWII': 'Taiwan',
    'J203.JO': 'South Africa',
    '^FCHI': 'France',
    '^BSESN': 'India',
    'XMC.TA': 'Israel', # Added from previous runs
    'MXX': 'Mexico', # Added from previous runs
    'IMOEX.ME': 'Russia', # Added from previous runs
    '^N100': 'Europe', # Added from previous runs
    '^ATX': 'Austria', # Added from previous runs
    'TWII': 'Taiwan', # Corrected from ^TWII as it might be without ^ sometimes
    'BVSP': 'Brazil', # Added from common knowledge
    'KS11': 'South Korea', # Another symbol for KOSPI
    'AS51.AX': 'Australia', # ASX 200
    'FTSEMIB.MI': 'Italy', # FTSE MIB
    'IMOEX': 'Russia', # MOEX Russia Index
    'SSMI.SW': 'Switzerland', # Swiss Market Index
    'AORD.AX': 'Australia', # All Ordinaries
    'NIFTY_50': 'India', # Nifty 50
    'STOXX50E': 'Europe', # EURO STOXX 50
    'RUT': 'USA', # Russell 2000
    'SENSEX': 'India', # S&P BSE SENSEX
    'FCHI': 'France', # CAC 40
    'AXJO': 'Australia', # S&P/ASX 200
    'VIX': 'USA', # CBOE Volatility Index
    'NDX': 'USA', # NASDAQ 100
    'NIFTY': 'India', # Nifty 50
    'EWJ': 'Japan', # iShares MSCI Japan ETF, assuming it represents Japan index
    'EWY': 'South Korea', # iShares MSCI South Korea ETF
    'EWC': 'Canada', # iShares MSCI Canada ETF
    'EWG': 'Germany', # iShares MSCI Germany ETF
    'EWH': 'Hong Kong (China)', # iShares MSCI Hong Kong ETF
    'EWA': 'Australia', # iShares MSCI Australia ETF
    'EWQ': 'France', # iShares MSCI France ETF
    'EWI': 'Italy', # iShares MSCI Italy ETF
    'EWL': 'Switzerland', # iShares MSCI Switzerland ETF
    'EWS': 'Singapore', # iShares MSCI Singapore ETF
    'EWU': 'United Kingdom', # iShares MSCI United Kingdom ETF
    'EWP': 'Spain', # iShares MSCI Spain ETF
    'EWW': 'Mexico', # iShares MSCI Mexico ETF
    'EWZ': 'Brazil', # iShares MSCI Brazil ETF
    'EZA': 'South Africa', # iShares MSCI South Africa ETF
    'FXI': 'China', # iShares China Large-Cap ETF
    'RSX': 'Russia', # VanEck Russia ETF
    'TUR': 'Turkey', # iShares MSCI Turkey ETF
    'ARGT': 'Argentina', # Global X MSCI Argentina ETF
    'COLX': 'Colombia', # Global X MSCI Colombia ETF
    'EGPT': 'Egypt', # VanEck Egypt Index ETF
    'GREK': 'Greece', # Global X MSCI Greece ETF
    'INDA': 'India', # iShares MSCI India ETF
    'KSA': 'Saudi Arabia', # iShares MSCI Saudi Arabia ETF
    'MXI': 'Mexico', # iShares MSCI Mexico Capped ETF
    'PERU': 'Peru', # iShares MSCI Peru Capped ETF
    'PLND': 'Poland', # iShares MSCI Poland Capped ETF
    'PTF': 'Portugal', # Global X MSCI Portugal ETF
    'SPY': 'USA', # SPDR S&P 500 ETF Trust
    'DIA': 'USA', # SPDR Dow Jones Industrial Average ETF Trust
    'QQQ': 'USA', # Invesco QQQ Trust
    'IWM': 'USA', # iShares Russell 2000 ETF
    'ACWI': 'Global', # iShares MSCI ACWI ETF
    'VEU': 'Global', # Vanguard FTSE All-World ex-US Index Fund ETF Shares
    'EEM': 'Emerging Markets', # iShares MSCI Emerging Markets ETF
    'EWGS': 'Germany', # iShares MSCI Germany Small-Cap ETF
    'EZU': 'Europe', # iShares MSCI Eurozone ETF
    'FEZ': 'Europe', # SPDR EURO STOXX 50 ETF
    'IEUR': 'Europe', # iShares Core MSCI Europe ETF
    'VGK': 'Europe', # Vanguard FTSE Europe ETF
    'IEF': 'USA', # iShares 7-10 Year Treasury Bond ETF
    'TLT': 'USA', # iShares 20+ Year Treasury Bond ETF
    'GLD': 'Global', # SPDR Gold Shares
    'SLV': 'Global', # iShares Silver Trust
    'USO': 'Global', # United States Oil Fund LP
    'UNG': 'Global', # United States Natural Gas Fund LP
    'SPX': 'USA', # S&P 500 Index
    'NKY': 'Japan', # Nikkei 225 Index
    'DAX': 'Germany', # DAX Index
    'CAC': 'France', # CAC 40 Index
    'FTSE': 'United Kingdom', # FTSE 100 Index
    'IBEX': 'Spain', # IBEX 35 Index
    'OMX': 'Sweden', # OMX Stockholm 30 Index
    'BEL': 'Belgium', # BEL 20 Index
    'AEX': 'Netherlands', # AEX Index
    'SSMI': 'Switzerland', # Swiss Market Index
    'ATX': 'Austria', # ATX Index
    'ISE': 'Ireland', # ISEQ Overall Index
    'OSX': 'Norway', # OSEBX Index
    'BUX': 'Hungary', # BUX Index
    'PX': 'Czech Republic', # PX Index
    'WIG': 'Poland', # WIG20 Index
    'RTS': 'Russia', # RTS Index
    'MICEX': 'Russia', # MOEX Russia Index
    'BIST': 'Turkey', # BIST 100 Index
    'TASI': 'Saudi Arabia', # Tadawul All Share Index
    'DFM': 'United Arab Emirates', # DFM General Index
    'ADX': 'United Arab Emirates', # ADX General Index
    'QSI': 'Qatar', # Qatar Exchange Index
    'KWSE': 'Kuwait', # Kuwait Stock Exchange Index
    'MSM': 'Oman', # Muscat Securities Market Index
    'BAX': 'Bahrain', # Bahrain All Share Index
    'CASE': 'Egypt', # EGX 30 Index
    'JCI': 'Indonesia', # Jakarta Composite Index
    'SET': 'Thailand', # SET Index
    'KLSE': 'Malaysia', # FTSE Bursa Malaysia KLCI
    'STI': 'Singapore', # Straits Times Index
    'NZ50': 'New Zealand', # S&P/NZX 50 Index
    'KSE': 'Pakistan', # PSX 100 Index
    'PSE': 'Philippines', # PSEi Index
    'VNINDEX': 'Vietnam', # VN-Index
    'SSEC': 'China', # SSE Composite Index
    'SZSC': 'China', # SZSE Component Index
    'TWSE': 'Taiwan', # Taiwan Stock Exchange Weighted Index
    'BSE': 'India', # BSE SENSEX
    'NSE': 'India', # Nifty 50
    'PKX': 'Pakistan', # Global X MSCI Pakistan ETF
    'EPI': 'India', # WisdomTree India Earnings Fund
    'INXX': 'India', # MSCI India Index (not an actual ticker, but for mapping)
    'EZA.JO': 'South Africa'
}


final_result = []
for index, ret in top_5_indices_returns:
    country = index_to_country.get(index, 'Unknown')
    final_result.append({'Index': index, 'Return': ret, 'Country': country})

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-15735413083344890865': 'file_storage/function-call-15735413083344890865.json', 'var_function-call-15933026684059475808': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
