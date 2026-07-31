# Quy tắc làm việc của AI Agent cho dự án NGHI DINH-QC-TCVN

## 1. Công cụ & Thư viện ưu tiên
- **Trích xuất PDF**: Luôn ưu tiên sử dụng thư viện `docling` để chuyển đổi PDF sang Markdown và JSON.
- **Xử lý hình ảnh từ PDF**: Đảm bảo sử dụng `docling` API mới nhất (`save_as_markdown` kết hợp `ImageRefMode`) để lưu trữ hình ảnh vào thư mục `images/`.
- **Toán học & Công thức**: Sử dụng thư viện `sympy` để sinh mã LaTeX cho các công thức, sau đó gắn trực tiếp vào file Markdown.

## 2. Quy ước lưu trữ và định dạng
- Mọi tài liệu sinh ra phải được lưu dưới định dạng Markdown (`*.md`) để dễ dàng đọc và hiển thị.
- Dữ liệu thô hoặc cấu trúc phân tích phức tạp nên được lưu song song dưới dạng `*.json`.
- Hình ảnh/Sơ đồ trích xuất từ PDF phải được tập trung vào thư mục `images/`.

## 3. Tự động hóa nghiệp vụ
- Nếu người dùng yêu cầu trích xuất toàn diện PDF, hãy tự động kích hoạt kỹ năng `docling-pdf-extraction` (đã được định nghĩa trong `skills/docling-pdf-extraction/SKILL.md`) hoặc chạy script `extract_all_docling.py`.
