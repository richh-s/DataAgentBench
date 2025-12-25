code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-5570592498162877174'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-5570592498162876679'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0.0)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def resolve_song(row):
    artist_raw = str(row['artist']) if row['artist'] is not None else "none"
    title_raw = str(row['title']) if row['title'] is not None else ""
    artist_norm = artist_raw.lower().strip()
    title_norm = title_raw.lower().strip()
    
    if artist_norm in ["none", "[unknown]", "unknown", "null", ""]:
        if " - " in title_norm:
            parts = title_norm.split(" - ", 1)
            artist_norm = parts[0].strip()
            title_norm = parts[1].strip()
        else:
            artist_norm = "unknown_artist"
            
    title_cleaned = re.sub(r'\(.*?\)', '', title_norm)
    title_cleaned = re.sub(r'\[.*?\]', '', title_cleaned)
    title_cleaned = re.split(r'\bfeat\.|\bft\.', title_cleaned)[0]
    
    if " - " in title_cleaned:
        title_cleaned = title_cleaned.split(" - ")[0]
        
    return artist_norm.strip(), title_cleaned.strip()

resolved = merged.apply(resolve_song, axis=1)
merged['clean_artist'] = resolved.apply(lambda x: x[0])
merged['clean_title'] = resolved.apply(lambda x: x[1])

# Filter unknown_artist
unknowns = merged[merged['clean_artist'] == 'unknown_artist'].groupby('clean_title')['total_revenue'].sum().reset_index()
top_unknowns = unknowns.sort_values(by='total_revenue', ascending=False).head(10)

# Get samples for top unknowns
debug_info = {}
for i, row in top_unknowns.iterrows():
    title_key = row['clean_title']
    samples = merged[
        (merged['clean_artist'] == 'unknown_artist') & 
        (merged['clean_title'] == title_key)
    ][['title', 'artist']].head(3).to_dict(orient='records')
    debug_info[title_key] = samples

print("__RESULT__:")
print(json.dumps({"top_unknowns": top_unknowns.to_dict(orient='records'), "debug": debug_info}))"""

env_args = {'var_function-call-5570592498162877174': 'file_storage/function-call-5570592498162877174.json', 'var_function-call-5570592498162876679': 'file_storage/function-call-5570592498162876679.json', 'var_function-call-7904594862415471008': [{'clean_artist': 'unknown_artist', 'clean_title': 'none', 'total_revenue': 14647.52}, {'clean_artist': 'unknown_artist', 'clean_title': '003-', 'total_revenue': 8333.2}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'total_revenue': 7634.02}, {'clean_artist': 'neil biggin', 'clean_title': 'chile', 'total_revenue': 6192.51}, {'clean_artist': 'moonbootica', 'clean_title': 'watt bird', 'total_revenue': 5921.33}, {'clean_artist': 'vrisak generacije', 'clean_title': 'ne veruj', 'total_revenue': 5867.83}, {'clean_artist': 'fischerspooner', 'clean_title': 'emerge', 'total_revenue': 5746.85}, {'clean_artist': 'guts pie earshot', 'clean_title': 'travel', 'total_revenue': 5674.44}, {'clean_artist': 'atb', 'clean_title': 'let u go', 'total_revenue': 5624.17}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'total_revenue': 5584.02}], 'var_function-call-9735090008789167404': {'top_songs': [{'clean_artist': 'unknown_artist', 'clean_title': 'none', 'total_revenue': 14647.52}, {'clean_artist': 'unknown_artist', 'clean_title': '003-', 'total_revenue': 8333.2}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'total_revenue': 7634.02}, {'clean_artist': 'neil biggin', 'clean_title': 'chile', 'total_revenue': 6192.51}, {'clean_artist': 'moonbootica', 'clean_title': 'watt bird', 'total_revenue': 5921.33}, {'clean_artist': 'vrisak generacije', 'clean_title': 'ne veruj', 'total_revenue': 5867.829999999999}, {'clean_artist': 'fischerspooner', 'clean_title': 'emerge', 'total_revenue': 5746.85}, {'clean_artist': 'guts pie earshot', 'clean_title': 'travel', 'total_revenue': 5674.4400000000005}, {'clean_artist': 'atb', 'clean_title': 'let u go', 'total_revenue': 5624.17}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'total_revenue': 5584.02}], 'debug': {'unknown_artist - none': [{'title': 'None', 'artist': 'None'}, {'title': 'None', 'artist': 'None'}, {'title': 'None', 'artist': 'None'}], 'unknown_artist - 003-': [{'title': '003-', 'artist': 'None'}, {'title': '003-', 'artist': 'None'}, {'title': '003-', 'artist': 'None'}], 'syb van der ploeg - zo gaat het leven aan je voor': [{'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg'}, {'title': 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'artist': 'None'}], 'neil biggin - chile': [{'title': 'Neil Biggin - Chile', 'artist': 'None'}, {'title': 'Chile (Re-Loaded)', 'artist': 'Neil Biggin'}, {'title': 'Chile - Re-Loaded', 'artist': 'Neil Biggin'}], 'moonbootica - watt bird': [{'title': 'Watt Bird - Watt Bird / Break of Light', 'artist': 'Moonbootica'}, {'title': 'Moonbootica - Watt Bird', 'artist': 'None'}, {'title': 'Watt Bird', 'artist': 'Moonbootica'}], 'vrisak generacije - ne veruj': [{'title': 'Ne veruj (Beer Drinkers Revenge)', 'artist': 'Vrisak generacije'}, {'title': 'Ne veruj - Beer Drinkers Revenge', 'artist': 'Vrisak generacije'}, {'title': 'Vrisak generacije - Ne veruj', 'artist': 'None'}], 'fischerspooner - emerge': [{'title': 'Emerge (Dave Clarke remix)', 'artist': 'Fischerspooner'}, {'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner'}, {'title': 'Fischerspooner - Emerge (Dexter remix)', 'artist': 'None'}], 'guts pie earshot - travel': [{'title': 'Guts Pie Earshot - Travel (live)', 'artist': 'None'}, {'title': 'Travel (live) (amparo fugaz)', 'artist': 'Guts Pie Earshot'}, {'title': 'Travel (live) - amparo fugaz', 'artist': 'Guts Pie Earshot'}], 'atb - let u go': [{'title': 'Let U Go (airplay mix) (All the Best)', 'artist': 'ATB'}, {'title': 'Let U Go (Tocadisco Remix) - Electronic House Sensation Vol. 1', 'artist': 'ATB'}, {'title': 'ATB - Let U Go (airplay mix)', 'artist': 'None'}], 'ske - vagga': [{'title': 'Ske - Vagga', 'artist': 'None'}, {'title': 'Vagga - Feelings Are Great', 'artist': 'Ske'}, {'title': 'Vagga (Feelings Are Great)', 'artist': 'Ske'}]}}}

exec(code, env_args)
