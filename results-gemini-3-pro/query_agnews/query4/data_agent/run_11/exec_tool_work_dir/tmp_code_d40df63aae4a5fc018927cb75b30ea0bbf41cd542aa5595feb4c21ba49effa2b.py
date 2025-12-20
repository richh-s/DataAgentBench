code = """import json
import re
from collections import Counter

# Load data (variables should be available, but good to be safe if I re-run everything)
with open(locals()['var_function-call-2683070877417335365'], 'r') as f:
    sql_results = json.load(f)

meta_map = {}
for row in sql_results:
    try:
        aid = int(row['article_id'])
        meta_map[aid] = row['region']
    except:
        pass

with open(locals()['var_function-call-12084950105935105518'], 'r') as f:
    articles = json.load(f)

# Improved Keywords
# Specific phrases for exclusion/boosting
phrases = {
    "Sports": ["world cup", "world series", "champions league", "premier league", "grand slam", "super bowl", "olympic games", "red sox", "white sox", "yankees", "manchester united", "real madrid", "arsenal", "chelsea", "liverpool", "formula one", "tiger woods", "lance armstrong", "us open", "australian open", "french open", "wimbledon", "davis cup", "ryder cup"],
    "Business": ["wall street", "dow jones", "nasdaq", "s&p", "federal reserve", "interest rate", "oil prices", "stock market", "initial public offering", "trade deficit", "mutual fund", "hedge fund", "private equity", "quarterly profit", "net income"],
    "Sci/Tech": ["microsoft", "google", "apple", "intel", "ibm", "oracle", "linux", "windows", "open source", "mobile phone", "digital camera", "video game", "space shuttle", "international space station", "stem cell", "global warming", "climate change"],
    "World": ["united nations", "european union", "middle east", "prime minister", "human rights", "car bomb", "peace talk", "nuclear weapon", "suicide bomber", "security council", "foreign minister", "west bank", "gaza strip", "north korea", "south korea", "al qaeda", "white house", "supreme court"] # White house/Supreme court often World/US Politics
}

keywords = {
    "World": [
        "international", "un", "nation", "diplomacy", "treaty", "peace", "war", "military", 
        "president", "minister", "parliament", "foreign", "terrorist", "bomb", "attack", 
        "government", "official", "authority", "election", "troops", "hostage", "kill", "blast", 
        "explosion", "crisis", "vote", "poll", "protest", "riot", "party", "border", "security", 
        "council", "refugee", "migration", "syria", "egypt", "libya", "sudan", "yemen", "nigeria", 
        "pakistan", "india", "venezuela", "brazil", "argentina", "mexico", "germany", "france", 
        "uk", "britain", "spain", "italy", "greece", "turkey", "saudi", "isis", "isil", "taliban",
        "jihad", "coup", "sanctions", "embassy", "ambassador", "nato", "baghdad", "kabul", "tehran"
    ],
    "Sports": [
        "sport", "game", "match", "cup", "league", "team", "score", "win", "lose", "olympic", 
        "championship", "football", "baseball", "basketball", "soccer", "tennis", "golf", 
        "athlete", "coach", "medal", "tournament", "player", "season", "club", "nba", "nfl", 
        "mlb", "nhl", "fifa", "run", "race", "title", "final", "victory", "defeat", "boxing", 
        "wrestling", "hockey", "cricket", "rugby", "stadium", "quarterback", "touchdown", "sack",
        "pitcher", "homerun", "goal", "striker", "midfielder", "defender", "goalkeeper"
    ],
    "Business": [
        "business", "market", "stock", "economy", "trade", "money", "deal", "profit", "loss", 
        "bank", "financial", "corporate", "company", "industry", "price", "rate", "investor", 
        "ceo", "merger", "acquisition", "dollar", "euro", "inflation", "earnings", "share", 
        "revenue", "sales", "fed", "exchange", "job", "hiring", "unemployment", "tax", "budget", 
        "deficit", "gdp", "consumer", "retail", "boeing", "airbus", "imf", "wto"
    ],
    "Sci/Tech": [
        "science", "technology", "tech", "computer", "web", "internet", "software", "hardware", 
        "space", "nasa", "study", "research", "medical", "health", "virus", "disease", "cancer", 
        "innovation", "gadget", "phone", "biology", "physics", "astronomy", "scientist", 
        "discovery", "drug", "fda", "online", "digital", "launch", "mission", "satellite", 
        "orbit", "moon", "mars", "robot", "ai", "browser", "server", "database", "wireless",
        "broadband"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    
    # Check phrases first (stronger signal)
    for cat, ph_list in phrases.items():
        for ph in ph_list:
            if ph in text:
                scores[cat] += 5
    
    # Check words
    words = re.findall(r'\w+', text)
    for word in words:
        for cat, kws in keywords.items():
            if word in kws:
                scores[cat] += 1
                
    # Penalty/Adjustments
    # If Sports > 0, "world" (word) should count less for World category
    # Actually, I removed "world" from keywords["World"] to avoid "World Cup" issue.
    # But "world" is a good keyword for actual world news.
    # So I will add it back ONLY if Sports score is low?
    # Or just rely on "international", "nation", etc.
    
    if "world" in words:
        # If looks like sports, ignore 'world'
        if scores["Sports"] < 2:
            scores["World"] += 1
            
    return max(scores, key=scores.get)

# Count
region_cat_counts = {}

for art in articles:
    try:
        aid = int(art['article_id'])
    except:
        continue
        
    if aid in meta_map:
        text = (art.get('title', '') + " " + art.get('description', ''))
        category = classify(text)
        
        r = meta_map[aid]
        if r not in region_cat_counts:
            region_cat_counts[r] = Counter()
        region_cat_counts[r][category] += 1

print("__RESULT__:")
print(json.dumps(region_cat_counts))"""

