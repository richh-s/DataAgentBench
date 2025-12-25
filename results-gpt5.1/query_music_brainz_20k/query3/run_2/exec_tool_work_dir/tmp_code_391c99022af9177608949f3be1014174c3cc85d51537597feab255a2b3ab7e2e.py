code = """import json, pandas as pd
from pathlib import Path

# Load full datasets
tracks_path = Path(var_call_wHSlgAuUnS1TedJN7kqfmJog)
sales_path = Path(var_call_KtIknATJUMVIjOktUR9ZJZlu)

with tracks_path.open() as f:
    tracks = json.load(f)
with sales_path.open() as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning
def norm(s):
    if s is None:
        return None
    s = str(s).strip().lower()
    return s if s != "none" and s != "" and s != "[unknown]" else None

tracks_df["title_norm"] = tracks_df["title"].apply(norm)
tracks_df["artist_norm"] = tracks_df["artist"].apply(norm)
tracks_df["album_norm"] = tracks_df["album"].apply(norm)

# Canonical key for entity resolution: use (title, artist) when available; else include album
tracks_df["entity_key"] = tracks_df.apply(
    lambda r: (
        r["title_norm"],
        r["artist_norm"],
        r["album_norm"] if r["artist_norm"] is None else None
    ), axis=1
)

# Map each track_id to its entity_key
track_entity = tracks_df.set_index("track_id")["entity_key"].to_dict()

# Attach entity_key to sales
sales_df["track_id"] = sales_df["track_id"].astype(str)
sales_df["entity_key"] = sales_df["track_id"].map(track_entity)

# Aggregate revenue by entity_key
agg = sales_df.groupby("entity_key")["revenue_usd"].sum().reset_index()

# revenue_usd may be strings; convert
agg["revenue_usd"] = agg["revenue_usd"].astype(float)

# Find max
max_row = agg.sort_values("revenue_usd", ascending=False).iloc[0]
entity_key = max_row["entity_key"]
max_revenue = float(max_row["revenue_usd"])

# Pick a representative track for reporting (first with that entity_key)
rep = tracks_df[tracks_df["entity_key"] == entity_key].iloc[0]

answer = {
    "title": rep["title"],
    "artist": rep["artist"],
    "album": rep["album"],
    "year": rep["year"],
    "total_revenue_usd": round(max_revenue, 2)
}

result = json.dumps(answer)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wHSlgAuUnS1TedJN7kqfmJog': 'file_storage/call_wHSlgAuUnS1TedJN7kqfmJog.json', 'var_call_KtIknATJUMVIjOktUR9ZJZlu': 'file_storage/call_KtIknATJUMVIjOktUR9ZJZlu.json', 'var_call_xET5ReYKrLRtfbcHCy7BUNHo': 'placeholder'}

exec(code, env_args)
