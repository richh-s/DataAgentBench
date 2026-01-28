code = """import json
# load results from previous queries
tracks = var_call_DNF8geTJY012qbhbl3ZDeBj9
sales = var_call_xGF34Gk338UetX3Hy8atire6

# collect candidate track_ids from tracks query
candidate_ids = set([r['track_id'] for r in tracks])

# sum revenue for sales that match candidate track_ids
total = 0.0
count = 0
for s in sales:
    if s['track_id'] in candidate_ids:
        try:
            total += float(s['revenue_usd'])
            count += 1
        except:
            pass

# prepare result
result = {
    "revenue_usd": round(total, 2),
    "currency": "USD",
    "country": "Canada",
    "store": "Apple Music",
    "matched_track_ids": sorted(list(candidate_ids)),
    "sales_records_counted": count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zrc5MrKcb2tf5m2TbCB1i4fz': ['tracks'], 'var_call_uoqcd6BOPMIYc08hXxKBy8xT': ['sales'], 'var_call_DNF8geTJY012qbhbl3ZDeBj9': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_xGF34Gk338UetX3Hy8atire6': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