env_args = {'var_function-call-2683070877417335365': 'file_storage/function-call-2683070877417335365.json', 'var_function-call-7837263819668175178': 6696, 'var_function-call-14907435017980586290': [{'_id': '6944f3d4dccdaaaa57646236', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f3d4dccdaaaa57646237', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f3d4dccdaaaa57646238', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f3d4dccdaaaa57646239', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f3d4dccdaaaa5764623a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4342570047527953099': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-9448599737516148075': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-530398534050118018': 'Done', 'var_function-call-12158221531579383913': {'count': 5, 'is_file': False}, 'var_function-call-12084950105935105518': 'file_storage/function-call-12084950105935105518.json', 'var_function-call-17835602813264065294': {'South America': 600, 'Africa': 587, 'Asia': 570, 'North America': 592, 'Europe': 598}, 'var_function-call-8415515240364671108': {'Europe': {'Sci/Tech': 256, 'Business': 236, 'Sports': 267, 'Unclassified': 226, 'World': 372}, 'South America': {'Business': 215, 'World': 384, 'Sci/Tech': 275, 'Sports': 242, 'Unclassified': 216}, 'Africa': {'Sci/Tech': 234, 'Unclassified': 213, 'World': 374, 'Sports': 277, 'Business': 247}, 'Asia': {'World': 372, 'Sci/Tech': 256, 'Business': 238, 'Unclassified': 198, 'Sports': 269}, 'North America': {'Unclassified': 225, 'Business': 215, 'Sci/Tech': 255, 'World': 367, 'Sports': 267}}, 'var_function-call-4508037185647663153': {'Europe': {'Sci/Tech': 223, 'Business': 231, 'Sports': 266, 'World': 473, 'Unclassified': 164}, 'South America': {'Business': 225, 'World': 471, 'Sci/Tech': 247, 'Sports': 232, 'Unclassified': 157}, 'Africa': {'Sci/Tech': 208, 'Unclassified': 156, 'World': 453, 'Sports': 277, 'Business': 251}, 'Asia': {'World': 479, 'Sci/Tech': 223, 'Business': 231, 'Unclassified': 142, 'Sports': 258}, 'North America': {'Unclassified': 176, 'Business': 220, 'Sci/Tech': 233, 'World': 436, 'Sports': 264}}, 'var_function-call-14012707744819470626': {'Unclassified': ['The Dream Factory Any product, any shape, any size -- manufactured on your desktop! The future is the fabricator. By Bruce Sterling from Wired magazine.', "Radcliffe suffers marathon agony An exhausted Paula Radcliffe fails to finish in Athens as Japan's Mizuki Noguchi wins the women's marathon.", 'Also from this section HBOS has yet to enter the bidding for Abbey National, yet it is already fighting its corner as if in the full intensity of battle.', 'Houllier favourite for Newcastle GERARD HOULLIER was today installed as the early favourite to succeed Sir Bobby Robson as Newcastle United manager. The former Liverpool boss is being tipped to take over with Magpies skipper Alan Shearer, who ', "Indie music label rejects lock-down CDs 'NO copy protection - respect the music' stamped on !K7 discs", 'Q A: Worthington Industries CIO Jonathan Dove on ERP upgrade Worthington Industries CIO Jonathan Dove tells Computerworld that he sees the role of the CIO changing.', 'Cruise in Britian for \'Collateral\' (AP) AP - Tom Cruise mingled with about 3,000 fans at the British premiere of "Collateral," chatting on their cell phones, posing for photos and signing autographs for more than two hours outside a theater in Leicester Square.', "In place of dollars, a cool change  Cash has never been so cool. Usher Raymond IV, the 25-year-old R amp;B singer who has been dubbed the king of pop, launched the Usher Debit MasterCard late last month. The sleek black card, which features the artist's face, has been passed out to concertgoers during his nationwide ''The Truth Tour. quot; The card is also available through a website, ushermc.com.", 'MPAA Revives P-to-P Lawsuit Group is asking the Supreme Court to overturn decision in favor of file-swapping networks.', 'Ogunleye Joins Bears With Eye Toward Sacks (AP) AP - With recorders and cameras rolling, Adewale Ogunleye gave the obligatory pronunciation of his name on his first day with the Chicago Bears.'], 'World': ['Japanese government hopes to allow woman on throne within years &lt;b&gt;...&lt;/b&gt; TOKYO : The Japanese government hopes to make changes to the constitution that will allow a woman to ascend the Chrysanthemum Throne within  quot;several years, quot; a news report said.', 'Thumb twiddling on cybersecurity Congresswoman Zoe Lofgren says bureaucratic miscues continue to hamstring serious government action to combat cyberattacks.', 'Blue Chips Inch Up, Oil Rise Caps Gains US blue-chip stocks rose slightly on Friday as government data showed better-than-expected demand in August for durable goods other than transportation equipment, but climbing oil prices limited gains.', 'G-7 likely won #39;t press China on yuan WASHINGTON (CBS.MW) -- Finance ministers from the world #39;s seven richest nations aren #39;t likely to pressure China on foreign-exchange policy when they meet with Chinese finance officials for the first time as a group in Washington at the end of the week, a ', 'Major powers meet in Egypt on Iraqs future Two-day meeting in Sharm el-Sheikh is to help Iraq emerge from violence, discuss other Mideast issues. By Marc Burleigh - SHARM EL-SHEIKH, Egypt.', "Challenges await ex-general Yudhoyono as Indonesia's sixth president (AFP) AFP - Susilo Bambang Yudhoyono was sworn in as Indonesia's sixth president, promising to revive a precarious economy by personally leading a war on endemic graft while also tackling terrorism.", 'Pressley Out of Scotland Squad Scotland manager Berti Vogts has suffered another setback ahead of the World Cup qualifiers against Norway and Moldova with the news that Steven Pressley has pulled out of the squad.', 'services will make cash flow, says Vodafone Vodafone, the world #39;s largest mobile phone company, believes it can generate an extra 2.5 billion in cash every year by reducing costs and getting customers to spend more on their phones.', "ACC Does QB Shuffle Tennessee, North Carolina State and Duke have no true quarterback starter. Maryland and Florida State are getting spotty play by their quarterbacks. And it's only September.", 'N.Korea Committed to 6-Way Nuclear Talks - China  BEIJING (Reuters) - North Korea says it is committed to  resolving the nuclear crisis through six-party talks, a Chinese  Foreign Ministry spokeswoman said on Tuesday, appearing to  reverse statements out of Pyongyang over recent months.']}}

exec(code, env_args)
