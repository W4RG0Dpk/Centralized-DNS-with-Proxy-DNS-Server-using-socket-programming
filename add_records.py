import sqlite3
proxy=r"C:\amrita_uni\s3\Computer Networks\DNS resolver\proxy_dns.db"  
mainDNS=r"C:\amrita_uni\s3\Computer Networks\DNS resolver\main_dns.db"
canonical=r"C:\amrita_uni\s3\Computer Networks\DNS resolver\canonical.db"
mail_alias=r"C:\amrita_uni\s3\Computer Networks\DNS resolver\mail_alias.db"
def create_main_dns_table():
    try:
        conn = sqlite3.connect(mainDNS)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dns_records (
            domain TEXT PRIMARY KEY,
            ip_addresses TEXT
        )
        """)
        conn.commit()
        conn.close()
        print("Database created successfully.\n")
    except Exception as e:
        print("An error occurred:", e)

def add_to_main_dns(domain,ip_addresses):
    try:
        conn= sqlite3.connect(mainDNS)
        cursor= conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO dns_records (domain, ip_addresses) VALUES (?, ?)",(domain,ip_addresses))
        conn.commit()
        conn.close()
        print(f"Added/Updated record in Main DNS: {domain} -> {ip_addresses}\n")
    except Exception as e:
        print("An error occured :",e)

def create_proxy_dns_table():
     try:
        conn=sqlite3.connect(proxy)
        cursor= conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS proxy_records(
                    domain TEXT PRIMARY KEY,
                    ip_addresses TEXT
                    )
""")
        conn.commit()
        conn.close()
        print("Database created successfully.\n")
     except Exception as e:
         print("An error occured :",e)   

def add_to_proxy_dns(domain,ip_addresses):
    try:
        conn=sqlite3.connect(proxy)
        cursor=conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO proxy_records(domain,ip_addresses) VALUES (?,?)",(domain,ip_addresses))
        conn.commit()
        conn.close()
        print(f"Added/Updated record in Proxy DNS: {domain} -> {ip_addresses}\n")
    except Exception as e:
        print("An error occured: ",e) 

def create_canonical_table():
    try:
        conn= sqlite3.connect(canonical)
        cursor= conn.cursor()
        cursor.execute("""
         CREATE TABLE IF NOT EXISTS canonical_records (
            canonical_name TEXT PRIMARY KEY,
            aliases TEXT
        )
""")
        conn.commit()
        conn.close()
        print(f"database created successfully.\n")
    except Exception as e:
        print("An error occured: ",e)

def add_to_canonical(canonical_name, aliases):
    try:
        conn=sqlite3.connect(canonical)
        cursor=conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO canonical_records(canonical_name,aliases) VALUES (?,?)",(canonical_name,aliases))
        conn.commit()
        conn.close()
        print(f"Added/Updated record in Canonical DNS: {canonical_name} -> {aliases}\n")
    except Exception as e:
        print("An error occured: ",e)

