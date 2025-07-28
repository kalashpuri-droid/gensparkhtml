import html

def placeholder_html(title: str) -> str:
    """Return minimal placeholder slide with the common blue header."""
    return f"""
<!DOCTYPE html>
<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\" />\n    <title>{title}</title>\n    <style>\n        body {{ margin: 0; font-family: Arial, sans-serif; width: 1280px; height: 720px; }}\n        .top-bar {{ height: 7px; background-color: #007abc; }}\n        .content {{ display: flex; align-items: center; justify-content: center; height: calc(100% - 7px); color: #666; }}\n    </style>\n</head>\n<body>\n    <div class=\"top-bar\"></div>\n    <div class=\"content\">{title} Placeholder</div>\n</body>\n</html>
"""

slides = [
    ("Title Slide/index.html", "Title Slide"),
    ("Category Overview/index .html", "Category Overview"),
    ("Competitve Landscape/index.html", "Competitive Landscape"),
    ("Regional Distribution/index.html", "Regional Distribution"),
    ("Pack Size Analysis/index.html", "Pack Size Analysis"),
    ("Price Band Segmentation/index (1).html", "Price Band Segmentation"),
    ("Availability and Listing/index (1).html", "Listing and Availability"),
    ("SOV analysis/index.html", "SOV Analysis"),
]

# Slides that should be rendered with placeholder content instead of the
# original HTML.
placeholder_titles = {
    "Regional Distribution",
    "Pack Size Analysis",
    "Price Band Segmentation",
    "Listing and Availability",
    "SOV Analysis",
}

header = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\" />
    <title>Complete Presentation</title>
    <style>
        body { margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f0f0f0; }
        iframe { border: none; width: 1280px; height: 720px; display: block; margin: 0 auto 20px; }
    </style>
</head>
<body>
"""
footer = "</body>\n</html>\n"

with open("FullPresentation.html", "w", encoding="utf-8") as out:
    out.write(header)
    for path, title in slides:
        if title in placeholder_titles:
            content = placeholder_html(title)
        else:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        escaped = html.escape(content, quote=True)
        out.write(f'    <iframe title="{title}" srcdoc=\'{escaped}\'></iframe>\n')
    out.write(footer)
