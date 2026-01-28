code = """import json
# var_call_45Cygi9xOU8nRkD0ukw33YFo contains the query result for max adjusted close
data = var_call_45Cygi9xOU8nRkD0ukw33YFo
val_str = None
if isinstance(data, list) and len(data) > 0:
    val_str = data[0].get('max_adj_close')
if val_str is None:
    result = {"symbol": "REAL", "company": "The RealReal, Inc.", "year": 2020, "max_adj_close": None}
else:
    try:
        val = float(val_str)
    except Exception:
        val = None
    # round to 2 decimal places if not None
    result = {"symbol": "REAL", "company": "The RealReal, Inc.", "year": 2020, "max_adj_close": round(val, 2) if val is not None else None}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iXfY5lo0wlRNkoLc8bnuUmVg': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_45Cygi9xOU8nRkD0ukw33YFo': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
