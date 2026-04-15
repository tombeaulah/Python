
from PyPDF2 import PdfReader, PdfWriter


pdf1 = r"C:\Users\tombe\Google Drive\Farm\Non-molestation Order\20260113-Letter_Postmarked_13012026.pdf"
pdf2 = r"C:\Users\tombe\Google Drive\Farm\Non-molestation Order\20260113-Letter_Postmarked_13012026-3.pdf"
output_pdf = r"C:\Users\tombe\Google Drive\Farm\Non-molestation Order\20260113-Letter_Postmarked_13012026-Final.pdf"




def combine_pdfs(pdf1, pdf2, output_pdf):
    writer = PdfWriter()

    # Add pages from first PDF
    reader1 = PdfReader(pdf1)
    for page in reader1.pages:
        writer.add_page(page)

    # Add pages from second PDF
    reader2 = PdfReader(pdf2)
    for page in reader2.pages:
        writer.add_page(page)

    # Write output PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

combine_pdfs(pdf1, pdf2, output_pdf)




# Open PDF

working_pdf = r"C:\Users\tombe\Google Drive\Farm\Non-molestation Order\20260113-Letter_Postmarked_13012026-Final.pdf"

reader = PdfReader(working_pdf)
writer = PdfWriter()

# Example: reorder pages manually
# Suppose original PDF has 5 pages, and you want new order: 2,1,3,4,5
order = [0, 1 ,3, 2]

for i in order:
    page = reader.pages[i]

    # Example: rotate page 2 (the one at index 1 in original PDF)
    if i == 6:
        page.rotate(0)

    writer.add_page(page)

# Save new PDF
with open(working_pdf, "wb") as f:
    writer.write(f)


# ✔️ Rotate only one page

working_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets.pdf"

reader = PdfReader(working_pdf)
writer = PdfWriter()


page = reader.pages[7]   # page index 3 = 4th page
page.rotate(180)
writer.add_page(page)




# mark up pages

import fitz  # PyMuPDF



# define function
def add_text_box(input_pdf, page_number, text, output_pdf):
    doc = fitz.open(input_pdf)
    page = doc[page_number - 1]

    # Define a rectangle for the box (adjust coordinates as needed)
    rect = fitz.Rect(50, 50, 400, 100)  # x0,y0,x1,y1

    # Draw the rectangle (border)
    page.draw_rect(rect, color=(1, 0, 0), width=1)  # red border

    # Insert text inside the rectangle
    page.insert_textbox(
        rect,
        text,
        fontsize=12,
        fontname="helv",
        color=(0, 0, 0),
        align=0  # left align
    )

    # Save the PDF
    doc.save(output_pdf)
    doc.close()

    return


working_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets_Original.pdf"
new_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets_Marked1.pdf"

add_text_box(working_pdf, 1, "Agriculutral Machinery", new_pdf)
add_text_box(working_pdf, 2, "Other Agriculutral Machinery" , new_pdf)
add_text_box(working_pdf, 3, "Land Rover", new_pdf)
add_text_box(working_pdf, 4, "Pickup", new_pdf)
add_text_box(working_pdf, 5, "Vintage Vehicles in Ag Use", new_pdf)
add_text_box(working_pdf, 6, "Rest of Vintage Vehicles in group", new_pdf)
add_text_box(working_pdf, 7, "Non-vehicle ag assets", new_pdf)
add_text_box(working_pdf, 8, "Stud Farm bldgs", new_pdf)
add_text_box(working_pdf, 9, "Home Farm Bldgs", new_pdf)










import fitz


current_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets_Marked1.pdf"
new_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets_Marked2.pdf"

# Open PDF
doc = fitz.open(new_pdf)

# Use first page
page = doc[0]

# Get page size
width, height = page.rect.width, page.rect.height
print(f"Page size: {width} x {height}")

# Make a rectangle near the top of the page (5% from top, full width minus margins)
rect = fitz.Rect(50, 50, width-50, 150)

# Draw a visible red border
page.draw_rect(rect, color=(1, 0, 0), width=2)

# Add text inside rectangle
page.insert_textbox(
    rect,
    "Test text box - should be visible",
    fontsize=20,
    fontname="helv",
    color=(0, 0, 0),
    align=1  # center
)

