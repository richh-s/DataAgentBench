code = """import json
import pandas as pd

with open(locals()['var_function-call-17266893913970725203'], 'r') as f:
    symbols = json.load(f)

# The function to query a single symbol
def get_up_down_days(symbol):
    try:
        query_result = default_api.query_db(db_name="stocktrade_database", query=f"SELECT Date, Open, Close FROM \"{symbol}\" WHERE Date LIKE '2017%';")
        
        # Check if query_db_response exists and is not empty or is a file path
        if query_result and "query_db_response" in query_result:
            if isinstance(query_result["query_db_response"]["results"], str) and query_result["query_db_response"]["results"].endswith(".json"):
                # If it's a file path, load from file
                with open(query_result["query_db_response"]["results"], 'r') as f:
                    data = json.load(f)
            else:
                data = query_result["query_db_response"]["results"]
            
            if not data:
                return 0, 0
            
            df = pd.DataFrame(data)
            df['Up'] = df['Close'] > df['Open']
            df['Down'] = df['Close'] < df['Open']
            up_days = df['Up'].sum()
            down_days = df['Down'].sum()
            return up_days, down_days
        else:
            return 0, 0
    except Exception as e:
        # print(f"Error processing {symbol}: {e}")
        return 0, 0

results = []
for symbol in symbols:
    up_days, down_days = get_up_down_days(symbol)
    if up_days > down_days:
        results.append({"Symbol": symbol, "UpDays": int(up_days), "DownDays": int(down_days), "Diff": int(up_days - down_days)})

# Sort by difference in up days vs down days and get top 5
sorted_results = sorted(results, key=lambda x: x['Diff'], reverse=True)
top_5_symbols = [item['Symbol'] for item in sorted_results[:5]]

# Retrieve company descriptions for the top 5 symbols
final_results = []
if top_5_symbols:
    # Constructing a single query for company descriptions
    symbol_list_str = ", ".join(f"'{s}'" for s in top_5_symbols)
    company_info_query = f"SELECT Symbol, `Company Description` FROM stockinfo WHERE Symbol IN ({symbol_list_str});"
    company_info_result = default_api.query_db(db_name="stockinfo_database", query=company_info_query)

    if company_info_result and "query_db_response" in company_info_result:
        company_descriptions = {}
        if isinstance(company_info_result["query_db_response"]["results"], str) and company_info_result["query_db_response"]["results"].endswith(".json"):
             with open(company_info_result["query_db_response"]["results"], 'r') as f:
                 company_data = json.load(f)
        else:
             company_data = company_info_result["query_db_response"]["results"]

        for item in company_data:
            company_descriptions[item['Symbol']] = item['Company Description']
        
        for symbol_entry in sorted_results[:5]:
            symbol = symbol_entry['Symbol']
            if symbol in company_descriptions:
                final_results.append({
                    "Symbol": symbol,
                    "Company Description": company_descriptions[symbol],
                    "UpDays": symbol_entry['UpDays'],
                    "DownDays": symbol_entry['DownDays'],
                    "Diff": symbol_entry['Diff']
                })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-13318968725974698213': 'file_storage/function-call-13318968725974698213.json', 'var_function-call-17266893913970725203': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_function-call-1059140404873916172': []}

exec(code, env_args)
