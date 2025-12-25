code = """import json

# Use the broader search results that likely contain all duplicates
tracks = var_call_1PUDeQIQ9lXnd6H9MyRcyHnN

# Determine which track_ids correspond to the real-world song 'Street Hype' by Brucqe Maginnis
# From inspection: all returned rows are clear variants of the same song.
track_ids = [int(row['track_id']) for row in tracks]

result = json.dumps(track_ids)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_QMdMrFK2gbL7t0u7XOaLzEio': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_1PUDeQIQ9lXnd6H9MyRcyHnN': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}]}

exec(code, env_args)
