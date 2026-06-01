import os
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

# Remove all sections except feedback and rewrite index.html
# We will just replace everything between </header> and <section class="feedback-cute-force fade-up">
# with <main id="menu-container"></main>

new_content = re.sub(r'</header>.*?(<section class="feedback-cute-force fade-up">)', r'</header>\n\n<main id="menu-container"></main>\n\n\1', content, flags=re.DOTALL)

# Replace <style>...</style> with <link rel="stylesheet" href="style.css">
new_content = re.sub(r'<style>.*?</style>', r'<link rel="stylesheet" href="style.css">', new_content, flags=re.DOTALL)

# Remove the inline scripts for toggleLanguage, form, and observer since they go to app.js
new_content = re.sub(r'<script>.*?</script>', '', new_content, flags=re.DOTALL)

# Add script tags before </body>
script_tags = '\n<script src="config.js"></script>\n<script src="app.js"></script>\n'
new_content = new_content.replace('</body>', script_tags + '</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