# Save to new file
doc.save(save_pdf)
doc.close()




import fitz  # PyMuPDF

def normalize_and_annotate(input_pdf, output_pdf, page_labels, box_height=80, margin=50, fontsize=16):
    """
    Normalize all pages to 0 rotation and annotate them with visible red text boxes at the bottom.

    input_pdf: path to the original PDF
    output_pdf: path to save annotated PDF
    page_labels: list of strings (one per page) OR single string for all pages
    box_height: height of the text box
    margin: distance from page edges
    fontsize: font size of the text
    """
    doc = fitz.open(input_pdf)
    
    for i, page in enumerate(doc):
        # normalize page rotation
        if page.rotation != 0:
            page.set_rotation(0)
        
        # determine label
        if isinstance(page_labels, list):
            label = page_labels[i] if i < len(page_labels) else ""
        else:
            label = page_labels

        if not label:
            continue  # skip empty labels

        # rectangle at bottom of page
        page_width, page_height = page.rect.width, page.rect.height
        rect = fitz.Rect(
            margin,
            page_height - margin - box_height,
            page_width - margin,
            page_height - margin
        )

        # draw visible border
        page.draw_rect(rect, color=(1, 0, 0), width=1)

        # insert centered red text
        page.insert_textbox(
            rect,
            label,
            fontsize=fontsize,
            fontname="helv",
            color=(1, 0, 0),
            align=1
        )

    # save the annotated PDF
    doc.save(output_pdf)
    doc.close()



labels = [
"Agricultural Machinery",
"Other Agricultural Machinery",
"Land Rover",
"Pickup",
"Vintage Vehicles",
"Non-vehicle Assets",
"All other vintage machiner grouped up",
"Stud Farm Buildings",
"Home Farm Buildings"
]



current_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets_Original.pdf"
new_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets_Marked.pdf"
annotate_pages(current_pdf, new_pdf, labels)


import fitz  # PyMuPDF

def annotate_pages_bottom(input_pdf, output_pdf, labels):
    """
    Adds bottom text labels to each page using insert_textbox.
    Handles any page rotation (0, 90, 180, 270) automatically.
    Ensures text appears upright at the visual bottom.
    """
    doc = fitz.open(input_pdf)

    for i, label in enumerate(labels):
        if i >= len(doc):
            break

        page = doc[i]
        rot = page.rotation             # 0, 90, 180, 270
        rect = page.rect                # original rectangle

        # Choose a nice height for the label area
        box_height = 40                 # points (≈ 14 mm)

        # ---- Determine the visual bottom rectangle depending on rotation ----
        if rot == 0:
            # Normal orientation
            box = fitz.Rect(rect.x0, rect.y1 - box_height, rect.x1, rect.y1)
            text_rot = 0

        elif rot == 90:
            # Page is rotated clockwise — bottom is on the left side
            box = fitz.Rect(rect.x0, rect.y0, rect.x0 + box_height, rect.y1)
            text_rot = -90              # counter-rotate text so it's upright

        elif rot == 180:
            # Page upside down — bottom is at the top edge
            box = fitz.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + box_height)
            text_rot = 180              # counter-rotate so upright

        elif rot == 270:
            # Page rotated 270 clockwise — bottom is on the right edge
            box = fitz.Rect(rect.x1 - box_height, rect.y0, rect.x1, rect.y1)
            text_rot = -270

        # ---- Insert text upright relative to viewer ----
        page.insert_textbox(
            box,
            label,
            fontsize=14,
            rotate=text_rot,
            color=(1, 0, 0),            # red
            align=fitz.TEXT_ALIGN_CENTER,
        )
    
    doc.save(output_pdf)
    doc.close()


labels = [
"Agricultural Machinery",
"Other Agricultural Machinery",
"Land Rover",
"Pickup",
"Vintage Vehicles",
"Non-vehicle Assets",
"All other vintage machinery grouped up",
"Stud Farm Buildings",
"Home Farm Buildings"
]

current_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets_Original.pdf"
new_pdf = r"C:\Users\tombe\Google Drive\Farm\Assets\20251211-Scans_Relevant_Pages_Farm_Insurance_Showing_Farm_Assets_Marked1.pdf"
annotate_pages_bottom(current_pdf, new_pdf, labels)


