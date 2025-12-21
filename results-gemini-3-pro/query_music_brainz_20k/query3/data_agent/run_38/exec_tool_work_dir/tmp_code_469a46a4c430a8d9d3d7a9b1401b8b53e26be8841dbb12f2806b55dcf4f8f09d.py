code = """import json
import re

with open(locals()['var_function-call-3828468449816819381'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-8657562732755232343'], 'r') as f:
    tracks_data = json.load(f)

def normalize_text(s):
    if not s: return ""
    s = str(s).lower()
    # Remove text in parens/brackets
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\[.*?\]', '', s)
    # Remove leading numbers (track nums)
    s = re.sub(r'^\d+[\s.-]+', '', s)
    # Remove punctuation/symbols, keep alphanumeric
    s = "".join(c for c in s if c.isalnum())
    return s

track_map = {}
entity_display = {} 

for t in tracks_data:
    tid = t['track_id']
    title = t['title'] if t['title'] != 'None' else ''
    artist = t['artist'] if t['artist'] != 'None' else ''
    
    # Fix missing artist
    if artist.lower() in ['[unknown]', 'unknown', '', 'none']:
        artist = ''
        if ' - ' in title:
            parts = title.split(' - ', 1)
            if parts[0].strip() and parts[1].strip():
                artist = parts[0].strip()
                title = parts[1].strip()

    n_artist = normalize_text(artist)
    n_title = normalize_text(title)
    
    # Skip if title becomes empty (e.g. only numbers or parens)
    if not n_title:
        # Fallback to simple normalization if aggressive killed it
        n_title = "".join(c for c in title.lower() if c.isalnum())
    
    key = f"{n_artist}|{n_title}"
    track_map[tid] = key
    
    # Keep best display title (longest, but prefer one without leading numbers if possible?)
    # Just longest is a good proxy for "most complete"
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

sorted_entities = sorted(entity_revenue.items(), key=lambda x: x[1], reverse=True)

results = []
for k, rev in sorted_entities[:10]:
    info = entity_display[k]
    results.append({
        'title': info['title'],
        'artist': info['artist'],
        'revenue': rev,
        'key': k
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3828468449816819381': 'file_storage/function-call-3828468449816819381.json', 'var_function-call-8657562732755232343': 'file_storage/function-call-8657562732755232343.json', 'var_function-call-11634248558502887746': {'title': '"Аркан" (цимбали, скрипка, дводенцівка, бубен) (Космацькі музики - Етнічна музика України)', 'artist': 'Космацькі музики', 'total_revenue_usd': 219645.05000000005, 'key': '|'}, 'var_function-call-13096650854876462206': [{'title': '   - .  ', 'artist': ' ', 'revenue': 17139.25, 'key': '|'}, {'title': '004-"" (, , , )', 'artist': ' ', 'revenue': 7271.32, 'key': '|004'}, {'title': '003-,  ', 'artist': '', 'revenue': 7090.130000000001, 'key': '|003'}, {'title': '00-1', 'artist': '', 'revenue': 6283.24, 'key': '|001'}, {'title': '005-    ', 'artist': ' ', 'revenue': 6155.29, 'key': '|005'}], 'var_function-call-2227425521675858518': {'top_20': [{'title': '   - .  ', 'artist': ' ', 'revenue': 17139.25, 'key': '|'}, {'title': '004-"" (, , , )', 'artist': ' ', 'revenue': 7271.32, 'key': '|004'}, {'title': '003-,  ', 'artist': '', 'revenue': 7090.130000000001, 'key': '|003'}, {'title': '00-1', 'artist': '', 'revenue': 6283.24, 'key': '|001'}, {'title': '005-    ', 'artist': ' ', 'revenue': 6155.29, 'key': '|005'}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34, 'key': 'richmatteson|groovey'}, {'title': '009-  ', 'artist': ' ', 'revenue': 5045.700000000001, 'key': '|009'}, {'title': '002-', 'artist': ' ', 'revenue': 5013.4400000000005, 'key': '|002'}, {'title': '010-', 'artist': ' ', 'revenue': 4734.360000000001, 'key': '|010'}, {'title': '012-', 'artist': ' ', 'revenue': 4641.08, 'key': '|012'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue': 4132.27, 'key': 'sybvanderploeg|zogaathetlevenaanjevoorhillichfjoerheiligvuur'}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 4110.55, 'key': 'lukebryan|allmyfriendssayalbumversion'}, {'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'revenue': 4091.12, 'key': 'kerstingier|kapitel01'}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 4004.4199999999996, 'key': 'damianmarley|beautifulinstrumental'}, {'title': 'The Story of Your Life', 'artist': 'Matthew Barber', 'revenue': 3962.9700000000003, 'key': 'matthewbarber|thestoryofyourlife'}, {'title': '006- ', 'artist': ' ', 'revenue': 3946.78, 'key': '|006'}, {'title': 'Thousand Finger Man - Salsoul 30th', 'artist': 'Candido', 'revenue': 3934.83, 'key': 'candido|thousandfingermansalsoul30th'}, {'title': 'A Wand\'ring Minstrel I, From "The Mikado"', 'artist': 'Sir William Gilbert & Sir Arthur Sullivan', 'revenue': 3877.4300000000003, 'key': 'sirwilliamgilbertandsirarthursullivan|awandringminstrelifromthemikado'}, {'title': 'Fret One (Grow Old) - Inside Your Wave', 'artist': 'Ugly Winner', 'revenue': 3844.0899999999997, 'key': 'uglywinner|fretonegrowoldinsideyourwave'}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4, 'key': 'russballard|thefirestillburns'}], 'debug_info': {'260': {'original': {'track_id': '260', 'source_id': '3', 'source_track_id': '60806713MB-01', 'title': 'On the Stairs - The Killer Elite', 'artist': 'Jerry Fielding', 'album': 'None', 'year': 'None', 'length': '2.35', 'language': 'English'}, 'mapped_key': 'jerryfielding|onthestairsthekillerelite', 'display': {'title': 'On the Stairs - The Killer Elite', 'artist': 'Jerry Fielding', 'len': 46}}, '1216': {'original': {'track_id': '1216', 'source_id': '2', 'source_track_id': 'MBox43952632-HH', 'title': 'Lemon D - Jah Love (VIP Remix)', 'artist': 'None', 'album': 'Jungle Renegades Vol. 2', 'year': 'None', 'length': 'None', 'language': 'English'}, 'mapped_key': 'lemond|jahlovevipremix', 'display': {'title': 'Jah Love (VIP Remix)', 'artist': 'Lemon D', 'len': 27}}, '2029': {'original': {'track_id': '2029', 'source_id': '2', 'source_track_id': 'MBox23963122-HH', 'title': "Bunny Sigler - Girl Don't Make Me Wait", 'artist': 'None', 'album': "Girl Don't Make Me Wait / Always in the Wrong Place (At the Wrong Time)", 'year': '66', 'length': 'None', 'language': 'English'}, 'mapped_key': 'bunnysigler|girldontmakemewait', 'display': {'title': "Girl Don't Make Me Wait", 'artist': 'Bunny Sigler', 'len': 35}}, '2780': {'original': {'track_id': '2780', 'source_id': '4', 'source_track_id': '226990-A035', 'title': '005-Just Stay', 'artist': 'Little Scout', 'album': 'Different in the Distance (2009)', 'year': 'None', 'length': '4m 14sec', 'language': 'Engg.'}, 'mapped_key': 'littlescout|005juststay', 'display': {'title': '005-Just Stay', 'artist': 'Little Scout', 'len': 25}}}}, 'var_function-call-4707951880112769144': {'top_valid': [{'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34, 'key': 'richmatteson|groovey'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue': 4132.27, 'key': 'sybvanderploeg|zogaathetlevenaanjevoorhillichfjoerheiligvuur'}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 4110.55, 'key': 'lukebryan|allmyfriendssayalbumversion'}, {'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'revenue': 4091.12, 'key': 'kerstingier|kapitel01'}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 4004.4199999999996, 'key': 'damianmarley|beautifulinstrumental'}], 'top_empty_artist': [{'title': 'unknown', 'artist': '', 'revenue': 3218.35, 'key': '|unknown'}, {'title': 'n.a.', 'artist': '', 'revenue': 2589.62, 'key': '|na'}, {'title': "006-Don't Want Fight", 'artist': '', 'revenue': 2212.4700000000003, 'key': '|006dontwantfight'}, {'title': '012-ONLY YOU', 'artist': '', 'revenue': 2029.8, 'key': '|012onlyyou'}, {'title': "009-L'espoir ", 'artist': '', 'revenue': 1833.4199999999996, 'key': '|009lespoir'}]}, 'var_function-call-2773907141779860492': {'lukebryan': [['lukebryan|allmyfriendssayalbumversion', 4110.55], ['lukebryan|002allmyfriendssayalbumversion', 1070.38]], 'damianmarley': [['damianmarley|beautifulinstrumental', 4004.4199999999996]], 'kerstingier': [['kerstingier|kapitel01', 4091.12], ['kerstingier|kapitel35lügendievonherzenkommenfeatnarratormirjabös', 1437.87], ['kerstingier|lugendievonherzenkommenfeatnarratormirjabos2008', 641.26], ['kerstingier|kapitel01lügendievonherzenkommenfeatnarratormirjabös', 492.78]], 'richmatteson': [['richmatteson|groovey', 5417.34], ['richmatteson|006groovey', 251.16]], 'sybvanderploeg': [['sybvanderploeg|zogaathetlevenaanjevoorhillichfjoerheiligvuur', 4132.27], ['sybvanderploeg|006zogaathetlevenaanjevoor', 1379.6699999999998], ['sybvanderploeg|zogaathetlevenaanjevoor', 3501.75]]}}

exec(code, env_args)
