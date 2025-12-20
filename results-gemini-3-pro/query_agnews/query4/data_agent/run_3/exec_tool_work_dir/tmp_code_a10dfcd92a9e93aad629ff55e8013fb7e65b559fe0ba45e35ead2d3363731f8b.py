code = """import json
import collections
import re

# Load metadata
with open(locals()['var_function-call-7730568976014147704'], 'r') as f:
    metadata_list = json.load(f)

# Load articles chunks
files = [
    locals()['var_function-call-6981073237739771094'],
    locals()['var_function-call-14487700868767090154'],
    locals()['var_function-call-17002506109613203559'],
    locals()['var_function-call-1546648637559739929'],
    locals()['var_function-call-18163362674092779993']
]

articles_map = {}
for file_path in files:
    with open(file_path, 'r') as f:
        chunk = json.load(f)
        for a in chunk:
            aid = str(a.get('article_id', ''))
            title = a.get('title', '')
            desc = a.get('description', '')
            articles_map[aid] = (title + " " + desc).lower()

# Keywords
world_kws = [
    "war", "military", "president", "minister", "official", "government", "united nations", "country", "nuclear", 
    "attack", "peace", "china", "russia", "iran", "iraq", "syria", "korea", "afghanistan", "isis", "terror", 
    "protest", "court", "law", "election", "parliament", "foreign", "international", "security", "treaty", 
    "ambassador", "diplomat", "refugee", "crisis", "bomb", "blast", "kill", "dead", "wound", "police", "shoot", 
    "prime minister", "leader", "state", "troops", "army", "navy", "air force", "rebel", "conflict", "explosion", 
    "strike", "hostage", "sanction", "gaza", "israel", "palestine", "ukraine", "putin", "obama", "bush", "clinton", 
    "yemen", "libya", "egypt", "venezuela", "pakistan", "india", "border", "migrant", "crash", "plane", "disaster", 
    "storm", "hurricane", "typhoon", "earthquake", "tsunami", "politics", "political", "democracy", "human rights", 
    "un", "nato", "eu", "african union", "au", "nation", "global", "usa", "america", "uk", "britain", "france", 
    "germany", "japan", "turkey", "saudi arabia", "sudan", "somalia", "congo", "kenya", "zimbabwe", "greece", "italy", 
    "spain", "brazil", "mexico", "canada", "australia", "vatican", "pope", "boko haram", "taliban", "al qaeda",
    "ebola", "outbreak", "virus", "chancellor", "premier", "secretary", "senate", "congress", "cuba"
]
sports_kws = ["game", "match", "score", "win", "loss", "defeat", "victory", "team", "player", "coach", "season", "league", "champion", "medal", "olympic", "race", "cup", "tournament", "sport", "football", "basketball", "baseball", "soccer", "tennis", "golf", "hockey", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "athlete", "stadium", "rugby", "cricket", "f1", "formula one", "driver", "club", "manager", "quarterback", "touchdown", "goal", "points", "ranking", "title", "gold", "silver", "bronze", "wimbledon", "us open", "super bowl", "world cup"]
business_kws = ["market", "stock", "dow", "nasdaq", "sp500", "economy", "dollar", "euro", "yen", "bank", "fed", "rate", "profit", "earnings", "revenue", "loss", "company", "corp", "inc", "ceo", "merger", "deal", "acquisition", "trade", "oil", "gold", "price", "invest", "share", "business", "industry", "finance", "financial", "wall st", "sales", "retail", "consumer", "inflation", "job", "unemployment", "hiring", "tax", "budget", "deficit", "ipo", "bid", "offer", "bankrupt", "debt", "loan", "mortgage", "fund", "equity", "asset", "imf", "world bank", "gm", "ford", "toyota", "boeing", "airbus", "walmart", "exxon", "chevron", "bp", "shell", "opec"]
scitech_kws = ["technology", "tech", "science", "research", "study", "space", "nasa", "launch", "orbit", "computer", "software", "hardware", "internet", "web", "online", "app", "mobile", "phone", "google", "apple", "microsoft", "facebook", "twitter", "amazon", "ibm", "intel", "chip", "device", "gadget", "cancer", "disease", "health", "gene", "robot", "ai", "artificial intelligence", "biotech", "lab", "scientist", "astronomer", "physicist", "discovery", "planet", "galaxy", "telescope", "mission", "satellite", "broadband", "wireless", "network", "server", "data", "cyber", "hack", "security", "update", "version", "windows", "linux", "android", "ios", "iphone", "ipad", "mac", "pc", "laptop", "tablet", "screen", "pixel", "camera", "video game", "console", "nintendo", "sony", "xbox", "playstation", "mars", "moon", "solar", "climate", "warming", "firefox", "browser", "spam", "blog"]

# Adjust "virus" to potentially be SciTech or World depending on context (e.g. Computer Virus vs Ebola).
# But here I put virus in World (if Ebola) and SciTech. It might double count or pick max.
# Let's remove virus from SciTech to avoid confusion or keep it.
# Actually, I'll count scores.

keywords = {"World": world_kws, "Sports": sports_kws, "Business": business_kws, "Sci_Tech": scitech_kws}

def classify(text):
    scores = {k: 0 for k in keywords}
    words = re.findall(r'\w+', text)
    for w in words:
        for cat, kws in keywords.items():
            if w in kws:
                scores[cat] += 1
    
    # Tie breaking logic
    # If "oil" is present, it's likely Business.
    # If "iraq" is present, it's World.
    # Let's trust the score.
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0: return "Unknown"
    return best_cat

world_counts = collections.defaultdict(int)
total_classified = 0

for m in metadata_list:
    aid = str(m['article_id'])
    region = m['region']
    
    if aid in articles_map:
        text = articles_map[aid]
        cat = classify(text)
        if cat == "World":
            world_counts[region] += 1
        total_classified += 1

sorted_regions = sorted(world_counts.items(), key=lambda x: x[1], reverse=True)
print(f"Total classified: {total_classified}")
print("__RESULT__:")
print(json.dumps(sorted_regions))"""

