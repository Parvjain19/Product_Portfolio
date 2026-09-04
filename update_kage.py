import os
path = "public/landing-pages/kage.html"
with open(path, "r") as f:
    content = f.read()

content = content.replace("Kage — Where stillness reveals the unseen", "PARV JAIN - Product Management Portfolio")
content = content.replace("Kage", "PARV JAIN")
content = content.replace("KAGE", "PARV JAIN")
content = content.replace("HIDDEN REALMS OF KYOTO", "PRODUCT MANAGEMENT PORTFOLIO")
content = content.replace("Chapter 00 — The Hidden Gate", "PARV JAIN - College")
content = content.replace("A five-chapter night walk through a Kyoto mountain temple.", "A product management portfolio by Parv Jain.")

with open(path, "w") as f:
    f.write(content)
print("Updated kage.html")
