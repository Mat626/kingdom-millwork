"""
Kingdom Millwork - Static Site Generator for GitHub Pages
Renders all Jinja2 templates into standalone, statically hostable HTML files.
"""

import os
import re
import app

def build_static_site(output_dir="."):
    client = app.app.test_client()
    
    pages = {
        "index.html": "/",
        "services.html": "/services",
        "portfolio.html": "/portfolio",
        "about.html": "/about",
        "contact.html": "/contact",
        "404.html": "/404"
    }
    
    os.makedirs(output_dir, exist_ok=True)
    
    for filename, route in pages.items():
        res = client.get(route)
        if res.status_code not in (200, 404):
            print(f"Error fetching {route}: {res.status_code}")
            continue
            
        html = res.data.decode("utf-8")
        
        # Convert Flask routes to relative static links
        html = re.sub(r'href="/"', 'href="index.html"', html)
        html = re.sub(r'href="/services"', 'href="services.html"', html)
        html = re.sub(r'href="/services#', 'href="services.html#', html)
        html = re.sub(r'href="/portfolio"', 'href="portfolio.html"', html)
        html = re.sub(r'href="/about"', 'href="about.html"', html)
        html = re.sub(r'href="/about#', 'href="about.html#', html)
        html = re.sub(r'href="/contact"', 'href="contact.html"', html)
        html = re.sub(r'href="/contact\?', 'href="contact.html?', html)
        html = re.sub(r'href="/contact#', 'href="contact.html#', html)
        
        # Convert static asset URLs to relative paths
        html = re.sub(r'href="/static/', 'href="static/', html)
        html = re.sub(r'src="/static/', 'src="static/', html)
        html = re.sub(r'content="/static/', 'content="static/', html)
        html = html.replace('http://localhost/static/', 'static/')
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
            
        print(f"Generated {filepath} ({len(html):,} bytes)")

if __name__ == "__main__":
    build_static_site()
