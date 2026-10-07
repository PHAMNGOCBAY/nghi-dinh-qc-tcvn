# Workspace Memory

## Tiết trình & Quy ước Dự án
- **Công cụ trích xuất PDF ưu tiên:** `docling`.
- **Lưu trữ dữ liệu:** Trích xuất song song thành Markdown (`.md`) và JSON (`.json`). Hình ảnh và sơ đồ được trích xuất lưu vào thư mục `images/` hoặc thư mục con tương ứng, tham chiếu bằng đường dẫn tương đối trong Markdown.
- **Quản lý phiên bản (Git):** Không bao giờ upload dữ liệu thực tế (ví dụ: thư mục dự án `22-GENERAL/` hoặc các file PDF nhạy cảm) lên GitHub. Luôn nhớ thêm các thư mục chứa dữ liệu thực tế vào file `.gitignore` (`*.json`, `22-GENERAL/`, v.v.).
- **Nguyên tắc không bịa, không suy diễn (Zero Hallucination & Zero Speculation):** Tuyệt đối không bịa đặt số liệu, không tự suy diễn; 100% trích dẫn căn cứ từ Ground Truth (văn bản quy phạm, tiêu chuẩn kỹ thuật thực tế); bắt buộc gọi công cụ kiểm chứng trước khi đưa ra kết luận; văn phong khoa học trung tính, không dùng emoji.

## Các tác vụ đã hoàn thành
- [x] Tạo script `convert_pdf_docling.py` và `convert_pdf_docling_json.py` để trích xuất văn bản cơ bản.
- [x] Tạo script `extract_all_docling.py` trích xuất toàn diện bao gồm cả hình ảnh và cập nhật đường dẫn ảnh tương đối trong Markdown.
- [x] Khởi tạo Git và upload mã nguồn lên GitHub (repository `nghi-dinh-qc-tcvn`), ngoại trừ các dữ liệu thực tế.
- [x] Thiết lập kỹ năng `docling-pdf-extraction` trong thư mục `.agents/skills/`.
- [x] Viết script `batch_extract.py` để xử lý hàng loạt nhiều file PDF từ một thư mục nguồn (ví dụ: ACCDocs) sang thư mục đích, bảo toàn cấu trúc thư mục.
- [x] Thêm `22-GENERAL/` vào `.gitignore` để đảm bảo bảo mật dữ liệu thực tế của dự án không bị đẩy lên kho lưu trữ công khai.
