code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-8471687202024638385'], 'r') as f:
    tracks = pd.DataFrame(json.load(f))
with open(locals()['var_function-call-8471687202024637006'], 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['total_revenue'] = pd.to_numeric(sales['total_revenue'])
df = pd.merge(tracks, sales, on='track_id')

# Helper for searching
def search(term):
    term = term.lower()
    mask = df['title'].str.lower().str.contains(term, na=False) | \
           df['artist'].str.lower().str.contains(term, na=False)
    return df[mask][['track_id', 'title', 'artist', 'total_revenue']]

print("__RESULT__:")
print(json.dumps({
    "fischerspooner": json.loads(search("fischerspooner").to_json(orient='records')),
    "emerge": json.loads(search("emerge").to_json(orient='records')),
    "syb": json.loads(search("syb").to_json(orient='records')),
    "ske": json.loads(search("ske").to_json(orient='records'))
}))"""

env_args = {'var_function-call-10791029874110747991': [{'COUNT(*)': '19375'}], 'var_function-call-10791029874110750228': [{'count(DISTINCT track_id)': '19375'}], 'var_function-call-8471687202024638385': 'file_storage/function-call-8471687202024638385.json', 'var_function-call-8471687202024637006': 'file_storage/function-call-8471687202024637006.json', 'var_function-call-14530195528525198333': [{'norm_artist': 'unknown', 'norm_title': '', 'total_revenue': 45147.94}, {'norm_artist': '', 'norm_title': '', 'total_revenue': 21799.12}, {'norm_artist': 'unknown', 'norm_title': 'none', 'total_revenue': 14647.52}, {'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'total_revenue': 6665.27}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'total_revenue': 6611.56}, {'norm_artist': 'echolyn', 'norm_title': 'letters a short essay', 'total_revenue': 6280.0}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'total_revenue': 6259.3}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'total_revenue': 6125.34}, {'norm_artist': 'neil biggin', 'norm_title': 'chile', 'total_revenue': 6008.71}], 'var_function-call-7101025515263731803': {'top_valid': [{'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'total_revenue': 6665.27}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'total_revenue': 6611.56}, {'norm_artist': 'echolyn', 'norm_title': 'letters a short essay', 'total_revenue': 6280.0}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'total_revenue': 6259.3}], 'junk_sample': [{'title': '007', 'artist': '[unknown]', 'norm_title': '007', 'norm_artist': 'unknown', 'total_revenue': 1259.27}, {'title': 'None', 'artist': 'Anathema', 'norm_title': 'none', 'norm_artist': 'anathema', 'total_revenue': 470.97}, {'title': '00-1', 'artist': 'None', 'norm_title': '1', 'norm_artist': 'unknown', 'total_revenue': 939.31}, {'title': '011- ', 'artist': '   ', 'norm_title': '', 'norm_artist': '', 'total_revenue': 283.95}, {'title': 'CharlyGarcíaNobombardeenBuenosAires', 'artist': 'None', 'norm_title': 'charlygarcíanobombardeenbuenosaires', 'norm_artist': 'unknown', 'total_revenue': 397.64}, {'title': '012-Lullabye', 'artist': 'None', 'norm_title': 'lullabye', 'norm_artist': 'unknown', 'total_revenue': 806.11}, {'title': 'None', 'artist': 'Stephan Sechi', 'norm_title': 'none', 'norm_artist': 'stephan sechi', 'total_revenue': 1156.28}, {'title': 'Red Chips', 'artist': 'None', 'norm_title': 'red chips', 'norm_artist': 'unknown', 'total_revenue': 880.65}, {'title': '***', 'artist': 'Wind Hearse', 'norm_title': '', 'norm_artist': 'wind hearse', 'total_revenue': 1486.9}, {'title': '011- ', 'artist': 'None', 'norm_title': '', 'norm_artist': 'unknown', 'total_revenue': 1021.46}], 'junk_stats': {'count': 545, 'total_revenue': 468466.16000000003}}}

exec(code, env_args)
