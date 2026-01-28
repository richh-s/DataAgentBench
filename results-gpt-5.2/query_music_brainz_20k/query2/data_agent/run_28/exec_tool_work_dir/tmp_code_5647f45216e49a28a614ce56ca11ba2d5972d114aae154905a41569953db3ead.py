code = """import json, pandas as pd

tracks_exact = pd.DataFrame(var_call_574eG78ghqg3meD4S4oNCDON)
tracks_candidates = pd.DataFrame(var_call_egRLZi8SDvrMjePtAKTMfNLg)

# Entity resolution: consider these three as the same song based on title similarity and album/year coherence.
resolved_track_ids = sorted(set(tracks_candidates['track_id'].astype(int).tolist()))

sales = pd.DataFrame(var_call_Do4pO9wdEEPc3owmgU3WMny9)
if not sales.empty:
    sales['track_id'] = sales['track_id'].astype(int)
    sales['revenue_usd'] = sales['revenue_usd'].astype(float)

sales_resolved = sales[sales['track_id'].isin(resolved_track_ids)].copy()

by_store = (sales_resolved.groupby('store', as_index=False)['revenue_usd'].sum()
            .sort_values(['revenue_usd','store'], ascending=[False, True]))

best = by_store.iloc[0].to_dict() if not by_store.empty else None

out = {
    'resolved_track_ids': resolved_track_ids,
    'revenue_by_store': by_store.to_dict(orient='records'),
    'best_store': best
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_574eG78ghqg3meD4S4oNCDON': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_egRLZi8SDvrMjePtAKTMfNLg': [{'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_p6GYcNmSYBcE36dOFzHaxPdl': ['sales'], 'var_call_Do4pO9wdEEPc3owmgU3WMny9': [{'track_id': '4122', 'store': 'Apple Music', 'country': 'Germany', 'units_sold': '47', 'revenue_usd': '47.52'}, {'track_id': '4122', 'store': 'Amazon Music', 'country': 'France', 'units_sold': '262', 'revenue_usd': '304.13'}, {'track_id': '4628', 'store': 'iTunes', 'country': 'France', 'units_sold': '469', 'revenue_usd': '505.61'}, {'track_id': '14080', 'store': 'Apple Music', 'country': 'UK', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
