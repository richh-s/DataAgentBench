code = """import json, pandas as pd
from pathlib import Path

symbols_info = json.loads(Path(var_call_gP1IxlZ2zvc6LTNaIgIhhOSQ).read_text())
symbols = [r['Symbol'] for r in symbols_info]

# Build DuckDB SQL to compute 2019 high-low condition counts per symbol
conditions = []
for s in symbols:
    # escape double quotes in symbol if any
    tbl = s.replace('"', '""')
    conditions.append(f"SELECT '{s}' AS Symbol, SUM(CASE WHEN Low > 0 AND (High - Low) / Low > 0.2 THEN 1 ELSE 0 END) AS days_exceed FROM '{tbl}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'")

union_sql = " UNION ALL ".join(conditions)

result = {'sql': f"WITH per_symbol AS ({union_sql}) SELECT Symbol, days_exceed FROM per_symbol"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IJuRdD3kxGYIhyNBk5CRauep': 'file_storage/call_IJuRdD3kxGYIhyNBk5CRauep.json', 'var_call_gP1IxlZ2zvc6LTNaIgIhhOSQ': 'file_storage/call_gP1IxlZ2zvc6LTNaIgIhhOSQ.json'}

exec(code, env_args)
