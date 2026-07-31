---
name: docling-pdf-extraction
description: Trích xuất toàn diện PDF sang Markdown, JSON, bao gồm sơ đồ và bảng biểu sử dụng Docling.
---

# Hướng dẫn sử dụng Docling để trích xuất PDF toàn diện

Kỹ năng này hướng dẫn cách trích xuất tài liệu PDF sang định dạng Markdown và JSON, đồng thời cấu hình để tự động trích xuất các **bảng biểu (tables)** và **sơ đồ/hình ảnh (pictures)** từ file PDF gốc.

## 1. Cài đặt môi trường
Bạn cần đảm bảo đã cài đặt thư viện `docling`:
```bash
pip install docling
```

## 2. Script Python trích xuất toàn diện (Markdown + JSON + Hình ảnh)

Đoạn script `extract_all_docling.py` dưới đây sẽ:
1. Đọc file PDF.
2. Trích xuất văn bản và bảng biểu mặc định của docling.
3. Cấu hình tính năng trích xuất hình ảnh/sơ đồ và lưu vào thư mục `images/`.
4. Xuất ra file `.md` với các thẻ chèn hình ảnh đã được liên kết đúng đường dẫn.
5. Xuất cấu trúc dữ liệu ra file `.json`.

```python
import sys
import json
import os
import pathlib
import re
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling_core.types.doc.base import ImageRefMode

def main():
    input_pdf = r"Y:\BIMREADI\2025-TCVN 14177\2025-TCVN 14177\Tai lieu huong dan Bo TCVN 14177.pdf"
    
    # Lấy thư mục của dự án hiện tại để lưu kết quả
    project_dir = r"g:\My Drive\NGHI DINH-QC-TCVN"
    base_name = "Tai_lieu_huong_dan_Bo_TCVN_14177_Full"
    
    output_md = os.path.join(project_dir, f"{base_name}.md")
    output_json = os.path.join(project_dir, f"{base_name}.json")
    output_images_dir = os.path.join(project_dir, "images")
    
    os.makedirs(output_images_dir, exist_ok=True)
    
    print(f"Bắt đầu trích xuất: {input_pdf}")
    print("Quá trình này có thể mất vài phút...")
    
    try:
        # Cấu hình Pipeline để trích xuất hình ảnh và sơ đồ
        pipeline_options = PdfPipelineOptions()
        pipeline_options.generate_picture_images = True # Bật trích xuất hình ảnh
        pipeline_options.generate_page_images = False
        
        # Khởi tạo DocumentConverter với cấu hình tùy chỉnh
        converter = DocumentConverter(
            format_options={
                "pdf": PdfFormatOption(pipeline_options=pipeline_options)
            }
        )
        
        # Tiến hành convert PDF
        result = converter.convert(input_pdf)
        
        # 1. Xuất ra Markdown (kèm đường dẫn hình ảnh)
        result.document.save_as_markdown(
            output_md,
            artifacts_dir=pathlib.Path(output_images_dir),
            image_mode=ImageRefMode.REFERENCED
        )
        print(f"Đã xuất Markdown tại: {output_md}")
        
        # 1.5. Sửa đường dẫn hình ảnh thành tương đối (để xem được trên GitHub)
        with open(output_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        def replace_path(match):
            full_path = match.group(1)
            # Xóa tiền tố thư mục tuyệt đối và sửa dấu xuyệt
            rel_path = full_path.replace(project_dir + "\\", "")
            rel_path = rel_path.replace(project_dir + "/", "")
            rel_path = rel_path.replace("\\", "/")
            return f"![Image]({rel_path})"
            
        md_content = re.sub(r"!\[Image\]\((.*?)\)", replace_path, md_content)
        
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Đã sửa đường dẫn ảnh thành tương đối trong Markdown!")
        
        # 2. Xuất ra JSON
        doc_dict = result.document.export_to_dict()
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(doc_dict, f, ensure_ascii=False, indent=2)
        print(f"Đã xuất JSON tại: {output_json}")
        
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## 3. Các công cụ thay thế (Alternatives)
Nếu kết quả từ `docling` đối với một số sơ đồ đặc thù chưa được như ý, bạn có thể cân nhắc:
- **`marker-pdf`**: Dùng lệnh `marker_single file.pdf --output_dir out/` (Chuyên trị công thức Toán và layout phức tạp).
- **`Camelot`** / **`pdfplumber`**: Chuyên dùng để trích xuất bảng biểu có độ chính xác cực cao sang file CSV/Excel.
- **Mermaid.js**: Nếu bạn muốn tự tạo và vẽ sơ đồ dạng Text-to-Diagram thẳng vào file Markdown.

## 4. Tạo và xử lý công thức Toán học (LaTeX) bằng Python
Nếu trong tài liệu có các công thức phức tạp và bạn muốn dùng Python để sinh ra mã LaTeX cho các công thức đó, thư viện **`sympy`** là lựa chọn tuyệt vời.

**Cài đặt:**
```bash
pip install sympy
```

**Script Python tạo mã LaTeX cho công thức:**
Đoạn code sau đây sử dụng `sympy` để tạo một biểu thức toán học phức tạp (ví dụ: Tích phân hoặc Phương trình) và xuất ra định dạng mã LaTeX chuẩn để chèn vào Markdown (`*.md`) hoặc file LaTeX (`*.tex`).

```python
import sympy as sp

def main():
    # Khai báo các biến toán học
    x, y, a, b = sp.symbols('x y a b')
    
    # 1. Tạo một công thức phương trình bậc 2
    equation = sp.Eq(a*x**2 + b*x, y)
    latex_eq = sp.latex(equation)
    
    # 2. Tạo một công thức tích phân
    integral = sp.Integral(sp.exp(-x**2), (x, -sp.oo, sp.oo))
    latex_integral = sp.latex(integral)
    
    print("--- Mã LaTeX cho Phương trình bậc 2 ---")
    print(f"$$ {latex_eq} $$")
    print("\n--- Mã LaTeX cho Tích phân Gauss ---")
    print(f"$$ {latex_integral} $$")

    # Bạn có thể lưu vào file
    with open("cong_thuc.md", "w", encoding="utf-8") as f:
        f.write("### Các công thức sinh bằng Python:\n\n")
        f.write(f"$$ {latex_eq} $$\n\n")
        f.write(f"$$ {latex_integral} $$\n")

if __name__ == "__main__":
    main()
```

Khi chạy code này, bạn sẽ nhận được mã LaTeX nguyên bản như `\int\limits_{-\infty}^{\infty} e^{- x^{2}}\, dx`. Các mã này khi dán vào file `.md` sẽ tự động được hiển thị thành công thức toán học cực chuẩn!
