code = """import json
import re

with open(locals()['var_function-call-3828468449816819381'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-8657562732755232343'], 'r') as f:
    tracks_data = json.load(f)

def normalize(s):
    if s is None:
        return ""
    s = str(s).lower()
    s = s.replace('&', 'and').replace('+', 'and')
    s = "".join(c for c in s if c.isalnum())
    return s

track_map = {}
entity_display = {} 

for t in tracks_data:
    tid = t['track_id']
    title = t['title'] if t['title'] != 'None' else ''
    artist = t['artist'] if t['artist'] != 'None' else ''
    
    if artist.lower() in ['[unknown]', 'unknown', '', 'none']:
        artist = ''
        if ' - ' in title:
            parts = title.split(' - ', 1)
            if parts[0].strip() and parts[1].strip():
                artist = parts[0].strip()
                title = parts[1].strip()

    n_artist = normalize(artist)
    n_title = normalize(title)
    key = f"{n_artist}|{n_title}"
    track_map[tid] = key
    
    current_len = len(title) + len(artist)
    if key not in entity_display or current_len > entity_display[key]['len']:
        entity_display[key] = {'title': title, 'artist': artist, 'len': current_len}

entity_revenue = {}
for s in sales_data:
    tid = s['track_id']
    rev = float(s['total_revenue']) if s['total_revenue'] else 0.0
    if tid in track_map:
        key = track_map[tid]
        entity_revenue[key] = entity_revenue.get(key, 0) + rev

# Separation
valid_results = []
empty_artist_results = []

for k, rev in entity_revenue.items():
    n_artist, n_title = k.split('|')
    info = entity_display[k]
    
    # Filter junk titles
    # If title is just numbers or very short
    if len(n_title) < 2 or n_title.isdigit():
        continue
        
    item = {
        'title': info['title'],
        'artist': info['artist'],
        'revenue': rev,
        'key': k
    }
    
    if n_artist:
        valid_results.append(item)
    else:
        empty_artist_results.append(item)

valid_results.sort(key=lambda x: x['revenue'], reverse=True)
empty_artist_results.sort(key=lambda x: x['revenue'], reverse=True)

print("__RESULT__:")
print(json.dumps({
    'top_valid': valid_results[:5],
    'top_empty_artist': empty_artist_results[:5]
}))"""

