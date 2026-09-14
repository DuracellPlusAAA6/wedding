#!/usr/bin/env python3
from PIL import Image
import os

# Input and output paths
church_input = 'assets/images/optimized/OIP.lV_zTfnOXEo41hYd6vYyqgHaET_optimized.jpg'
church_output = 'assets/images/optimized/OIP.lV_zTfnOXEo41hYd6vYyqgHaET_400x300.jpg'

venue_input = 'assets/images/optimized/Nunta-in-aer-liber-Liria-events-Lacul-Aroneanu-cort-nunti-cort-evenimente-nunta-la-cort-botez-iasi-corporate-1-400x300_optimized.jpg'
venue_output = 'assets/images/optimized/Nunta-in-aer-liber-Liria-events-Lacul-Aroneanu-cort-nunti-cort-evenimente-nunta-la-cort-botez-iasi-corporate-1-400x300.jpg'  # Overwrite or save new

# Target size
target_size = (400, 300)

def resize_and_crop(input_path, output_path):
    img = Image.open(input_path)
    
    # Resize to maintain aspect ratio, then crop to target size
    img.thumbnail((target_size[0] * 2, target_size[1] * 2))  # Upscale if needed
    width, height = img.size
    
    # Crop to center
    left = (width - target_size[0]) / 2
    top = (height - target_size[1]) / 2
    right = (width + target_size[0]) / 2
    bottom = (height + target_size[1]) / 2
    
    img = img.crop((left, top, right, bottom))
    img.save(output_path, quality=85)
    print(f'Saved: {output_path} ({img.size})')

# Resize and crop both images
resize_and_crop(church_input, church_output)
resize_and_crop(venue_input, venue_output)

print('Done!')