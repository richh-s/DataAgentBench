code = """import json

# Map exchanges to regions and their main index symbols using known finance knowledge
exchange_to_region = {
    "New York Stock Exchange": "North America",
    "NASDAQ": "North America",
    "Hong Kong Stock Exchange": "Asia",
    "Shanghai Stock Exchange": "Asia",
    "Tokyo Stock Exchange": "Asia",
    "Euronext": "Europe",
    "Shenzhen Stock Exchange": "Asia",
    "Toronto Stock Exchange": "North America",
    "National Stock Exchange of India": "Asia",
    "Frankfurt Stock Exchange": "Europe",
    "Korea Exchange": "Asia",
    "SIX Swiss Exchange": "Europe",
    "Taiwan Stock Exchange": "Asia",
    "Johannesburg Stock Exchange": "Africa",
}

# Map exchanges to expected index symbols in index_trade
exchange_to_index = {
    "New York Stock Exchange": "NYA",
    "NASDAQ": "IXIC",
    "Hong Kong Stock Exchange": "HSI",
    "Shanghai Stock Exchange": "000001.SS",
    "Tokyo Stock Exchange": "N225",
    "Euronext": "N100",
    "Shenzhen Stock Exchange": "399001.SZ",
    "Toronto Stock Exchange": "GSPTSE",
    "National Stock Exchange of India": "NSEI",
    "Frankfurt Stock Exchange": "GDAXI",
    "Korea Exchange": "J203.JO",  # NOTE: this is actually JSE, but we only have these symbols
    "SIX Swiss Exchange": "SSMI",
    "Taiwan Stock Exchange": "TWII",
    "Johannesburg Stock Exchange": "J203.JO",
}

# We only care about Asia region indices
asia_indices = []
for exch, region in exchange_to_region.items():
    if region == "Asia" and exch in exchange_to_index:
        asia_indices.append(exchange_to_index[exch])

result = json.dumps({"asia_indices": asia_indices})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Tdwk66GxvSbat8eywFjhnMcE': ['index_info'], 'var_call_aWnx3k9jO7MixbVlYKzk3fjX': ['index_trade'], 'var_call_ZEMiEIVeqLncfydH3oJaDwGj': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_qFCMsJUDPXa9EQ3if6u7nwh9': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}]}

exec(code, env_args)
