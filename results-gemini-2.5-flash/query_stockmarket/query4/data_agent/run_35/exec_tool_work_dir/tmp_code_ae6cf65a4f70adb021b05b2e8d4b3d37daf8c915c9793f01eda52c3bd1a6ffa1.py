code = """import pandas as pd
import json

# Load the NYSE stock information
with open(locals()['var_function-call-1475240843527081014'], 'r') as f:
    nyse_stocks_info = json.load(f)

nyse_stocks_df = pd.DataFrame(nyse_stocks_info)

stock_performance = []

for index, row in nyse_stocks_df.iterrows():
    symbol = row['Symbol']
    company_description = row['Company Description']

    # Construct the query string. DuckDB requires table names with special characters
    # or mixed case to be double-quoted. All stock symbols appear to be uppercase, so double-quoting is appropriate.
    # The LIKE clause for dates uses single quotes.
    query_string = "SELECT Date, Open, Close FROM \"" + symbol + "\" WHERE Date LIKE '2017-%';"

    try:
        # Correctly call the query_db function using default_api
        query_result = default_api.query_db(
            db_name="stocktrade_database",
            query=query_string
        )

        if query_result and 'results' in query_result and query_result['results']:
            stock_data = query_result['results']

            up_days = 0
            down_days = 0

            for day_data in stock_data:
                # Ensure numeric conversions for comparison
                open_price = float(day_data['Open'])
                close_price = float(day_data['Close'])

                if close_price > open_price:
                    up_days += 1
                elif close_price < open_price:
                    down_days += 1

            if up_days > down_days:
                stock_performance.append({
                    'Symbol': symbol,
                    'Company Description': company_description,
                    'Up Days': up_days,
                    'Down Days': down_days,
                    'Difference': up_days - down_days
                })
    except Exception as e:
        # Log errors for debugging if needed, but continue processing other stocks
        # print(f"Error processing stock {symbol}: {e}")
        continue

# Sort by difference in descending order and get the top 5
top_5_stocks = sorted(stock_performance, key=lambda x: x['Difference'], reverse=True)[:5]

# Extract only company descriptions for the final answer
final_answer = [stock['Company Description'] for stock in top_5_stocks]

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-11820878449294623413': 'file_storage/function-call-11820878449294623413.json', 'var_function-call-2353068768197412516': [], 'var_function-call-6386032267884681873': [], 'var_function-call-12109383824988029975': [], 'var_function-call-5615837029812849117': 'file_storage/function-call-5615837029812849117.json', 'var_function-call-4321617129231401927': [{'Date': '1987-09-30', 'Open': '14.988152503967283', 'Close': '15.107105255126951'}], 'var_function-call-7866009266541559027': 'file_storage/function-call-7866009266541559027.json', 'var_function-call-9261700538938387197': [], 'var_function-call-9707489483092941224': 'file_storage/function-call-9707489483092941224.json', 'var_function-call-17299308845485818496': [], 'var_function-call-6396896753408482335': 'file_storage/function-call-6396896753408482335.json', 'var_function-call-15489448046703615035': 'file_storage/function-call-15489448046703615035.json', 'var_function-call-192796813735409244': [], 'var_function-call-3057223277246291935': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_function-call-17856188803145736618': [], 'var_function-call-1605914778053107880': 'file_storage/function-call-1605914778053107880.json', 'var_function-call-12927138052212023094': 'file_storage/function-call-12927138052212023094.json', 'var_function-call-6089715383767261500': [], 'var_function-call-1021649864149984083': [], 'var_function-call-13154562845507486668': [], 'var_function-call-9625433344101057818': 'file_storage/function-call-9625433344101057818.json', 'var_function-call-13889125415046620691': [], 'var_function-call-1475240843527081014': 'file_storage/function-call-1475240843527081014.json'}

exec(code, env_args)
