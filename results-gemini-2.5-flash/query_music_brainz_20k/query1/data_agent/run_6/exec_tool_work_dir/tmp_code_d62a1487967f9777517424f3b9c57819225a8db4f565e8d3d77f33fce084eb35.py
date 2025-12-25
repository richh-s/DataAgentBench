code = """import json
import pandas as pd

tracks_data = locals()['var_function-call-5550198362541354546']
track_ids = [track['track_id'] for track in tracks_data]

print("__RESULT__:")
print(json.dumps(track_ids))"""

env_args = {'var_function-call-5550198362541354546': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}]}

exec(code, env_args)
