"""Genereaza fisele de lucru (Week 03-06) pentru proiectul 4120 MacArthur Facade TI."""
import io, sys, subprocess, os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PIL import Image

SRC = "/root/.claude/uploads/0fb19c51-1548-587f-858c-9317acef7479/d1c614c0-4118_MacArthur_TI_CD_Checkset_08.28.26.pdf"
TMP = "/tmp/claude-0/-home-user-Sorinol/0fb19c51-1548-587f-858c-9317acef7479/scratchpad/hi"
OUT = "/home/user/Sorinol/fise/MacArthur_Fise_Week03-06.pdf"
os.makedirs(TMP, exist_ok=True)
subprocess.run(["pdftoppm", "-r", "200", "-png", SRC, f"{TMP}/p"], check=True)

W, H = landscape(letter)
M = 0.5 * inch

def crop(page, fx0, fy0, fx1, fy1):
    im = Image.open(f"{TMP}/p-{page:02d}.png")
    w, h = im.size
    return im.crop((int(fx0*w), int(fy0*h), int(fx1*w), int(fy1*h)))

def header(c, title):
    c.setFont("Helvetica-Bold", 13); c.drawString(M, H-M, title)
    c.setFont("Helvetica", 8.5)
    c.drawRightString(W-M, H-M, "CMCE 2410 - Construction Documents III")
    c.drawRightString(W-M, H-M-11, "New York City College of Technology")
    c.setLineWidth(0.7); c.line(M, H-M-16, W-M, H-M-16)

def text(c, x, y, lines, size=9.5, lead=12.5, maxw=None):
    c.setFont("Helvetica", size)
    for ln in lines:
        if ln.startswith("# "):
            c.setFont("Helvetica-Bold", size); c.drawString(x, y, ln[2:]); c.setFont("Helvetica", size)
        else:
            c.drawString(x, y, ln)
        y -= lead
    return y

from reportlab.lib.utils import simpleSplit
def para(c, x, y, txt, size=9, lead=12, width=None):
    width = width or (W - 2*M)
    c.setFont("Helvetica", size)
    for ln in simpleSplit(txt, "Helvetica", size, width):
        c.drawString(x, y, ln); y -= lead
    return y

def image(c, im, x, top, w, h):
    """Draw image anchored to top-left inside box (x, top, w, h). Returns bottom y."""
    iw, ih = im.size; s = min(w/iw, h/ih)
    c.drawImage(ImageReader(im), x, top - ih*s, iw*s, ih*s)
    return top - ih*s

c = canvas.Canvas(OUT, pagesize=landscape(letter))
c.setTitle("4120 MacArthur Facade TI - Worksheets Week 03-06")
INTRO = "Project: 4120 MacArthur Facade TI, 4118-4124 MacArthur Blvd, Oakland CA (source: Studio 144 Architects CD checkset 08.28.26)"

# ---------- Week 03 : Survey ----------
header(c, "EXISTING BUILDING LAYOUT - SURVEY (Week 03)")
y = para(c, M, H-M-32, INTRO, 8.5, 11)
y = para(c, M, y, "Below is the existing ground-floor plan of the building (sheet A1.31). Document the existing conditions in Revit before any demolition or renovation. Dimensions on the sheet are given to the interior face of the walls unless otherwise noted.", 9, 12)
TOP = y - 6
image(c, crop(4, .22, .22, .63, .86), M, TOP, 5.4*inch, TOP - M)
text(c, M+5.7*inch, TOP-8, [
 "# Set up",
 "- Levels: MAIN LEVEL - 01 = 0'-0\";",
 "  TOP OF GARAGE = 11'-1 1/2\"; EYEBROW LEVEL =",
 "  10'-10 1/2\"; TOP OF PARAPET = 18'-10\".",
 "- Work from the Imperial template, units in feet-inches.",
 "",
 "# Spaces to model (names as on sheet)",
 "- Tenant spaces 4118, 4120, 4122, 4124 (front, along",
 "  MacArthur Blvd, west side)",
 "- Rear: 4118-U (tenant space), 4118-V (storage),",
 "  4118-W (office)",
 "- Existing toilets 4120-T and 4122-T; rear corridor",
 "",
 "# Key dimensions (verify on A1.31)",
 "- Tenant depths N-S: 18'-11 1/2\", 18'-10\", 17'-7\",",
 "  18'-5 1/2\"",
 "- Length along 4120: 55'-2 1/2\"   South wall: 52'-2\"",
 "- Rear corridor width: 8'-10 1/2\"",
 "- 4118-U: 17'-2 1/2\" N-S",
 "",
 "Note: the west (street) wall is not square to the",
 "others - it is skewed. Model it from the dimensions,",
 "do not assume 90 degrees.",
], 8.8, 11.5)
c.showPage()

