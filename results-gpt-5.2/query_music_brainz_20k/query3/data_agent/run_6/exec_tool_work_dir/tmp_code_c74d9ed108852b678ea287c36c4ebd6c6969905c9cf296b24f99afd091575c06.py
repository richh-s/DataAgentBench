code = """import json, pandas as pd, re

def load_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

sales_totals = load_result(var_call_wU69cCz1JibEWfrYfdIDXuM1)
tracks = load_result(var_call_w7CL69Bnvl2DOIRHhuGZch8X)

sales_df = pd.DataFrame(sales_totals)
tracks_df = pd.DataFrame(tracks)

# types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# pick top revenue track_id (single record)
top_row = sales_df.sort_values('total_revenue_usd', ascending=False).iloc[0]
top_track_id = int(top_row['track_id'])

rec = tracks_df[tracks_df['track_id'] == top_track_id].iloc[0].to_dict()

answer = {
    'track_id': top_track_id,
    'title': rec.get('title'),
    'artist': rec.get('artist'),
    'album': rec.get('album'),
    'year': rec.get('year'),
    'total_revenue_usd': float(top_row['total_revenue_usd'])
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_wU69cCz1JibEWfrYfdIDXuM1': 'file_storage/call_wU69cCz1JibEWfrYfdIDXuM1.json', 'var_call_w7CL69Bnvl2DOIRHhuGZch8X': 'file_storage/call_w7CL69Bnvl2DOIRHhuGZch8X.json'}

exec(code, env_args)
