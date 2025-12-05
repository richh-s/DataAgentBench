code = """import json, pandas as pd
from pathlib import Path
symbols = json.load(open(var_call_wsLlo5WL8oajUAP335Xuj82G))
# Just keep for now; filtering will be done after joining with stockinfo
result = json.dumps(symbols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wsLlo5WL8oajUAP335Xuj82G': 'file_storage/call_wsLlo5WL8oajUAP335Xuj82G.json', 'var_call_jRSW6QeUSSMM8v5ABpxKRewW': 'file_storage/call_jRSW6QeUSSMM8v5ABpxKRewW.json'}

exec(code, env_args)
