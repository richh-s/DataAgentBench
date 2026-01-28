code = """import json
path_info = var_call_8UvW6KsMY3Sq7CHGXoSaQiC8
path_trade = var_call_HRvR8LlnRtRJNSMY9MC1q8G7
info = json.load(open(path_info, 'r'))
trade_tables = set(json.load(open(path_trade, 'r')))
symbols_info = [rec['Symbol'] for rec in info]
symbols = [s for s in symbols_info if s in trade_tables]
# Output the list of symbols as JSON
print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_call_8UvW6KsMY3Sq7CHGXoSaQiC8': 'file_storage/call_8UvW6KsMY3Sq7CHGXoSaQiC8.json', 'var_call_HRvR8LlnRtRJNSMY9MC1q8G7': 'file_storage/call_HRvR8LlnRtRJNSMY9MC1q8G7.json'}

exec(code, env_args)
