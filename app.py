"""
Kingdom Millwork (KMW) - Premium Construction & Finish Carpentry Website
Flask Backend Server (Frontend-Only serving layer)
License: LIC# 1150491
"""

from flask import Flask, render_template

app = Flask(__name__)

# Centralized Company Configuration
# Any change here propagates to all templates, headers, footers, meta tags, and schema data
COMPANY = {
    "name": "Kingdom Millwork",
    "monogram": "KMW",
    "license": "LIC# 1150491",
    "license_type": "California State Licensed C-6 Millwork & Class B General Contractor",
    "tagline": "Mastery in Every Cut. Distinction in Every Detail.",
    "subtagline": "Architectural finish carpentry, bespoke cabinetry, and master installation for luxury residences throughout Southern California.",
    "phone": "(949) 555-0188",
    "phone_raw": "+19495550188",
    "email": "concierge@kingdommillwork.com",
    "address_street": "1824 E. Enterprise Way, Suite 100",
    "address_city": "Costa Mesa",
    "address_state": "CA",
    "address_zip": "92626",
    "full_address": "1824 E. Enterprise Way, Suite 100, Costa Mesa, CA 92626",
    "hours_weekday": "Monday – Friday: 7:00 AM – 5:30 PM",
    "hours_weekend": "Saturday: 8:00 AM – 2:00 PM (Showroom by Appt.) | Sunday: Closed",
    "years_experience": 25,
    "projects_completed": "1,250+",
    "google_rating": "4.9",
    "reviews_count": "320+",
    "service_areas": [
        "Newport Beach",
        "Corona del Mar",
        "Laguna Beach",
        "Newport Coast",
        "Irvine & Shady Canyon",
        "Costa Mesa",
        "Dana Point",
        "San Clemente",
        "Huntington Beach",
        "Pasadena & San Marino",
        "Beverly Hills & Bel-Air",
        "Manhattan Beach"
    ],
    "social": {
        "instagram": "https://instagram.com/kingdommillwork",
        "facebook": "https://facebook.com/kingdommillwork",
        "houzz": "https://houzz.com/pro/kingdommillwork",
        "linkedin": "https://linkedin.com/company/kingdommillwork"
    }
}

@app.context_processor
def inject_company():
    return dict(company=COMPANY)

@app.route("/")
def index():
    return render_template("index.html", active_page="home")

@app.route("/services")
def services():
    return render_template("services.html", active_page="services")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", active_page="portfolio")

@app.route("/about")
def about():
    return render_template("about.html", active_page="about")

@app.route("/contact")
def contact():
    return render_template("contact.html", active_page="contact")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", active_page="404"), 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
