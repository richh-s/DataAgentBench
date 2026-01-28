code = """import json
import pandas as pd
# var_call_XuluQuL9bhjymtKjFC7XCB4i contains the stockinfo query results (list of dicts)
# var_call_tVILwlranVjeUxQC74j9olYj contains the list of tables in stocktrade_database
stockinfo = pd.DataFrame(var_call_XuluQuL9bhjymtKjFC7XCB4i)
trade_tables = list(var_call_tVILwlranVjeUxQC74j9olYj)
# extract symbols from stockinfo
symbols = stockinfo['Symbol'].tolist()
# keep only symbols that have corresponding tables in stocktrade_database
symbols_in_trade = [s for s in symbols if s in trade_tables]
# prepare output
out = {
    'num_symbols_from_stockinfo': len(symbols),
    'num_symbols_with_trade_table': len(symbols_in_trade),
    'symbols_in_trade_sample_first_100': symbols_in_trade[:100],
    'all_symbols_in_trade': symbols_in_trade
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_XuluQuL9bhjymtKjFC7XCB4i': 'file_storage/call_XuluQuL9bhjymtKjFC7XCB4i.json', 'var_call_tVILwlranVjeUxQC74j9olYj': 'file_storage/call_tVILwlranVjeUxQC74j9olYj.json'}

exec(code, env_args)
