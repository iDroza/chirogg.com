"""Export the presentation-only page after npm run build, with npm run dev running.
Usage: python scripts/export-static.py [http://localhost:3000/]
The output intentionally needs no JavaScript: navigation and email links are native.
"""
from pathlib import Path
from urllib.request import urlopen
import re, shutil, sys
root=Path(__file__).resolve().parents[1]
html=urlopen(sys.argv[1] if len(sys.argv)>1 else 'http://localhost:3000/').read().decode()
assert 'Great care.' in html and 'ads@chirogg.com' in html
html=re.sub(r'<script\b[^>]*>.*?</script>','',html,flags=re.S)
html=re.sub(r'<link\b[^>]*rel="(?:modulepreload|preload|stylesheet)"[^>]*>','',html)
html=re.sub(r'<style\b[^>]*>.*?</style>','',html,flags=re.S)
html=html.replace('</head>','<link rel="stylesheet" href="/site.css"/><link rel="canonical" href="https://chirogg.com/"/></head>')
css=list((root/'dist/client/_next/static/css').glob('*.css'))
assert len(css)==1,'Run npm run build first'
(root/'index.html').write_text(html,encoding='utf-8')
shutil.copy2(css[0],root/'site.css')
shutil.copytree(root/'public/images',root/'images',dirs_exist_ok=True)
shutil.copy2(root/'public/favicon.svg',root/'favicon.svg')
print('Exported standalone homepage, stylesheet, favicon and photos.')
