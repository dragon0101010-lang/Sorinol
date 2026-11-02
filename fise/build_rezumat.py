"""Rezumat structurat - 4120 MacArthur Facade TI (romana)."""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")

body = ParagraphStyle("b", fontName="DV", fontSize=9, leading=12.5, spaceAfter=3)
h1 = ParagraphStyle("h1", parent=body, fontName="DVB", fontSize=16, leading=20, spaceAfter=6)
h2 = ParagraphStyle("h2", parent=body, fontName="DVB", fontSize=11.5, leading=15, spaceBefore=10, spaceAfter=4, keepWithNext=1)
note = ParagraphStyle("n", parent=body, backColor=colors.HexColor("#F3F0E4"), borderPadding=5, spaceBefore=4, spaceAfter=8)
cell = ParagraphStyle("c", parent=body, fontSize=8.3, leading=10.5, spaceAfter=0)
cellb = ParagraphStyle("cb", parent=cell, fontName="DVB")

def table(rows, widths, bold_first_col=False):
    data = []
    for i, r in enumerate(rows):
        data.append([Paragraph(str(x), cellb if (i == 0) else cell) for x in r])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E2E2E2")),
        ("GRID",(0,0),(-1,-1),0.4,colors.grey),("VALIGN",(0,0),(-1,-1),"TOP"),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, colors.HexColor("#FAFAFA")])]))
    return t

def footer(c, d):
    c.setFont("DV", 7.5)
    c.drawString(0.7*inch, 0.45*inch, "Rezumat proiect - 4120 MacArthur Facade TI (nr. 20263) | sursă: set CD Studio 144, 08.28.26")
    c.drawRightString(letter[0]-0.7*inch, 0.45*inch, f"pag. {d.page}")

P = lambda t, s=body: Paragraph(t, s)
W = 6.9*inch
s = [P("Rezumat structurat al proiectului", h1),
     P("<b>4120 MacArthur Facade TI</b> — 4118-4124 MacArthur Blvd, Oakland, CA 94619"),
     P("Toate datele vin din setul de execuție de 12 foi. Cotele sunt citite de pe desen: verifică-le pe foaia originală înainte de utilizare. Câmpurile marcate „nespecificat” nu apar în set.", note)]

s += [P("1. Date generale", h2), table([
 ["Câmp", "Valoare"],
 ["Proiectant", "Studio 144 Architects, Oakland (arhitect: Brittany D. Dhawan)"],
 ["Nr. proiect / dată", "20263 / 2026-08-31"],
 ["Județ / oraș / APN", "Alameda / Oakland / 30-1981-117"],
 ["Tip construcție / ocupanță", "V-B, nesprinklerată / B (afaceri)"],
 ["Spații comerciale", "5 (4118, 4120, 4122, 4124 și spațiile din spate, unitatea G)"],
 ["Parcare existentă", "4 locuri; locuri ADA: niciunul"],
 ["Structură", "Clădire din lemn cu ferme; pereții comuni sunt portanți, fațada nu"],
 ["Suprafață totală clădire", "nespecificat"],
 ["Coduri", "CBC, CEC, CMC, CPC, Energy, CFC, CALGreen, 2025 (Title 24 C.C.R.)"]], [1.9*inch, W-1.9*inch])]

s += [P("2. Domeniul lucrărilor", h2), table([
 ["Element", "Descriere"],
 ["Fațadă", "Pereți și vitrări noi, uși de intrare noi, grile de securitate rulante la toate deschiderile"],
 ["Coridor din spate", "Coridor nou de ieșire cu rezistență la foc 1 oră"],
 ["Interior", "Toalete unisex noi (4118-T, 4124-T), sală de pauză, cameră de masaj, birouri/depozite"],
 ["Structură", "Fără modificări majore; pereții comuni rămân; modificări minore la îmbinări"],
 ["Antreprenor", "Pregătirea zonelor, reparații la elementele afectate de demolări, autorizații, deșeuri, cerințe seismice"]], [1.5*inch, W-1.5*inch])]

s += [P("3. Niveluri", h2), table([
 ["Nivel", "Cotă"],
 ["MAIN LEVEL - 01", "0'-0\""],
 ["EYEBROW LEVEL", "10'-10 1/2\""],
 ["TOP OF GARAGE", "11'-1 1/2\""],
 ["TOP OF PARAPET", "18'-10\""],
 ["Înălțime plafon (C-1)", "8'-6\" A.F.F."]], [2.5*inch, 2*inch])]

