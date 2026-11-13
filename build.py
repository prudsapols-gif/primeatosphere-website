"""Build the Prime Atosphere static site.

Edit content in src/partials/*.html and the PAGES list below, then run:
    python3 build.py
Output goes to ./docs (GitHub Pages publishes this folder).
"""
import os, json, shutil

SITE = "https://www.primeatosphere.com"
SRC = os.path.join(os.path.dirname(__file__), "src")
DIST = os.path.join(os.path.dirname(__file__), "docs")

NAV = [("products/", "ผลิตภัณฑ์", "Products"),
       ("solutions/", "โซลูชัน", "Solutions"),
       ("3m-novec-replacement/", "ทดแทน 3M Novec™", "3M Novec™ Guide"),
       ("about/", "เกี่ยวกับเรา", "About"),
       ("contact/", "ติดต่อ", "Contact")]

# path, title, description, eyebrow (th,en), heading (th,en), partials
PAGES = [
    ("", "Prime Atosphere | Thermal Management Solutions ประเทศไทย",
     "สารทำความเย็น ของไหลระบายความร้อน และสารทำความสะอาดระบบ จาก Climalife, Inventec และ AGC พร้อมทีมที่ปรึกษา ทางเลือกแทน 3M Novec™",
     None, None, ["hero", "trust", "products-overview", "why", "partners", "cta"]),
    ("products/", "ผลิตภัณฑ์ | สารทำความเย็น ของไหลระบายความร้อน สารทำความสะอาด | Prime Atosphere",
     "THERMASOLV, PROMOSOLV NEO B2, สารทำความเย็น Climalife, AGC AMOLEA™ และ ASAHIKLIN™ สำหรับอุตสาหกรรมไทย",
     ("ผลิตภัณฑ์", "Products"), ("ผลิตภัณฑ์ของเรา", "Our products"), ["products-detail", "cta"]),
    ("water-treatment/", "ผลิตภัณฑ์เคมีสำหรับระบบน้ำอุตสาหกรรม | Anti Scale, Biocide, Sodium Hypochlorite | Prime Atosphere",
     "สารควบคุมตะกรัน สารควบคุมจุลินทรีย์ และ Sodium Hypochlorite 10% สำหรับระบบน้ำหล่อเย็นอุตสาหกรรม บรรจุ 20 กก. พร้อม SDS ไทย–อังกฤษ",
     ("ผลิตภัณฑ์", "Products"), ("ผลิตภัณฑ์เคมีสำหรับระบบน้ำอุตสาหกรรม", "Industrial water treatment chemicals"), ["wt-category", "cta"]),
    ("water-treatment/anti-scale-for-cooling/", "Anti Scale for Cooling สารควบคุมตะกรันหอหล่อเย็น | Prime Atosphere",
     "Anti Scale for Cooling สารควบคุมตะกรันสำหรับระบบน้ำหอหล่อเย็น (HEDP) บรรจุ 20 กก. พร้อม SDS ไทย–อังกฤษ",
     None, None, ["wt-anti-scale-for-cooling", "cta"]),
    ("water-treatment/biocide-for-cooling/", "Biocide for Cooling สารควบคุมจุลินทรีย์ระบบน้ำหล่อเย็น | Prime Atosphere",
     "Biocide for Cooling สารควบคุมจุลินทรีย์สำหรับระบบน้ำหล่อเย็น บรรจุ 20 กก. พร้อม SDS ไทย–อังกฤษ",
     None, None, ["wt-biocide-for-cooling", "cta"]),
    ("water-treatment/sodium-hypochlorite-10/", "Sodium Hypochlorite 10% (NaOCl) | Prime Atosphere",
     "Sodium Hypochlorite 10% (NaOCl) Available chlorine ขั้นต่ำ 10% บรรจุ 20 กก. พร้อม SDS ไทย–อังกฤษ",
     None, None, ["wt-sodium-hypochlorite-10", "cta"]),
    ("solutions/", "โซลูชันตามอุตสาหกรรม | HVAC-R โรงงาน โฟม ดาต้าเซ็นเตอร์ | Prime Atosphere",
     "โซลูชันการจัดการความร้อนสำหรับโรงงาน ช่างแอร์และชิลเลอร์ ผู้ผลิตโฟม และดาต้าเซ็นเตอร์",
     ("โซลูชัน", "Solutions"), ("โซลูชันตามกลุ่มลูกค้า", "Solutions by industry"), ["solutions", "cta"]),
    ("3m-novec-replacement/", "สารทดแทน 3M Novec™ 649, 7100, 7200, 7300, 7500, 73DE | Prime Atosphere",
     "3M Novec™ เลิกผลิตแล้ว ตารางเทียบสารทดแทน THERMASOLV และ PROMOSOLV NEO B2 จาก Inventec",
     ("คู่มือทดแทน", "Replacement guide"), ("สารทดแทน 3M Novec™", "3M Novec™ replacements"), ["novec-table", "novec-faq", "cta"]),
    ("about/", "เกี่ยวกับเรา | Prime Atosphere",
     "Prime Atosphere ก่อตั้งปี 2567 ที่ปรึกษาและตัวแทนจำหน่ายสารทำความเย็นและเคมีภัณฑ์ระบายความร้อน คลังสินค้าบางปู สมุทรปราการ",
     ("เกี่ยวกับเรา", "About"), ("เกี่ยวกับ Prime Atosphere", "About Prime Atosphere"), ["about", "partners"]),
    ("contact/", "ติดต่อ / ขอใบเสนอราคา | Prime Atosphere",
     "ติดต่อ Prime Atosphere เพื่อขอใบเสนอราคาสารทำความเย็นและเคมีภัณฑ์ระบายความร้อน BD@primeatosphere.com",
     ("ติดต่อ", "Contact"), ("ขอใบเสนอราคา", "Request a quote"), ["contact"]),
]

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Prime Atosphere", "legalName": "Prime Atosphere (Thailand) Co., Ltd.",
       "url": SITE + "/", "logo": SITE + "/assets/img/logo.png", "email": "BD@primeatosphere.com", "description": "Thermal management solutions: refrigerants, cooling fluids, cleaning solvents and automation.",
       "address": {"@type": "PostalAddress", "streetAddress": "888/66 Moo 3, Bang Pu Mai", "addressLocality": "Mueang Samut Prakan",
                   "addressRegion": "Samut Prakan", "postalCode": "10280", "addressCountry": "TH"}}