def create_mail_alias_table():
    try:
        conn=sqlite3.connect(mail_alias)
        cursor=conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mail_alias_records (
            email TEXT PRIMARY KEY,
            aliases TEXT
        )""")
        conn.commit()
        conn.close()
        print("Mail alias table created successfully.\n")
    except Exception as e:
        print("An error occured: ",e)

def add_to_mail_alias(email,aliases):
    try:
        conn=sqlite3.connect(mail_alias)
        cursor=conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO mail_alias_records(email,aliases) VALUES (?,?)",(email,aliases))
        conn.commit()
        conn.close()
        print(f"Added/Updated record in Mail Alias table: {email} -> {aliases}\n")
    except Exception as e:
        print("An error occured: ",e)

if __name__ == "__main__":
    create_main_dns_table()
    add_to_main_dns("youtube.com", "142.250.77.142,142.250.77.143,142.250.77.145")
    add_to_main_dns("google.com", "142.250.72.206,142.250.72.207,142.250.72.208,142.250.72.209")
    add_to_main_dns("gmail.com", "142.250.67.30,142.250.67.38,142.250.67.36,142.250.67.40,142.250.67.42")
    add_to_main_dns("webtoons.com", "110.93.151.134,110.93.151.131,110.93.151.132")
    add_to_main_dns("facebook.com", "163.70.138.32,163.70.138.33,163.70.138.34,163.70.138.35")
    add_to_main_dns("twitter.com", "104.244.42.65,104.244.42.63,104.244.42.64,104.244.42.66")
    add_to_main_dns("amrita.edu", "75.2.112.168,75.2.112.164,75.2.112.165,75.2.112.166")
    add_to_main_dns("github.com", "20.207.73.82,20.207.73.84,20.207.73.81")
    add_to_main_dns("geeksforgeeks.com", "199.59.243.287,199.59.243.258,199.59.243.228,199.59.243.229")
    add_to_main_dns("wikipedia.org", "103.102.166.224,103.102.166.222,103.102.166.225,103.102.166.226,103.102.166.227")
    add_to_main_dns("amazon.com", "205.251.242.103,205.251.242.101,205.251.242.102")
    add_to_main_dns("instagram.com", "157.240.229.174,157.240.229.172,157.240.229.173,157.240.229.175")
    add_to_main_dns("linkedin.com", "108.174.10.10,108.174.11.10,108.174.12.10")
    add_to_main_dns("netflix.com", "54.208.127.124,54.208.127.125,54.208.127.126,54.208.127.127")
    add_to_main_dns("bing.com", "204.79.197.200,204.79.197.201,204.79.197.202,204.79.197.203,204.79.197.204")
    add_to_main_dns("yahoo.com", "74.6.143.25,74.6.143.26,74.6.143.27")
    add_to_main_dns("apple.com", "17.253.144.10,17.253.144.11,17.253.144.12,17.253.144.13")
    add_to_main_dns("reddit.com", "151.101.1.140,151.101.65.140,151.101.129.140")
    add_to_main_dns("quora.com", "104.16.121.36,104.16.120.36,104.16.122.36,104.16.123.36")
    add_to_main_dns("stackoverflow.com", "151.101.193.69,151.101.129.69,151.101.65.69")
    add_to_main_dns("bbc.com", "151.101.192.81,151.101.64.81,151.101.128.81,151.101.192.82,151.101.192.83")
    add_to_main_dns("cnn.com", "151.101.193.67,151.101.65.67,151.101.129.67,151.101.193.68")
    add_to_main_dns("nytimes.com", "151.101.65.164,151.101.129.164,151.101.193.164")
    add_to_main_dns("aliexpress.com", "203.119.219.6,203.119.219.7,203.119.219.8,203.119.219.9")
    add_to_main_dns("flipkart.com", "163.53.78.92,163.53.78.93,163.53.78.94")
    add_to_main_dns("spotify.com", "35.186.224.52,35.186.224.53,35.186.224.54,35.186.224.55,35.186.224.56")
    add_to_main_dns("adobe.com", "193.104.215.58,193.104.215.59,193.104.215.60")
    add_to_main_dns("twitch.tv", "151.101.2.167,151.101.66.167,151.101.130.167,151.101.194.167")
    add_to_main_dns("pinterest.com", "151.101.64.84,151.101.128.84,151.101.192.84")
    add_to_main_dns("zoom.us", "170.114.10.20,170.114.10.21,170.114.10.22,170.114.10.23")
    add_to_main_dns("oracle.com", "137.254.16.101,137.254.16.102,137.254.16.103,137.254.16.104")
    add_to_main_dns("salesforce.com", "13.110.20.101,13.110.20.102,13.110.20.103")
    add_to_main_dns("wordpress.com", "192.0.77.33,192.0.77.34,192.0.77.35,192.0.77.36,192.0.77.37")
    add_to_main_dns("cloudflare.com", "104.16.45.2,104.16.45.3,104.16.45.4")
    add_to_main_dns("kickstarter.com", "151.101.1.185,151.101.65.185,151.101.129.185,151.101.193.185")
    add_to_main_dns("paypal.com", "64.4.250.36,64.4.250.37,64.4.250.38")
    add_to_main_dns("dropbox.com", "162.125.4.18,162.125.4.19,162.125.4.20,162.125.4.21")
    add_to_main_dns("ebay.com", "66.135.192.87,66.135.192.88,66.135.192.89")
    add_to_main_dns("canva.com", "104.18.8.25,104.18.9.25,104.18.10.25")
    add_to_main_dns("medium.com", "162.159.152.4,162.159.152.5,162.159.152.6,162.159.152.7")
    add_to_main_dns("mozilla.org", "44.236.72.26,44.236.72.27,44.236.72.28,44.236.72.29,44.236.72.30")
    add_to_main_dns("tumblr.com", "74.114.154.22,74.114.154.23,74.114.154.24")
    add_to_main_dns("wikihow.com", "151.101.2.137,151.101.66.137,151.101.130.137,151.101.194.137")
    add_to_main_dns("unsplash.com", "104.16.248.249,104.16.249.249,104.16.250.249")
    add_to_main_dns("coursera.org", "54.239.26.220,54.239.26.221,54.239.26.222,54.239.26.223")
    add_to_main_dns("edx.org", "104.18.20.185,104.18.21.185,104.18.22.185")
    add_to_main_dns("udemy.com", "104.17.208.70,104.17.209.70,104.17.210.70,104.17.211.70")
    add_to_main_dns("airbnb.com", "35.157.210.1,35.157.210.2,35.157.210.3,35.157.210.4")
    add_to_main_dns("zomato.com", "13.227.251.55,13.227.251.56,13.227.251.57")
    add_to_main_dns("tripadvisor.com", "192.229.182.112,192.229.182.113,192.229.182.114,192.229.182.115,192.229.182.116")

    print()

    create_proxy_dns_table()
    add_to_proxy_dns("google.com", "142.250.72.206,142.250.72.207")
    add_to_proxy_dns("bing.com", "13.107.21.200")
    add_to_proxy_dns("zomato.com", "13.227.251.55,13.227.251.56,13.227.251.57")

    print()

    create_canonical_table()
    
    add_to_canonical("youtube.com", "youtube.uk, youtube.in, yt.uk, yt.in")
    add_to_canonical("google.com", "google.uk, google.in, g.uk, g.in")
    add_to_canonical("gmail.com", "gmail.uk, gmail.in, mail.uk, mail.in")
    add_to_canonical("webtoons.com", "webtoons.uk, webtoons.in, wt.uk, wt.in")
    add_to_canonical("facebook.com", "facebook.uk, facebook.in, fb.uk, fb.in")
    add_to_canonical("twitter.com", "twitter.uk, twitter.in, tw.uk, tw.in")
    add_to_canonical("amrita.edu", "amrita.uk, amrita.in, a.uk, a.in")
    add_to_canonical("github.com", "github.uk, github.in, gh.uk, gh.in")
    add_to_canonical("geeksforgeeks.com", "geeksforgeeks.uk, geeksforgeeks.in, gfg.uk, gfg.in")
    add_to_canonical("wikipedia.org", "wikipedia.uk, wikipedia.in, wiki.uk, wiki.in")
    add_to_canonical("amazon.com", "amazon.uk, amazon.in, amz.uk, amz.in")
    add_to_canonical("instagram.com", "instagram.uk, instagram.in, insta.uk, insta.in")
    add_to_canonical("linkedin.com", "linkedin.uk, linkedin.in, ln.uk, ln.in")
    add_to_canonical("netflix.com", "netflix.uk, netflix.in, nflx.uk, nflx.in")
    add_to_canonical("bing.com", "bing.uk, bing.in, b.uk, b.in")
    add_to_canonical("yahoo.com", "yahoo.uk, yahoo.in, yh.uk, yh.in")
    add_to_canonical("apple.com", "apple.uk, apple.in, ap.uk, ap.in")
    add_to_canonical("reddit.com", "reddit.uk, reddit.in, rd.uk, rd.in")
    add_to_canonical("quora.com", "quora.uk, quora.in, qr.uk, qr.in")
    add_to_canonical("stackoverflow.com", "stackoverflow.uk, stackoverflow.in, so.uk, so.in")
    add_to_canonical("bbc.com", "bbc.uk, bbc.in, bbcnews.uk, bbcnews.in")
    add_to_canonical("cnn.com", "cnn.uk, cnn.in, news.uk, news.in")
    add_to_canonical("nytimes.com", "nytimes.uk, nytimes.in, nyt.uk, nyt.in")
    add_to_canonical("aliexpress.com", "aliexpress.uk, aliexpress.in, ae.uk, ae.in")
    add_to_canonical("flipkart.com", "flipkart.uk, flipkart.in, fk.uk, fk.in")
    add_to_canonical("spotify.com", "spotify.uk, spotify.in, spot.uk, spot.in")
    add_to_canonical("adobe.com", "adobe.uk, adobe.in, ad.uk, ad.in")
    add_to_canonical("twitch.tv", "twitch.uk, twitch.in, tv.uk, tv.in")
    add_to_canonical("pinterest.com", "pinterest.uk, pinterest.in, pin.uk, pin.in")
    add_to_canonical("zoom.us", "zoom.uk, zoom.in, zm.uk, zm.in")
    add_to_canonical("oracle.com", "oracle.uk, oracle.in, or.uk, or.in")
    add_to_canonical("salesforce.com", "salesforce.uk, salesforce.in, sf.uk, sf.in")
    add_to_canonical("wordpress.com", "wordpress.uk, wordpress.in, wp.uk, wp.in")
    add_to_canonical("cloudflare.com", "cloudflare.uk, cloudflare.in, cf.uk, cf.in")
    add_to_canonical("kickstarter.com", "kickstarter.uk, kickstarter.in, ks.uk, ks.in")
    add_to_canonical("paypal.com", "paypal.uk, paypal.in, pp.uk, pp.in")
    add_to_canonical("dropbox.com", "dropbox.uk, dropbox.in, db.uk, db.in")
    add_to_canonical("ebay.com", "ebay.uk, ebay.in, eb.uk, eb.in")
    add_to_canonical("canva.com", "canva.uk, canva.in, cv.uk, cv.in")
    add_to_canonical("medium.com", "medium.uk, medium.in, md.uk, md.in")
    add_to_canonical("mozilla.org", "mozilla.uk, mozilla.in, moz.uk, moz.in")
    add_to_canonical("tumblr.com", "tumblr.uk, tumblr.in, tb.uk, tb.in")
    add_to_canonical("wikihow.com", "wikihow.uk, wikihow.in, wh.uk, wh.in")
    add_to_canonical("unsplash.com", "unsplash.uk, unsplash.in, usp.uk, usp.in")
    add_to_canonical("coursera.org", "coursera.uk, coursera.in, cs.uk, cs.in")
    add_to_canonical("edx.org", "edx.uk, edx.in, ex.uk, ex.in")
    add_to_canonical("udemy.com", "udemy.uk, udemy.in, ud.uk, ud.in")
    add_to_canonical("airbnb.com", "airbnb.uk, airbnb.in, ab.uk, ab.in")
    add_to_canonical("zomato.com", "zomato.uk, zomato.in, zt.uk, zt.in")
    add_to_canonical("tripadvisor.com", "tripadvisor.uk, tripadvisor.in, ta.uk, ta.in")

    create_mail_alias_table()
    add_to_mail_alias("relay1.west-coast.hotmail.com", "relay1.com, westcoast.com, hotmailrelay.com, hotmailwest.com")
    add_to_mail_alias("smtp.gmail.com", "gmail.com, googlemail.com, gmailrelay.com, googlerelay.com")
    add_to_mail_alias("mail.yahoo.com", "yahoo.com, ymail.com, yahoomail.com, yahoolive.com")
    add_to_mail_alias("outbound.mail.aol.com", "aol.com, aolmail.com, aolrelay.com, americaonline.com")
    add_to_mail_alias("smtp.office365.com", "office365.com, outlook.com, microsoftmail.com, o365relay.com")
    add_to_mail_alias("mail.protonmail.com", "protonmail.com, securemail.com, protonrelay.com, pmail.com")
    add_to_mail_alias("relay1.aws.amazon.com", "amazon.com, awsrelay.com, amazonmail.com, aws.com")
    add_to_mail_alias("smtp.zoho.com", "zoho.com, zohomail.com, zohorelay.com, zmail.com")
    add_to_mail_alias("smtp.mailgun.org", "mailgun.com, mailgunrelay.com, mgmail.com, mgrelay.com")
    add_to_mail_alias("smtp.sendgrid.net", "sendgrid.com, sendmail.com, gridrelay.com, sgmail.com")
    add_to_mail_alias("mail.fastmail.com", "fastmail.com, fmrelay.com, fastrelay.com, fmail.com")
    add_to_mail_alias("mail.yandex.com", "yandex.com, yandexmail.com, yandexrelay.com, ymrelay.com")
    add_to_mail_alias("relay1.godaddy.com", "godaddy.com, gdmail.com, godaddyrelay.com, godaddymail.com")
    add_to_mail_alias("mail.cloudflare.com", "cloudflare.com, cfmail.com, cloudrelay.com, flaremail.com")
    add_to_mail_alias("smtp.bluehost.com", "bluehost.com, bluehostmail.com, bluehostrelay.com, bhmail.com")
    add_to_mail_alias("relay1.rackspace.com", "rackspace.com, rackrelay.com, rackmail.com, rsrelay.com")
    add_to_mail_alias("smtp.apple.com", "apple.com, icloud.com, applerelay.com, applemail.com")
    add_to_mail_alias("smtp.postmarkapp.com", "postmark.com, postmail.com, postrelay.com, pmrelay.com")
    add_to_mail_alias("mail.hostgator.com", "hostgator.com, hgmail.com, hostrelay.com, gatorrelay.com")
    add_to_mail_alias("smtp.mail.com", "mail.com, mailrelay.com, mailglobal.com, universalmail.com")

    add_to_main_dns("youtube.uk", "142.250.77.142,142.250.77.146,142.250.77.147")
    add_to_main_dns("youtube.in", "142.250.77.142,142.250.77.148,142.250.77.149")
    add_to_main_dns("yt.uk", "142.250.77.142,142.250.77.150,142.250.77.151")
    add_to_main_dns("yt.in", "142.250.77.142,142.250.77.152,142.250.77.153")

    add_to_main_dns("google.uk", "142.250.72.206,142.250.72.209,142.250.72.210")
    add_to_main_dns("google.in", "142.250.72.206,142.250.72.211,142.250.72.212")
    add_to_main_dns("g.uk", "142.250.72.206,142.250.72.213,142.250.72.214")
    add_to_main_dns("g.in", "142.250.72.206,142.250.72.215,142.250.72.216")

    add_to_main_dns("gmail.uk", "142.250.67.30,142.250.67.40,142.250.67.41")
    add_to_main_dns("gmail.in", "142.250.67.30,142.250.67.42,142.250.67.43")
    add_to_main_dns("mail.uk", "142.250.67.30,142.250.67.44,142.250.67.45")
    add_to_main_dns("mail.in", "142.250.67.30,142.250.67.46,142.250.67.47")

    add_to_main_dns("webtoons.uk", "110.93.151.134,110.93.151.133,110.93.151.135")
    add_to_main_dns("webtoons.in", "110.93.151.134,110.93.151.136,110.93.151.137")
    add_to_main_dns("wt.uk", "110.93.151.134,110.93.151.138,110.93.151.139")
    add_to_main_dns("wt.in", "110.93.151.134,110.93.151.140,110.93.151.141")

    add_to_main_dns("facebook.uk", "163.70.138.32,163.70.138.35,163.70.138.36")
    add_to_main_dns("facebook.in", "163.70.138.32,163.70.138.37,163.70.138.38")
    add_to_main_dns("fb.uk", "163.70.138.32,163.70.138.39,163.70.138.40")
    add_to_main_dns("fb.in", "163.70.138.32,163.70.138.41,163.70.138.42")

    add_to_main_dns("twitter.uk", "104.244.42.65,104.244.42.66,104.244.42.67")
    add_to_main_dns("twitter.in", "104.244.42.65,104.244.42.68,104.244.42.69")
    add_to_main_dns("tw.uk", "104.244.42.65,104.244.42.70,104.244.42.71")
    add_to_main_dns("tw.in", "104.244.42.65,104.244.42.72,104.244.42.73")

    add_to_main_dns("amrita.edu", "75.2.112.168,75.2.112.164,75.2.112.165")
    add_to_main_dns("amrita.uk", "75.2.112.168,75.2.112.166,75.2.112.167")
    add_to_main_dns("amrita.in", "75.2.112.168,75.2.112.169,75.2.112.170")
    add_to_main_dns("a.uk", "75.2.112.168,75.2.112.171,75.2.112.172")
    add_to_main_dns("a.in", "75.2.112.168,75.2.112.173,75.2.112.174")

    add_to_main_dns("github.uk", "20.207.73.82,20.207.73.85,20.207.73.86")
    add_to_main_dns("github.in", "20.207.73.82,20.207.73.87,20.207.73.88")
    add_to_main_dns("gh.uk", "20.207.73.82,20.207.73.89,20.207.73.90")
    add_to_main_dns("gh.in", "20.207.73.82,20.207.73.91,20.207.73.92")

    add_to_main_dns("geeksforgeeks.uk", "199.59.243.287,199.59.243.229,199.59.243.230")
    add_to_main_dns("geeksforgeeks.in", "199.59.243.287,199.59.243.231,199.59.243.232")
    add_to_main_dns("gfg.uk", "199.59.243.287,199.59.243.233,199.59.243.234")
    add_to_main_dns("gfg.in", "199.59.243.287,199.59.243.235,199.59.243.236")

    add_to_main_dns("wikipedia.org", "103.102.166.224,103.102.166.222,103.102.166.225")
    add_to_main_dns("wikipedia.uk", "103.102.166.224,103.102.166.226,103.102.166.227")
    add_to_main_dns("wikipedia.in", "103.102.166.224,103.102.166.228,103.102.166.229")
    add_to_main_dns("wiki.uk", "103.102.166.224,103.102.166.230,103.102.166.231")
    add_to_main_dns("wiki.in", "103.102.166.224,103.102.166.232,103.102.166.233")

    add_to_main_dns("amazon.uk", "205.251.242.103,205.251.242.104,205.251.242.105")
    add_to_main_dns("amazon.in", "205.251.242.103,205.251.242.106,205.251.242.107")
    add_to_main_dns("amz.uk", "205.251.242.103,205.251.242.108,205.251.242.109")
    add_to_main_dns("amz.in", "205.251.242.103,205.251.242.110,205.251.242.111")

    add_to_main_dns("instagram.uk", "157.240.229.174,157.240.229.175,157.240.229.176")
    add_to_main_dns("instagram.in", "157.240.229.174,157.240.229.177,157.240.229.178")
    add_to_main_dns("insta.uk", "157.240.229.174,157.240.229.179,157.240.229.180")
    add_to_main_dns("insta.in", "157.240.229.174,157.240.229.181,157.240.229.182")

    add_to_main_dns("linkedin.uk", "108.174.10.10,108.174.10.13,108.174.10.14")
    add_to_main_dns("linkedin.in", "108.174.10.10,108.174.10.15,108.174.10.16")
    add_to_main_dns("ln.uk", "108.174.10.10,108.174.10.17,108.174.10.18")
    add_to_main_dns("ln.in", "108.174.10.10,108.174.10.19,108.174.10.20")

    add_to_main_dns("netflix.uk", "52.89.124.25,52.89.124.28,52.89.124.29")
    add_to_main_dns("netflix.in", "52.89.124.25,52.89.124.30,52.89.124.31")
    add_to_main_dns("nflx.uk", "52.89.124.25,52.89.124.32,52.89.124.33")
    add_to_main_dns("nflx.in", "52.89.124.25,52.89.124.34,52.89.124.35")

    add_to_main_dns("bing.uk", "204.79.197.200,204.79.197.203,204.79.197.204")
    add_to_main_dns("bing.in", "204.79.197.200,204.79.197.205,204.79.197.206")
    add_to_main_dns("b.uk", "204.79.197.200,204.79.197.207,204.79.197.208")
    add_to_main_dns("b.in", "204.79.197.200,204.79.197.209,204.79.197.210")

    add_to_main_dns("yahoo.uk", "74.6.231.21,74.6.231.24,74.6.231.25")
    add_to_main_dns("yahoo.in", "74.6.231.21,74.6.231.26,74.6.231.27")
    add_to_main_dns("yh.uk", "74.6.231.21,74.6.231.28,74.6.231.29")
    add_to_main_dns("yh.in", "74.6.231.21,74.6.231.30,74.6.231.31")

    add_to_main_dns("apple.uk", "17.172.224.47,17.172.224.50,17.172.224.51")
    add_to_main_dns("apple.in", "17.172.224.47,17.172.224.52,17.172.224.53")
    add_to_main_dns("ap.uk", "17.172.224.47,17.172.224.54,17.172.224.55")
    add_to_main_dns("ap.in", "17.172.224.47,17.172.224.56,17.172.224.57")

    add_to_main_dns("reddit.uk", "151.101.1.140,151.101.193.140,151.101.1.141")
    add_to_main_dns("reddit.in", "151.101.1.140,151.101.65.141,151.101.129.141")
    add_to_main_dns("rd.uk", "151.101.1.140,151.101.193.141,151.101.1.142")
    add_to_main_dns("rd.in", "151.101.1.140,151.101.65.142,151.101.129.142")

    add_to_main_dns("quora.uk", "104.16.121.36,104.16.121.37,104.16.121.38,104.16.121.40")
    add_to_main_dns("quora.in", "104.16.121.36,104.16.121.39,104.16.121.41,104.16.121.42")
    add_to_main_dns("qr.uk", "104.16.121.36,104.16.121.43,104.16.121.44,104.16.121.45")
    add_to_main_dns("qr.in", "104.16.121.36,104.16.121.46,104.16.121.47,104.16.121.48")

    add_to_main_dns("stackoverflow.uk", "151.101.193.69,151.101.193.70,151.101.193.71,151.101.193.72")
    add_to_main_dns("stackoverflow.in", "151.101.193.69,151.101.193.73,151.101.193.74,151.101.193.75")
    add_to_main_dns("so.uk", "151.101.193.69,151.101.193.76,151.101.193.77,151.101.193.78")
    add_to_main_dns("so.in", "151.101.193.69,151.101.193.79,151.101.193.80,151.101.193.81")

    add_to_main_dns("bbc.uk", "151.101.192.81,151.101.192.82,151.101.192.83,151.101.192.84")
    add_to_main_dns("bbc.in", "151.101.192.81,151.101.192.85,151.101.192.86,151.101.192.87")
    add_to_main_dns("bbcnews.uk", "151.101.192.81,151.101.192.88,151.101.192.89,151.101.192.90")
    add_to_main_dns("bbcnews.in", "151.101.192.81,151.101.192.91,151.101.192.92,151.101.192.93")

    add_to_main_dns("cnn.uk", "151.101.193.67,151.101.193.68,151.101.193.69,151.101.193.70")
    add_to_main_dns("cnn.in", "151.101.193.67,151.101.193.71,151.101.193.72,151.101.193.73")
    add_to_main_dns("news.uk", "151.101.193.67,151.101.193.74,151.101.193.75,151.101.193.76")
    add_to_main_dns("news.in", "151.101.193.67,151.101.193.77,151.101.193.78,151.101.193.79")

    add_to_main_dns("nytimes.uk", "151.101.65.164,151.101.65.165,151.101.65.166,151.101.65.167")
    add_to_main_dns("nytimes.in", "151.101.65.164,151.101.65.168,151.101.65.169,151.101.65.170")
    add_to_main_dns("nyt.uk", "151.101.65.164,151.101.65.171,151.101.65.172,151.101.65.173")
    add_to_main_dns("nyt.in", "151.101.65.164,151.101.65.174,151.101.65.175,151.101.65.176")

    add_to_main_dns("aliexpress.uk", "203.119.219.6,203.119.219.7,203.119.219.8,203.119.219.9")
    add_to_main_dns("aliexpress.in", "203.119.219.6,203.119.219.10,203.119.219.11,203.119.219.12")
    add_to_main_dns("ae.uk", "203.119.219.6,203.119.219.13,203.119.219.14,203.119.219.15")
    add_to_main_dns("ae.in", "203.119.219.6,203.119.219.16,203.119.219.17,203.119.219.18")

    add_to_main_dns("flipkart.uk", "163.53.78.92,163.53.78.93,163.53.78.94,163.53.78.95")
    add_to_main_dns("flipkart.in", "163.53.78.92,163.53.78.96,163.53.78.97,163.53.78.98")
    add_to_main_dns("fk.uk", "163.53.78.92,163.53.78.99,163.53.78.100,163.53.78.101")
    add_to_main_dns("fk.in", "163.53.78.92,163.53.78.102,163.53.78.103,163.53.78.104")

    add_to_main_dns("spotify.uk", "35.186.224.52,35.186.224.53,35.186.224.54,35.186.224.55")
    add_to_main_dns("spotify.in", "35.186.224.52,35.186.224.56,35.186.224.57,35.186.224.58")
    add_to_main_dns("spot.uk", "35.186.224.52,35.186.224.59,35.186.224.60,35.186.224.61")
    add_to_main_dns("spot.in", "35.186.224.52,35.186.224.62,35.186.224.63,35.186.224.64")

    add_to_main_dns("adobe.uk", "193.104.215.58,193.104.215.59,193.104.215.60,193.104.215.61")
    add_to_main_dns("adobe.in", "193.104.215.58,193.104.215.62,193.104.215.63,193.104.215.64")
    add_to_main_dns("ad.uk", "193.104.215.58,193.104.215.65,193.104.215.66,193.104.215.67")
    add_to_main_dns("ad.in", "193.104.215.58,193.104.215.68,193.104.215.69,193.104.215.70")

    add_to_main_dns("twitch.uk", "151.101.2.167,151.101.2.168,151.101.2.169,151.101.2.170")
    add_to_main_dns("twitch.in", "151.101.2.167,151.101.2.171,151.101.2.172,151.101.2.173")
    add_to_main_dns("tv.uk", "151.101.2.167,151.101.2.174,151.101.2.175,151.101.2.176")
    add_to_main_dns("tv.in", "151.101.2.167,151.101.2.177,151.101.2.178,151.101.2.179")

    add_to_main_dns("pinterest.uk", "151.101.64.84,151.101.64.85,151.101.64.86,151.101.64.87")
    add_to_main_dns("pinterest.in", "151.101.64.84,151.101.64.88,151.101.64.89,151.101.64.90")
    add_to_main_dns("pin.uk", "151.101.64.84,151.101.64.91,151.101.64.92,151.101.64.93")
    add_to_main_dns("pin.in", "151.101.64.84,151.101.64.94,151.101.64.95,151.101.64.96")

    add_to_main_dns("zoom.uk", "170.114.10.20,170.114.10.21,170.114.10.22,170.114.10.23")
    add_to_main_dns("zoom.in", "170.114.10.20,170.114.10.24,170.114.10.25,170.114.10.26")
    add_to_main_dns("zm.uk", "170.114.10.20,170.114.10.27,170.114.10.28,170.114.10.29")
    add_to_main_dns("zm.in", "170.114.10.20,170.114.10.30,170.114.10.31,170.114.10.32")

    add_to_main_dns("oracle.uk", "137.254.16.101,137.254.16.102,137.254.16.103,137.254.16.104")
    add_to_main_dns("oracle.in", "137.254.16.101,137.254.16.105,137.254.16.106,137.254.16.107")
    add_to_main_dns("or.uk", "137.254.16.101,137.254.16.108,137.254.16.109,137.254.16.110")
    add_to_main_dns("or.in", "137.254.16.101,137.254.16.111,137.254.16.112,137.254.16.113")

    add_to_main_dns("salesforce.uk", "13.110.20.101,13.110.20.102,13.110.20.103,13.110.20.104")
    add_to_main_dns("salesforce.in", "13.110.20.101,13.110.20.105,13.110.20.106,13.110.20.107")
    add_to_main_dns("sf.uk", "13.110.20.101,13.110.20.108,13.110.20.109,13.110.20.110")
    add_to_main_dns("sf.in", "13.110.20.101,13.110.20.111,13.110.20.112,13.110.20.113")

    add_to_main_dns("wordpress.uk", "192.0.77.33,192.0.77.34,192.0.77.35,192.0.77.36")
    add_to_main_dns("wordpress.in", "192.0.77.33,192.0.77.37,192.0.77.38,192.0.77.39")
    add_to_main_dns("wp.uk", "192.0.77.33,192.0.77.40,192.0.77.41,192.0.77.42")
    add_to_main_dns("wp.in", "192.0.77.33,192.0.77.43,192.0.77.44,192.0.77.45")

    add_to_main_dns("cloudflare.uk", "104.16.45.2,104.16.45.3,104.16.45.4,104.16.45.5")
    add_to_main_dns("cloudflare.in", "104.16.45.2,104.16.45.6,104.16.45.7,104.16.45.8")
    add_to_main_dns("cf.uk", "104.16.45.2,104.16.45.9,104.16.45.10,104.16.45.11")
    add_to_main_dns("cf.in", "104.16.45.2,104.16.45.12,104.16.45.13,104.16.45.14")

    add_to_main_dns("kickstarter.uk", "151.101.1.185,151.101.1.186,151.101.1.187,151.101.1.188")
    add_to_main_dns("kickstarter.in", "151.101.1.185,151.101.1.189,151.101.1.190,151.101.1.191")
    add_to_main_dns("ks.uk", "151.101.1.185,151.101.1.192,151.101.1.193,151.101.1.194")
    add_to_main_dns("ks.in", "151.101.1.185,151.101.1.195,151.101.1.196,151.101.1.197")

    add_to_main_dns("paypal.uk", "64.4.250.36,64.4.250.37,64.4.250.38,64.4.250.39")
    add_to_main_dns("paypal.in", "64.4.250.36,64.4.250.40,64.4.250.41,64.4.250.42")
    add_to_main_dns("pp.uk", "64.4.250.36,64.4.250.43,64.4.250.44,64.4.250.45")
    add_to_main_dns("pp.in", "64.4.250.36,64.4.250.46,64.4.250.47,64.4.250.48")

    add_to_main_dns("dropbox.uk", "162.125.4.18,162.125.4.19,162.125.4.20,162.125.4.21")
    add_to_main_dns("dropbox.in", "162.125.4.18,162.125.4.22,162.125.4.23,162.125.4.24")
    add_to_main_dns("db.uk", "162.125.4.18,162.125.4.25,162.125.4.26,162.125.4.27")
    add_to_main_dns("db.in", "162.125.4.18,162.125.4.28,162.125.4.29,162.125.4.30")

    add_to_main_dns("ebay.uk", "66.135.192.87,66.135.192.88,66.135.192.89,66.135.192.90")
    add_to_main_dns("ebay.in", "66.135.192.87,66.135.192.91,66.135.192.92,66.135.192.93")
    add_to_main_dns("eb.uk", "66.135.192.87,66.135.192.94,66.135.192.95,66.135.192.96")
    add_to_main_dns("eb.in", "66.135.192.87,66.135.192.97,66.135.192.98,66.135.192.99")

    add_to_main_dns("canva.uk", "104.18.8.25,104.18.9.25,104.18.10.25,104.18.11.25")
    add_to_main_dns("canva.in", "104.18.8.25,104.18.12.25,104.18.13.25,104.18.14.25")
    add_to_main_dns("cv.uk", "104.18.8.25,104.18.15.25,104.18.16.25,104.18.17.25")
    add_to_main_dns("cv.in", "104.18.8.25,104.18.18.25,104.18.19.25,104.18.20.25")

    add_to_main_dns("medium.uk", "162.159.152.4,162.159.152.5,162.159.152.6,162.159.152.7")
    add_to_main_dns("medium.in", "162.159.152.4,162.159.152.8,162.159.152.9,162.159.152.10")
    add_to_main_dns("md.uk", "162.159.152.4,162.159.152.11,162.159.152.12,162.159.152.13")
    add_to_main_dns("md.in", "162.159.152.4,162.159.152.14,162.159.152.15,162.159.152.16")

    add_to_main_dns("mozilla.uk", "44.236.72.26,44.236.72.27,44.236.72.28,44.236.72.29")
    add_to_main_dns("mozilla.in", "44.236.72.26,44.236.72.30,44.236.72.31,44.236.72.32")
    add_to_main_dns("moz.uk", "44.236.72.26,44.236.72.33,44.236.72.34,44.236.72.35")
    add_to_main_dns("moz.in", "44.236.72.26,44.236.72.36,44.236.72.37,44.236.72.38")

    add_to_main_dns("spotify.uk", "35.186.224.25,35.186.224.26,35.186.224.27,35.186.224.28")
    add_to_main_dns("spotify.in", "35.186.224.25,35.186.224.29,35.186.224.30,35.186.224.31")
    add_to_main_dns("sp.uk", "35.186.224.25,35.186.224.32,35.186.224.33,35.186.224.34")
    add_to_main_dns("sp.in", "35.186.224.25,35.186.224.35,35.186.224.36,35.186.224.37")

    add_to_main_dns("linkedin.uk", "108.174.10.10,108.174.10.11,108.174.10.12,108.174.10.13")
    add_to_main_dns("linkedin.in", "108.174.10.10,108.174.10.14,108.174.10.15,108.174.10.16")
    add_to_main_dns("ln.uk", "108.174.10.10,108.174.10.17,108.174.10.18,108.174.10.19")
    add_to_main_dns("ln.in", "108.174.10.10,108.174.10.20,108.174.10.21,108.174.10.22")

    add_to_main_dns("twitter.uk", "104.244.42.65,104.244.42.66,104.244.42.67,104.244.42.68")
    add_to_main_dns("twitter.in", "104.244.42.65,104.244.42.69,104.244.42.70,104.244.42.71")
    add_to_main_dns("tw.uk", "104.244.42.65,104.244.42.72,104.244.42.73,104.244.42.74")
    add_to_main_dns("tw.in", "104.244.42.65,104.244.42.75,104.244.42.76,104.244.42.77")

    add_to_main_dns("facebook.uk", "157.240.22.35,157.240.22.36,157.240.22.37,157.240.22.38")
    add_to_main_dns("facebook.in", "157.240.22.35,157.240.22.39,157.240.22.40,157.240.22.41")
    add_to_main_dns("fb.uk", "157.240.22.35,157.240.22.42,157.240.22.43,157.240.22.44")
    add_to_main_dns("fb.in", "157.240.22.35,157.240.22.45,157.240.22.46,157.240.22.47")

    add_to_main_dns("instagram.uk", "185.60.216.35,185.60.216.36,185.60.216.37,185.60.216.38")
    add_to_main_dns("instagram.in", "185.60.216.35,185.60.216.39,185.60.216.40,185.60.216.41")
    add_to_main_dns("ig.uk", "185.60.216.35,185.60.216.42,185.60.216.43,185.60.216.44")
    add_to_main_dns("ig.in", "185.60.216.35,185.60.216.45,185.60.216.46,185.60.216.47")

    add_to_main_dns("netflix.uk", "52.31.34.15,52.31.34.16,52.31.34.17,52.31.34.18")
    add_to_main_dns("netflix.in", "52.31.34.15,52.31.34.19,52.31.34.20,52.31.34.21")
    add_to_main_dns("nf.uk", "52.31.34.15,52.31.34.22,52.31.34.23,52.31.34.24")
    add_to_main_dns("nf.in", "52.31.34.15,52.31.34.25,52.31.34.26,52.31.34.27")

    add_to_main_dns("pinterest.uk", "151.101.64.84,151.101.64.85,151.101.64.86,151.101.64.87")
    add_to_main_dns("pinterest.in", "151.101.64.84,151.101.64.88,151.101.64.89,151.101.64.90")
    add_to_main_dns("pt.uk", "151.101.64.84,151.101.64.91,151.101.64.92,151.101.64.93")
    add_to_main_dns("pt.in", "151.101.64.84,151.101.64.94,151.101.64.95,151.101.64.96")

    add_to_main_dns("youtube.uk", "172.217.6.46,172.217.6.47,172.217.6.48,172.217.6.49")
    add_to_main_dns("youtube.in", "172.217.6.46,172.217.6.50,172.217.6.51,172.217.6.52")
    add_to_main_dns("yt.uk", "172.217.6.46,172.217.6.53,172.217.6.54,172.217.6.55")
    add_to_main_dns("yt.in", "172.217.6.46,172.217.6.56,172.217.6.57,172.217.6.58")

    add_to_main_dns("aliexpress.uk", "203.119.219.6,203.119.219.11,203.119.219.12,203.119.219.13")
    add_to_main_dns("aliexpress.in", "203.119.219.6,203.119.219.14,203.119.219.15,203.119.219.16")
    add_to_main_dns("ae.uk", "203.119.219.6,203.119.219.17,203.119.219.18,203.119.219.19")
    add_to_main_dns("ae.in", "203.119.219.6,203.119.219.20,203.119.219.21,203.119.219.22")

    add_to_main_dns("flipkart.uk", "163.53.78.92,163.53.78.96,163.53.78.97,163.53.78.98")
    add_to_main_dns("flipkart.in", "163.53.78.92,163.53.78.99,163.53.78.100,163.53.78.101")
    add_to_main_dns("fk.uk", "163.53.78.92,163.53.78.102,163.53.78.103,163.53.78.104")
    add_to_main_dns("fk.in", "163.53.78.92,163.53.78.105,163.53.78.106,163.53.78.107")

    add_to_main_dns("bbc.uk", "151.101.192.81,151.101.192.85,151.101.192.86,151.101.192.87")
    add_to_main_dns("bbc.in", "151.101.192.81,151.101.192.88,151.101.192.89,151.101.192.90")
    add_to_main_dns("bbcnews.uk", "151.101.192.81,151.101.192.91,151.101.192.92,151.101.192.93")
    add_to_main_dns("bbcnews.in", "151.101.192.81,151.101.192.94,151.101.192.95,151.101.192.96")

    add_to_main_dns("cnn.uk", "151.101.193.67,151.101.193.71,151.101.193.72,151.101.193.73")
    add_to_main_dns("cnn.in", "151.101.193.67,151.101.193.74,151.101.193.75,151.101.193.76")
    add_to_main_dns("news.uk", "151.101.193.67,151.101.193.77,151.101.193.78,151.101.193.79")
    add_to_main_dns("news.in", "151.101.193.67,151.101.193.80,151.101.193.81,151.101.193.82")

    add_to_main_dns("nytimes.uk", "151.101.65.164,151.101.65.168,151.101.65.169,151.101.65.170")
    add_to_main_dns("nytimes.in", "151.101.65.164,151.101.65.171,151.101.65.172,151.101.65.173")
    add_to_main_dns("nyt.uk", "151.101.65.164,151.101.65.174,151.101.65.175,151.101.65.176")
    add_to_main_dns("nyt.in", "151.101.65.164,151.101.65.177,151.101.65.178,151.101.65.179")

    add_to_main_dns("zomato.uk", "13.227.251.55,13.227.251.59,13.227.251.60,13.227.251.61")
    add_to_main_dns("zomato.in", "13.227.251.55,13.227.251.62,13.227.251.63,13.227.251.64")
    add_to_main_dns("zt.uk", "13.227.251.55,13.227.251.65,13.227.251.66,13.227.251.67")
    add_to_main_dns("zt.in", "13.227.251.55,13.227.251.68,13.227.251.69,13.227.251.70")

    add_to_main_dns("tripadvisor.uk", "192.229.182.112,192.229.182.116,192.229.182.117,192.229.182.118")
    add_to_main_dns("tripadvisor.in", "192.229.182.112,192.229.182.119,192.229.182.120,192.229.182.121")
    add_to_main_dns("ta.uk", "192.229.182.112,192.229.182.122,192.229.182.123,192.229.182.124")
    add_to_main_dns("ta.in", "192.229.182.112,192.229.182.125,192.229.182.126,192.229.182.127")

