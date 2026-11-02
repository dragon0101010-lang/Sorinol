"""Ghid de modelare in Revit - 4120 MacArthur Facade TI (in romana)."""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")

body = ParagraphStyle("b", fontName="DV", fontSize=9.2, leading=13, spaceAfter=3)
h1 = ParagraphStyle("h1", parent=body, fontName="DVB", fontSize=16, leading=20, spaceAfter=6)
h2 = ParagraphStyle("h2", parent=body, fontName="DVB", fontSize=11.5, leading=15, spaceBefore=10, spaceAfter=4)
bul = ParagraphStyle("bul", parent=body, leftIndent=14, bulletIndent=3)
note = ParagraphStyle("n", parent=body, backColor=colors.HexColor("#F3F0E4"), borderPadding=5, spaceBefore=4, spaceAfter=8)
cell = ParagraphStyle("c", parent=body, fontSize=8.5, leading=11, spaceAfter=0)

def P(t, s=body): return Paragraph(t, s)
def B(items): return [Paragraph(i, bul, bulletText="•") for i in items]
def table(rows, widths):
    t = Table([[Paragraph(str(x), cell) for x in r] for r in rows], colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E2E2E2")),
        ("GRID",(0,0),(-1,-1),0.4,colors.grey),("VALIGN",(0,0),(-1,-1),"TOP")]))
    return t

def footer(c, d):
    c.setFont("DV", 7.5)
    c.drawString(0.7*inch, 0.45*inch, "CMCE 2410 - Construction Documents III | Ghid Revit - 4120 MacArthur Facade TI")
    c.drawRightString(letter[0]-0.7*inch, 0.45*inch, f"pag. {d.page}")

s = []
s += [P("Ghid de modelare în Revit", h1),
      P("<b>4120 MacArthur Facade TI</b> — 4118-4124 MacArthur Blvd, Oakland, CA<br/>Sursă: setul de execuție Studio 144 Architects (08.28.26). Ghidul urmează ordinea săptămânilor 3-6 din curs."),
      P("Cotele sunt citite de pe desen. Verifică-le pe foaia originală înainte de a le introduce în model. Unde setul nu dă informația (de exemplu poziția corpurilor de iluminat), ghidul spune explicit că alegerea îți aparține.", note)]

s += [P("0. Pregătire proiect", h2)]
s += B(["Pornește din șablonul <b>Imperial</b> al cursului (unități: picioare și inci). Salvează ca <i>MacArthur_TI.rvt</i>.",
        "<b>Niveluri</b> (se creează în vedere de secțiune sau elevație, nu în plan):"])
s += [table([["Nivel", "Cotă", "Observație"],
   ["MAIN LEVEL - 01", "0'-0\"", "Planșeul spațiilor comerciale"],
   ["EYEBROW LEVEL", "10'-10 1/2\"", "Streașina / copertina fațadei"],
   ["TOP OF GARAGE", "11'-1 1/2\"", "Acoperișul inferior din spate"],
   ["TOP OF PARAPET", "18'-10\"", "Parapetul fațadei"]], [1.6*inch, 1.2*inch, 3.9*inch])]
s += B(["Creează planurile asociate: Level 1 (existent), Demo, Proposed, RCP. Redenumește-le exact ca pe foi (<i>DEMO - LEVEL 1 PLAN</i>, <i>PROPOSED - LEVEL 1 PLAN</i>, <i>PROPOSED LEVEL 1 - RCP</i>).",
        "<b>Faze</b> (Phasing): <i>Existing</i> și <i>New Construction</i>. Tot ce e măsurat în releveu intră în <i>Existing</i>."])

s += [P("1. Săptămâna 3 — Releveul și planul existent (foaia A1.31)", h2)]
s += B(["Clădirea e din lemn (ferme de lemn, pereții comuni sunt portanți, fațada nu). Peretele dinspre stradă (vest) <b>nu e perpendicular</b> pe ceilalți: modelează-l din cote, nu presupune 90°.",
        "Desenează întâi perimetrul, apoi separările dintre spațiile 4118, 4120, 4122 și 4124 (adâncimi N-S: 18'-11 1/2\", 18'-10\", 17'-7\", 18'-5 1/2\").",
        "Lungimi de verificat: 55'-2 1/2\" (lângă 4120), 52'-2\" (peretele sud), coridorul din spate 8'-10 1/2\" lățime, 4118-U 17'-2 1/2\" N-S.",
        "Adaugă spațiile din spate: 4118-U (spațiu închiriat), 4118-V (depozit), 4118-W (birou) și toaletele existente 4120-T și 4122-T.",
        "Pune camere (Room) și etichete cu numerele de pe foaie."])

