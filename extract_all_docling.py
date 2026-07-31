import sys
import json
import os
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

def main():
    input_pdf = r"Y:\BIMREADI\2025-TCVN 14177\2025-TCVN 14177\Tai lieu huong dan Bo TCVN 14177.pdf"
    
    project_dir = r"g:\My Drive\NGHI DINH-QC-TCVN"
    base_name = "Tai_lieu_huong_dan_Bo_TCVN_14177_Full"
    
    output_md = os.path.join(project_dir, f"{base_name}.md")
    output_json = os.path.join(project_dir, f"{base_name}.json")
    output_images_dir = os.path.join(project_dir, "images")
    
    os.makedirs(output_images_dir, exist_ok=True)
    
    print(f"Bat dau trich xuat toan dien: {input_pdf}")
    
    try:
        pipeline_options = PdfPipelineOptions()
        pipeline_options.generate_picture_images = True
        pipeline_options.generate_page_images = False
        
        converter = DocumentConverter(
            format_options={
                "pdf": PdfFormatOption(pipeline_options=pipeline_options)
            }
        )
        
        result = converter.convert(input_pdf)
        
        # 1. Export Markdown with image references
        markdown_content = result.document.export_to_markdown(
            image_dir=output_images_dir
        )
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Da xuat Markdown thanh cong!")
        
        # 2. Export JSON
        doc_dict = result.document.export_to_dict()
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(doc_dict, f, ensure_ascii=False, indent=2)
        print(f"Da xuat JSON thanh cong!")
        
    except Exception as e:
        print(f"Da xay ra loi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
