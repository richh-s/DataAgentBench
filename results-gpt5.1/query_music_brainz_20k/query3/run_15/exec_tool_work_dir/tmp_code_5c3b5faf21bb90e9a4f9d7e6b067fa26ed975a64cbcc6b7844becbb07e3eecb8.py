code = """import json, pandas as pd
from pathlib import Path

# Load full data from files
tracks_path = Path(var_call_TghkkXGMQNHPYVkXVRMv4KUe)
sales_path = Path(var_call_4RudakJm41zTxjUgXEH78RdW)

with tracks_path.open() as f:
    tracks = json.load(f)
with sales_path.open() as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize title/artist/album for fuzzy deduping
for col in ["title", "artist", "album"]:
    tracks_df[col] = tracks_df[col].fillna("").astype(str).str.strip().str.lower()

# Create a simple canonical key using title + artist + album
tracks_df["canon_key"] = (
    tracks_df["title"].str.replace(r"[^a-z0-9]+", " ", regex=True).str.strip() + "|" +
    tracks_df["artist"].str.replace(r"[^a-z0-9]+", " ", regex=True).str.strip() + "|" +
    tracks_df["album"].str.replace(r"[^a-z0-9]+", " ", regex=True).str.strip()
)

# Map each track_id to its canonical key
track_id_to_key = tracks_df.set_index("track_id")["canon_key"].to_dict()

# Attach canonical key to sales via track_id
sales_df["canon_key"] = sales_df["track_id"].map(track_id_to_key)

# Aggregate total revenue by canonical track (across all stores and countries)
agg = sales_df.groupby("canon_key", dropna=False)["revenue_usd"].astype(float).sum().reset_index(name="total_revenue_usd")

# Find the canonical track with max revenue
best = agg.sort_values("total_revenue_usd", ascending=False).head(1).iloc[0]

best_key = best["canon_key"]
max_revenue = float(best["total_revenue_usd"])

# Get a representative metadata row for this canonical track
rep = tracks_df[tracks_df["canon_key"] == best_key].iloc[0]

result = {
    "title": rep["title"],
    "artist": rep["artist"],
    "album": rep["album"],
    "year": rep["year"],
    "language": rep["language"],
    "total_revenue_usd": round(max_revenue, 2)
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_TghkkXGMQNHPYVkXVRMv4KUe': 'file_storage/call_TghkkXGMQNHPYVkXVRMv4KUe.json', 'var_call_4RudakJm41zTxjUgXEH78RdW': 'file_storage/call_4RudakJm41zTxjUgXEH78RdW.json', 'var_call_WLq5EPusgwuoImrckZMEerfY': ['tracks'], 'var_call_zRb9G2X2bYwjtKhaYnkn8FG9': ['sales']}

exec(code, env_args)