def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read()


def bi(th, en):
    return f'<span lang="th">{th}</span><span lang="en">{en}</span>'


def render(path, title, desc, eyebrow, heading, parts):
    root = "../" * path.count("/")
    nav = "\n".join(f'      <a href="{root}{p}">{bi(th, en)}</a>' for p, th, en in NAV)
    body = ""
    if heading:
        body += (f'<section class="hero" style="padding:0"><div class="wrap" style="padding-top:64px;padding-bottom:64px">'
                 f'<div class="eyebrow">{bi(*eyebrow)}</div><h1>{bi(*heading)}</h1></div></section>\n')
    body += "\n".join(read(f"partials/{p}.html") for p in parts)
    body = body.replace("{{root}}", root)
    return f'''<!doctype html>
<html lang="th" data-lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Prime Atosphere">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{path}">
<link rel="icon" href="{root}assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
<meta property="og:image" content="{SITE}/assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Prompt:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css">
<script type="application/ld+json">{json.dumps(ORG, ensure_ascii=False)}</script>
</head>
<body>
<header>
  <div class="wrap nav">
    <a class="logo" href="{root or './'}" aria-label="Prime Atosphere">
      <img class="logo-light" src="{root}assets/img/logo.png" alt="Prime Atosphere" width="138" height="57">
      <img class="logo-dark" src="{root}assets/img/logo-white.png" alt="" width="138" height="57">
    </a>
    <nav class="menu">
{nav}
    </nav>
    <div class="lang" role="group" aria-label="Language"><button data-set="th">TH</button><button data-set="en">EN</button></div>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="wrap">
    <div><img src="{root}assets/img/logo-white.png" alt="Prime Atosphere" width="146" height="60" style="display:block;margin-bottom:10px">{bi("บริษัท ไพรม์ อโตสเฟียร์ (ประเทศไทย) จำกัด", "Prime Atosphere (Thailand) Co., Ltd.")}<br>{bi("โซลูชันการจัดการความร้อนครบวงจร", "Thermal Management Solutions")}<br>BD@primeatosphere.com</div>
    <div>{bi("เลขประจำตัวผู้เสียภาษี", "Tax ID")} 0115567012305<br>© 2026 Prime Atosphere</div>
  </div>
</footer>
<script src="{root}assets/main.js"></script>
</body>
</html>
'''


def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(os.path.join(DIST, "assets"))
    shutil.copy(os.path.join(SRC, "style.css"), os.path.join(DIST, "assets/style.css"))
    shutil.copy(os.path.join(SRC, "main.js"), os.path.join(DIST, "assets/main.js"))
    shutil.copytree(os.path.join(SRC, "img"), os.path.join(DIST, "assets/img"))
    if os.path.isdir(os.path.join(SRC, "sds")):
        shutil.copytree(os.path.join(SRC, "sds"), os.path.join(DIST, "sds"))
    for name in ("favicon.svg", "404.html", "CNAME"):
        if os.path.exists(os.path.join(SRC, name)):
            shutil.copy(os.path.join(SRC, name), os.path.join(DIST, name))
    for page in PAGES:
        out = os.path.join(DIST, page[0], "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(render(*page))
    urls = "\n".join(f"  <url><loc>{SITE}/{p[0]}</loc></url>" for p in PAGES)
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    open(os.path.join(DIST, ".nojekyll"), "w").close()
    with open(os.path.join(DIST, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(PAGES), "pages ->", DIST)


if __name__ == "__main__":
    main()
