code = """import json
# var_call_d0viNYf5U0icElCnN0nOm2gM and var_call_I6GIcNMIOXM04vwbdpdH5VzZ are available from storage
# Prepare final answer JSON
symbol = var_call_d0viNYf5U0icElCnN0nOm2gM[0]['Symbol']
company = var_call_d0viNYf5U0icElCnN0nOm2gM[0]['Company Description']
max_adj = var_call_I6GIcNMIOXM04vwbdpdH5VzZ[0]['max_adj_close']
# Compose result as plain text sentence
answer_text = f"The maximum adjusted closing price in 2020 for {symbol} (The RealReal, Inc.) was ${float(max_adj):.2f}."
print("__RESULT__:")
print(json.dumps(answer_text))"""

env_args = {'var_call_d0viNYf5U0icElCnN0nOm2gM': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_I6GIcNMIOXM04vwbdpdH5VzZ': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
