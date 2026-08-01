import os
import json
import re

# File paths
EIR_FILE = r"G:\My Drive\NGHI DINH-QC-TCVN\22-GENERAL\221-EIR\HTM_(EIR) Yeu cau thong tin_TKKT_V3.md"
QD348_FILE = r"G:\My Drive\NGHI DINH-QC-TCVN\BXD_348-QD-BXD_TLHD.md"
QD347_FILE = r"G:\My Drive\NGHI DINH-QC-TCVN\BXD_347-QD-BXD_TLHDCT.md"
OUTPUT_JSON = r"G:\My Drive\NGHI DINH-QC-TCVN\so sánh EIR và 347-348-HTM.json"
OUTPUT_MD = r"G:\My Drive\NGHI DINH-QC-TCVN\so sánh EIR và 347-348-HTM.md"

def read_markdown(filepath):
    if not os.path.exists(filepath):
        print(f"Warning: File not found {filepath}")
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def extract_sections(markdown_text):
    """Trích xuất các heading và nội dung của nó."""
    sections = {}
    current_heading = "General"
    current_content = []
    
    for line in markdown_text.split('\n'):
        if line.startswith('#'):
            if current_heading:
                sections[current_heading] = '\n'.join(current_content).strip()
            current_heading = line.strip()
            current_content = []
        else:
            current_content.append(line)
            
    if current_heading:
        sections[current_heading] = '\n'.join(current_content).strip()
    return sections

def find_relevant_content(sections, keywords):
    """Tìm nội dung liên quan dựa trên từ khóa trong Heading hoặc Nội dung."""
    relevant_content = []
    for heading, content in sections.items():
        if any(kw.lower() in heading.lower() for kw in keywords):
            # Lấy 500 ký tự đầu tiên để tóm tắt
            summary = content[:500] + '...' if len(content) > 500 else content
            relevant_content.append(f"**{heading}**\n{summary}")
    return "\n\n".join(relevant_content) if relevant_content else "Không tìm thấy thông tin rõ ràng."

def main():
    print("Reading documents...")
    eir_text = read_markdown(EIR_FILE)
    qd348_text = read_markdown(QD348_FILE)
    qd347_text = read_markdown(QD347_FILE)
    
    eir_sections = extract_sections(eir_text)
    qd348_sections = extract_sections(qd348_text)
    qd347_sections = extract_sections(qd347_text)
    
    # Định nghĩa các tiêu chí so sánh chi tiết theo mẫu EIR của QĐ 348 và 347
    criteria = {
        "[348] 1. Thông tin dự án": ["thông tin dự án", "thông tin chung", "tiến độ dự án"],
        "[348] 2. Các quy định áp dụng": ["quy định áp dụng", "căn cứ pháp lý", "tiêu chuẩn áp dụng"],
        "[348] 3. Mục tiêu và nội dung BIM": ["mục tiêu", "nội dung áp dụng", "mục đích", "ứng dụng", "bim use"],
        "[348] 4. Phạm vi công việc và sản phẩm": ["phạm vi công việc", "sản phẩm", "kế hoạch chuyển giao", "phân chia trách nhiệm"],
        "[348] 5. Mức độ phát triển thông tin": ["mức độ phát triển", "lod", "loi", "log"],
        "[348] 6. Các nội dung về quản lý": ["nội dung về quản lý", "môi trường dữ liệu chung", "cde", "quy tắc đặt tên", "phối hợp"],
        "[348] 7. Các nội dung về kỹ thuật": ["nội dung về kỹ thuật", "nền tảng phần mềm", "phần mềm", "tạo lập bản vẽ", "hệ tọa độ"],
        "[348] 8. Đào tạo": ["đào tạo"],
        "[348] 9. Đánh giá năng lực": ["đánh giá năng lực"],
        "[347] Yêu cầu thông tin cho Kiến trúc/Kết cấu/Cơ điện": ["kiến trúc", "kết cấu", "cơ điện", "hvac", "pccc"],
        "[347] Yêu cầu thông tin cho Công trình giao thông (Cầu/Đường)": ["giao thông", "cầu", "đường", "hạ tầng", "địa hình", "đào đất dạng tuyến"]
    }
    
    comparison_results = []
    
    print("Analyzing and comparing...")
    for crit, keywords in criteria.items():
        eir_content = find_relevant_content(eir_sections, keywords)
        qd348_content = find_relevant_content(qd348_sections, keywords)
        qd347_content = find_relevant_content(qd347_sections, keywords)
        
        # Tạo đánh giá tự động (rất cơ bản, có thể dùng AI để nâng cao)
        status = "Cần Review"
        if eir_content != "Không tìm thấy thông tin rõ ràng." and (qd348_content != "Không tìm thấy thông tin rõ ràng." or qd347_content != "Không tìm thấy thông tin rõ ràng."):
            status = "Có quy định đối chiếu"
        
        comparison_results.append({
            "Tiêu chí": crit,
            "EIR Dự án HTM": eir_content,
            "QĐ 348 (Hướng dẫn chung)": qd348_content,
            "QĐ 347 (Hướng dẫn chi tiết)": qd347_content,
            "Đánh giá sơ bộ": status
        })
    
    # 1. Lưu ra JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(comparison_results, f, ensure_ascii=False, indent=4)
    print(f"Saved JSON: {OUTPUT_JSON}")
    
    # 2. Sinh ra Markdown
    md_lines = [
        "# Báo Cáo So Sánh EIR và Quyết định 347, 348 (Dự án HTM)\n",
        "*Báo cáo được sinh tự động dựa trên từ khóa và phân tích cấu trúc tài liệu.*\n",
        "| Tiêu chí | EIR Dự án HTM | QĐ 348 | QĐ 347 | Đánh giá sơ bộ |",
        "|---|---|---|---|---|"
    ]
    
    for row in comparison_results:
        # Thay thế newline bằng thẻ <br> để không vỡ bảng MD
        eir_cell = row["EIR Dự án HTM"].replace('\n', '<br>')
        qd348_cell = row["QĐ 348 (Hướng dẫn chung)"].replace('\n', '<br>')
        qd347_cell = row["QĐ 347 (Hướng dẫn chi tiết)"].replace('\n', '<br>')
        
        md_lines.append(f"| {row['Tiêu chí']} | {eir_cell} | {qd348_cell} | {qd347_cell} | {row['Đánh giá sơ bộ']} |")
        
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f"Saved MD: {OUTPUT_MD}")

if __name__ == "__main__":
    main()
