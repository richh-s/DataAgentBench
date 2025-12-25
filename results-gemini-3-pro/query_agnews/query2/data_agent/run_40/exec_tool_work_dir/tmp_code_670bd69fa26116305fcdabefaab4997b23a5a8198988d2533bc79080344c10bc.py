code = """import json
import re

# Load the articles
with open(locals()['var_function-call-9867695846899870663'], 'r') as f:
    articles = json.load(f)

# Define keywords
categories = {
    "Science/Technology": [
        "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", 
        "cyber", "digital", "wireless", "mobile", "phone", "gadget", "robot", "space", "nasa", "mars", 
        "astronomy", "physics", "biology", "chemistry", "genome", "research", "lab", "scientist", 
        "innovation", "innovative", "silicon", "google", "microsoft", "apple", "intel", "ibm", "linux", 
        "windows", "virus", "spam", "hacker", "browser", "broadband", "network", "telecom", 
        "video game", "gaming", "nintendo", "sony", "xbox", "playstation", "console", "ipod", "mp3", 
        "dvd", "gps", "satellite", "engine", "machine", "device", "app", "blog", "search engine",
        "gameboy", "micro-game", "gyro-gen", "electricity", "ocean waves", "biotech", "spam", "net",
        "firefox", "explorer", "server", "chip", "semiconductor", "laser", "nanotech", "cloning", "stem cell",
        "probe", "capsule", "sun", "samples", "study", "environment", "water", "virus-throttling", "itunes"
    ],
    "Sports": [
        "sport", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "cricket", 
        "rugby", "athlete", "player", "coach", "team", "stadium", "league", "tournament", "championship", 
        "olympic", "medal", "race", "racing", "f1", "nascar", "driver", "score", "goal", "touchdown", 
        "run", "wicket", "inning", "quarter", "match", "win", "loss", "victory", "defeat", "cup", 
        "season", "club", "nfl", "nba", "mlb", "nhl", "pro bowl", "cornerback", "receiver", "broncos",
        "red sox", "yankees", "lakers", "bulls", "real madrid", "barcelona", "chelsea",
        "arsenal", "liverpool", "juventus", "milan", "inter", "bayern", "dortmund", "psg", "ajax",
        "davis cup", "wimbledon", "open", "masters", "world cup", "super bowl", "world series", "stanley cup",
        "boxing", "fighter", "round", "knockout", "marathon", "sprint", "cycling", "cyclist", "gold medal", 
        "manchester united", "manchester city", "leeds united", "newcastle united"
    ],
    "Business": [
        "business", "economy", "economic", "market", "stock", "share", "trade", "finance", "financial", 
        "bank", "banking", "invest", "investment", "investor", "money", "dollar", "euro", "currency", 
        "profit", "revenue", "earning", "loss", "debt", "bankrupt", "merger", "acquisition", "deal", 
        "contract", "ceo", "cfo", "executive", "company", "corporation", "firm", "industry", "sector", 
        "price", "cost", "rate", "inflation", "tax", "budget", "wall street", "dow jones", "nasdaq", 
        "oil", "gas", "energy", "retail", "sales", "mining", "commodity", "bhp", "billiton", "yukos", 
        "gazprom", "airline", "airbus", "boeing", "ford", "gm", "toyota", "honda", "nissan", "vw",
        "oracle", "people soft", "bid", "hostile", "takeover", "shareholder", "product sales", "quarter", "q1", "q2", "q3", "q4",
        "kroger", "supermarket", "gold production"
    ],
    "World": [
        "world", "international", "nation", "country", "government", "politics", "political", "president", 
        "minister", "leader", "official", "diplomat", "war", "peace", "conflict", "military", "army", 
        "soldier", "troop", "police", "attack", "bomb", "blast", "kill", "death", "died", "victim", 
        "disaster", "earthquake", "flood", "storm", "hurricane", "tsunami", "election", "vote", "poll", 
        "campaign", "party", "democrat", "republican", "parliament", "congress", "senate", "law", 
        "court", "judge", "trial", "prison", "right", "un", "united nations", "eu", "nato", "iraq", 
        "iran", "afghanistan", "israel", "palestine", "syria", "russia", "china", "korea", "nuclear", 
        "weapon", "terror", "terrorism", "al qaeda", "bin laden", "bush", "putin", "blair", "chirac",
        "arafat", "sharon", "kofi annan", "powell", "rice", "rumsfeld", "baghdad", "fallujah", "gaza",
        "settlement", "occupied", "territory", "sworn in", "mediator", "parliament", "prime minister", "kathmandu", "nepal"
    ]
}

def classify(title, desc):
    # Preprocessing
    text = (str(title) + " " + str(desc)).lower()
    clean_text = re.sub(r'[^a-z0-9]', ' ', text)
    words = clean_text.split()
    
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for kw in keywords:
            if " " in kw:
                if kw in text: # Substring match for phrases
                    scores[cat] += 1
            else:
                if kw in words: # Exact word match
                    scores[cat] += 1
    
    # Specific Boosts
    if any(w in words for w in ["profit", "revenue", "earning", "stock", "share", "market", "economy", "investment", "investor"]):
        scores["Business"] += 2

    if any(w in words for w in ["nfl", "nba", "mlb", "nhl", "football", "soccer", "tennis", "olympic", "championship", "tournament", "medal"]):
        scores["Sports"] += 2
        
    if any(w in words for w in ["war", "president", "minister", "election", "bomb", "attack", "killed", "dead", "peace", "iraq", "gaza"]):
        scores["World"] += 2

    if any(w in words for w in ["science", "software", "internet", "browser", "nasa", "space", "robot", "linux", "microsoft", "google"]):
        scores["Science/Technology"] += 2

    # Disambiguation
    if "game" in text:
        if any(w in text for w in ["video", "console", "nintendo", "sony", "xbox", "boy", "micro"]):
            scores["Science/Technology"] += 3
        elif any(w in text for w in ["match", "league", "cup", "season", "score", "coach"]):
            scores["Sports"] += 3

    if "cup" in text:
        if "world cup" in text or "davis cup" in text:
            scores["Sports"] += 3

    # Tie-breaking logic:
    if scores["Business"] >= 1 and scores["Science/Technology"] >= 1:
        if any(w in text for w in ["revenue", "profit", "stock", "share", "market", "estimate", "drop", "rise", "sales"]):
             scores["Business"] += 2
        elif any(w in text for w in ["unveil", "launch", "release", "new", "feature", "software", "device"]):
             scores["Science/Technology"] += 1

    # Fix Liverpool
    if "liverpool" in words:
        scores["Sports"] += 5

    # Fix Placer Dome (Business)
    if "mining" in words or "gold production" in text:
        scores["Business"] += 3

    if sum(scores.values()) == 0:
        return "Unclassified"
    
    return max(scores, key=scores.get)

results = []
for art in articles:
    cat = classify(art.get('title', ''), art.get('description', ''))
    results.append({"title": art.get('title'), "category": cat})

# Count
total = len(results)
scitech_count = sum(1 for r in results if r['category'] == "Science/Technology")

print("__RESULT__:")
print(json.dumps({"total": total, "scitech_count": scitech_count, "fraction": scitech_count/total if total else 0, "details": results}))"""