s += [P("4. Spații și încărcare de ocupanți (foaia A0.51)", h2), table([
 ["Unitate / spațiu", "Suprafață", "Tip (factor)", "Ocupanți"],
 ["4118 — tenant space", "1.389 SF", "B (150)", "10"],
 ["4120 — tenant space", "1.120 SF", "B (150)", "8"],
 ["4120 — break room", "143 SF", "B (150)", "1"],
 ["4120 — storage", "23 SF", "S (300)", "1"],
 ["4122 — tenant space", "585 SF", "B (150)", "4"],
 ["4122 — tenant space (interior)", "331 SF", "B (150)", "3"],
 ["4122 — storage room", "358 SF", "S (300)", "2"],
 ["4124 — tenant space", "559 SF", "B (150)", "4"],
 ["4124 — rear office & storage", "560 SF", "B (150)", "4"],
 ["G — tenant space", "564 SF", "B (150)", "4"],
 ["G — tenant space (mic)", "208 SF", "B (150)", "2"],
 ["G — storage space", "426 SF", "S (300)", "2"]], [2.8*inch, 1.3*inch, 1.4*inch, 1.4*inch])]
s += [Spacer(1,4), P("Totaluri pe unitate: 4118 = 10, 4120 = 10, 4122 = 9, 4124 = 8, G = 8 ocupanți. Cea mai mare sarcină (10 persoane) este sub pragul care cere sprinklere.", body)]

s += [P("5. Evacuare (foaia A0.51)", h2), table([
 ["Punct", "Unitate", "Distanță până la ieșire", "Limită"],
 ["A", "4118", "81'", "100' (cale comună, grup B)"],
 ["B", "4120", "77' (65' + 12')", "100'"],
 ["C", "4122", "73' (23' + 31' + 19')", "100'"],
 ["D", "4124", "69' (37' + 32')", "100'"],
 ["E", "G", "44' (24' + 4' + 16')", "100'"]], [0.8*inch, 1.0*inch, 2.5*inch, 2.6*inch])]
s += [Spacer(1,4), P("Distanța maximă de parcurs conform CBC 1017.2 pentru B și S-1: 200'. Rezultat: sprinklerele nu sunt necesare. Uși: 36\" simplă = 168 persoane, 72\" dublă = 342; uși de ieșire min. 36\" lățime, căi min. 44\".", body)]

s += [P("6. Uși (foaia A8.01)", h2), table([
 ["Tip", "Descriere", "Dimensiuni / observații"],
 ["A", "Ușă exterioară de intrare, lemn, vitrată dublu, Solarban 70, geam securizat conf. CBC", "36\" x 80\", grosime min. 1 7/8\""],
 ["B", "Ușă exterioară/interioară, lemn, nerezistentă la foc", "36\" x 80\", min. 1 7/8\""],
 ["C", "Ușă de dulap interior, lemn, rezistență la foc 1 h", "36\" x 80\", min. 1 7/8\""],
 ["D1 / D2 / D3", "Grilă rulantă de securitate, cu suprascriere de ieșire, tuburi oțel 3\", comutator cu cheie", "D1 (4118): 13'-9\" x 10'-10 1/2\"; D2 (4120): 14'-5\" x 10'-10 1/2\"; D3 (4122): 15'-3\" x 10'-10 1/2\""],
 ["E", "Ușă rulantă plină, tuburi oțel 3\", comutator cu cheie (4118-U)", "10'-0\" x 8'-6\""]], [1.0*inch, 3.2*inch, 2.7*inch])]

s += [P("7. Ferestre", h2), table([
 ["Tip", "Descriere", "Dimensiuni"],
 ["1", "Fixă, cadru lemn, vitraj dublu, nerezistentă la foc (în set: „verifică dacă trebuie securizat”)", "24\" x 63\", buiandrug 8'-6\""],
 ["2", "Batantă (awning), cadru lemn, vitraj dublu", "36\" x 18\", buiandrug 8'-9\""]], [0.6*inch, 4.0*inch, 2.3*inch])]

s += [P("8. Tipuri de pereți (foaia A8.01)", h2), table([
 ["Tip", "Compoziție"],
 ["1A", "Partiție interioară nerezistentă: gips-carton 5/8\" + montanți lemn 2x4 la 16\" o.c. + izolație termo-acustică + placă de ciment 1/2\" pe fața dinspre baie"],
 ["1B", "Partiție interioară nerezistentă: gips-carton 5/8\" + montanți lemn 2x4 la 16\" o.c. + gips-carton 5/8\""],
 ["3", "La fel ca 1A, cu montanți 2x6"],
 ["Fațadă", "Tencuială exterioară pe placaj; finisaj de cărămidă subțire demolat și înlocuit cu stucco la pereții de capăt"],
 ["Parapet", "Coping oțel 24 GA, flashing, nailer placaj, BUR peste izolație înclinată (detaliu 1/A8.01, sursă NRCA)"]], [1.0*inch, W-1.0*inch])]

