code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-4676097286613530552'], 'r') as f:
    tracks_data = json.load(f)

df_tracks = pd.DataFrame(tracks_data)

# Search for variants
ske_tracks = df_tracks[df_tracks['artist'].str.lower().str.contains('ske', na=False) & df_tracks['title'].str.lower().str.contains('vagga', na=False)]
syb_tracks = df_tracks[df_tracks['artist'].str.lower().str.contains('syb', na=False) & df_tracks['title'].str.lower().str.contains('zo gaat', na=False)]

print("__RESULT__:")
print(json.dumps({
    "ske_tracks": ske_tracks[['track_id', 'title', 'artist']].to_dict(orient='records'),
    "syb_tracks": syb_tracks[['track_id', 'title', 'artist']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-18223064204633629849': 'file_storage/function-call-18223064204633629849.json', 'var_function-call-4676097286613530552': 'file_storage/function-call-4676097286613530552.json', 'var_function-call-163489723723416212': [{'clean_artist': 'unknown', 'clean_title': '', 'revenue_usd': 43888.21}, {'clean_artist': '', 'clean_title': '', 'revenue_usd': 19489.71}, {'clean_artist': 'unknown', 'clean_title': 'none', 'revenue_usd': 14647.52}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'revenue_usd': 5158.72}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'revenue_usd': 5152.0}, {'clean_artist': 'fischerspooner', 'clean_title': 'emerge', 'revenue_usd': 5054.81}, {'clean_artist': 'guts pie earshot', 'clean_title': 'travel', 'revenue_usd': 4933.9}, {'clean_artist': 'scott walker', 'clean_title': 'stormy', 'revenue_usd': 4677.15}, {'clean_artist': 'neil biggin', 'clean_title': 'chile', 'revenue_usd': 4676.22}, {'clean_artist': 'vrisak generacije', 'clean_title': 'ne veruj', 'revenue_usd': 4667.12}], 'var_function-call-15271443817704179144': [{'artist': 'Syb van der Ploeg', 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'revenue_usd': 5158.72}, {'artist': 'Ske', 'title': '011-Vagga', 'clean_artist': 'ske', 'clean_title': 'vagga', 'revenue_usd': 5152.0}, {'artist': 'Fischerspooner', 'title': 'Emerge (Dave Clarke remix)', 'clean_artist': 'fischerspooner', 'clean_title': 'emerge', 'revenue_usd': 5054.81}, {'artist': 'Guts Pie Earshot', 'title': 'Travel (live) (amparo fugaz)', 'clean_artist': 'guts pie earshot', 'clean_title': 'travel', 'revenue_usd': 4933.9}, {'artist': 'Scott Walker', 'title': 'Stormy (Scott: The Collection 1967-1970)', 'clean_artist': 'scott walker', 'clean_title': 'stormy', 'revenue_usd': 4677.15}]}

exec(code, env_args)
