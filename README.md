# Kingdom Millwork (KMW) — Luxury Construction & Architectural Millwork Website

A complete, premium, multi-section website for **Kingdom Millwork** (California License #1150491), a luxury US-based fine woodworking, custom cabinetry, and architectural finish carpentry firm headquartered in Costa Mesa, California.

---

## 🌐 Live Website (GitHub Pages)

The website is fully exported to standalone static HTML/CSS/JS and ready to be viewed directly online without installing anything:

👉 **Live URL**: [https://mat626.github.io/kingdom-millwork/](https://mat626.github.io/kingdom-millwork/)

### One-Click Activation on GitHub:
1. Go to repository **Settings** &rarr; **Pages** (or visit [https://github.com/Mat626/kingdom-millwork/settings/pages](https://github.com/Mat626/kingdom-millwork/settings/pages))
2. Under **Build and deployment** &gt; **Source**, choose **Deploy from a branch**
3. Under **Branch**, select **`main`** and **`/ (root)`**, then click **Save**
4. In about 60 seconds, your site will be live and viewable by anyone on desktop, tablet, and mobile!

---

## Brand & Design Foundation

- **Company Name**: Kingdom Millwork (KMW)
- **License**: CSLB LIC# 1150491 (C-6 Cabinet, Millwork & Finish Carpentry / Class B General Contractor)
- **Tagline**: *Mastery in Every Cut. Distinction in Every Detail.*
- **Palette**: Deep Obsidian Black (`#070709`), Warm Gold Accents (sampled directly from the official logo: `#F6D763`, `#D4AF37`, `#B58111`), Chrome / Polished Silver (`#E0E0E8`), and Architectural Warm Linen (`#F8F7F4`).
- **Typography**: Editorial serif headings (*Playfair Display*) paired with clean geometric body text (*Inter*) via Google Fonts.
- **Imagery**: Custom photorealistic high-resolution architectural interior photography, real before/after pair, and craftsman workshop portraits.

---

## Key Features & Polish

1. **Multi-Page Architecture**:
   - **Home (`/`)**: Full-screen slow-zoom hero with dual CTAs, trust stats bar with live animated counters, 3 core discipline cards with hover zoom, interactive before/after kitchen transformation slider, curated portfolio preview, why choose us pillars, 4-step precision process timeline, testimonials carousel, Southern California service area coverage, and final CTA banner.
   - **Services (`/services`)**: Deep technical breakdowns of Installation, Finish Carpentry, and Custom Cabinets, complete with material specifications, Blum hardware details, wood species showcase (White Oak, Walnut, Maple, Brass), and an interactive FAQ accordion.
   - **Portfolio / Gallery (`/portfolio`)**: Filterable project gallery (All, Cabinets, Finish Carpentry, Installation) with interactive lightbox modal displaying project photography, scope, materials used, and quick inquiry buttons.
   - **About (`/about`)**: 25-year company heritage story, 4 core values (Mastery, Integrity, Precision, Respect), leadership team portraits (Marcus Vance, Elena Rostova, David Chen), and verified licensing/insurance credentials.
   - **Contact / Quote (`/contact`)**: Polished quote request form with US phone number mask `(XXX) XXX-XXXX`, service selectors, budget brackets, simulated architectural blueprint upload dropzone, live client-side validation, and instant animated confirmation modal with unique reference ID (`KMW-XXXXX`). Includes workshop details and styled SVG coverage map.
   - **Custom 404 (`/404`)**: Themed error page with quick navigation back to core sections.
2. **Interactive UI Polish**:
   - Draggable Before / After image comparison slider with touch and mouse support.
   - Sticky header with glassmorphism blur that condenses smoothly on scroll.
   - Mobile slide-in drawer with hamburger animation and ESC key accessibility.
   - Floating mobile "Call Now" and "Free Quote" bottom quick-action bar.
   - Animated number counters triggered when trust bar scrolls into view.
   - LocalBusiness Schema.org JSON-LD structured data for US local SEO.

---

## File Structure

```
construction/
├── app.py                      # Minimal Flask application serving all routes
├── export_static.py            # Static site generator for GitHub Pages
├── requirements.txt            # Python dependencies (Flask >= 3.0.0)
├── README.md                   # Setup & documentation
├── templates/
│   ├── base.html               # Master layout (Header, Drawer, Footer, Lightbox, SEO)
│   ├── index.html              # Homepage
│   ├── services.html           # Detailed services & material showcase
│   ├── portfolio.html          # Filterable project gallery with lightbox
│   ├── about.html              # Heritage, values & team
│   ├── contact.html            # Interactive quote request form & map
│   └── 404.html                # Custom error page
└── static/
    ├── css/
    │   └── style.css           # Master stylesheet with CSS variables & responsive design
    ├── js/
    │   └── main.js             # Vanilla JS interactions (No heavy frameworks required)
    ├── images/
    │   ├── logo.jpg            # Original company logo
    │   ├── logo-transparent.png# Anti-aliased transparent company logo
    │   ├── favicon.png         # Browser favicon
    │   ├── hero-luxury-kitchen.jpg
    │   ├── service-installation.jpg
    │   ├── service-carpentry.jpg
    │   ├── service-cabinets.jpg
    │   ├── before-kitchen.jpg
    │   ├── after-kitchen.jpg
    │   ├── project-library.jpg
    │   ├── project-staircase.jpg
    │   ├── project-vanity.jpg
    │   ├── project-wine-cellar.jpg
    │   ├── project-entryway.jpg
    │   ├── about-workshop.jpg
    │   ├── team-marcus.jpg
    │   ├── team-elena.jpg
    │   ├── team-david.jpg
    │   ├── material-white-oak.jpg
    │   ├── material-walnut.jpg
    │   ├── material-maple.jpg
    │   └── material-brass.jpg
    └── favicon.ico
```

---

## Quick Start & Run Instructions

### 1. Requirements
- Python 3.9+
- Pip

### 2. Installation
Open a terminal in the project directory:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Server
```bash
python app.py
```

### 4. Open in Browser
Navigate to:
```
http://127.0.0.1:5000
```

---

## Centralized Company Configuration
To modify the company name, phone number, address, license number, or service areas in one place, simply edit the `COMPANY` dictionary located at the top of `app.py`. All templates, footers, headers, metadata, and JSON-LD schema automatically consume this object.
