import re
from bs4 import BeautifulSoup
import csv

html_content = open("index.html", "r", encoding="utf-8").read()
soup = BeautifulSoup(html_content, "html.parser")

data = []

sections = soup.find_all("section")
for sec in sections:
    h2 = sec.find("h2")
    if not h2 or h2.get_text().strip() == "رأيكم يهمّنا ويساعدنا نطوّر نفسنا 🤍":
        continue
    
    cat_ar = h2.get("data-ar", h2.get_text().strip())
    cat_en = h2.get("data-en", "")
    
    note_div = sec.find("div", class_="note")
    note_ar = ""
    note_en = ""
    if note_div:
        note_ar = note_div.get("data-ar", note_div.get_text().strip())
        note_en = note_div.get("data-en", "")
        
    menu_items = sec.find_all("div", class_="menu-item")
    for item in menu_items:
        spans = item.find_all("span")
        if len(spans) >= 2:
            item_name_span = spans[0]
            item_ar = item_name_span.get("data-ar", item_name_span.get_text().strip())
            item_en = item_name_span.get("data-en", "")
            
            price_span = spans[1]
            price = price_span.get_text().strip()
            
            data.append({
                "Category_AR": cat_ar,
                "Category_EN": cat_en,
                "Note_AR": note_ar,
                "Note_EN": note_en,
                "Item_AR": item_ar,
                "Item_EN": item_en,
                "Price": price
            })

with open("menu_extracted.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Category_AR", "Category_EN", "Note_AR", "Note_EN", "Item_AR", "Item_EN", "Price"])
    writer.writeheader()
    writer.writerows(data)

print("Extracted", len(data), "items.")