# ---------- Week 03 : Demolition ----------
header(c, "EXISTING BUILDING LAYOUT - DEMOLITION PLAN (Week 03)")
y = para(c, M, H-M-32, "Existing / Demo floor plan (A1.31). Items shown in RED are to be demolished; gray elements remain. Each student ends the class with an Existing Plan, a Demolition Plan and a Construction Plan. Week 04 puts them on sheets.", 9, 12)
TOP = y - 6
image(c, crop(4, .22, .22, .63, .86), M, TOP, 5.4*inch, TOP - M)
text(c, M+5.7*inch, TOP-8, [
 "# Steps",
 "1. Duplicate the Existing Plan view twice and rename:",
 "   'DEMO - LEVEL 1 PLAN' and 'PROPOSED - LEVEL 1 PLAN'.",
 "2. Create Phases: 'Existing' and 'New Construction'.",
 "3. Put all surveyed elements in the 'Existing' phase.",
 "4. In the Demo view, use the Demolish tool on:",
 "   - the street (west) facade wall and its doors",
 "   - the rear toilet enclosure at 4118",
 "   - parts of the rear/corridor walls around 4120 and",
 "     the door openings in the rear corridor wall",
 "   - the rear toilet and door at 4118-U",
 "5. Set the Phase Filter so demolished items show",
 "   red/dashed.",
 "6. Add dimension strings and room tags as on the sheet.",
 "",
 "Check: the Demo view must show the same room names and",
 "numbers as the Existing view (4118, 4120, 4122, 4124,",
 "4118-U / V / W).",
], 8.8, 11.5)
c.showPage()

# ---------- Week 04 : Walls ----------
header(c, "EXISTING BUILDING LAYOUT - REVIT WALLS (Week 04)")
y = para(c, M, H-M-32, INTRO, 8.5, 11)
y = para(c, M, y, "Translate the survey into Revit. Walls are set to their actual thickness while all dimensions stay as in the survey. This building is wood-framed (wood truss roof; party walls act as bearing walls; the facade is NOT bearing).", 9, 12)
TOP = y - 6
image(c, crop(12, .35, .66, .71, .93), M, TOP, 5.5*inch, TOP - M)
text(c, M+5.7*inch, TOP-8, [
 "# Wall types (A8.01 - Wall Types Legend)",
 "- WALL TYPE 1A / 1B: interior non-rated partition",
 "    5/8\" gyp. bd. + 2x4 wood studs @ 16\" o.c. + 5/8\" gyp.",
 "    1A adds thermal & acoustic batt insulation and 1/2\"",
 "    cement board (Durock) on the bathroom side, tile as",
 "    scheduled on A5.11.",
 "- WALL TYPE 3: same as 1A with 2x6 studs.",
 "- Existing party walls and rear walls: keep as surveyed",
 "  (gray on A1.31).",
 "- New west facade: exterior plaster on plywood; existing",
 "  thin-brick finish removed and replaced with stucco at",
 "  the end walls.",
 "",
 "# Do",
 "- Duplicate Basic Wall types; name them 1A, 1B, 3 and",
 "  'Ext. Plaster on Plywood'; edit layers in Edit Type.",
 "- Set location lines so dimensions hit the right face.",
 "",
 "Note: no 2HR walls on this project; the new rear exit",
 "corridor is required to be 1-hour rated (see A0.00 scope).",
], 8.8, 11.5)
c.showPage()