s += [P("2. Săptămâna 3 — Planul de demolare", h2)]
s += B(["Duplică planul existent și redenumește-l <i>DEMO - LEVEL 1 PLAN</i>.",
        "Cu <b>Demolish</b> marchează ce e în roșu pe A1.31: peretele și ușile fațadei din vest, încăperea toaletei din spatele 4118, părți din pereții de coridor din spate din jurul 4120 și golurile de ușă, toaleta și ușa de la 4118-U.",
        "Filtrul de faze al vederii: <i>Show Previous + Demo</i>, ca elementele demolate să apară în roșu, întrerupt.",
        "<b>Verificare:</b> numele și numerele camerelor trebuie să fie identice în vederea Existing și în Demo."])

s += [PageBreak(), P("3. Săptămâna 4 — Pereții cu grosimile reale", h2),
      P("Foaia A8.01 definește tipurile de pereți. Diferă de exemplul din curs (acolo: CMU și 2HR); aici totul e cadru de lemn.")]
s += [table([["Tip", "Compoziție", "Unde"],
   ["1A / 1B", "Gips-carton 5/8\" + montanți lemn 2x4 la 16\" o.c. + gips-carton 5/8\". 1A are și izolație termo-acustică și placă de ciment 1/2\" (Durock) pe fața dinspre baie, pentru plăci ceramice", "Compartimentări interioare nerezistente la foc"],
   ["3", "La fel ca 1A, dar cu montanți 2x6", "Unde indică foaia"],
   ["Exterior", "Tencuială exterioară pe placaj (fațada); finisajul vechi din cărămidă subțire se demolează și se înlocuiește cu stucco la pereții de capăt", "Fațada vest și capetele"]],
   [0.8*inch, 3.9*inch, 2.0*inch])]
s += B(["Duplică <i>Basic Wall</i> pentru fiecare tip și definește straturile în <b>Edit Type → Structure</b>.",
        "Setează <b>Location Line</b> astfel încât cotele din releveu să cadă pe fața corectă a peretelui.",
        "Nu folosi culori speciale pe pereți (cum cere și cursul).",
        "Coridorul nou de ieșire din spate trebuie să aibă rezistență la foc de 1 oră (A0.00). Setul nu detaliază compoziția: cere indicații înainte să inventezi un tip de perete."])

s += [P("4. Săptămâna 4 — Deschiderile fațadei (storefront)", h2),
      P("Foaia A3.32 (elevația de vest) dă deschiderile pentru fiecare magazin:")]
s += [table([["Magazin", "Lățime deschidere", "Ușă / grilă"],
   ["4118", "13'-9\"", "Grilă rulantă D1, 13'-9\" x 10'-10 1/2\""],
   ["4120", "14'-5\"", "Grilă rulantă D2, 14'-5\" x 10'-10 1/2\""],
   ["4122", "15'-3\"", "Grilă rulantă D3, 15'-3\" x 10'-10 1/2\""],
   ["4124", "13'-9 1/2\"", "Grilă rulantă (în mod tipic, conform notei de pe foaie)"]], [1.0*inch, 1.6*inch, 4.1*inch])]
s += B(["Între deschideri: 3'-0\". Cota din stânga: 2'-1\".",
        "Folosește <b>Curtain Wall: Storefront</b> sau familiile <i>Curtain Wall Dbl Glass / Sgl Glass</i> din biblioteca Imperial pentru vitrinele de la nivelul 0'-0\" până la streașina de 10'-10 1/2\".",
        "Ușa tip A: exterioară, 36\" x 80\", lemn, vitrată dublu. Fereastra 1: fixă, 24\" x 63\" (în set e marcat 'verifică dacă trebuie securizat/tempered'). Fereastra 2: batantă, 36\" x 18\".",
        "Atenție la alinierea pe verticală cu nivelurile (streașină, parapet); fațada se aliniază cu clădirea vecină 4116 (notă pe A3.31)."])

