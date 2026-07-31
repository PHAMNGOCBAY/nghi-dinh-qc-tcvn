import os
import glob
import pathlib
import json
import re
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling_core.types.doc.base import ImageRefMode

def main():
    source_dir = r"C:\Users\TEMP.PNBAYBIMGIS.004\DC\ACCDocs\BIM-A2Z-HCM\HCM-TL-MT-TKKT\Project Files\2-SHARED\22-GENERAL"
    target_dir = r"g:\My Drive\NGHI DINH-QC-TCVN\22-GENERAL"
    
    # Configure Pipeline to extract images
    pipeline_options = PdfPipelineOptions()
    pipeline_options.generate_picture_images = True
    pipeline_options.generate_page_images = False
    pipeline_options.images_scale = 4.0
    
    converter = DocumentConverter(
        format_options={
            "pdf": PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".pdf"):
                input_pdf = os.path.join(root, file)
                rel_path = os.path.relpath(root, source_dir)
                
                # Output paths
                out_folder = os.path.join(target_dir, rel_path) if rel_path != "." else target_dir
                os.makedirs(out_folder, exist_ok=True)
                
                base_name = os.path.splitext(file)[0]
                base_name_sanitized = re.sub(r'[\\/*?:"<>|]', "_", base_name)
                
                output_md = os.path.join(out_folder, f"{base_name_sanitized}.md")
                output_json = os.path.join(out_folder, f"{base_name_sanitized}.json")
                output_images_dir = os.path.join(out_folder, f"{base_name_sanitized}_images")
                
                os.makedirs(output_images_dir, exist_ok=True)
                
                print(f"Processing: {input_pdf}")
                try:
                    result = converter.convert(input_pdf)
                    
                    # 1. Export Markdown
                    result.document.save_as_markdown(
                        output_md,
                        artifacts_dir=pathlib.Path(output_images_dir),
                        image_mode=ImageRefMode.REFERENCED
                    )
                    
                    # 1.5. Post-process Markdown to use relative paths for images
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
                        
                    # 2. Export JSON
                    doc_dict = result.document.export_to_dict()
                    with open(output_json, "w", encoding="utf-8") as f:
                        json.dump(doc_dict, f, ensure_ascii=False, indent=2)
                        
                    print(f"Success for: {file}")
                except Exception as e:
                    print(f"Failed for: {file} - {e}")

if __name__ == "__main__":
    main()