s += [P("9. Fațada de vest (foaia A3.32)", h2), table([
 ["Magazin", "Deschidere", "Lățime travee"],
 ["4118", "13'-9\"", "17'-6 7/8\""],
 ["4120", "14'-5\"", "17'-4 15/16\""],
 ["4122", "15'-3\"", "18'-2 7/8\""],
 ["4124", "13'-9 1/2\"", "16'-9 9/16\""]], [1.5*inch, 2.0*inch, 2.0*inch])]
s += [Spacer(1,4), P("Între deschideri: 3'-0\". Firme de magazin 7'-0\" tipic. Grile rulante la toate deschiderile. Fațada rămâne aliniată cu clădirea vecină 4116 (A3.31).", body)]

s += [P("10. Cote ale planului existent (foaia A1.31)", h2), table([
 ["Element", "Cotă"],
 ["Adâncime N-S: 4118 / 4120 / 4122 / 4124", "18'-11 1/2\" / 18'-10\" / 17'-7\" / 18'-5 1/2\""],
 ["Lungime lângă 4120", "55'-2 1/2\" (+ 10'-11\")"],
 ["Perete sud", "52'-2\""],
 ["Lățime coridor din spate", "8'-10 1/2\""],
 ["4118-U, N-S", "17'-2 1/2\""]], [3.2*inch, W-3.2*inch])]

s += [P("11. Camere (după foile A2.31 și A2.42)", h2), table([
 ["Cod", "Nume", "Cod", "Nume"],
 ["4118", "Tenant space", "4120-T", "(E) toilet"],
 ["4120", "Tenant space", "4120-BR", "Break room"],
 ["4122", "Tenant space", "4120-M", "Massage room"],
 ["4124", "Tenant space", "4122-T", "(E) toilet"],
 ["4118-T", "Unisex toilet (nou)", "4122-O / 4122-S / 4122-H", "Office / Storage / Hallway"],
 ["4124-T", "(N) unisex toilet", "4124-O", "Office"],
 ["4118-U", "Tenant space (spate)", "4118-V / 4118-W", "Storage / Office (spate)"]], [0.9*inch, 2.0*inch, 1.9*inch, 2.1*inch])]

s += [P("12. Toalete accesibile (foaia A5.11)", h2), table([
 ["Element", "Specificație"],
 ["Plan 4118-T", "aprox. 7'-10\" x 7'-7\"; cerc de manevră 60\""],
 ["Plan 4124-T", "aprox. 6'-10 1/2\" lățime; cerc de manevră 60\""],
 ["Echipare", "Bare de sprijin 36\" (GB), lavoar LAV-1 American Standard Murro ADA, WC ADA Madera 16 1/2\" înălțime, 1,28 GPF, oglindă, coș șervețele, dispenser hârtie, săpun, uscător de mâini, masă de schimbat bebeluși"],
 ["Finisaj", "Plăci tip cărămidă pe pereți; detalii de montaj în A1.00"]], [1.6*inch, W-1.6*inch])]

s += [P("13. Lista foilor", h2), table([
 ["Foaie", "Nume", "Foaie", "Nume"],
 ["A0.00", "Site Plan", "A2.42", "Proposed RCP"],
 ["A0.51", "Egress Plan", "A3.11", "Building Sections"],
 ["A1.00", "Code / Accessibility Details", "A3.31", "Proposed North & East Elev"],
 ["A1.31", "Existing / Demo Floor Plan", "A3.32", "South & West Elevations"],
 ["A2.31", "Proposed Floor Plan - Level 01", "A5.11", "Enlarged Plan & Interior Elevations"],
 ["A2.32", "Proposed Roof Plan", "A8.01", "Door & Window Schedules, Details"]], [0.8*inch, 2.6*inch, 0.8*inch, 2.7*inch])]

SimpleDocTemplate("MacArthur_Rezumat_Proiect.pdf", pagesize=letter, leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.7*inch, bottomMargin=0.75*inch, title="Rezumat - 4120 MacArthur Facade TI").build(s, onFirstPage=footer, onLaterPages=footer)
print("OK")
