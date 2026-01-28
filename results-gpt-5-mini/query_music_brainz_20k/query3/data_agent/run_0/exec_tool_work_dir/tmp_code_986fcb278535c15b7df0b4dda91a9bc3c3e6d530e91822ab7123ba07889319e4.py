code = """import json
import re
from collections import Counter

# Load data from storage files
tracks = json.load(open(var_call_uA0nVtVTUMmK6bTCIGa9nKKG, 'r'))
sales = json.load(open(var_call_R8BiFVpORnqPzyIOz1vVLqdZ, 'r'))

# Helper functions
def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip().lower()
    # remove contents in parentheses or brackets
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # replace common separators with space
    s = re.sub(r"[-_\/:]+", " ", s)
    # remove non-alphanumeric (keep spaces)
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Preprocess tracks: try to extract artist from title if artist missing and title has pattern 'Artist - Title'
for t in tracks:
    title = t.get('title') or ''
    artist = t.get('artist') or ''
    if isinstance(artist, str) and artist.strip().lower() in ('none', '[unknown]', '', '   '):
        if isinstance(title, str) and ' - ' in title:
            parts = title.split(' - ', 1)
            left = parts[0].strip()
            right = parts[1].strip()
            if left and right:
                t['artist'] = left
                t['title'] = right

# Build mapping from track_id to normalized entity key
trackid_to_entity = {}
entity_to_tracks = {}
for t in tracks:
    tid = str(t.get('track_id'))
    title = t.get('title') or ''
    artist = t.get('artist') or ''
    norm_title = normalize_text(title)
    norm_artist = normalize_text(artist)
    # If artist missing, include album/year to help grouping
    if not norm_artist:
        album = t.get('album') or ''
        year = t.get('year') or ''
        norm_album = normalize_text(album)
        norm_year = normalize_text(year)
        key = f"{norm_title}||{norm_artist}||{norm_album}||{norm_year}"
    else:
        key = f"{norm_title}||{norm_artist}"
    trackid_to_entity[tid] = key
    entity_to_tracks.setdefault(key, []).append(t)

# Aggregate revenue by entity
entity_revenue = {}
entity_sales_count = {}
entity_track_ids = {}
for s in sales:
    tid = str(s.get('track_id'))
    revenue = s.get('revenue_usd')
    try:
        rev = float(revenue)
    except:
        # try to clean
        try:
            rev = float(str(revenue).replace(',', '').strip())
        except:
            rev = 0.0
    key = trackid_to_entity.get(tid)
    if key is None:
        # track not found in tracks table; skip
        continue
    entity_revenue[key] = entity_revenue.get(key, 0.0) + rev
    entity_sales_count[key] = entity_sales_count.get(key, 0) + 1
    entity_track_ids.setdefault(key, set()).add(tid)

# Find top entity by revenue
if not entity_revenue:
    result = {"title": None, "artist": None, "total_revenue_usd": 0.0, "track_ids": []}
else:
    top_key = max(entity_revenue.items(), key=lambda x: x[1])[0]
    total_rev = entity_revenue[top_key]
    track_ids = sorted(list(entity_track_ids.get(top_key, [])), key=lambda x: int(x))
    # choose representative title and artist: most common among tracks in this entity
    tracks_in_entity = entity_to_tracks.get(top_key, [])
    titles = [t.get('title') or '' for t in tracks_in_entity]
    artists = [t.get('artist') or '' for t in tracks_in_entity]
    rep_title = Counter(titles).most_common(1)[0][0] if titles else ''
    rep_artist = Counter(artists).most_common(1)[0][0] if artists else ''
    result = {"title": rep_title, "artist": rep_artist, "total_revenue_usd": round(total_rev, 2), "track_ids": track_ids, "num_sales_records": entity_sales_count.get(top_key,0)}

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uA0nVtVTUMmK6bTCIGa9nKKG': 'file_storage/call_uA0nVtVTUMmK6bTCIGa9nKKG.json', 'var_call_R8BiFVpORnqPzyIOz1vVLqdZ': 'file_storage/call_R8BiFVpORnqPzyIOz1vVLqdZ.json'}

exec(code, env_args)
