from PIL import Image
from collections import Counter

def get_dominant_color(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        img = img.resize((50, 50))  # Resize to speed up processing
        pixels = list(img.getdata())
        # Filter out transparent pixels if any (though we converted to RGB)
        # simplistic approach: most common color
        counts = Counter(pixels)
        most_common = counts.most_common(1)[0][0]
        return "#{:02x}{:02x}{:02x}".format(most_common[0], most_common[1], most_common[2])
    except Exception as e:
        return str(e)

image_path = r"C:/Users/Nneka/.gemini/antigravity/brain/e3a0980a-113e-4df6-addf-40cc8220a44e/uploaded_image_1765152925703.png"
print(get_dominant_color(image_path))
