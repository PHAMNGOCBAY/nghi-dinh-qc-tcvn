import os
import pathlib
import json
import re
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling_core.types.doc.base import ImageRefMode

def convert_pdf(input_pdf):
    target_dir = os.path.dirname(input_pdf)
    file = os.path.basename(input_pdf)
    
    pipeline_options = PdfPipelineOptions()
    pipeline_options.generate_picture_images = True
    pipeline_options.generate_page_images = False
    pipeline_options.images_scale = 4.0
    
    converter = DocumentConverter(
        format_options={
            "pdf": PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    base_name = os.path.splitext(file)[0]
    base_name_sanitized = re.sub(r'[\\/*?:"<>|]', "_", base_name)
    
    output_md = os.path.join(target_dir, f"{base_name_sanitized}.md")
    output_json = os.path.join(target_dir, f"{base_name_sanitized}.json")
    output_images_dir = os.path.join(target_dir, f"{base_name_sanitized}_images")
    
    os.makedirs(output_images_dir, exist_ok=True)
    
    print(f"Processing: {input_pdf}")
    try:
        result = converter.convert(input_pdf)
        
        result.document.save_as_markdown(
            output_md,
            artifacts_dir=pathlib.Path(output_images_dir),
            image_mode=ImageRefMode.REFERENCED
        )
        
        with open(output_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        def replace_path(match):
            full_path = match.group(1)
            full_path_normalized = full_path.replace("\\", "/")
            basename = os.path.basename(full_path_normalized)
            return f"![Image]({base_name_sanitized}_images/{basename})"
            
        md_content = re.sub(r"!\[Image\]\((.*?)\)", replace_path, md_content)
        
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        doc_dict = result.document.export_to_dict()
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(doc_dict, f, ensure_ascii=False, indent=2)
            
        print(f"Success for: {file}")
    except Exception as e:
        print(f"Failed for: {file} - {e}")

if __name__ == "__main__":
    files_to_convert = [
        r"g:\My Drive\NGHI DINH-QC-TCVN\TCVN14177-1_2024_921449.pdf",
        r"g:\My Drive\NGHI DINH-QC-TCVN\TCVN14177-2_2024_921451.pdf"
    ]
    for f in files_to_convert:
        convert_pdf(f)
