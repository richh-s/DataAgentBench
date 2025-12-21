code = """import json, pandas as pd, math
from pathlib import Path

tracks_path = Path(var_call_wHSlgAuUnS1TedJN7kqfmJog)
sales_path = Path(var_call_KtIknATJUMVIjOktUR9ZJZlu)

with tracks_path.open() as f:
    tracks = json.load(f)
with sales_path.open() as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Clean revenue_usd to numeric robustly
import re

def to_float(x):
    if x is None:
        return 0.0
    s = str(x)
    # extract all numbers and dots, then keep last contiguous numeric pattern
    m = re.findall(r"[0-9]+(?:\.[0-9]+)?", s)
    if not m:
        return 0.0
    try:
        return float(m[-1])
    except:
        return 0.0

sales_df["revenue_usd"] = sales_df["revenue_usd"].apply(to_float)

# Normalization for entity resolution

def norm(s):
    if s is None:
        return None
    s = str(s).strip().lower()
    return s if s not in ("none", "", "[unknown]") else None

tracks_df["title_norm"] = tracks_df["title"].apply(norm)
tracks_df["artist_norm"] = tracks_df["artist"].apply(norm)
tracks_df["album_norm"] = tracks_df["album"].apply(norm)

# Build entity key: (title, artist) if both present; if artist missing, use (title, None, album)

def make_key(r):
    if r["title_norm"] is None:
        return (None, None, None)
    if r["artist_norm"] is not None:
        return (r["title_norm"], r["artist_norm"], None)
    return (r["title_norm"], None, r["album_norm"])

tracks_df["entity_key"] = tracks_df.apply(make_key, axis=1)

track_entity = tracks_df.set_index("track_id")["entity_key"].to_dict()

sales_df["track_id"] = sales_df["track_id"].astype(str)
sales_df["entity_key"] = sales_df["track_id"].map(track_entity)

agg = sales_df.groupby("entity_key")["revenue_usd"].sum().reset_index()

max_row = agg.sort_values("revenue_usd", ascending=False).iloc[0]
entity_key = max_row["entity_key"]
max_revenue = float(max_row["revenue_usd"])

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
