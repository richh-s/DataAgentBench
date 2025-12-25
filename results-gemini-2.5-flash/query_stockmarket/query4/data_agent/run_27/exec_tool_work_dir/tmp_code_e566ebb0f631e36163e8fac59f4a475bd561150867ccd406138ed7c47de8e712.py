code = """import json
import pandas as pd

stock_data_path = locals()['var_function-call-12875624375361337078']
with open(stock_data_path, 'r') as f:
    nyse_non_etf_stocks_list = json.load(f)
nyse_non_etf_stocks_df = pd.DataFrame(nyse_non_etf_stocks_list)

all_stocktrade_tables_path = locals()['var_function-call-12136435633102572331']
with open(all_stocktrade_tables_path, 'r') as f:
    all_stocktrade_tables = json.load(f)

valid_symbols = nyse_non_etf_stocks_df[nyse_non_etf_stocks_df['Symbol'].isin(all_stocktrade_tables)]

print("__RESULT__:")
print(valid_symbols.to_json(orient='records'))"""

env_args = {'var_function-call-7012121346479986777': [], 'var_function-call-14268070821149566659': ['stockinfo'], 'var_function-call-9560150834155655279': [{'cid': '0', 'name': 'Nasdaq Traded', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Symbol', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Listing Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Market Category', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'ETF', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Round Lot Size', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'Test Issue', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Financial Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'NextShares', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'Company Description', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-15441623965883092874': [{"'Listing Exchange'": 'Listing Exchange'}], 'var_function-call-15605829244534943214': [{'Listing Exchange': 'P'}, {'Listing Exchange': 'Q'}, {'Listing Exchange': 'Z'}, {'Listing Exchange': 'A'}, {'Listing Exchange': 'N'}], 'var_function-call-2119554328766442667': 'file_storage/function-call-2119554328766442667.json', 'var_function-call-12875624375361337078': 'file_storage/function-call-12875624375361337078.json', 'var_function-call-600631153782604547': 234, 'var_function-call-12136435633102572331': 'file_storage/function-call-12136435633102572331.json', 'var_function-call-13037626783966000532': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}], 'var_function-call-12116122488726255436': []}

exec(code, env_args)
