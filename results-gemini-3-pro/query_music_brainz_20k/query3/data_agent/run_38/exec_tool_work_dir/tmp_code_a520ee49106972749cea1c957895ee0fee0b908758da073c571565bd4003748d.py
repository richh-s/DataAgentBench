code = """import json

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
    key = f"{normalize(artist)}|{normalize(title)}"
    track_map[tid] = key

entity_revenue = {}
for s in sales_data:
    tid = s['track_id']
    rev = float(s['total_revenue']) if s['total_revenue'] else 0.0
    if tid in track_map:
        key = track_map[tid]
        entity_revenue[key] = entity_revenue.get(key, 0) + rev

# Check variants for top artists
top_artists = ["richmatteson", "sybvanderploeg", "lukebryan", "kerstingier", "damianmarley"]
variants = {}

for k, rev in entity_revenue.items():
    for artist_key in top_artists:
        if k.startswith(artist_key):
            if artist_key not in variants:
                variants[artist_key] = []
            variants[artist_key].append((k, rev))

print("__RESULT__:")
print(json.dumps(variants))"""

env_args = {'var_function-call-3828468449816819381': 'file_storage/function-call-3828468449816819381.json', 'var_function-call-8657562732755232343': 'file_storage/function-call-8657562732755232343.json', 'var_function-call-11634248558502887746': {'title': '"Аркан" (цимбали, скрипка, дводенцівка, бубен) (Космацькі музики - Етнічна музика України)', 'artist': 'Космацькі музики', 'total_revenue_usd': 219645.05000000005, 'key': '|'}, 'var_function-call-13096650854876462206': [{'title': '   - .  ', 'artist': ' ', 'revenue': 17139.25, 'key': '|'}, {'title': '004-"" (, , , )', 'artist': ' ', 'revenue': 7271.32, 'key': '|004'}, {'title': '003-,  ', 'artist': '', 'revenue': 7090.130000000001, 'key': '|003'}, {'title': '00-1', 'artist': '', 'revenue': 6283.24, 'key': '|001'}, {'title': '005-    ', 'artist': ' ', 'revenue': 6155.29, 'key': '|005'}], 'var_function-call-2227425521675858518': {'top_20': [{'title': '   - .  ', 'artist': ' ', 'revenue': 17139.25, 'key': '|'}, {'title': '004-"" (, , , )', 'artist': ' ', 'revenue': 7271.32, 'key': '|004'}, {'title': '003-,  ', 'artist': '', 'revenue': 7090.130000000001, 'key': '|003'}, {'title': '00-1', 'artist': '', 'revenue': 6283.24, 'key': '|001'}, {'title': '005-    ', 'artist': ' ', 'revenue': 6155.29, 'key': '|005'}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34, 'key': 'richmatteson|groovey'}, {'title': '009-  ', 'artist': ' ', 'revenue': 5045.700000000001, 'key': '|009'}, {'title': '002-', 'artist': ' ', 'revenue': 5013.4400000000005, 'key': '|002'}, {'title': '010-', 'artist': ' ', 'revenue': 4734.360000000001, 'key': '|010'}, {'title': '012-', 'artist': ' ', 'revenue': 4641.08, 'key': '|012'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue': 4132.27, 'key': 'sybvanderploeg|zogaathetlevenaanjevoorhillichfjoerheiligvuur'}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 4110.55, 'key': 'lukebryan|allmyfriendssayalbumversion'}, {'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'revenue': 4091.12, 'key': 'kerstingier|kapitel01'}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 4004.4199999999996, 'key': 'damianmarley|beautifulinstrumental'}, {'title': 'The Story of Your Life', 'artist': 'Matthew Barber', 'revenue': 3962.9700000000003, 'key': 'matthewbarber|thestoryofyourlife'}, {'title': '006- ', 'artist': ' ', 'revenue': 3946.78, 'key': '|006'}, {'title': 'Thousand Finger Man - Salsoul 30th', 'artist': 'Candido', 'revenue': 3934.83, 'key': 'candido|thousandfingermansalsoul30th'}, {'title': 'A Wand\'ring Minstrel I, From "The Mikado"', 'artist': 'Sir William Gilbert & Sir Arthur Sullivan', 'revenue': 3877.4300000000003, 'key': 'sirwilliamgilbertandsirarthursullivan|awandringminstrelifromthemikado'}, {'title': 'Fret One (Grow Old) - Inside Your Wave', 'artist': 'Ugly Winner', 'revenue': 3844.0899999999997, 'key': 'uglywinner|fretonegrowoldinsideyourwave'}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4, 'key': 'russballard|thefirestillburns'}], 'debug_info': {'260': {'original': {'track_id': '260', 'source_id': '3', 'source_track_id': '60806713MB-01', 'title': 'On the Stairs - The Killer Elite', 'artist': 'Jerry Fielding', 'album': 'None', 'year': 'None', 'length': '2.35', 'language': 'English'}, 'mapped_key': 'jerryfielding|onthestairsthekillerelite', 'display': {'title': 'On the Stairs - The Killer Elite', 'artist': 'Jerry Fielding', 'len': 46}}, '1216': {'original': {'track_id': '1216', 'source_id': '2', 'source_track_id': 'MBox43952632-HH', 'title': 'Lemon D - Jah Love (VIP Remix)', 'artist': 'None', 'album': 'Jungle Renegades Vol. 2', 'year': 'None', 'length': 'None', 'language': 'English'}, 'mapped_key': 'lemond|jahlovevipremix', 'display': {'title': 'Jah Love (VIP Remix)', 'artist': 'Lemon D', 'len': 27}}, '2029': {'original': {'track_id': '2029', 'source_id': '2', 'source_track_id': 'MBox23963122-HH', 'title': "Bunny Sigler - Girl Don't Make Me Wait", 'artist': 'None', 'album': "Girl Don't Make Me Wait / Always in the Wrong Place (At the Wrong Time)", 'year': '66', 'length': 'None', 'language': 'English'}, 'mapped_key': 'bunnysigler|girldontmakemewait', 'display': {'title': "Girl Don't Make Me Wait", 'artist': 'Bunny Sigler', 'len': 35}}, '2780': {'original': {'track_id': '2780', 'source_id': '4', 'source_track_id': '226990-A035', 'title': '005-Just Stay', 'artist': 'Little Scout', 'album': 'Different in the Distance (2009)', 'year': 'None', 'length': '4m 14sec', 'language': 'Engg.'}, 'mapped_key': 'littlescout|005juststay', 'display': {'title': '005-Just Stay', 'artist': 'Little Scout', 'len': 25}}}}, 'var_function-call-4707951880112769144': {'top_valid': [{'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34, 'key': 'richmatteson|groovey'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue': 4132.27, 'key': 'sybvanderploeg|zogaathetlevenaanjevoorhillichfjoerheiligvuur'}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 4110.55, 'key': 'lukebryan|allmyfriendssayalbumversion'}, {'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'revenue': 4091.12, 'key': 'kerstingier|kapitel01'}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 4004.4199999999996, 'key': 'damianmarley|beautifulinstrumental'}], 'top_empty_artist': [{'title': 'unknown', 'artist': '', 'revenue': 3218.35, 'key': '|unknown'}, {'title': 'n.a.', 'artist': '', 'revenue': 2589.62, 'key': '|na'}, {'title': "006-Don't Want Fight", 'artist': '', 'revenue': 2212.4700000000003, 'key': '|006dontwantfight'}, {'title': '012-ONLY YOU', 'artist': '', 'revenue': 2029.8, 'key': '|012onlyyou'}, {'title': "009-L'espoir ", 'artist': '', 'revenue': 1833.4199999999996, 'key': '|009lespoir'}]}}

exec(code, env_args)
