code = """import json, pandas as pd
from pathlib import Path

# load symbols list
p = Path(var_call_uLyJm1FW9XUZpkWFLLdTk1x8)
recs = json.loads(p.read_text())
df = pd.DataFrame(recs)
# Keep likely common-stock tickers only (exclude units/warrants/preferred etc.)
# Heuristics: exclude tickers containing '^' or '/' or '.'; exclude those ending with common SPAC/unit suffixes
exclude_suffixes = ('U','W','WS','R','P')

def is_common(sym):
    if any(ch in sym for ch in ['^','/','.']):
        return False
    # exclude if length>4 and endswith U/WS/W etc (e.g., ALACU, CPAAU, CDMOP)
    if len(sym) > 4:
        for suf in exclude_suffixes:
            if sym.endswith(suf):
                return False
    return True

common = df[df['Symbol'].map(is_common)].copy()
# take up to 120 symbols for feasibility
symbols = common['Symbol'].tolist()[:120]

result = {
  'n_total_symbols': int(df.shape[0]),
  'n_common_symbols': int(common.shape[0]),
  'symbols_sample': symbols[:30]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uLyJm1FW9XUZpkWFLLdTk1x8': 'file_storage/call_uLyJm1FW9XUZpkWFLLdTk1x8.json'}

exec(code, env_args)
