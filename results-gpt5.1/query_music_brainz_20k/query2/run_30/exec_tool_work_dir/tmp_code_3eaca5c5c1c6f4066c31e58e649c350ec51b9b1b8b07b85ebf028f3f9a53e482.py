code = """import json
import pandas as pd

tracks = pd.DataFrame(var_call_BnGvbldvmBYyXIzRvNB1rz6P)

canonical = tracks.iloc[0]

candidate_ids = tracks['track_id'].astype(int).tolist()

result = json.dumps(candidate_ids)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_tZG50VLYv5FPILr8jAYvYSWv': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_BnGvbldvmBYyXIzRvNB1rz6P': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}]}

exec(code, env_args)