s += [P("5. Săptămâna 5 — Planul de plafon (RCP, foaia A2.42)", h2)]
s += B(["Creează plafoane cu <b>Ceiling → Sketch</b>, offset <b>8'-6\"</b> (tag C-1).",
        "Încarcă din biblioteca Imperial: <i>Downlight Recessed Can 6\"</i>, <i>Ceiling Light Linear Box 1'x4'</i>, <i>Pendant Light Linear 2 Lamp 48\"</i>, <i>Square Supply Diffuser 12\"/24\"</i>, <i>Square Return Register 12\"/24\"</i>.",
        "Setul <b>nu arată</b> amplasarea corpurilor de iluminat. Amplasează-le tu, centrat pe camere, ca în exercițiul de curs.",
        "Pune etichete de înălțime de plafon și etichetele camerelor (4118-4124, 4122-O, 4124-O, 4122-S, 4122-H, 4120-M, 4120-BR, 4120-T, 4122-T, 4124-T, 4118-U/V/W)."])

s += [PageBreak(), P("6. Săptămâna 6 — Secțiuni, toalete și detalii (în locul scării)", h2),
      P("Clădirea are un singur nivel, deci nu există scară. Fișa cursului pentru scară se înlocuiește cu:")]
s += B(["<b>Secțiuni prin coridorul din spate</b> (A3.11), versiunile Demo și Proposed, la 1/8\" = 1'-0\".",
        "<b>Toalete mărite</b> 4118-T (7'-10\" x 7'-7\") și 4124-T (aprox. 6'-10 1/2\" lățime), la 1/2\" = 1'-0\": cerc de manevră de 60\", bare de sprijin (GB) 36\", lavoar LAV-1 (American Standard Murro, ADA), WC ADA 16 1/2\" înălțime, oglindă, coș pentru șervețele, dispenser hârtie, săpun, uscător de mâini, masă de schimbat bebeluși.",
        "<b>Elevații interioare</b> 3-10 cu finisaj de tip cărămidă (A5.11).",
        "<b>Detaliu de parapet</b> cu coping și BUR flashing, la 3\" = 1'-0\" (A8.01).",
        "Înălțimi de montaj și spații libere: A1.00 (foaie de cod și accesibilitate)."])

s += [P("7. Foile finale (titleblock)", h2),
      P("Pune vederile pe foi cu cartuș, după lista din setul original:")]
s += [table([["Foaie", "Nume", "Vederi de plasat"],
  ["A0.00", "Site Plan", "Plan de situație, informații, legendă"],
  ["A0.51", "Egress Plan", "Plan de evacuare, sarcini de ocupanți (opțional)"],
  ["A1.31", "Existing / Demo Floor Plan", "Planul existent și Demo"],
  ["A2.31", "Proposed Floor Plan - Level 01", "Plan propus și planul nivelului de streașină"],
  ["A2.32", "Proposed Roof Plan", "Plan de acoperiș"],
  ["A2.42", "Proposed RCP", "Plan de plafon"],
  ["A3.11", "Building Sections", "Secțiuni Demo / Proposed"],
  ["A3.31 / A3.32", "Elevații", "Nord, Est, Sud, Vest"],
  ["A5.11", "Enlarged Plan & Interior Elevations", "Toalete și elevații interioare"],
  ["A8.01", "Door & Window Schedules, Details", "Legende uși/ferestre, pereți, parapet"]], [1.0*inch, 2.4*inch, 3.3*inch])]
s += [Spacer(1,6), P("Verificare finală: scările desenelor (1/8\", 3/16\", 1/4\", 1/2\", 3\") corespund cu cele din foi, iar numerele camerelor sunt aceleași în toate vederile.", note)]

SimpleDocTemplate("MacArthur_Ghid_Revit.pdf", pagesize=letter, leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.7*inch, bottomMargin=0.75*inch, title="Ghid Revit - 4120 MacArthur Facade TI").build(s, onFirstPage=footer, onLaterPages=footer)
print("OK")