env_args = {'var_function-call-3828468449816819381': 'file_storage/function-call-3828468449816819381.json', 'var_function-call-8657562732755232343': 'file_storage/function-call-8657562732755232343.json', 'var_function-call-11634248558502887746': {'title': '"Аркан" (цимбали, скрипка, дводенцівка, бубен) (Космацькі музики - Етнічна музика України)', 'artist': 'Космацькі музики', 'total_revenue_usd': 219645.05000000005, 'key': '|'}, 'var_function-call-13096650854876462206': [{'title': '   - .  ', 'artist': ' ', 'revenue': 17139.25, 'key': '|'}, {'title': '004-"" (, , , )', 'artist': ' ', 'revenue': 7271.32, 'key': '|004'}, {'title': '003-,  ', 'artist': '', 'revenue': 7090.130000000001, 'key': '|003'}, {'title': '00-1', 'artist': '', 'revenue': 6283.24, 'key': '|001'}, {'title': '005-    ', 'artist': ' ', 'revenue': 6155.29, 'key': '|005'}], 'var_function-call-2227425521675858518': {'top_20': [{'title': '   - .  ', 'artist': ' ', 'revenue': 17139.25, 'key': '|'}, {'title': '004-"" (, , , )', 'artist': ' ', 'revenue': 7271.32, 'key': '|004'}, {'title': '003-,  ', 'artist': '', 'revenue': 7090.130000000001, 'key': '|003'}, {'title': '00-1', 'artist': '', 'revenue': 6283.24, 'key': '|001'}, {'title': '005-    ', 'artist': ' ', 'revenue': 6155.29, 'key': '|005'}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34, 'key': 'richmatteson|groovey'}, {'title': '009-  ', 'artist': ' ', 'revenue': 5045.700000000001, 'key': '|009'}, {'title': '002-', 'artist': ' ', 'revenue': 5013.4400000000005, 'key': '|002'}, {'title': '010-', 'artist': ' ', 'revenue': 4734.360000000001, 'key': '|010'}, {'title': '012-', 'artist': ' ', 'revenue': 4641.08, 'key': '|012'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue': 4132.27, 'key': 'sybvanderploeg|zogaathetlevenaanjevoorhillichfjoerheiligvuur'}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 4110.55, 'key': 'lukebryan|allmyfriendssayalbumversion'}, {'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'revenue': 4091.12, 'key': 'kerstingier|kapitel01'}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 4004.4199999999996, 'key': 'damianmarley|beautifulinstrumental'}, {'title': 'The Story of Your Life', 'artist': 'Matthew Barber', 'revenue': 3962.9700000000003, 'key': 'matthewbarber|thestoryofyourlife'}, {'title': '006- ', 'artist': ' ', 'revenue': 3946.78, 'key': '|006'}, {'title': 'Thousand Finger Man - Salsoul 30th', 'artist': 'Candido', 'revenue': 3934.83, 'key': 'candido|thousandfingermansalsoul30th'}, {'title': 'A Wand\'ring Minstrel I, From "The Mikado"', 'artist': 'Sir William Gilbert & Sir Arthur Sullivan', 'revenue': 3877.4300000000003, 'key': 'sirwilliamgilbertandsirarthursullivan|awandringminstrelifromthemikado'}, {'title': 'Fret One (Grow Old) - Inside Your Wave', 'artist': 'Ugly Winner', 'revenue': 3844.0899999999997, 'key': 'uglywinner|fretonegrowoldinsideyourwave'}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4, 'key': 'russballard|thefirestillburns'}], 'debug_info': {'260': {'original': {'track_id': '260', 'source_id': '3', 'source_track_id': '60806713MB-01', 'title': 'On the Stairs - The Killer Elite', 'artist': 'Jerry Fielding', 'album': 'None', 'year': 'None', 'length': '2.35', 'language': 'English'}, 'mapped_key': 'jerryfielding|onthestairsthekillerelite', 'display': {'title': 'On the Stairs - The Killer Elite', 'artist': 'Jerry Fielding', 'len': 46}}, '1216': {'original': {'track_id': '1216', 'source_id': '2', 'source_track_id': 'MBox43952632-HH', 'title': 'Lemon D - Jah Love (VIP Remix)', 'artist': 'None', 'album': 'Jungle Renegades Vol. 2', 'year': 'None', 'length': 'None', 'language': 'English'}, 'mapped_key': 'lemond|jahlovevipremix', 'display': {'title': 'Jah Love (VIP Remix)', 'artist': 'Lemon D', 'len': 27}}, '2029': {'original': {'track_id': '2029', 'source_id': '2', 'source_track_id': 'MBox23963122-HH', 'title': "Bunny Sigler - Girl Don't Make Me Wait", 'artist': 'None', 'album': "Girl Don't Make Me Wait / Always in the Wrong Place (At the Wrong Time)", 'year': '66', 'length': 'None', 'language': 'English'}, 'mapped_key': 'bunnysigler|girldontmakemewait', 'display': {'title': "Girl Don't Make Me Wait", 'artist': 'Bunny Sigler', 'len': 35}}, '2780': {'original': {'track_id': '2780', 'source_id': '4', 'source_track_id': '226990-A035', 'title': '005-Just Stay', 'artist': 'Little Scout', 'album': 'Different in the Distance (2009)', 'year': 'None', 'length': '4m 14sec', 'language': 'Engg.'}, 'mapped_key': 'littlescout|005juststay', 'display': {'title': '005-Just Stay', 'artist': 'Little Scout', 'len': 25}}}}}

exec(code, env_args)