env_args = {'var_function-call-14802185822981372221': [{'author_id': '218'}], 'var_function-call-14553611907080601669': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-15828535751467272093': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'title': 1, 'description': 1, 'article_id': 1, '_id': 0}}, 'var_function-call-8677478758674628797': [{'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-6582939166409369247': {'total': 5, 'scitech_count': 1, 'fraction': 0.2, 'details': [{'title': 'GameBoy mini-games win prize', 'category': 'Science/Technology'}, {'title': 'Bailey Tries WR', 'category': 'Unclassified'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Unclassified'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Unclassified'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Unclassified'}]}, 'var_function-call-9867695846899870663': 'file_storage/function-call-9867695846899870663.json', 'var_function-call-7082704008961575475': {'total': 111, 'scitech_count': 18, 'fraction': 0.16216216216216217, 'details': [{'title': 'GameBoy mini-games win prize', 'category': 'Science/Technology'}, {'title': 'Bailey Tries WR', 'category': 'Sports'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Science/Technology'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Science/Technology'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Business'}, {'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'category': 'Business'}, {'title': 'Even in win, nasty vibes', 'category': 'Sports'}, {'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'category': 'World'}, {'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'category': 'World'}, {'title': 'Somalians sworn in', 'category': 'World'}, {'title': 'Muenzer races for gold', 'category': 'Sports'}, {'title': 'Israelis to Expand West Bank Settlements', 'category': 'World'}, {'title': 'Stocks End Up as Oil Prices Fall', 'category': 'Business'}, {'title': 'WTO Rejects U.S. Appeal on Canadian Wheat', 'category': 'World'}, {'title': 'Capriati Scrambles Past Chladkova Challenge at Open', 'category': 'Sports'}, {'title': 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'category': 'World'}, {'title': 'UPDATE: Intel lowers Q3 revenue estimates', 'category': 'Business'}, {'title': 'Calm as Kathmandu curfew lifted', 'category': 'Unclassified'}, {'title': 'Israeli Missiles Kill 13 Militants', 'category': 'World'}, {'title': 'Serena Blasts Umpire After Dramatic Defeat', 'category': 'Sports'}, {'title': 'Space Probe Fails to Deploy Its Parachute and Crashes', 'category': 'Science/Technology'}, {'title': 'Producer Prices Drop, Trade Gap Narrows', 'category': 'Business'}, {'title': 'Shuttle repair price tag soars', 'category': 'Science/Technology'}, {'title': 'Microsoft settles with UK phone maker', 'category': 'Science/Technology'}, {'title': 'Champions League to provide upsets', 'category': 'Sports'}, {'title': 'The Associated Press', 'category': 'Sports'}, {'title': 'Not all sweet for Lou', 'category': 'Sports'}, {'title': 'Law pays tribute to record-breaking Ruud', 'category': 'Sports'}, {'title': 'Negotiations Seek End to IRA Threat', 'category': 'World'}, {'title': "Kerry Questions Bush's Judgment on Iraq", 'category': 'World'}, {'title': 'Giants gain on Dodgers', 'category': 'Sports'}, {'title': 'EMC Unveils E-mail Storage For Microsoft Exchange', 'category': 'Science/Technology'}, {'title': 'Bed Bath   Beyond Profit Up, Shares Fall (Reuters)', 'category': 'Business'}, {'title': 'A Strategy for Shell?', 'category': 'Business'}, {'title': 'Placer Dome forecasts higher 2005 gold production', 'category': 'Sports'}, {'title': 'Liverpool prepares for life without Gerrard', 'category': 'Science/Technology'}, {'title': 'ICC Champions Trophy final today', 'category': 'Sports'}, {'title': 'Swedes fire into top two spots', 'category': 'Sports'}, {'title': 'Israel Defense Official Threatens Syria (AP)', 'category': 'World'}, {'title': 'TechBrief: Vodafone seeks new frontiers', 'category': 'Science/Technology'}, {'title': 'Ex-Astronaut Casts Doubt on Space Tourism', 'category': 'Science/Technology'}, {'title': 'Charging Els moves to the top', 'category': 'Sports'}, {'title': 'Finance Leaders Urge Vigilance on Terror (Reuters)', 'category': 'Business'}, {'title': 'German food retailer Spar sells 50-pct stake in Netto discount to ITM (AFP)', 'category': 'Business'}, {'title': 'But hurricanes and more impact in the third quarter', 'category': 'Business'}, {'title': 'Diabetes delay adds to AstraZeneca #39;s ills', 'category': 'Business'}, {'title': 'Soldering plays Spadea next', 'category': 'Sports'}, {'title': 'Stocks: Stocks rise as investors bet on profit reports', 'category': 'Business'}, {'title': 'NZ stocks: Sharemarket softens, but Air NZ takes off', 'category': 'Business'}, {'title': 'Devastating blow', 'category': 'Sports'}, {'title': 'Man remanded over Danielle murder', 'category': 'World'}, {'title': 'Two Soldiers Die After Crash in Iraq', 'category': 'World'}, {'title': 'Texas Instruments Posts Higher 3Q Profits (AP)', 'category': 'Business'}, {'title': 'Sergeant in Abu Ghraib Case Pleads Guilty to 8 Counts', 'category': 'World'}, {'title': "'Treasure hunt' for bandit's loot", 'category': 'World'}, {'title': 'Citigroup Says SEC May Take Action Against Jones (Update6)', 'category': 'Business'}, {'title': 'Burma army intelligence  #39;purged #39;', 'category': 'World'}, {'title': 'Memos Warned of Billing Fraud by Firm in Iraq', 'category': 'World'}, {'title': 'Owenagainlifts Real Madrid from the doldrums', 'category': 'Sports'}, {'title': 'Brazilian GP Race Report: Montoya claims first win of 2004', 'category': 'Sports'}, {'title': 'Clinton jumps into campaign, as missing explosives force Bush on defensive (AFP)', 'category': 'World'}, {'title': 'FCC Approves Merger, Wireless Giant Created', 'category': 'Business'}, {'title': 'Crude prices fall after good news from Norway', 'category': 'World'}, {'title': 'Maryland 20, No. 5 Florida State 17', 'category': 'Sports'}, {'title': 'Satellite write-downs widen DirecTV #39;s loss', 'category': 'Science/Technology'}, {'title': 'Report: Stottlemyre won #39;t return', 'category': 'Sports'}, {'title': 'Backs off drastic fare  amp; service plans', 'category': 'Unclassified'}, {'title': 'Goodyear Sees Profit; Stock Up', 'category': 'Business'}, {'title': 'Israel to free Egyptian students: Cairo media', 'category': 'World'}, {'title': 'Why I had to leave Australia', 'category': 'Unclassified'}, {'title': '. . . and Lost Chances', 'category': 'World'}, {'title': 'Coke CEO: the company may face tough times. Earnings targets &lt;b&gt;...&lt;/b&gt;', 'category': 'Business'}, {'title': 'Vote Fraud Theories, Spread by Blogs, Are Quickly Buried', 'category': 'World'}, {'title': 'Lord Black is charged with fraud', 'category': 'World'}, {'title': 'AMCC to Lay Off 150', 'category': 'Business'}, {'title': 'Revealed: why the fear factor runs with the pack', 'category': 'Unclassified'}, {'title': 'Gunshots echo in Indian-controlled Kashmir', 'category': 'World'}, {'title': 'Ontario to dedicate  #36;12.5 million to water studies and watershed protection (Canadian Press)', 'category': 'Unclassified'}, {'title': 'India offers unqualified talks on Kashmir', 'category': 'World'}, {'title': 'Mylan Shares Up As Drug Stocks Close Down', 'category': 'Business'}, {'title': 'Sorenstam Leads ADT Championship by Three (AP)', 'category': 'Sports'}, {'title': "Cherkasky says Marsh may settle Spitzer's lawsuit within a month", 'category': 'Business'}, {'title': 'Call Service with a Sneer (Reuters)', 'category': 'Sports'}, {'title': 'Lehmann slams  #39;arrogant #39; ref', 'category': 'Sports'}, {'title': "Blunkett denies visa 'fast-track'", 'category': 'Unclassified'}, {'title': 'Anglican Leader Warns Churches on Gay Hate Message (Reuters)', 'category': 'World'}, {'title': 'After adjusting, Pats get busy', 'category': 'Sports'}, {'title': 'Asean signs historic deal with China', 'category': 'Business'}, {'title': 'Rams not in Pack #39;s league', 'category': 'Sports'}, {'title': 'Death toll rises to 63 in Shaanxi coalmine explosion', 'category': 'World'}, {'title': 'HP to launch  #39;virus-throttling #39; software', 'category': 'Science/Technology'}, {'title': 'XM CEO Sees Satellite Radio on Cell Phones', 'category': 'Science/Technology'}, {'title': "'Tis the season to be greeted with silliness", 'category': 'Sports'}, {'title': "EBay Adds 'Want It Now' Feature (Reuters)", 'category': 'Science/Technology'}, {'title': 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'category': 'Science/Technology'}, {'title': 'Virgin Atlantic Inaugural Flight Lands in Sydney', 'category': 'Unclassified'}, {'title': 'Ford #39;s Scheele to Retire as President on Feb. 1 (Update2)', 'category': 'World'}, {'title': 'NBA Wrap: McGrady Leads Rockets to Stunning Win', 'category': 'Sports'}, {'title': 'Paypal and Apple iTunes link-up', 'category': 'Science/Technology'}, {'title': 'Arab reform dreams run aground', 'category': 'World'}, {'title': 'US mobile groups confirm merger', 'category': 'Science/Technology'}, {'title': 'Bush Ordering Better Ocean Oversight (AP)', 'category': 'World'}, {'title': 'Indonesian extremists influence Thai Muslims, prime minister says &lt;b&gt;...&lt;/b&gt;', 'category': 'World'}, {'title': 'Peace delegation leaves Najaf empty-handed as fighting continues', 'category': 'World'}, {'title': 'Schumacher in uncharted territory', 'category': 'Sports'}, {'title': 'Karzai deputy escapes a roadside bombing', 'category': 'World'}, {'title': 'Ban for former Ahold executives', 'category': 'Business'}, {'title': 'Hendrick Motorsports', 'category': 'Sports'}, {'title': 'Protests in Canada over Ukraine crisis (AFP)', 'category': 'World'}, {'title': 'Log on to be a satellite spy', 'category': 'Science/Technology'}, {'title': 'NASD Warns of Risky Home-Equity Investing', 'category': 'Business'}]}}

exec(code, env_args)