env_args = {'var_function-call-7730568976014147704': 'file_storage/function-call-7730568976014147704.json', 'var_function-call-17267860317809745023': 'file_storage/function-call-17267860317809745023.json', 'var_function-call-16112416981574014912': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6981073237739771094': 'file_storage/function-call-6981073237739771094.json', 'var_function-call-3205073669013618760': [['Africa', 106], ['South America', 92], ['Asia', 85], ['North America', 79], ['Europe', 76]], 'var_function-call-17108972308054004622': [['Africa', 117], ['South America', 111], ['Asia', 97], ['Europe', 89], ['North America', 89]], 'var_function-call-2586345171542887921': {'Business': 314, 'Sci_Tech': 243, 'Unknown': 140, 'World': 503, 'Sports': 287}, 'var_function-call-1992657977849178575': {'overlap': 1487}, 'var_function-call-3602182154067894502': {'max_meta': 127570, 'max_fetched': 29999}, 'var_function-call-14487700868767090154': [{'article_id': '30000', 'title': 'Kerry Accuses Bush of Hiding the Truth About Iraq', 'description': 'Senator Kerry leveled his charges in a speech prepared for delivery later today before the National Guard Association in Las Vegas.'}, {'article_id': '30001', 'title': 'Things don #39;t go better as Coke #39;s profit warning weighs Dow', 'description': 'A PROFIT warning from Coca-Cola put the skids under US equities yesterday and a Goldman Sachs survey showing softening corporate spending on technology added to the gloomy mood.'}, {'article_id': '30002', 'title': 'Ex-Shell Chairman Challenges Watchdog over Oil Reserves Scandal', 'description': 'The former chairman of oil group Royal Dutch/Shell today challenged the City watchdog over its findings on the companys oil reserves scandal.'}, {'article_id': '30003', 'title': 'Vodafone Peddles New BlackBerry', 'description': 'Research In Motion #39;s BlackBerry 7100v, which sports the company #39;s latest keyboard technology, is being offered exclusively through Vodafone.'}, {'article_id': '30004', 'title': 'shuttle fragment found in Texas', 'description': 'A large piece of space shuttle Columbia debris was found recently in southeast Texas, a NASA official said. The 6-foot-long piece of the crew compartment was discovered two weeks ago '}], 'var_function-call-17002506109613203559': [{'article_id': '60000', 'title': 'BYTE OF THE APPLE', 'description': 'Apple lost one war to Microsoft by not licensing its Mac operating system. It may repeat the error with its iPod and music software.'}, {'article_id': '60001', 'title': 'Child porn fight gets \\$5M', 'description': 'Ontario police forces will get \\$5 million to develop a co-ordinated strategy to fight Internet child pornography, Attorney General Michael Bryant said yesterday.'}, {'article_id': '60002', 'title': 'SpaceShipOne a flight away from claiming \\$10 million X Prize', 'description': 'MOJAVE, Calif. -- SpaceShipOne is one flight away from clinching the Ansari X Prize, a \\$10 million award for the first privately developed manned rocket to reach space twice within 14 days.'}, {'article_id': '60003', 'title': 'Arrest over internet sex claims', 'description': 'Police in America have issued an arrest warrant for a North Yorkshire man who allegedly had sex with a teenager he met in an internet chat room.'}, {'article_id': '60004', 'title': 'Ultima Online: Samurai Empire is Golden', 'description': 'October 13, 2004 - Electronic Arts announced that Ultima Online: Samurai Empire went gold today. The highly-anticipated expansion pack for Ultima Online is on schedule to release on November 2, 2004.'}], 'var_function-call-1546648637559739929': [{'article_id': '90000', 'title': "Davenport's Victory Over Williams May Not Be Enough", 'description': ' LOS ANGELES (Reuters) - Top-ranked Lindsay Davenport pulled  off a stunning 3-6, 7-5, 6-1 win over Serena Williams at the  WTA Tour Championships Saturday, but her battling effort may  still might not be enough to get her into the semifinals.'}, {'article_id': '90001', 'title': 'Do New Drugs Always Have to Cost So Much?', 'description': 'Some economists say the government can reduce pharmaceutical prices by changing how the nation pays for innovation.'}, {'article_id': '90002', 'title': 'A Bond Strategy Once Thought Foolish Now Looks Smart', 'description': 'Despite warnings that interest rates would climb sharply, some risk-averse investors stuck with the bond market in 2004.'}, {'article_id': '90003', 'title': 'Out of the rut at last', 'description': 'NEW YORK: Wall Street has finally broken to the upside after hovering in a narrow range for most of the year, and many analysts are optimistic going into the traditionally strong year-end period.'}, {'article_id': '90004', 'title': 'Novell vs. Microsoft, Again', 'description': 'belmolis writes  quot;As they promised, Novell has filed suit against Microsoft over WordPerfect. Here #39;s the complaint, and here is Microsoft #39;s press release in response.'}], 'var_function-call-18163362674092779993': [{'article_id': '120000', 'title': 'Fears for T N pension after talks', 'description': "Unions representing workers at Turner   Newall say they are 'disappointed' after talks with stricken parent firm Federal Mogul."}, {'article_id': '120001', 'title': 'The Race is On: Second Private Team Sets Launch Date for Human Spaceflight (SPACE.com)', 'description': 'SPACE.com - TORONTO, Canada -- A second\\team of rocketeers competing for the  #36;10 million Ansari X Prize, a contest for\\privately funded suborbital space flight, has officially announced the first\\launch date for its manned rocket.'}, {'article_id': '120002', 'title': 'Ky. Company Wins Grant to Study Peptides (AP)', 'description': 'AP - A company founded by a chemistry researcher at the University of Louisville won a grant to develop a method of producing better peptides, which are short chains of amino acids, the building blocks of proteins.'}, {'article_id': '120003', 'title': 'Prediction Unit Helps Forecast Wildfires (AP)', 'description': "AP - It's barely dawn when Mike Fitzpatrick starts his shift with a blur of colorful maps, figures and endless charts, but already he knows what the day will bring. Lightning will strike in places he expects. Winds will pick up, moist places will dry and flames will roar."}, {'article_id': '120004', 'title': 'Calif. Aims to Limit Farm-Related Smog (AP)', 'description': "AP - Southern California's smog-fighting agency went after emissions of the bovine variety Friday, adopting the nation's first rules to reduce air pollution from dairy cow manure."}]}

exec(code, env_args)
