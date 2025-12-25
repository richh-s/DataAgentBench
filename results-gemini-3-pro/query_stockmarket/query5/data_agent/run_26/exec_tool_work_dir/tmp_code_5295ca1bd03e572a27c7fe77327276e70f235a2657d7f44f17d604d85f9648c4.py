code = """import json
import os

# Helper to load data
def load_data(var_value):
    if isinstance(var_value, str) and os.path.exists(var_value):
        with open(var_value, 'r') as f:
            return json.load(f)
    return var_value

# Load batch 1 results
results1 = load_data(locals()['var_function-call-12448096286975785336'])

# Load batch 2 results
results2 = load_data(locals()['var_function-call-7285021775102685059'])

# Combine
all_results = results1 + results2

# Convert Days to int just in case
for r in all_results:
    r['Days'] = int(r['Days'])

# Sort
sorted_results = sorted(all_results, key=lambda x: x['Days'], reverse=True)

# Top 5
top5 = sorted_results[:5]

# Load stockinfo to get names
# The first tool call result was definitely a file path because it was large
stock_info = load_data(locals()['var_function-call-441098270662308992'])

# Create symbol -> description map
info_map = {item['Symbol']: item['Company Description'] for item in stock_info}

# Add description to top 5
final_list = []
for item in top5:
    sym = item['Symbol']
    desc = info_map.get(sym, "Unknown")
    # Extract Company Name from description
    # Most descriptions are like "Company Name Inc. specializes..."
    # I'll try to split by some keywords or just take the first few words.
    # But for the answer, the full description helps or I can just list the symbol and description.
    final_list.append({"Symbol": sym, "Days": item['Days'], "Company Name": desc})

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-441098270662308992': 'file_storage/function-call-441098270662308992.json', 'var_function-call-10433719829515190866': 'file_storage/function-call-10433719829515190866.json', 'var_function-call-2958366835203944472': ['BOSC', 'BWEN', 'MBNKP', 'GTEC', 'XPEL', 'CFBK', 'PECK', 'PCSB', 'CBAT', 'FTFT', 'IDEX', 'SSNT', 'NXTD', 'IOTS', 'STKS', 'CCCL', 'FNCB', 'PFIE', 'POPE', 'GLG', 'CVV', 'GRNVU', 'MMAC', 'OPOF', 'BIOC', 'MLND', 'BKYI', 'MNPR', 'FSBW', 'CLRB', 'ANDA', 'VMD', 'TGLS', 'ISNS', 'CUBA', 'BHAT', 'CPAH', 'PLIN', 'BOTJ', 'AGMH', 'HCCOU', 'VVPR', 'BLFS', 'HRTX', 'VERB', 'NVEE', 'CORV', 'AMHC', 'ALACU', 'DZSI', 'PBFS', 'TMSR', 'ORGO', 'WHLM', 'GDYN', 'OPTT', 'XBIOW', 'PEIX', 'HQI', 'APEX', 'CEMI', 'MNCLU', 'ORSNU', 'PBTS', 'CPAAU', 'EYEG', 'HNNA', 'CDMOP', 'EXPC', 'WHLR', 'SNSS', 'ELSE', 'SHSP', 'IGIC', 'MCEP', 'OTEL', 'BCLI', 'MBCN', 'SES', 'CFFA', 'VTIQW', 'VRRM', 'QRHC', 'LACQ', 'FAMI', 'ITI'], 'var_function-call-17333126425019614728': 'file_storage/function-call-17333126425019614728.json', 'var_function-call-889469310385412798': 'file_storage/function-call-889469310385412798.json', 'var_function-call-12448096286975785336': [{'Symbol': 'BOSC', 'Days': '3'}, {'Symbol': 'BWEN', 'Days': '5'}, {'Symbol': 'MBNKP', 'Days': '0'}, {'Symbol': 'GTEC', 'Days': '0'}, {'Symbol': 'XPEL', 'Days': '4'}, {'Symbol': 'CFBK', 'Days': '0'}, {'Symbol': 'PECK', 'Days': '19'}, {'Symbol': 'PCSB', 'Days': '0'}, {'Symbol': 'CBAT', 'Days': '23'}, {'Symbol': 'FTFT', 'Days': '21'}, {'Symbol': 'IDEX', 'Days': '15'}, {'Symbol': 'SSNT', 'Days': '11'}, {'Symbol': 'NXTD', 'Days': '15'}, {'Symbol': 'IOTS', 'Days': '1'}, {'Symbol': 'STKS', 'Days': '0'}, {'Symbol': 'CCCL', 'Days': '13'}, {'Symbol': 'FNCB', 'Days': '1'}, {'Symbol': 'PFIE', 'Days': '2'}, {'Symbol': 'POPE', 'Days': '0'}, {'Symbol': 'GLG', 'Days': '42'}, {'Symbol': 'CVV', 'Days': '0'}, {'Symbol': 'GRNVU', 'Days': '0'}, {'Symbol': 'MMAC', 'Days': '1'}, {'Symbol': 'OPOF', 'Days': '0'}, {'Symbol': 'BIOC', 'Days': '21'}, {'Symbol': 'MLND', 'Days': '3'}, {'Symbol': 'BKYI', 'Days': '16'}, {'Symbol': 'MNPR', 'Days': '4'}, {'Symbol': 'FSBW', 'Days': '0'}, {'Symbol': 'CLRB', 'Days': '14'}, {'Symbol': 'ANDA', 'Days': '0'}, {'Symbol': 'VMD', 'Days': '1'}, {'Symbol': 'TGLS', 'Days': '0'}, {'Symbol': 'ISNS', 'Days': '0'}, {'Symbol': 'CUBA', 'Days': '0'}, {'Symbol': 'BHAT', 'Days': '10'}, {'Symbol': 'CPAH', 'Days': '16'}, {'Symbol': 'PLIN', 'Days': '1'}, {'Symbol': 'BOTJ', 'Days': '0'}, {'Symbol': 'AGMH', 'Days': '13'}, {'Symbol': 'HCCOU', 'Days': '0'}, {'Symbol': 'VVPR', 'Days': '14'}, {'Symbol': 'BLFS', 'Days': '0'}], 'var_function-call-7285021775102685059': [{'Symbol': 'HRTX', 'Days': '1'}, {'Symbol': 'VERB', 'Days': '38'}, {'Symbol': 'NVEE', 'Days': '1'}, {'Symbol': 'CORV', 'Days': '10'}, {'Symbol': 'AMHC', 'Days': '0'}, {'Symbol': 'ALACU', 'Days': '0'}, {'Symbol': 'DZSI', 'Days': '1'}, {'Symbol': 'PBFS', 'Days': '0'}, {'Symbol': 'TMSR', 'Days': '40'}, {'Symbol': 'ORGO', 'Days': '15'}, {'Symbol': 'WHLM', 'Days': '0'}, {'Symbol': 'GDYN', 'Days': '0'}, {'Symbol': 'OPTT', 'Days': '12'}, {'Symbol': 'XBIOW', 'Days': '7'}, {'Symbol': 'PEIX', 'Days': '12'}, {'Symbol': 'HQI', 'Days': '2'}, {'Symbol': 'APEX', 'Days': '15'}, {'Symbol': 'CEMI', 'Days': '3'}, {'Symbol': 'MNCLU', 'Days': '0'}, {'Symbol': 'ORSNU', 'Days': '0'}, {'Symbol': 'PBTS', 'Days': '8'}, {'Symbol': 'CPAAU', 'Days': '0'}, {'Symbol': 'EYEG', 'Days': '18'}, {'Symbol': 'HNNA', 'Days': '0'}, {'Symbol': 'CDMOP', 'Days': '0'}, {'Symbol': 'EXPC', 'Days': '0'}, {'Symbol': 'WHLR', 'Days': '15'}, {'Symbol': 'SNSS', 'Days': '32'}, {'Symbol': 'ELSE', 'Days': '0'}, {'Symbol': 'SHSP', 'Days': '1'}, {'Symbol': 'IGIC', 'Days': '0'}, {'Symbol': 'MCEP', 'Days': '14'}, {'Symbol': 'OTEL', 'Days': '1'}, {'Symbol': 'BCLI', 'Days': '0'}, {'Symbol': 'MBCN', 'Days': '0'}, {'Symbol': 'SES', 'Days': '51'}, {'Symbol': 'CFFA', 'Days': '0'}, {'Symbol': 'VTIQW', 'Days': '6'}, {'Symbol': 'VRRM', 'Days': '0'}, {'Symbol': 'QRHC', 'Days': '3'}, {'Symbol': 'LACQ', 'Days': '0'}, {'Symbol': 'FAMI', 'Days': '23'}, {'Symbol': 'ITI', 'Days': '0'}]}

exec(code, env_args)
