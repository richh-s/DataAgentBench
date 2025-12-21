code = """import json
candidates = var_call_B63l4c1gENzO7GsZ8oYbvqdY
# All four look like the same real-world track; collect their track_ids
track_ids = [int(r['track_id']) for r in candidates]
result = json.dumps(track_ids)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_mByiX16JJcxJIXgx838iKXHk': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_B63l4c1gENzO7GsZ8oYbvqdY': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}]}

exec(code, env_args)
