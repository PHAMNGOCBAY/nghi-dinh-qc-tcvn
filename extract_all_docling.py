import sys
import json
import os
import pathlib
import os
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling_core.types.doc.base import ImageRefMode

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
        result.document.save_as_markdown(
            output_md,
            artifacts_dir=pathlib.Path(output_images_dir),
            image_mode=ImageRefMode.REFERENCED
        )
        print(f"Da xuat Markdown thanh cong!")
        
        # 1.5. Post-process Markdown to use relative paths for images
        import re
        with open(output_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        def replace_path(match):
            full_path = match.group(1)
            # Remove absolute prefix and fix slashes
            rel_path = full_path.replace(project_dir + "\\", "")
            rel_path = rel_path.replace(project_dir + "/", "")
            rel_path = rel_path.replace("\\", "/")
            return f"![Image]({rel_path})"
            
        md_content = re.sub(r"!\[Image\]\((.*?)\)", replace_path, md_content)
        
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Da sua duong dan anh thanh tuong doi trong Markdown!")
        
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
