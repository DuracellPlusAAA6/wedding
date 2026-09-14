# Wedding Website Development Documentation

**Repository**: [https://github.com/DuracellPlusAAA6/wedding](https://github.com/DuracellPlusAAA6/wedding)
**Last Updated**: 14 September 2026

---

## **1. Overview**
This documentation covers all the changes made to the **wedding website** for **Alexandra & Bruno**, including:
- Text updates (names, dates, locations).
- Navbar flags (SVG integration).
- Image resizing and consistency.
- GitHub commits and deployments.

---

## **2. Changes Made**

### **2.1. Text Updates**
#### **Objective**
- Swap all instances of `Bruno & Alexandra` to `Alexandra & Bruno`.
- Add the date (`10 September 2027 | Iași, Romania`) to key pages.

#### **Files Modified**
| File | Change |
|------|--------|
| `index.html` | Updated `<title>`, hero section (`<h1>`), and footer. |
| `contact.html` | Updated `<title>`, team section, and footer. |
| `plan.html` | Updated `<title>` to include date (`Schedule - 10 September 2027 | Alexandra & Bruno`). |
| `info.html` | Added `10 September 2027 | Iași, Romania` to the top. |
| `plan.html` | Added `10 September 2027 | Iași, Romania` to the top. |

#### **Rationale**
- Ensure consistency in branding across all pages.
- Highlight the wedding date and location prominently.

---

### **2.2. Navbar Flags**
#### **Objective**
- Replace local PNG flags with **SVG flags** from [flagicons.lipis.dev](https://flagicons.lipis.dev).
- Ensure flags are visible on all pages.

#### **Flags Used**
| Language | SVG URL |
|----------|---------|
| Portuguese (PT) | `https://flagicons.lipis.dev/flags/4x3/pt.svg` |
| English (EN) | `https://flagicons.lipis.dev/flags/4x3/gb.svg` |
| Romanian (RO) | `https://flagicons.lipis.dev/flags/4x3/ro.svg` |

#### **Files Modified**
| File | Change |
|------|--------|
| All HTML files (`index.html`, `contact.html`, `plan.html`, etc.) | Replaced `<img>` tags with SVG URLs. |
| `assets/css/style.css` | Updated CSS for SVG flags (width, height, alignment). |

#### **Rationale**
- SVG flags are **scalable, high-quality, and load faster** than PNGs.
- Ensures consistency across all devices and screen sizes.

---

### **2.3. Image Resizing**
#### **Objective**
- Resize the **church** and **venue** images on the homepage to `400x300` for consistency.

#### **Files Modified**
| File | Change |
|------|--------|
| `index.html` | Updated `<img>` tags to reference resized images. |
| `assets/images/optimized/` | Resized `OIP.lV_zTfnOXEo41hYd6vYyqgHaET_optimized.jpg` and `Nunta-in-aer-liber-Liria-events-Lacul-Aroneanu-cort-nunti-cort-evenimente-nunta-la-cort-botez-iasi-corporate-1-400x300_optimized.jpg` to `400x300`. |

#### **Script Used**
```python
#!/usr/bin/env python3
from PIL import Image

def resize_and_crop(input_path, output_path, target_size=(400, 300)):
    img = Image.open(input_path)
    img.thumbnail((target_size[0] * 2, target_size[1] * 2))  # Upscale if needed
    width, height = img.size
    
    # Crop to center
    left = (width - target_size[0]) / 2
    top = (height - target_size[1]) / 2
    right = (width + target_size[0]) / 2
    bottom = (height + target_size[1]) / 2
    
    img = img.crop((left, top, right, bottom))
    img.save(output_path, quality=85)
```

#### **Rationale**
- Ensures **visual consistency** across the homepage.
- Improves loading performance with optimized images.

---

### **2.4. GitHub Commits**
#### **Commits Summary**
| Commit Hash | Message | Date |
|-------------|---------|------|
| `2be3284` | Fix flags visibility on all pages and add date/location to wedding and schedule pages | 14 Sep 2026 |
| `eb1f44b` | Update navbar flags to use SVG from flagicons.lipis.dev | 14 Sep 2026 |
| `6b4cc93` | Update names to Alexandra & Bruno, add date to schedule, move flags to navbar, and resize church/venue images to 400x300 for consistency | 14 Sep 2026 |

#### **How to Deploy**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DuracellPlusAAA6/wedding.git
   cd wedding
   ```
2. **Preview Locally**:
   ```bash
   xdg-open index.html
   ```
3. **Push Changes**:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push
   ```

---

## **3. Future Updates**
### **3.1. Adding New Pages**
1. Create a new HTML file (e.g., `accommodation.html`).
2. Copy the navbar and footer from an existing page.
3. Update the flags and CSS as needed.

### **3.2. Updating Images**
1. Use the `resize_images.py` script to resize new images.
2. Update the `<img>` tags in the HTML files.

### **3.3. Changing Text**
1. Use the `edit` tool or a text editor to update HTML files.
2. Commit and push changes to GitHub.

---

## **4. Troubleshooting**
### **4.1. Flags Not Visible**
- **Cause**: CSS caching or missing `!important` rules.
- **Fix**: Hard refresh (`Ctrl + F5`) or clear browser cache.

### **4.2. Images Not Loading**
- **Cause**: Incorrect file paths or missing images.
- **Fix**: Verify paths in `<img>` tags and ensure images exist in `assets/images/optimized/`.

### **4.3. GitHub Sync Issues**
- **Cause**: Local changes not pushed to GitHub.
- **Fix**: Run `git push` to sync changes.

---

## **5. Contact**
For questions or issues, reach out to:
- **Email**: [wedding@marquessilva.eu](mailto:wedding@marquessilva.eu)
- **GitHub**: [https://github.com/DuracellPlusAAA6/wedding](https://github.com/DuracellPlusAAA6/wedding)

---

## **6. Conversation Metadata**
```json
{
  "chat_id": "+351961073277",
  "message_id": "1789378160479",
  "sender_id": "+351961073277",
  "sender": "Bruno Silva",
  "timestamp": "Mon 2026-09-14 11:29:20 GMT+2",
  "inbound_event_kind": "user_request"
}
```

**Sender**:
```json
{
  "label": "Bruno Silva (+351961073277)",
  "id": "+351961073277",
  "name": "Bruno Silva"
}
```