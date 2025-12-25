code = """import json
import re

# Load data
path_sql_result = locals()['var_function-call-1215328646878465519']
with open(path_sql_result, 'r') as f:
    articles_2015_list = json.load(f)

id_to_region = {str(item['article_id']): item['region'] for item in articles_2015_list}

path_articles = locals()['var_function-call-13855097331714845970']
with open(path_articles, 'r') as f:
    all_articles = json.load(f)

# Expanded keyword lists
keywords = {
    "World": {
        "president", "minister", "prime minister", "official", "leader", "parliament", "congress", "senate", "election", "vote", "poll", "campaign",
        "war", "military", "army", "troop", "soldier", "rebel", "militia", "attack", "bomb", "blast", "explosion", "kill", "death", "dead", "injured", "casualty",
        "peace", "treaty", "agreement", "talks", "summit", "meeting", "negotiation", "diplomacy", "diplomat", "envoy", "ambassador",
        "united nations", "un", "nato", "eu", "european union", "au", "african union", "imf", "wto", "who", "ngo",
        "government", "state", "federal", "national", "agency", "court", "judge", "law", "legal", "ban", "rule", "police", "security",
        "refugee", "migrant", "aid", "humanitarian", "crisis", "disaster", "famine", "drought", "flood", "earthquake", "tsunami",
        "protest", "demonstration", "riot", "strike", "sanction", "embargo",
        "afghanistan", "albania", "algeria", "andorra", "angola", "antigua", "argentina", "armenia", "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan", "bolivia", "bosnia", "botswana", "brazil", "brunei", "bulgaria", "burkina", "burundi", "cambodia", "cameroon", "canada", "cape verde", "chad", "chile", "china", "colombia", "comoros", "congo", "costa rica", "croatia", "cuba", "cyprus", "czech", "denmark", "djibouti", "dominica", "ecuador", "egypt", "salvador", "guinea", "eritrea", "estonia", "ethiopia", "fiji", "finland", "france", "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea", "guyana", "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel", "italy", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati", "korea", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "macedonia", "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshall", "mauritania", "mauritius", "mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar", "namibia", "nauru", "nepal", "netherlands", "new zealand", "nicaragua", "niger", "nigeria", "norway", "oman", "pakistan", "palau", "panama", "papua", "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "samoa", "saudi", "senegal", "serbia", "seychelles", "sierra", "singapore", "slovakia", "slovenia", "solomon", "somalia", "south africa", "spain", "lanka", "sudan", "suriname", "swaziland", "sweden", "switzerland", "syria", "taiwan", "tajikistan", "tanzania", "thailand", "togo", "tonga", "trinidad", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "uae", "uk", "us", "usa", "uruguay", "uzbekistan", "vanuatu", "vatican", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe", "britain", "american", "palestinian"
    },
    "Sports": {
        "sport", "game", "match", "tournament", "championship", "league", "cup", "series", "season", "playoff", "final",
        "team", "club", "squad", "player", "athlete", "coach", "manager", "referee", "umpire",
        "win", "won", "lose", "lost", "beat", "defeat", "draw", "tie", "score", "goal", "point", "run", "touchdown", "basket",
        "football", "soccer", "baseball", "basketball", "tennis", "golf", "cricket", "rugby", "hockey", "racing", "driver", "olympic", "medal", "f1", "nascar", "nba", "nfl", "mlb", "nhl", "fifa", "uefa"
    },
    "Business": {
        "business", "company", "firm", "corporation", "corp", "inc", "ltd", "enterprise", "startup",
        "market", "stock", "share", "equity", "bond", "trade", "exchange", "wall street", "dow jones", "nasdaq", "nyse",
        "economy", "economic", "financial", "finance", "bank", "central bank", "fed", "reserve", "interest rate", "inflation", "deflation", "recession", "gdp",
        "profit", "loss", "revenue", "earnings", "quarter", "result", "dividend",
        "price", "cost", "value", "expensive", "cheap", "sale", "buy", "sell", "merge", "acquisition", "deal", "bid", "offer",
        "oil", "gas", "energy", "crude", "barrel",
        "ceo", "cfo", "executive", "chairman", "director", "investor", "investment"
    },
    "Sci/Tech": {
        "science", "scientific", "scientist", "research", "study", "discovery", "experiment", "lab", "laboratory",
        "technology", "tech", "technological", "computer", "computing", "software", "hardware", "internet", "web", "online", "digital", "cyber", "network", "server", "data",
        "phone", "mobile", "cellphone", "smartphone", "tablet", "device", "gadget", "app", "application",
        "space", "nasa", "astronomy", "planet", "mars", "moon", "star", "galaxy", "orbit", "satellite", "launch", "rocket",
        "biology", "biological", "chemistry", "chemical", "physics", "physical", "medical", "medicine", "drug", "virus", "disease", "health", "cancer", "gene", "genetic", "dna",
        "microsoft", "google", "apple", "ibm", "intel", "facebook", "twitter", "amazon", "yahoo", "browser", "windows", "linux"
    }
}

def classify(text):
    text = text.lower()
    normalized = re.sub(r'[^a-z0-9]', ' ', text)
    tokens = set(normalized.split())
    
    scores = {cat: 0 for cat in keywords}
    
    for cat, words in keywords.items():
        for word in words:
            if ' ' not in word:
                if word in tokens:
                    scores[cat] += 1
            else:
                if word in text:
                    scores[cat] += 1
    
    if max(scores.values()) == 0:
        return "Unknown"
    return max(scores, key=scores.get)

world_region_counts = {}

for article in all_articles:
    aid = str(article.get('article_id'))
    if aid in id_to_region:
        title = article.get('title', '')
        desc = article.get('description', '')
        full_text = title + " " + desc
        category = classify(full_text)
        
        if category == "World":
            region = id_to_region[aid]
            world_region_counts[region] = world_region_counts.get(region, 0) + 1

print("__RESULT__:")
print(json.dumps(world_region_counts))"""

