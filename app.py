from PIL import Image, ImageEnhance

def convert_image_to_color_ascii(image_path="krishna.jpg", new_width=160):
    # Detailed ASCII Character Set
    ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrftj1i]|()1{}[]?-+~<>i!lI;:,\"^`'. "

    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # Image Clarity Increase (Contrast & Sharpness Enhance)
    img = ImageEnhance.Contrast(img).enhance(1.8)
    img = ImageEnhance.Sharpness(img).enhance(2.0)

    # High Resolution Aspect Ratio Adjustment
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.5)
    
    img_resized = img.resize((new_width, new_height))
    img_gray = img_resized.convert("L")

    pixels_color = list(img_resized.getdata())
    pixels_gray = list(img_gray.getdata())

    # HTML Code Generation (Colored ASCII Output)
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                background-color: #050b14;
                font-family: 'Courier New', monospace;
                font-size: 7px;
                line-height: 5px;
                letter-spacing: 1px;
                white-space: pre;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }}
        </style>
    </head>
    <body><div>"""

    num_chars = len(ASCII_CHARS)
    for i in range(len(pixels_gray)):
        if i > 0 and i % new_width == 0:
            html_content += "<br/>"
        
        # Color & Character Mapping
        r, g, b = pixels_color[i][:3]
        char = ASCII_CHARS[pixels_gray[i] * (num_chars - 1) // 255]
        html_content += f'<span style="color: rgb({r},{g},{b});">{char}</span>'

    html_content += "</div></body></html>"

    with open("krishna_colored_art.html", "w") as file:
        file.write(html_content)

    print("\nColored High-Detail Art 'krishna_colored_art.html' file mein save ho gayi hai!")

convert_image_to_color_ascii()