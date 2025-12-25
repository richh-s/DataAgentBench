code = """import pandas as pd
import json

top_5_indices = pd.read_json(locals()['var_function-call-1138837210924073315'])

# Manually map indices to countries based on general knowledge
index_to_country = {
    "IXIC": "United States",  # NASDAQ Composite
    "NYA": "United States",   # NYSE Composite
    "N225": "Japan",         # Nikkei 225
    "GDAXI": "Germany",       # DAX
    "GSPTSE": "Canada"        # S&P/TSX Composite Index
}

top_5_indices['Country'] = top_5_indices['Index'].map(index_to_country)

final_result = top_5_indices[['Index', 'OverallReturn', 'Country']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-8311487335704339999': 'file_storage/function-call-8311487335704339999.json', 'var_function-call-1138837210924073315': [{'Index': 'IXIC', 'OverallReturn': 3913.7501498979}, {'Index': 'NYA', 'OverallReturn': 1124.610566241}, {'Index': 'N225', 'OverallReturn': 360.9818492169}, {'Index': 'GDAXI', 'OverallReturn': 329.2276982793}, {'Index': 'GSPTSE', 'OverallReturn': 296.7902229179}]}

exec(code, env_args)
