import fitz  # PyMuPDF
from PIL import Image, ImageChops

def trim_with_margin(image, margin=30):
    """Обрезает пустое пространство, оставляя margin пикселей по краям."""
    # Находим границы содержимого 
    bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    
    if not bbox:
        return image  # Если нет пустого пространства
    
    # Расширяем bbox, добавляя margin, но не выходя за границы изображения
    x0, y0, x1, y1 = bbox
    x0 = max(0, x0 - margin)
    y0 = max(0, y0 - margin)
    x1 = min(image.width, x1 + margin)
    y1 = min(image.height, y1 + margin)
    
    return image.crop((x0, y0, x1, y1))

def pdf_to_trimmed_png(pdf_path, output_prefix):
    pdf = fitz.open(pdf_path)
    for i, page in enumerate(pdf):
        pix = page.get_pixmap(dpi=150)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_trimmed = trim_with_margin(img)  # Обрезка пустого пространства
        img_trimmed.save(f"{output_prefix}_{i+1}.png")
    pdf.close()

for name in ["_pl_", "_st_"]:
    for n in range(1, 13):
        pdf_to_trimmed_png(rf"D:\geoma_bot\pdfs\fig{name}{n}.pdf", rf"D:\geoma_bot\pictures\pic{name}{n}")