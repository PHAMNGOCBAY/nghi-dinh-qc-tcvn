import sys
from docling.document_converter import DocumentConverter

def main():
    input_pdf = r"Y:\BIMREADI\2025-TCVN 14177\2025-TCVN 14177\Tai lieu huong dan Bo TCVN 14177.pdf"
    output_md = r"Y:\BIMREADI\2025-TCVN 14177\2025-TCVN 14177\Tai lieu huong dan Bo TCVN 14177.md"
    
    print(f"Converting {input_pdf} to markdown...")
    try:
        converter = DocumentConverter()
        result = converter.convert(input_pdf)
        markdown_content = result.document.export_to_markdown()
        
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Successfully converted and saved to {output_md}")
    except ImportError:
        print("Error: The 'docling' library is not installed. Please install it using: pip install docling")
        sys.exit(1)
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
