import html

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
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        escaped = html.escape(content, quote=True)
        out.write(f'    <iframe title="{title}" srcdoc=\'{escaped}\'></iframe>\n')
    out.write(footer)
