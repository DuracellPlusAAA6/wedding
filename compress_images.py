#!/usr/bin/env python3
from PIL import Image
import os

# Input and output directories
input_dir = "assets/images"
output_dir = "assets/images/optimized"
os.makedirs(output_dir, exist_ok=True)

# Compress images
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_optimized.jpg")
        
        try:
            img = Image.open(input_path)
            # Resize if larger than 1200px
            if img.width > 1200:
                ratio = 1200 / img.width
                new_height = int(img.height * ratio)
                img = img.resize((1200, new_height), Image.LANCZOS)
            
            # Convert PNG with alpha to JPEG (white background)
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            
            # Save as JPEG with 80% quality
            img.save(output_path, "JPEG", quality=80, optimize=True)
            print(f"Compressed {filename} -> {output_path}")
        except Exception as e:
            print(f"Failed to compress {filename}: {e}")