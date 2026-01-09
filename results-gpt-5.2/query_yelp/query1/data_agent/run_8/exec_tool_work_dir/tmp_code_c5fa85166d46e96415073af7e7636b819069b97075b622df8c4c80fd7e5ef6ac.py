code = """import json
biz = var_call_y31uJFp75jIW89JOZdM3UoBf
avg_all = var_call_OusWqh9NzcphEn8USHCXEqDS
if not biz:
    out = {"error":"No businesses matched 'Indianapolis, Indiana' in business.description; cannot compute city-specific average with given data.","avg_rating_all_reviews": float(avg_all[0]["avg_rating_all_reviews"]) if avg_all and avg_all[0].get("avg_rating_all_reviews") is not None else None}
else:
    out = {"business_count": len(biz)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_y31uJFp75jIW89JOZdM3UoBf': [], 'var_call_OusWqh9NzcphEn8USHCXEqDS': [{'avg_rating_all_reviews': '3.515'}]}

exec(code, env_args)
