import fitz  # PyMuPDF

def convert_pdf_to_png(pdf_path, output_png_path):
    print("📄 Step 1: Extracting flat design from PDF...")
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        
        # Get the first page
        page = doc.load_page(0)
        
        # Set the resolution (dpi=300 for high quality texture)
        zoom_x = 4.0  # horizontal zoom
        zoom_y = 4.0  # vertical zoom
        mat = fitz.Matrix(zoom_x, zoom_y)
        
        # Render page to an image
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        # Save as PNG
        pix.save(output_png_path)
        print(f"   ✅ Dieline texture saved to {output_png_path}")
        return output_png_path
        
    except Exception as e:
        print(f"❌ Error converting PDF: {e}")
        return None