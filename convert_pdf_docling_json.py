import sys
import json
from docling.document_converter import DocumentConverter

def main():
    input_pdf = r"Y:\BIMREADI\2025-TCVN 14177\2025-TCVN 14177\Tai lieu huong dan Bo TCVN 14177.pdf"
    output_json = r"g:\My Drive\NGHI DINH-QC-TCVN\Tai lieu huong dan Bo TCVN 14177.json"
    
    print(f"Converting {input_pdf} to JSON...")
    try:
        converter = DocumentConverter()
        result = converter.convert(input_pdf)
        
        doc_dict = result.document.export_to_dict()
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(doc_dict, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully converted and saved to {output_json}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
