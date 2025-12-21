code = """import json, pandas as pd
from pathlib import Path

# Load full data from files
tracks_path = Path(var_call_Ll1HA5Mcvm8xqP0oqEr6FFou)
sales_path = Path(var_call_fHwT97oNiQFesBShx0Rxbv17)

with tracks_path.open() as f:
    tracks = json.load(f)
with sales_path.open() as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize title/artist/album strings for entity resolution
for col in ["title", "artist", "album"]:
    tracks_df[col] = tracks_df[col].astype(str).str.strip().str.lower()

# Create a simple canonical key using title + artist + album
tracks_df["canon_key"] = (
    tracks_df["title"].fillna("") + " | " +
    tracks_df["artist"].fillna("") + " | " +
    tracks_df["album"].fillna("")
)

# Map each track_id to its canonical key
id_to_key = tracks_df.set_index("track_id")["canon_key"].to_dict()

# Add canonical key to sales via track_id
sales_df["track_id"] = sales_df["track_id"].astype(str)
tracks_df["track_id"] = tracks_df["track_id"].astype(str)

id_to_key = tracks_df.set_index("track_id")["canon_key"].to_dict()
sales_df["canon_key"] = sales_df["track_id"].map(id_to_key)

# Aggregate total revenue per canonical track (across all stores & countries)
revenue_per_track = sales_df.groupby("canon_key")["revenue_usd"].apply(lambda x: x.astype(float).sum()).reset_index()

# Find the canonical track with maximum revenue
max_row = revenue_per_track.sort_values("revenue_usd", ascending=False).iloc[0]
max_key = max_row["canon_key"]
max_revenue = float(max_row["revenue_usd"])

# Decode canonical key back to representative title/artist/album from tracks_df
rep = tracks_df[tracks_df["canon_key"] == max_key].iloc[0]
result = {
    "title": rep["title"],
    "artist": rep["artist"],
    "album": rep["album"],
    "total_revenue_usd": round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Ll1HA5Mcvm8xqP0oqEr6FFou': 'file_storage/call_Ll1HA5Mcvm8xqP0oqEr6FFou.json', 'var_call_fHwT97oNiQFesBShx0Rxbv17': 'file_storage/call_fHwT97oNiQFesBShx0Rxbv17.json', 'var_call_Gmual9X7tk9xftog1ynSqcny': ['tracks'], 'var_call_4xW5onhgVe4PKzEkoGKPzdMy': ['sales']}

exec(code, env_args)
