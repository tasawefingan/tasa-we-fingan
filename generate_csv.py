import csv

data = [
    # Category: طاسة 🥘
    [1, "طاسة 🥘", "Tasa 🥘", "كبدة", "Liver", "تقدم مع عيش بلدي + مخلل + طحينة", "Served with baladi bread, pickles & tahini", "100", "", "TRUE", 1],
    [2, "طاسة 🥘", "Tasa 🥘", "سجق", "Sausage", "تقدم مع عيش بلدي + مخلل + طحينة", "Served with baladi bread, pickles & tahini", "100", "", "TRUE", 2],
    [3, "طاسة 🥘", "Tasa 🥘", "هوت دوج", "Hot Dog", "تقدم مع عيش بلدي + مخلل + طحينة", "Served with baladi bread, pickles & tahini", "110", "", "TRUE", 3],
    [4, "طاسة 🥘", "Tasa 🥘", "شيش طاووق", "Shish Tawook", "تقدم مع عيش بلدي + مخلل + طحينة", "Served with baladi bread, pickles & tahini", "135", "", "TRUE", 4],
    [5, "طاسة 🥘", "Tasa 🥘", "فاهيتا فراخ", "Chicken Fajita", "تقدم مع عيش بلدي + مخلل + طحينة", "Served with baladi bread, pickles & tahini", "135", "", "TRUE", 5],
    [6, "طاسة 🥘", "Tasa 🥘", "إضافة موتزاريلا", "Add Mozzarella", "تقدم مع عيش بلدي + مخلل + طحينة", "Served with baladi bread, pickles & tahini", "25", "", "TRUE", 6],

    # Category: ساندوتشات 🌭
    [7, "ساندوتشات 🌭", "Sandwiches 🌭", "كبدة إسكندراني", "Alexandrian Liver", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "60 - 30", "", "TRUE", 7],
    [8, "ساندوتشات 🌭", "Sandwiches 🌭", "سجق إسكندراني", "Alexandrian Sausage", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "60 - 30", "", "TRUE", 8],
    [9, "ساندوتشات 🌭", "Sandwiches 🌭", "كلاوي", "Kidney", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "60 - 30", "", "TRUE", 9],
    [10, "ساندوتشات 🌭", "Sandwiches 🌭", "كفتة", "Kofta", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "95 - 50", "", "TRUE", 10],
    [11, "ساندوتشات 🌭", "Sandwiches 🌭", "سوسيس", "Susis", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "90 - 45", "", "TRUE", 11],
    [12, "ساندوتشات 🌭", "Sandwiches 🌭", "برجر", "Burger", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "100", "", "TRUE", 12],
    [13, "ساندوتشات 🌭", "Sandwiches 🌭", "برجر جبنة وبيض", "Burger with Cheese & Egg", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "115", "", "TRUE", 13],
    [14, "ساندوتشات 🌭", "Sandwiches 🌭", "بانيه فريش", "Fresh Pane", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "90 - 45", "", "TRUE", 14],
    [15, "ساندوتشات 🌭", "Sandwiches 🌭", "كريسبي", "Crispy Chicken", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "100 - 55", "", "TRUE", 15],
    [16, "ساندوتشات 🌭", "Sandwiches 🌭", "شيش طاووق فريش", "Fresh Shish Tawook", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "110 - 55", "", "TRUE", 16],
    [17, "ساندوتشات 🌭", "Sandwiches 🌭", "فاهيتا فراخ فريش", "Fresh Chicken Fajitas", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "110 - 55", "", "TRUE", 17],
    [18, "ساندوتشات 🌭", "Sandwiches 🌭", "زنجر", "Zinger", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "140", "", "TRUE", 18],
    [19, "ساندوتشات 🌭", "Sandwiches 🌭", "اضافة كومبو", "Add combo", "(عيش فرنساوي - عيش فينو)", "(French bread - Feno bread)", "50", "", "TRUE", 19],

    # Category: بطاطس 🍟
    [20, "بطاطس 🍟", "Potatoes 🍟", "(كاتشب و مايونيز عيش فرنساوي) ساندوتش بطاطس", "Fries Sandwich (ketchup and mayonnaise on French bread)", "", "", "40", "", "TRUE", 20],
    [21, "بطاطس 🍟", "Potatoes 🍟", "(عيش فرنساوي) ساندوتش بطاطس بالموتزاريلا", "Fries with Mozzarella(French bread)", "", "", "60", "", "TRUE", 21],
    [22, "بطاطس 🍟", "Potatoes 🍟", "باكت بطاطس", "Fries Box", "", "", "40", "", "TRUE", 22],
    [23, "بطاطس 🍟", "Potatoes 🍟", "باكت بطاطس رانش", "Ranch Fries Box", "", "", "65", "", "TRUE", 23],
    [24, "بطاطس 🍟", "Potatoes 🍟", "بطاطس شيدر", "Cheddar Fries Box", "", "", "70", "", "TRUE", 24],
    [25, "بطاطس 🍟", "Potatoes 🍟", "بطاطس حلزوني", "Curly Fries Box", "", "", "45", "", "TRUE", 25],

    # Category: كريب حادق
    [26, "كريب حادق", "Savory Crepe", "بانيه", "Pane", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "100", "", "TRUE", 26],
    [27, "كريب حادق", "Savory Crepe", "بانيه فريش", "Fresh Pane", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "140", "", "TRUE", 27],
    [28, "كريب حادق", "Savory Crepe", "سوسيس", "Susis", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "110", "", "TRUE", 28],
    [29, "كريب حادق", "Savory Crepe", "كفتة لحم", "Beef Kofta", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "140", "", "TRUE", 29],
    [30, "كريب حادق", "Savory Crepe", "برجر لحم", "Beef Burger", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "145", "", "TRUE", 30],
    [31, "كريب حادق", "Savory Crepe", "فراخ ستربس", "Strips chickens", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "120", "", "TRUE", 31],
    [32, "كريب حادق", "Savory Crepe", "فراخ زنجر", "Zinger chickens", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "155", "", "TRUE", 32],
    [33, "كريب حادق", "Savory Crepe", "شيش طاووق", "Shish Tawook", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "140", "", "TRUE", 33],
    [34, "كريب حادق", "Savory Crepe", "بطاطس", "Fries", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "65", "", "TRUE", 34],
    [35, "كريب حادق", "Savory Crepe", "مزاج طاسة وفنجان (سوسيس + بانيه +كفته)", "Mazag tasa & finjan (sausage + breaded chicken + kofta)", "موتزاريلا + فلفل ألوان + زيتون + صوصات", "Mozzarella, bell peppers, olives & sauces", "170", "", "TRUE", 35],

    # Category: إضافات +
    [36, "إضافات +", "Extras +", "إضافة موتزاريلا", "Add Mozzarella", "", "", "35", "", "TRUE", 36],
    [37, "إضافات +", "Extras +", "إضافة بطاطس", "Add Fries", "", "", "20", "", "TRUE", 37],
    [38, "إضافات +", "Extras +", "إضافة كومبو", "Add Combo", "", "", "50", "", "TRUE", 38],

    # Category: وجبات🍽️
    [39, "وجبات🍽️", "Meals🍽️", "ربع فرخة (ورك)", "Quarter Chicken (Leg)", "يقدم مع ارز بسمتي و سلطة طحينة و مخلل", "Serve with Basmati rice, tahini salad, and pickles", "130", "", "TRUE", 39],
    [40, "وجبات🍽️", "Meals🍽️", "ربع فرخة (صدر)", "Quarter Chicken (Breast)", "يقدم مع ارز بسمتي و سلطة طحينة و مخلل", "Serve with Basmati rice, tahini salad, and pickles", "145", "", "TRUE", 40],
    [41, "وجبات🍽️", "Meals🍽️", "كفتة", "Kofta Meal", "يقدم مع ارز بسمتي و سلطة طحينة و مخلل", "Serve with Basmati rice, tahini salad, and pickles", "145", "", "TRUE", 41],
    [42, "وجبات🍽️", "Meals🍽️", "شيش طاووق", "Shish Tawook", "يقدم مع ارز بسمتي و سلطة طحينة و مخلل", "Serve with Basmati rice, tahini salad, and pickles", "170", "", "TRUE", 42],
    [43, "وجبات🍽️", "Meals🍽️", "شيش طاووق + كفتة", "Shish Tawook + Kofta", "يقدم مع ارز بسمتي و سلطة طحينة و مخلل", "Serve with Basmati rice, tahini salad, and pickles", "215", "", "TRUE", 43],
    [44, "وجبات🍽️", "Meals🍽️", 'نصف فرخة "(ورك + صدر)"', 'Half Chicken "(Hip + Breast)"', "يقدم مع ارز بسمتي و سلطة طحينة و مخلل", "Serve with Basmati rice, tahini salad, and pickles", "240", "", "TRUE", 44],

    # Category: وافل 🧇
    [45, "وافل 🧇", "Waffle 🧇", "وافل مربي", "Jam Waffle", "دولسيك - قالب", "Single or Double", "30 / 45", "", "TRUE", 45],
    [46, "وافل 🧇", "Waffle 🧇", "وافل شوكولاتة", "Chocolate Waffle", "دولسيك - قالب", "Single or Double", "35 / 55", "", "TRUE", 46],
    [47, "وافل 🧇", "Waffle 🧇", "وافل مكس فروت وشوكولاتة", "Mixed Fruit & Chocolate Waffle", "دولسيك - قالب", "Single or Double", "55 / 85", "", "TRUE", 47],
    [48, "وافل 🧇", "Waffle 🧇", "وافل موز وشوكولاتة", "Banana & Chocolate Waffle", "دولسيك - قالب", "Single or Double", "50 / 80", "", "TRUE", 48],
    [49, "وافل 🧇", "Waffle 🧇", "وافل شوكولاتة بيضاء", "White Chocolate Waffle", "دولسيك - قالب", "Single or Double", "45 / 65", "", "TRUE", 49],
    [50, "وافل 🧇", "Waffle 🧇", "وافل لوتس", "Lotus Waffle", "دولسيك - قالب", "Single or Double", "45 / 65", "", "TRUE", 50],
    [51, "وافل 🧇", "Waffle 🧇", "وافل أوريو", "Oreo Waffle", "دولسيك - قالب", "Single or Double", "70", "", "TRUE", 51],
    [52, "وافل 🧇", "Waffle 🧇", "وافل هوهوز", "Hohoz Waffle", "دولسيك - قالب", "Single or Double", "70", "", "TRUE", 52],
    [53, "وافل 🧇", "Waffle 🧇", "وافل بستاشيو", "Pistachio Waffle", "دولسيك - قالب", "Single or Double", "50 / 75", "", "TRUE", 53],

    # Category: كريب حلو
    [54, "كريب حلو", "Sweet Crepe", "شوكولاتة", "Chocolate", "", "", "85", "", "TRUE", 54],
    [55, "كريب حلو", "Sweet Crepe", "شوكولاتة وموز", "Chocolate & Banana", "", "", "100", "", "TRUE", 55],
    [56, "كريب حلو", "Sweet Crepe", "شوكولاتة بيضاء", "White Chocolate", "", "", "100", "", "TRUE", 56]
]

with open("menu_data.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "category_ar", "category_en", "name_ar", "name_en", "description_ar", "description_en", "price", "image_url", "availability", "display_order"])
    writer.writerows(data)