env_args = {'var_function-call-1215328646878465519': 'file_storage/function-call-1215328646878465519.json', 'var_function-call-5697295960649122566': 'file_storage/function-call-5697295960649122566.json', 'var_function-call-17915382622122817248': [{'_id': '6944f27fa4e85337bc21f1cb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f27fa4e85337bc21f1cc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f27fa4e85337bc21f1cd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f27fa4e85337bc21f1ce', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f27fa4e85337bc21f1cf', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13990457352297790652': {'type': 'list', 'count': 5}, 'var_function-call-13855097331714845970': 'file_storage/function-call-13855097331714845970.json', 'var_function-call-6690540850406755014': {'Asia': 556, 'North America': 519, 'Europe': 555, 'South America': 570, 'Africa': 541}, 'var_function-call-12749906648065848949': {'SA': [{'title': "News: Climate Change Could Doom Alaska's Tundra", 'desc': 'In the next 100 years, Alaska will experience a massive loss of its historic tundra, as global warming allows these vast regions of cold, dry, lands to support forests and other vegetation that will dramatically alter native ecosystems. (Oregon State University press release)'}, {'title': 'Building Dedicated to Space Shuttle Columbia Astronauts', 'desc': 'By BILL KACZOR    PENSACOLA, Fla. (AP) -- A former dormitory converted to classrooms at the Pensacola Naval Air Station was dedicated Friday to two Columbia astronauts who were among the seven who died in the shuttle disaster Feb...'}, {'title': 'California urged to use open source, VoIP', 'desc': 'Authors of a performance review tell the beleaguered state government it could save millions of dollars by adopting open-source software and Internet-based phone calling.'}, {'title': 'Ex-colleague backs Scrafton on PM #39;s call', 'desc': 'A FORMER senior Defence Department bureaucrat last night backed her former colleague Michael Scrafton #39;s version of a phone call with John Howard over the children overboard affair. '}, {'title': 'Building permits increase 5.7, reversing June downturn', 'desc': 'WASHINGTON (CBS.MW) -- Construction of new homes recovered in July, as US homebuilders started homes at a seasonally adjusted annual rate of 1.978 million, the Commerce Department said Tuesday. '}], 'EU': [{'title': 'Reverse Psychology', 'desc': "\\\\I really hope SUN doesn't Open Source Java at JavaOne this year.  It would be a\\terrible decision and seriously hurt the tech industry.  Also, it would hurt SUN\\and I'm sure their responsible enough to realize this.\\\\(Lets hope that works!)\\\\"}, {'title': 'News: Warmer Weather, Human Disturbances Interact to Change Forests', 'desc': "While a rapidly changing climate may alter the composition of northern Wisconsin's forests, disturbances such as logging also will play a critical role in how these sylvan ecosystems change over time. (University of Wisconsin-Madison press release)"}, {'title': 'Win XP Update: A Quiet Start', 'desc': "Little fallout reported from service pack, but maybe it's because everyone's being cautious."}, {'title': 'News: U.S. tackles Emergency Alert System insecurity', 'desc': 'The FCC acknowledges that the government-mandated network that lets officials interrupt radio and television broadcasts in an emergency  is vulnerable to electronic tampering.\\'}, {'title': "Eye on Athens, China stresses a 'frugal' 2008 Olympics", 'desc': 'Amid a reevaluation, officials this week pushed the completion date for venues back to 2007.'}]}, 'var_function-call-11095129645530190574': {'Asia': 359, 'South America': 355, 'Europe': 352, 'North America': 336, 'Africa': 371}}

exec(code, env_args)