# ---------- Week 04 : Curtain wall / storefront ----------
header(c, "RENOVATED LAYOUT - FACADE OPENINGS / STOREFRONT (Week 04)")
y = para(c, M, H-M-32, "Follow along in class to complete the new street facade (West elevation, A3.32). Pay close attention to dimensions and alignment.", 9, 12)
TOP = y - 6
bot = image(c, crop(10, .12, .63, .84, .96), M, TOP, W-2*M, 3.4*inch)
text(c, M, bot-14, [
 "# Openings at the shops (from the elevation)",
 "- Shop 4118: 13'-9\"   Shop 4120: 14'-5\"   Shop 4122: 15'-3\"   Shop 4124: 13'-9 1/2\"   (3'-0\" between openings)",
 "- Door types (A8.01): A = exterior front door, 36\" x 80\" wood, dual glazed lite. D1-D3 = ceiling roll-down security grille",
 "  (13'-9\", 14'-5\", 15'-3\" wide x 10'-10 1/2\" high).  Window 1: fixed 24\" x 63\".  Window 2: awning 36\" x 18\".",
 "- Levels: Main 0'-0\", Eyebrow 10'-10 1/2\", Top of Garage 11'-1 1/2\", Top of Parapet 18'-10\".",
 "Use Curtain Wall: Storefront (or the Curtain Wall Dbl/Sgl Glass families from the Imperial Library) for the shop openings.",
], 8.6, 11.5)
c.showPage()

# ---------- Week 05 : RCP ----------
header(c, "RENOVATED LAYOUT - RCP (Week 05)")
y = para(c, M, H-M-32, "Follow along in class to produce a Reflected Ceiling Plan (sheet A2.42). Load from the Imperial Library: Downlight Recessed Can 6\" | Ceiling Light Linear Box 1'x4' | Pendant Light Linear 2 Lamp 48\" | Square Supply Diffuser 12\"/24\" | Square Return Register 12\"/24\"", 8.8, 11.5)
TOP = y - 6
image(c, crop(7, .26, .22, .66, .94), M, TOP, 5.2*inch, TOP - M)
text(c, M+5.5*inch, TOP-8, [
 "# What the sheet shows",
 "- Ceiling height C-1: 8'-6\" A.F.F., tagged where called out.",
 "- Rooms: tenant spaces 4118-4124, offices 4122-O / 4124-O,",
 "  storage 4122-S, hallway 4122-H, massage room 4120-M,",
 "  break room 4120-BR, toilets (E) 4120-T, (E) 4122-T,",
 "  (N) unisex 4124-T, rear 4118-U / V / W.",
 "- Callout: '(N) rear upper walls to connect to (E) lower",
 "  roof to remain'.",
 "",
 "# Steps",
 "1. Create 'PROPOSED LEVEL 1 - RCP' from the ceiling plan.",
 "2. Add ceilings with the sketch tool, height offset 8'-6\".",
 "3. Place fixtures and diffusers/registers from the course",
 "   list, aligned to room centers.",
 "4. Add ceiling-height tags and room tags.",
 "",
 "The checkset sheet has no fixture layout: the fixture",
 "positions are left to you, as in the course exercise.",
], 8.6, 11.2)
c.showPage()

# ---------- Week 06 : replacement for stair ----------
header(c, "RENOVATED LAYOUT - SECTIONS, TOILETS AND DETAILS (Week 06)")
y = para(c, M, H-M-32, "This building is single storey, so there is no stair. Week 06 is replaced with the sections and enlarged views on A3.11, A5.11 and A8.01.", 9, 12)
TOP = y - 6
bot = image(c, crop(8, .03, .06, .72, .26), M, TOP, W-2*M, 1.8*inch)
TOP2 = bot - 10
image(c, crop(11, .02, .03, .72, .36), M, TOP2, 5.6*inch, TOP2 - M)
text(c, M+5.8*inch, TOP2-8, [
 "# Tasks",
 "1. Section through the rear corridor, Demo and",
 "   Proposed versions (A3.11), 1/8\" = 1'-0\".",
 "2. Enlarged toilet plans 4118-T (7'-10\" x 7'-7\") and",
 "   4124-T (6'-10 1/2\" wide), 1/2\" = 1'-0\", with 60\"",
 "   turning circle, grab bars, LAV-1, WC, mirror, napkin",
 "   disposal, TPD, soap dispenser, hand dryer, baby",
 "   changing station.",
 "3. Interior elevations 3-10 with brick-pattern finish.",
 "4. Parapet coping and BUR flashing detail, 3\" = 1'-0\".",
 "5. Door and window legend from A8.01.",
], 8.6, 11.2)
c.showPage()
c.save()
print("OK", OUT)
