BỘ XÂY DỰNG ---------o0o---------

## TÀI LIỆU

HƯỚNG DẪN CHI TIẾT ÁP DỤNG MÔ HÌNH THÔNG TIN CÔNG TRÌNH (BIM) ĐỐI VỚI CÔNG TRÌNH DÂN DỤNG VÀ HẠ TẦNG KỸ THUẬT ĐÔ THỊ

## MỤC LỤC

## Outline (Tự động tạo)

  - [TÀI LIỆU](#tài-liệu)
  - [DANH MỤC HÌNH VẼ](#danh-mục-hình-vẽ)
  - [1. Lời giới thiệu](#1-lời-giới-thiệu)
  - [2. Phạm vi hướng dẫn](#2-phạm-vi-hướng-dẫn)
  - [3. Tài liệu viện dẫn](#3-tài-liệu-viện-dẫn)
  - [MỞ ĐẦU](#mở-đầu)
  - [4. Thuật ngữ và định nghĩa](#4-thuật-ngữ-và-định-nghĩa)
  - [PHẦN 1: MỘT SỐ NỘI DUNG TRIỂN KHAI BIM TRONG CÔNG TRÌNH DÂN DỤNG](#phần-1-một-số-nội-dung-triển-khai-bim-trong-công-trình-dân-dụng)
  - [1. Định dạng trao đổi dữ liệu](#1-định-dạng-trao-đổi-dữ-liệu)
  - [2. Mức độ phát triển thông tin](#2-mức-độ-phát-triển-thông-tin)
  - [3. Bảng gán màu cấu kiện](#3-bảng-gán-màu-cấu-kiện)
  - [4. Hướng dẫn phối hợp và xử lý xung đột](#4-hướng-dẫn-phối-hợp-và-xử-lý-xung-đột)
  - [4.1. Trách nhiệm trong việc phối hợp đa bộ môn ở giai đoạn thiết kế](#41-trách-nhiệm-trong-việc-phối-hợp-đa-bộ-môn-ở-giai-đoạn-thiết-kế)
  - [a. Điều phối BIM](#a-điều-phối-bim)
  - [b. Kỹ thuật viên BIM](#b-kỹ-thuật-viên-bim)
  - [4.2. Phương pháp phối hợp](#42-phương-pháp-phối-hợp)
  - [a. Phối hợp giai đoạn thiết kế sơ bộ](#a-phối-hợp-giai-đoạn-thiết-kế-sơ-bộ)
  - [b. Phối hợp thiết kế giai đoạn thiết kế cơ sở](#b-phối-hợp-thiết-kế-giai-đoạn-thiết-kế-cơ-sở)
  - [c. Phối hợp thiết kế giai đoạn thiết kế kỹ thuật, bản vẽ thi công](#c-phối-hợp-thiết-kế-giai-đoạn-thiết-kế-kỹ-thuật-bản-vẽ-thi-công)
  - [4.3. Tần suất phối hợp](#43-tần-suất-phối-hợp)
  - [4.4. Xử lý xung đột](#44-xử-lý-xung-đột)
  - [a.](#a)
  - [Hình 4 Sơ đồ tổng thể quá trình xử lý xung đột](#hình-4-sơ-đồ-tổng-thể-quá-trình-xử-lý-xung-đột)
  - [b. Thiết lập ma trận va chạm](#b-thiết-lập-ma-trận-va-chạm)
  - [c. Các đối tượng không cần kiểm tra xử lý va chạm](#c-các-đối-tượng-không-cần-kiểm-tra-xử-lý-va-chạm)
  - [5.](#5)
  - [d. Thiết lập các nhóm va chạm](#d-thiết-lập-các-nhóm-va-chạm)
  - [e. Quy tắc đặt tên](#e-quy-tắc-đặt-tên)
  - [f. Định dạng tập tin trong quá trình xử lý xung đột](#f-định-dạng-tập-tin-trong-quá-trình-xử-lý-xung-đột)
  - [Yêu cầu thông tin trao đổi đối với bộ môn kiến trúc](#yêu-cầu-thông-tin-trao-đổi-đối-với-bộ-môn-kiến-trúc)
  - [5.1. Trong giai đoạn thiết kế sơ bộ](#51-trong-giai-đoạn-thiết-kế-sơ-bộ)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [5.2. Trong giai đoạn thiết kế cơ sở](#52-trong-giai-đoạn-thiết-kế-cơ-sở)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [5.3. Trong giai đoạn thiết kế kỹ thuật](#53-trong-giai-đoạn-thiết-kế-kỹ-thuật)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b.](#b)
  - [Yêu cầu về mô hình thông tin](#yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [5.4. Trong giai đoạn thiết kế bản vẽ thi công](#54-trong-giai-đoạn-thiết-kế-bản-vẽ-thi-công)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [5.5. Nội dung kiểm tra chủ yếu mô hình kiến trúc](#55-nội-dung-kiểm-tra-chủ-yếu-mô-hình-kiến-trúc)
  - [6. Yêu cầu thông tin trao đổi đối với bộ môn kết cấu](#6-yêu-cầu-thông-tin-trao-đổi-đối-với-bộ-môn-kết-cấu)
  - [6.1. Trong giai đoạn thiết kế sơ bộ](#61-trong-giai-đoạn-thiết-kế-sơ-bộ)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [6.2. Trong giai đoạn thiết kế cơ sở](#62-trong-giai-đoạn-thiết-kế-cơ-sở)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [Yêu cầu về mô hình thông tin](#yêu-cầu-về-mô-hình-thông-tin)
  - [b.](#b)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [6.3. Trong giai đoạn thiết kế kỹ thuật](#63-trong-giai-đoạn-thiết-kế-kỹ-thuật)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c.](#c)
  - [Đầu ra / Sản phẩm](#đầu-ra-sản-phẩm)
  - [6.4. Trong giai đoạn thiết kế bản vẽ thi công](#64-trong-giai-đoạn-thiết-kế-bản-vẽ-thi-công)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [6.5. Danh sách kiểm tra chủ yếu cho mô hình kết cấu](#65-danh-sách-kiểm-tra-chủ-yếu-cho-mô-hình-kết-cấu)
  - [7. Yêu cầu thông tin trao đổi đối với bộ môn cơ điện](#7-yêu-cầu-thông-tin-trao-đổi-đối-với-bộ-môn-cơ-điện)
  - [7.1. Trong giai đoạn thiết kế cơ sở](#71-trong-giai-đoạn-thiết-kế-cơ-sở)
  - [7.1.1. Hệ thống HVAC](#711-hệ-thống-hvac)
  - [Yêu cầu về mô hình thông tin](#yêu-cầu-về-mô-hình-thông-tin)
  - [Đầu ra/ sản phẩm](#đầu-ra-sản-phẩm)
  - [b.](#b)
  - [c.](#c)
  - [7.1.2. Hệ thống điện](#712-hệ-thống-điện)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [Yêu cầu về mô hình thông tin](#yêu-cầu-về-mô-hình-thông-tin)
  - [c.](#c)
  - [Đầu ra / Sản phẩm](#đầu-ra-sản-phẩm)
  - [7.1.3.](#713)
  - [Hệ thống phòng cháy chữa cháy](#hệ-thống-phòng-cháy-chữa-cháy)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [b.](#b)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.1.4. Hệ thống cấp thoát nước](#714-hệ-thống-cấp-thoát-nước)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.2. Trong giai đoạn thiết kế kỹ thuật](#72-trong-giai-đoạn-thiết-kế-kỹ-thuật)
  - [7.2.1. Hệ thống HVAC](#721-hệ-thống-hvac)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.2.2.](#722)
  - [Hệ thống điện](#hệ-thống-điện)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.2.3. Hệ thống phòng cháy chữa cháy](#723-hệ-thống-phòng-cháy-chữa-cháy)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.2.4. Hệ thống cấp thoát nước](#724-hệ-thống-cấp-thoát-nước)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c.](#c)
  - [7.3. Trong giai đoạn thiết kế bản vẽ thi công](#73-trong-giai-đoạn-thiết-kế-bản-vẽ-thi-công)
  - [7.3.1.](#731)
  - [Hệ thống HVAC](#hệ-thống-hvac)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.3.2. Hệ thống điện](#732-hệ-thống-điện)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.3.3. Hệ thống phòng cháy chữa cháy](#733-hệ-thống-phòng-cháy-chữa-cháy)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.3.4. Hệ thống cấp thoát nước](#734-hệ-thống-cấp-thoát-nước)
  - [a. Yêu cầu đầu vào](#a-yêu-cầu-đầu-vào)
  - [b. Yêu cầu về mô hình thông tin](#b-yêu-cầu-về-mô-hình-thông-tin)
  - [c. Đầu ra / Sản phẩm](#c-đầu-ra-sản-phẩm)
  - [7.4. Mức độ mô hình hoá đối với hệ thống cơ điện](#74-mức-độ-mô-hình-hoá-đối-với-hệ-thống-cơ-điện)
  - [7.5. Danh sách kiểm tra chủ yếu cho mô hình cơ điện](#75-danh-sách-kiểm-tra-chủ-yếu-cho-mô-hình-cơ-điện)
  - [PHẦN 2: MỘT SỐ NỘI DUNG TRIỂN KHAI BIM TRONG CÔNG TRÌNH HẠ TẦNG KỸ THUẬT ĐÔ THỊ](#phần-2-một-số-nội-dung-triển-khai-bim-trong-công-trình-hạ-tầng-kỹ-thuật-đô-thị)
  - [1. Định dạng trao đổi dữ liệu](#1-định-dạng-trao-đổi-dữ-liệu)
  - [2. Mức độ phát triển thông tin](#2-mức-độ-phát-triển-thông-tin)
  - [3. Bảng gán mã màu hệ thống](#3-bảng-gán-mã-màu-hệ-thống)
  - [4. Một số yêu cầu đối với mô hình hoá bề mặt](#4-một-số-yêu-cầu-đối-với-mô-hình-hoá-bề-mặt)
  - [4.1. Các yêu cầu độ chính xác của đối tượng là bề mặt ( bao gồm đường, địa hình)](#41-các-yêu-cầu-độ-chính-xác-của-đối-tượng-là-bề-mặt-bao-gồm-đường-địa-hình)
  - [4.2. Tính liên tục của các đối tượng đường ngắt (Breaklines) và bề mặt (Surface)](#42-tính-liên-tục-của-các-đối-tượng-đường-ngắt-breaklines-và-bề-mặt-surface)
  - [Yêu cầu](#yêu-cầu)
  - [Hướng dẫn](#hướng-dẫn)
  - [4.3. Tính đều đặn của lưới tam giác](#43-tính-đều-đặn-của-lưới-tam-giác)
  - [4.4. Độ chính xác hình học của mô hình bề mặt Yêu cầu](#44-độ-chính-xác-hình-học-của-mô-hình-bề-mặt-yêu-cầu)
  - [Hướng dẫn](#hướng-dẫn)
  - [Các giá trị (S)](#các-giá-trị-s)
  - [5. Yêu cầu thông tin trao đổi đối với công trình giao thông (cầu, đường)](#5-yêu-cầu-thông-tin-trao-đổi-đối-với-công-trình-giao-thông-cầu-đường)
  - [5.1. Dữ liệu ban đầu](#51-dữ-liệu-ban-đầu)
  - [5.2. Giai đoạn lập quy hoạch](#52-giai-đoạn-lập-quy-hoạch)
  - [5.3. Thiết kế cơ sở](#53-thiết-kế-cơ-sở)
  - [Mô hình các phương án](#mô-hình-các-phương-án)
  - [5.4. Thiết kế kỹ thuật và thiết kế bản vẽ thi công](#54-thiết-kế-kỹ-thuật-và-thiết-kế-bản-vẽ-thi-công)
  - [5.5. Mô hình hóa giai đoạn thi công xây dựng (nhà thầu thi công)](#55-mô-hình-hóa-giai-đoạn-thi-công-xây-dựng-nhà-thầu-thi-công)
  - [PHỤ LỤC 01: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN HÌNH HỌC CỦA MỘT SỐ LOẠI CẤU KIỆN TRONG CÔNG TRÌNH XÂY DỰNG DÂN DỰNG DÂN DỤNG](#phụ-lục-01-mức-độ-phát-triển-thông-tin-hình-học-của-một-số-loại-cấu-kiện-trong-công-trình-xây-dựng-dân-dựng-dân-dụng)
  - [1. Mô hình kiến trúc](#1-mô-hình-kiến-trúc)
  - [a. Các hệ thống kiến trúc](#a-các-hệ-thống-kiến-trúc)
  - [a1. Bề mặt khu đất:](#a1-bề-mặt-khu-đất)
  - [2. Mô hình kết cấu](#2-mô-hình-kết-cấu)
  - [b. Hệ thống kết cấu](#b-hệ-thống-kết-cấu)
  - [b2. Cấu kiện dạng thanh:](#b2-cấu-kiện-dạng-thanh)
  - [3.](#3)
  - [Mô hình CƠ ĐIỆN](#mô-hình-cơ-điện)
  - [c. Hệ thống HVAC:](#c-hệ-thống-hvac)
  - [c1. Trang thiết bị:](#c1-trang-thiết-bị)
  - [c5. Phần loại trừ:](#c5-phần-loại-trừ)
  - [d. Hệ thống điện:](#d-hệ-thống-điện)
  - [e. Hệ thống cấp thoát nước và Phòng cháy chữa cháy:](#e-hệ-thống-cấp-thoát-nước-và-phòng-cháy-chữa-cháy)
  - [e2. Đường ống cấp nước:](#e2-đường-ống-cấp-nước)
  - [4. Mô hình hạ tầng khu vực](#4-mô-hình-hạ-tầng-khu-vực)
  - [f. Công trình hạ tầng khu vực:](#f-công-trình-hạ-tầng-khu-vực)
  - [f2. Yếu tố cảnh quan:](#f2-yếu-tố-cảnh-quan)
  - [f3. Công trình hạ tầng kỹ thuật vá các bộ phận chi tiết:](#f3-công-trình-hạ-tầng-kỹ-thuật-vá-các-bộ-phận-chi-tiết)
  - [BẢNG MỨC ĐỘ PHÁT TRIỂN THÔNG TIN PHI HÌNH HỌC BỘ MÔN KIẾN TRÚC - KẾT CẤU](#bảng-mức-độ-phát-triển-thông-tin-phi-hình-học-bộ-môn-kiến-trúc---kết-cấu)
  - [BẢNG MỨC ĐỘ PHÁT TRIỂN THÔNG TIN PHI HÌNH HỌC BỘ MÔN MEP](#bảng-mức-độ-phát-triển-thông-tin-phi-hình-học-bộ-môn-mep)
  - [PHỤ LỤC 03: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN CỦA MỘT SỐ LOẠI CẤU KIỆN TRONG CÔNG TRÌNH HẠ TẦNG KỸ THUẬT ĐÔ THỊ (GIAO THÔNG, CẤP THOÁT NƯỚC)](#phụ-lục-03-mức-độ-phát-triển-thông-tin-của-một-số-loại-cấu-kiện-trong-công-trình-hạ-tầng-kỹ-thuật-đô-thị-giao-thông-cấp-thoát-nước)
  - [1. Ví dụ Bảng mức độ phát triển mô hình theo giai đoạn trình tự đầu tư](#1-ví-dụ-bảng-mức-độ-phát-triển-mô-hình-theo-giai-đoạn-trình-tự-đầu-tư)
  - [2. Địa hình](#2-địa-hình)
  - [3. San lấp mặt bằng](#3-san-lấp-mặt-bằng)
  - [4. Hố móng](#4-hố-móng)
  - [5. Đào đất dạng tuyến](#5-đào-đất-dạng-tuyến)
  - [6. Đường bộ và đường sắt](#6-đường-bộ-và-đường-sắt)
  - [7. Trang thiết bị của đường bộ và đường sắt](#7-trang-thiết-bị-của-đường-bộ-và-đường-sắt)
  - [8. Hệ thống đường ống hiện trạng](#8-hệ-thống-đường-ống-hiện-trạng)
  - [9. Hệ thống thoát nước](#9-hệ-thống-thoát-nước)
  - [10. Móng, cấu kiện bê tông đúc sẵn](#10-móng-cấu-kiện-bê-tông-đúc-sẵn)
  - [11. Móng đổ tại chổ](#11-móng-đổ-tại-chổ)
  - [12. Tấm bê tông đổ tại chỗ](#12-tấm-bê-tông-đổ-tại-chỗ)
  - [13. Tấm bê tông chế tạo sẵn](#13-tấm-bê-tông-chế-tạo-sẵn)
  - [14. Dầm bê tông, cấu kiện](#14-dầm-bê-tông-cấu-kiện)
  - [15. Dầm bê tông đổ tại chỗ](#15-dầm-bê-tông-đổ-tại-chỗ)
  - [16. Dầm thép](#16-dầm-thép)
  - [17. Cột thép](#17-cột-thép)
  - [18. Hệ thống phụ trợ, tiện ích](#18-hệ-thống-phụ-trợ-tiện-ích)
  - [19. Hệ thống đường ống](#19-hệ-thống-đường-ống)
  - [20. Hệ thống cấp, thoát nước](#20-hệ-thống-cấp-thoát-nước)
  - [21. Máng cáp](#21-máng-cáp)
  - [22. Một số loại hố ga](#22-một-số-loại-hố-ga)
  - [22.1. Hố ga loại 1](#221-hố-ga-loại-1)
  - [22.3. Hố ga loại 3](#223-hố-ga-loại-3)
  - [22.4. Hố ga loại 4](#224-hố-ga-loại-4)
  - [23. Một số loại nắp hố ga](#23-một-số-loại-nắp-hố-ga)
  - [23.1. Nắp hố ga loại 1](#231-nắp-hố-ga-loại-1)
  - [23.2. Nắp hố ga loại 2](#232-nắp-hố-ga-loại-2)
  - [24. Thang lên xuống](#24-thang-lên-xuống)
  - [25. Biển báo](#25-biển-báo)
  - [PHỤ LỤC 04: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN PHI HÌNH HỌC CỦA MỘT SỐ CẤU KIỆN TRONG CÔNG TRÌNH CẦU](#phụ-lục-04-mức-độ-phát-triển-thông-tin-phi-hình-học-của-một-số-cấu-kiện-trong-công-trình-cầu)
  - [1. Cọc đóng/ ép](#1-cọc-đóng-ép)
  - [2. Cọc khoan nhồi](#2-cọc-khoan-nhồi)
  - [3. Rào chắn](#3-rào-chắn)
  - [4. Bê tông vỉa hè](#4-bê-tông-vỉa-hè)
  - [5. Xà Mũ](#5-xà-mũ)
  - [6. Hàng rào bê tông](#6-hàng-rào-bê-tông)
  - [7. Sàn bê tông dự ứng lực](#7-sàn-bê-tông-dự-ứng-lực)
  - [8. Sàn bê tông liên hợp](#8-sàn-bê-tông-liên-hợp)
  - [9. Mặt đường- cầu](#9-mặt-đường--cầu)
  - [10. Dầm Super T](#10-dầm-super-t)


| ....................................................................................................                               |                                                             |
|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| 1. LỜI GIỚI THIỆU                                                                                                                  | 1                                                           |
| 2. PHẠM VI HƯỚNG DẪN .......................................................................................                       | 1                                                           |
| 3. TÀI LIỆU VIỆN DẪN ............................................................................................                  | 1                                                           |
| 4. THUẬT NGỮ VÀ ĐỊNH NGHĨA ...........................................................................                             | 2                                                           |
| PHẦN 1: MỘT SỐ NỘI DUNG TRIỂN KHAI BIM TRONG CÔNG TRÌNH DÂN                                                                        | PHẦN 1: MỘT SỐ NỘI DUNG TRIỂN KHAI BIM TRONG CÔNG TRÌNH DÂN |
| DỤNG ............................................................................................................................. | 3                                                           |
| 1. ĐỊNH DẠNG TRAO ĐỔI DỮ LIỆU ......................................................................                               | 3                                                           |
| 2. MỨC ĐỘ PHÁT TRIỂN THÔNG TIN ...................................................................                                 | 3                                                           |
| 3. BẢNG GÁN MÀU CẤU KIỆN...............................................................................                            | 3                                                           |
| 4. HƯỚNG DẪN PHỐI HỢP VÀ XỬ LÝ XUNG ĐỘT .............................................                                              | 5                                                           |
| 4.1. Trách nhiệm trong việc phối hợp đa bộ môn ở giai đoạn thiết kế .......................                                        | 5                                                           |
| 4.2. Phương pháp phối hợp .......................................................................................                  | 5                                                           |
| 4.3. Tần suất phối hợp...............................................................................................              | 8                                                           |
| 4.4. Xử lý xung đột ....................................................................................................           | 8                                                           |
| 5. YÊU CẦU THÔNG TIN TRAO ĐỔI ĐỐI VỚI BỘ MÔN KIẾN TRÚC ..............                                                              | 13                                                          |
| 5.1. Trong giai đoạn thiết kế sơ bộ ..........................................................................                     | 13                                                          |
| 5.2. Trong giai đoạn thiết kế cơ sở ..........................................................................                     | 15                                                          |
| 5.3. Trong giai đoạn thiết kế kỹ thuật ......................................................................                      | 16                                                          |
| 5.4. Trong giai đoạn thiết kế bản vẽ thi công ...........................................................                          | 18                                                          |
| 5.5. Nội dung kiểm tra chủ yếu mô hình kiến trúc ....................................................                              | 19                                                          |
| 6. YÊU CẦU THÔNG TIN TRAO ĐỔI ĐỐI VỚI BỘ MÔN KẾT CẤU ..................                                                            | 20                                                          |
| 6.1. Trong giai đoạn thiết kế sơ bộ ..........................................................................                     | 20                                                          |
| 6.2. Trong giai đoạn thiết kế cơ sở ..........................................................................                     | 20                                                          |
| 6.3. Trong giai đoạn thiết kế kỹ thuật ......................................................................                      | 21                                                          |
| 6.4. Trong giai đoạn thiết kế bản vẽ thi công ...........................................................                          | 23                                                          |
| 6.5. Danh sách kiểm tra chủ yếu cho mô hình kết cấu .............................................                                  | 24                                                          |
| 7. YÊU CẦU THÔNG TIN TRAO ĐỔI ĐỐI VỚI BỘ MÔN CƠ ĐIỆN ...................                                                           | 25                                                          |
| 7.1. Trong giai đoạn thiết kế cơ sở ..........................................................................                     | 25                                                          |
| 7.2. Trong giai đoạn thiết kế kỹ thuật ......................................................................                      | 26                                                          |
| 7.3. Trong giai đoạn thiết kế bản vẽ thi công ...........................................................                          | 27                                                          |
| 7.4. Mức độ mô hình hoá đối với hệ thống cơ điện ..................................................                                | 32                                                          |
| 7.5. Danh sách kiểm tra chủ yếu cho mô hình cơ điện .............................................                                  | 33                                                          |

| 1. ĐỊNH DẠNG TRAO ĐỔI DỮ LIỆU ....................................................................                                                                                            |   34 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 2. MỨC ĐỘ PHÁT TRIỂN THÔNG TIN .................................................................                                                                                              |   34 |
| 3. BẢNG GÁN MÃ MÀU HỆ THỐNG ....................................................................                                                                                              |   34 |
| 4. MỘT SỐ YÊU CẦU ĐỐI VỚI MÔ HÌNH HOÁ BỀ MẶT ...................................                                                                                                              |   35 |
| 4.1. Các yêu cầu độ chính xác của đối tượng là bề mặt ( bao gồm đường, địa hình)                                                                                                              |   35 |
| 4.2. Tính liên tục của các đối tượng đường ngắt (Breaklines) và bề mặt (Surface) ..                                                                                                           |   35 |
| 4.3. Tính đều đặn của lưới tam giác ........................................................................                                                                                  |   36 |
| 4.4. Độ chính xác hình học của mô hình bề mặt ......................................................                                                                                          |   37 |
| 5. YÊU CẦU THÔNG TIN TRAO ĐỔI ĐỐI VỚI CÔNG TRÌNH GIAO THÔNG (CẦU, ĐƯỜNG) .......................................................................................................              |   38 |
| 5.1. Dữ liệu ban đầu ...............................................................................................                                                                          |   38 |
| 5.2. Giai đoạn lập quy hoạch ..................................................................................                                                                               |   39 |
| 5.3. Thiết kế cơ sở ...................................................................................................                                                                       |   39 |
| 5.4. Thiết kế kỹ thuật và thiết kế bản vẽ thi công .....................................................                                                                                      |   41 |
| 5.5. Mô hình hóa giai đoạn thi công xây dựng (nhà thầu thi công) ..........................                                                                                                   |   43 |
| PHỤ LỤC 01: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN HÌNH HỌC CỦA MỘT SỐ LOẠI CẤU KIỆN TRONG CÔNG TRÌNH XÂY DỰNG DÂN DỤNG ................... PHỤ LỤC 02: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN PHI HÌNH HỌC CỦA MỘT |   44 |

## DANH MỤC HÌNH VẼ

| Hình 1 Phối hợp mô hình giữa kiến trúc và kết cấu ..........................................................                                                                                          | 6                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Hình 2 Phối hợp mô hình giữa kiến trúc/ kết cấu và cơ điện ............................................                                                                                               | 7                                                                                                      |
| Hình 3 Minh hoạ mô hình phối hợp sau khi phối hợp và xử lý xung đột ..........................                                                                                                        | 8                                                                                                      |
| Hình 4 Sơ đồ tổng thể quá trình xử lý xung đột                                                                                                                                                        | ................................................................ 9                                     |
| Hình 5 Quy trình phối hợp xử lý xung đột                                                                                                                                                              | ..................................................................... 10                               |
| Hình 6 Báo cáo va chạm trong quá trình kiểm tra xung đột ............................................                                                                                                 | 11                                                                                                     |
| Hình 7 Mô hình khối (massing) .....................................................................................                                                                                   | 14                                                                                                     |
| Hình 8 Mô hình địa hình ................................................................................................                                                                              | 15                                                                                                     |
| Hình 9 Mô hình kiến trúc của Dự án D26 Trụ sở Viettel trong giai đoạn thiết kế cơ sở                                                                                                                  | .. 16                                                                                                  |
| Hình 10 Mô hình kiến trúc của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình trong giai thiết kế kỹ thuật ...................................................................................................... | đoạn 18                                                                                                |
| Hình 11 Mô hình của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình hoàn thiện phối hợp đa môn giai đoạn thiết kế bản vẽ thi công ....................................................................            | bộ 19                                                                                                  |
| Hình 12 Mô hình kết cấu của Dự án D26 Trụ sở Viettel trong giai đoạn thiết kế cơ sở                                                                                                                   | .. 21                                                                                                  |
| Hình 13 Mô hình kết cấu của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình trong giai đoạn                                                                                                                       | thiết                                                                                                  |
| kế kỹ thuật ..............................................................................................................                                                                            | 23                                                                                                     |
| Hình 14 Mô hình kết cấu của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình trong giai đoạn                                                                                                                       | thiết                                                                                                  |
| kế bản vẽ thi công Hình 15 Mô hình hệ thống HVAC của Dự án Bệnh viện Hồng Ngọc- Mỹ Đình                                                                                                               | ................................................................................................... 24 |
| trong                                                                                                                                                                                                 | giai                                                                                                   |
| đoạn thiết kế bản vẽ thi công ..................................................................................                                                                                      | 28                                                                                                     |
| Hình 16 Mô hình hệ thống điện của Dự án Bệnh viện Hồng Ngọc - Mỹ đình trong                                                                                                                           | giai                                                                                                   |
| đoạn thiết kế bản vẽ thi công ..................................................................................                                                                                      | 29                                                                                                     |
| 17 Mô hình hệ thống phòng cháy chữa cháy của Dự án Bệnh viện Hồng Ngọc                                                                                                                                | - Mỹ                                                                                                   |
| Hình 18 Mô hình hệ thống cấp thoát nước của Dự án Bệnh viện Hồng Ngọc - Mỹ công...................................................................                                                    | 31                                                                                                     |
| Hình 19 Mô hình phòng máy của Dự án D26 Trụ sở Viettel trong giai đoạn thiết kế                                                                                                                       | bản vẽ                                                                                                 |
| thi công...................................................................................................................                                                                           | 31                                                                                                     |
| Hình 20 Mô hình hệ thống cơ điện của Dự án D26 Trụ sở Viettel trong giai đoạn thiết                                                                                                                   | kế                                                                                                     |
| .......................................................................................................                                                                                               | 32                                                                                                     |
| Hình 21 Mô hình phối hợp các hệ thống cơ điện của Dự án Bệnh viện Hồng                                                                                                                                | Mỹ                                                                                                     |
| Hình 22 Ví dụ tính liên tục lý tưởng của các đường ngắt và bề mặt trong một nút                                                                                                                       | .. 36                                                                                                  |
| Hình 23 Ảnh phối cảnh của một mô hình tam giác bề mặt đường ..................................                                                                                                        | 37                                                                                                     |
| Hình 24 Phối cảnh và minh hoạ phương án sử dụng                                                                                                                                                       |                                                                                                        |
| đất                                                                                                                                                                                                   |                                                                                                        |
|                                                                                                                                                                                                       | 40                                                                                                     |
| .................................................                                                                                                                                                     |                                                                                                        |
| đình trong giai đoạn thiết kế bản vẽ thi công                                                                                                                                                         |                                                                                                        |
| Hình                                                                                                                                                                                                  |                                                                                                        |
| Đình trong giai đoạn thiết kế bản vẽ thi công                                                                                                                                                         |                                                                                                        |
|                                                                                                                                                                                                       | 30                                                                                                     |
| trong giai đoạn thiết kế bản vẽ thi                                                                                                                                                                   |                                                                                                        |
| ..........................................................                                                                                                                                            |                                                                                                        |
|                                                                                                                                                                                                       | Đình                                                                                                   |
| bản vẽ thi công                                                                                                                                                                                       |                                                                                                        |
|                                                                                                                                                                                                       | 32                                                                                                     |
| giao                                                                                                                                                                                                  | giao                                                                                                   |
| ...........................................................                                                                                                                                           | ...........................................................                                            |
| Ngọc -                                                                                                                                                                                                | Ngọc -                                                                                                 |

| Hình 25 Mô hình thiết kế Dự án cầu Cửa Đại - Quảng Ngãi trong giai đoạn thiết kế cơ sở ............................................................................................................................... 41   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hình 26 Mô hình dự án cầu Thủ Thiêm 2 trong giai đoạn thiết kế kỹ thuật .................... 42                                                                                                                             |
| DANH MỤC BẢNG BIỂU                                                                                                                                                                                                          |
| Bảng 1 Bảng giải thích thuật ngữ ..................................................................................... 2                                                                                                    |
| Bảng 2 Bảng mã màu cho một số hệ thống Cơ điện ......................................................... 4                                                                                                                  |
| Bảng 3 Ví dụ về Ma trận kiểm tra va chạm .................................................................... 12                                                                                                            |
| Bảng 4 Bảng mã màu cho một số hệ thống .................................................................... 35                                                                                                              |
| Bảng 5 Cự ly điểm đường ngắt tối đa ở các bán kính cong khác nhau (R) và bán kính đường                                                                                                                                     |
| tròn ......................................................................................................................... 37                                                                                           |
| Bảng 6 Chiều dài tối đa của các đường ngắt song song với tuyến bình đồ theo các giá trị đường "clothoids" khác nhau .................................................................................. 38                   |

## 1. Lời giới thiệu

Hướng dẫn chi tiết áp dụng Mô hình thông tin công trình (BIM) đối với công trình dân dụng và hạ tầng kỹ thuật đô thị do Viện Kinh tế xây dựng tổ chức biên soạn, Bộ Xây dựng công bố trong khuôn khổ Đề án áp dụng Mô hình thông tin công trình (BIM) trong hoạt động xây dựng và quản lý vận hành công trình theo Quyết định số 2500/QĐ-TTg ngày 22/12/2016 của Thủ tướng Chính phủ.

Trong Hướng dẫn này làm rõ thêm một số nội dung có tính chất đặc thù liên quan đến tạo dựng Mô hình BIM trong công trình dân dụng (nhà ở, văn phòng, trụ sở,…) và công trình hạ tầng kỹ thuật đô thị (liên quan đến giao thông, cấp thoát, nước). Các nội dung hướng dẫn áp dụng Mô hình thông tin công trình (BIM) tổng thể trong dự án đầu tư xây dựng tham khảo theo Hướng dẫn chung áp dụng Mô hình thông tin công trình (BIM).

## 2. Phạm vi hướng dẫn

Hướng dẫn này để các cơ quan, tổ chức, cá nhân có liên quan tham khảo khi triển khai áp dụng BIM cho công trình dân dụng (nhà ở, văn phòng, trụ sở,…) và công trình hạ tầng kỹ thuật đô thị (công trình cầu, đường bộ, cấp thoát nước).

## 3. Tài liệu viện dẫn

Các tài liệu viện dẫn sau là cần thiết khi áp dụng Hướng dẫn này. Đối với các tài liệu viện dẫn ghi năm công bố thì áp dụng theo phiên bản được nêu. Đối với các tài liệu viện dẫn không ghi năm công bố thì áp dụng phiên bản mới nhất, bao gồm cả các sửa đổi, bổ sung (nếu có).

- -Luật Xây dựng số 50/2014/QH13 ngày 18 tháng 6 năm 2014;
- -Luật Xây dựng số 62/2020/QH14 ngày 17 tháng 6 năm 2020;
- -Nghị định số 59/2015/NĐ-CP ngày 18 tháng 6 năm 2015 của Chính phủ về Quản lý dự án đầu tư xây dựng (sau đây viết tắt là Nghị định 59/2015/NĐ-CP);
- -Nghị định số 06/2021/NĐ-CP ngày 26 tháng 1 năm 2021 của Chính phủ Quy định chi tiết một số nội dung về quản lý chất lượng thi công xây dựng và bảo trì công trình xây dựng;
- -Các tiêu chuẩn Hệ thống tài liệu thiết kế xây dựng;
- -BIMForum, Level of Development (LOD) Specification 2019 Part I  &amp; Commentary - For Building Information Models and Data (Chỉ dẫn về Mức độ phát triển thông tin cấu kiện 2019 Phần 1 và chú thích - Dành cho Mô hình thông tin công trình và dữ liệu).

## MỞ ĐẦU

## 4. Thuật ngữ và định nghĩa

Một số thuật ngữ, định nghĩa sử dụng trong Hướng dẫn này được diễn giải, định nghĩa tại Bảng 1 Bảng giải thích thuật ngữ

Bảng 1 Bảng giải thích thuật ngữ

|   STT | Thuật ngữ          | Định nghĩa                                                                                                                                      | Từ tiếng Anh    | Viết tắt   |
|-------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|------------|
|     1 | Mô hình khối       | Mô hình thể hiện hình dạng, kích thước, không gian kiến trúc của công trình ở giai đoạn sơ bộ.                                                  | Massing         |            |
|     2 | Mô hình liên hợp   | Mô hình liên hợp là mô hình BIM được tổng hợp từ các mô hình thành phần.                                                                        | Federated Model |            |
|     3 | Mô hình thành phần | Mô hình thành phần là mô hình được phân chia theo gói thầu hoặc hạng mục hoặc bộ môn hoặc tuyến, … nhằm tối ưu trong quá trình tạo lập mô hình. |                 |            |

## PHẦN 1: MỘT SỐ NỘI DUNG TRIỂN KHAI BIM TRONG CÔNG TRÌNH DÂN DỤNG

## 1. Định dạng trao đổi dữ liệu

Định dạng trao đổi dữ liệu trong quá trình tạo lập và chuyển giao mô hình BIM có thể ở định dạng gốc và định dạng mở. Dưới dây là một số định dạng mở thông dụng:

- -Mô hình kiến trúc, kết cấu, Cơ điện… (IFC, DXF…)
- -Mô hình phân tích năng lượng (gbXML, DXF, IFC,EPW,…)
- -Phối hợp, theo dõi va chạm (BCF)

## 2. Mức độ phát triển thông tin

Khi thực hiện áp dụng BIM, việc xây dựng Bảng các thành phần mô hình có thể tham khảo phần Thành phần hình học trong tài liệu BIM Forum (2019) Level of Development Specification phát hành tháng 4 năm 2019.

Mức độ phát triển thông tin hình học của một số loại cấu kiện theo các giai đoạn thực hiện dự án tham khảo Phụ lục 01: Mức độ phát triển thông tin hình học của một số loại cấu kiện trong công trình xây dựng dân dựng dân dụng.

Mức độ phát triển thông tin phi hình học của cấu kiện được xây dựng dựa trên các yêu cầu kỹ thuật cần thể hiện về vật liệu, sản phẩm và các thông tin liên quan khác sử dụng trong công tác thiết kế, thi công, quản lý vận hành. Mức độ chi tiết các thông tin cần phù hợp với từng giai đoạn thực hiện dự án.

Mức độ phát triển thông tin phi hình học của một số loại cấu kiện theo giai đoạn thực hiện tham khảo Phụ lục 02: Mức độ phát triển thông tin phi hình học của một số cấu kiện trong công trình xây dựng dân dụng.

## 3. Bảng gán màu cấu kiện

Để thuận lợi cho việc sàng lọc, nhận diện, kiểm tra trực quan, cần thiết phải gán mã màu cho từng loại cấu kiện/ hệ thống trong mô hình. Việc gán màu cần được thống nhất trước khi triển khai mô hình hoá.

Quy định về màu sắc áp dụng cho từng loại cấu kiện/ hệ thống trong công trình cần tuân thủ quy định của cơ quan nhà nước có thẩm quyền (nếu có) hoặc yêu cầu chung của dự án. Dưới đây là Bảng mã màu cho một số hệ thống Cơ điện (Bảng 2), các dự án có thể tham khảo (Tham khảo bảng mã màu tại tài liệu của tổ chức Quản lý dịch vụ hành chính Hoa Kỳ (U.S general service administration)).

Bảng 2 Bảng mã màu cho một số hệ thống Cơ điện

|                                  | Màu RGB     |
|----------------------------------|-------------|
| Hệ thống đường ống               |             |
| Cấp khí nén                      | 0,0,255     |
| Cống thoát nước mưa              | 128,0,255   |
| Tràn thoát nước mưa              | 219,183,255 |
| Hệ nước cấp lạnh                 | 0,63,255    |
| Hệ hồi nước cấp nóng             | 255,170,170 |
| Hệ nước cấp nóng                 | 255,60,60   |
| Cấp khí tự nhiên                 | 255,255,0   |
| Vệ sinh                          | 255,127,0   |
| Lỗ thông hơi vệ sinh             | 255,191,0   |
| Ống chưa xác định                | 76,38,38    |
| Hệ thống HVAC                    |             |
| Hệ hồi nước cấp nóng             | 255,0,127   |
| Hệ nước cấp nóng                 | 255,0,63    |
| Hệ ống gió thải chung            | 103,165,82  |
| Bên ngoài                        | 0,191,255   |
| Hệ ống gió hồi                   | 0,255,127   |
| Hệ ống gió cấp                   | 0,127,255   |
| Hệ ống hút khói                  | 127,255,0   |
| Hệ ống gió tạo áp                | 0,104,78    |
| Hệ thống phòng cháy chữa cháy    |             |
| Phòng cháy chữa cháy - Sprinkler | 255,0,0     |
| Phòng cháy chữa cháy - CO2       | 255,0,191   |
| Phòng cháy chữa cháy - Halon     | 255,170,234 |
| Phòng cháy chữa cháy - Khí trơ   | 189,0,141   |
| Hệ thống hơi nước                |             |
| Hơi nước - Áp suất cao           | 0,94,189    |
| Hơi nước - Áp suất trung bình    | 126,157,189 |
| Hơi nước - Áp suất thấp          | 170,212,255 |
| Hệ thống sưởi ấm và làm mát      |             |
| Hệ hồi nước cấp lạnh             | 191,0,255   |
| Hệ nước cấp lạnh                 | 234,170,255 |
| Hệ hồi nước làm mát tháp         | 141,0,189   |
| Hệ nước cấp làm mát tháp         | 173,126,189 |
| Hệ thống điện                    |             |
| Viễn thông                       | 189,189,126 |
| Phân phối điện                   | 189,189,0   |

| Chiếu sáng   | 255,255,170   |
|--------------|---------------|
| Bảo mật      | 255,255,0     |

## 4. Hướng dẫn phối hợp và xử lý xung đột

## 4.1. Trách nhiệm trong việc phối hợp đa bộ môn ở giai đoạn thiết kế

Thực hiện trong quá trình phối hợp đa bộ môn liên quan đến nhiệm vụ của một số thành viên trong nhóm thực hiện bao gồm: Điều phối BIM (BIM Coordinator) và các Kỹ thuật viên BIM (BIM Modeller). Vai trò và trách nhiệm của Quản lý BIM, Điều phối BIM, Kỹ thuật viên BIM được hướng dẫn tại tại Hướng dẫn chung áp dụng Mô hình thông tin công trình (BIM).

Trách nhiệm cụ thể của từng thành viên trong việc phối hợp xử lý xung đột có thể được quy định khác nhau trong từng dự án. Dưới đây là một số trách nhiệm chính để các dự án có thể tham khảo:

## a. Điều phối BIM

- -Chủ trì cuộc họp phối hợp;
- -Tạo lập mô hình phối hợp, kiểm tra các lỗi xung đột trước buổi họp phối hợp;
- -Thực hiện phát hiện xung đột và xuất báo cáo;
- -Gửi báo cáo lỗi xung đột đến các nhóm thực hiện;
- -Điều phối BIM chịu trách nhiệm duy trì việc tạo lập và đảm bảo chất lượng Mô hình thông tin các bộ môn.

## b. Kỹ thuật viên BIM

Cập nhật các mô hình thành phần từ kết quả buổi họp phối hợp.

## 4.2. Phương pháp phối hợp

Phối hợp đa bộ môn cần được thực hiện theo đúng kế hoạch đã đặt ra. Tại mỗi giai đoạn thực hiện dự án, việc phối hợp đa bộ môn sẽ được tập chung vào các thông tin cần thiết phải bàn giao ở giai đoạn đó.

## a. Phối hợp giai đoạn thiết kế sơ bộ

Trong giai đoạn thiết kế sơ bộ, đơn vị tư vấn khảo sát chuyển các thông tin cần thiết về vị trí, toạ độ, bề mặt địa hình (nếu có)… của công trình cho bộ phận thiết kế (thông thường là bộ phận thiết kế kiến trúc). Từ đó, bộ phận thiết kế kiến trúc thiết lập toạ độ gốc, hệ lưới, trục, cao trình, lập mô hình khối.

Ở giai đoạn này, các kiến trúc sư có thể thực hiện cả mô hình kết cấu. Tuy nhiên cần tham khảo thêm ý kiến về chuyên môn của các kỹ sư kết cấu.

## b. Phối hợp thiết kế giai đoạn thiết kế cơ sở

Trong giai đoạn thiết kế cơ sở, phối hợp mô hình chủ yếu giữa mô hình kiến trúc và mô hình kết cấu. Bộ phận thiết kế kiến trúc, kết cấu và cơ điện tham gia phối hợp trao đổi thông tin và đưa ra các yêu cầu về không gian, kỹ thuật,…

Trong quá trình mô hình hoá bộ môn kết cấu, mô hình kiến trúc cần được liên kết để thuận tiện trong quá trình lên phương án, lập mô hình. Quy trình phối hợp giữa mô hình kiến trúc và kết cấu thể hiện tại Hình 1

Hình 1 Phối hợp mô hình giữa kiến trúc và kết cấu

![Image](images/image_000000_7589e34571df2bc46b80a8b3269d0283a1e0cb86d05d261c5de81ec481aad74d.png)

## c. Phối hợp thiết kế giai đoạn thiết kế kỹ thuật, bản vẽ thi công

Mô hình kiến trúc/ kết cấu sẽ được liên kết vào mô hình cơ điện. Bộ phận thiết kế cơ điện sẽ đặt các cấu kiện, đường ống, máng cáp, bố trí lỗ mở xuyên tầng,… vào vị trí dự kiến. Quản lý BIM cần xác định các khu vực quan trọng ưu tiên phối hợp.

Trong quá trình mô hình hoá, các bộ phận thiết kế cần chủ động xử lý các lỗi va chạm (nếu có). Quá trình phối hợp giữa các bộ môn trong giai đoạn thiết kế kỹ thuật/ bản vẽ thi công được thể hiện tại Hình 2.

Hình 2 Phối hợp mô hình giữa kiến trúc/ kết cấu và cơ điện

![Image](images/image_000001_bca633d3685b7949c4dec77874c25e49c1fedd9b8a552affa8954819415e6579.png)

Hình 3 Minh hoạ mô hình phối hợp sau khi phối hợp và xử lý xung đột

![Image](images/image_000002_c65e1830f57e8ae2c60e0a0218579bc813896e0b4f012bc84fd4844bff01503d.png)

## 4.3. Tần suất phối hợp

Thời gian, tần suất, nội dung và thời điểm phối hợp cần được thống nhất trước trong kế hoạch triển khai công tác và phải được phổ biến rộng rãi cho các bên liên quan.

## 4.4. Xử lý xung đột

## a.

- Quy trình xử lý xung đột Việc phối hợp xử lý xung đột tổng thể được thực hiện theo Hình 4

![Image](images/image_000003_c4a29837b991265be8976e2bb8bfb805ae47b2cdeb86be5e5098239b0a70ef2e.png)

## Hình 4 Sơ đồ tổng thể quá trình xử lý xung đột

Trước khi thực hiện kiểm tra xung đột, các cá nhân/ đơn vị phải đảm bảo mô hình của mình đạt các yêu cầu/ quy định của dự án và ở phiên bản phù hợp cho việc phối hợp đa bộ môn. Sau khi mô hình được gửi đến Quản lý BIM, Quản lý BIM cần kiểm tra lại thông tin như sau:

- -Kiểm tra sơ bộ mô hình (toạ độ gốc, các lỗi trong mô hình, tiêu chuẩn của dự án…);
- -Kiểm tra các lỗi/ va chạm trong lần kiểm tra trước đã được sửa trong mô hình chưa?;
- -So sánh mô hình với các bản vẽ để đảm bảo các bản vẽ xuất ra tương ứng với mô hình;
- -Các nội dung khác theo yêu cầu.

Sau khi đã kiểm tra thông tin được đưa vào, Quản lý BIM cần ghi lại báo cáo các kiểm tra này. Trong trường hợp cần thiết, Quản lý BIM có thể gửi lại các báo cáo này cho các cá nhân/ đơn vị phụ trách để cập nhật lại mô hình trước khi đưa vào phối hợp.

Sau khi các mô hình thành phần đạt chất lượng, Quản lý BIM sẽ tiến hành phối hợp đa bộ môn theo các thiết lập phù hợp với từng giai đoạn, từng loại cấu kiện. Với một số xung đột có thể xử lý trực tiếp sau này trong quá trình thi công, Quản lý BIM có thể bỏ qua mà không thực hiện báo cáo. Dưới đây (Hình 5) là quy trình kiểm tra và xử lý xung đột.

Hình 5 Quy trình phối hợp xử lý xung đột

![Image](images/image_000004_22559c51267055065d184673d1f1b04124f8c2e467be177698eb4c11421ef004.png)

Hình 6 Báo cáo va chạm trong quá trình kiểm tra xung đột

![Image](images/image_000005_613232b732af92720979fe324c5b35f15c0edbc6fd4011dd264a4f56cae33edf.png)

Để đảm bảo các bên có thể phối hợp xem xét, phản hồi thuận tiện, cần quy định các nền tảng sử dụng chung trong việc quản lý va chạm. Quản lý BIM có thể lựa chọn các giải pháp khác nhau để thực hiện việc quản lý va chạm, trong đó có thể chia thành 2 giải pháp chính như sau:

- -Quản lý bằng các công cụ (phần mềm): các công cụ này sẽ tự động trích xuất các va chạm từ công cụ phối hợp mô hình, gửi thông báo đến các cá nhân/ tổ chức có trách nhiệm, cập nhật tình hình chỉnh sửa mô hình.
- -Quản lý bằng bảng biểu: Các báo cáo về va chạm sẽ được Quản lý BIM cập nhật, gửi đến các cá nhân/ đơn vị có trách nhiệm và tổ chức các buổi họp phối hợp để thống nhất phương án giải quyết. Khi các điều chỉnh được thực hiện, các bên sẽ báo cáo với Quản lý BIM để cập nhật trạng thái của các va chạm này trong báo cáo.

Báo cáo va chạm cần thể hiện các nội dung sau: vị trí, mô tả, loại va chạm…

## b. Thiết lập ma trận va chạm

Trong quá trình phối hợp cần lập ma trận phối hợp mô hình trong Kế hoạch thực hiện BIM để xác định thứ tự ưu tiên khi kiểm tra và xử lý xung đột/ va chạm.

Ma trận này xác định các thành phần sẽ phối hợp với nhau, mức độ ưu tiên của các thành phần khi phối hợp. Tuy nhiên, yêu cầu phối hợp sẽ khác nhau trong từng giai đoạn. Ví dụ: trong giai đoạn thiết kế cơ sở và thiết kế kỹ thuật, có thể phối hợp mô hình dựa trên các mô hình bộ môn, tuy nhiên, ở giai đoạn thiết kế bản vẽ thi công cần phối hợp dựa trên các đối tượng cụ thể.

Một số va chạm có thể phát hiện trong quá trình kiểm tra, tuy nhiên việc giải quyết các va chạm đó có thể không cần thiết xử lý trực tiếp trên mô hình (ví dụ: đèn led gắn trần không cần kiểm tra va chạm với ống gió hoặc cửa vì trong quá trình thi công có thể dễ dàng xử lý).

Dưới đây là ví dụ Bảng ma trận phối hợp trong giai đoạn thiết kế bản vẽ thi công (Bảng 3). Các dự án có thể tham khảo, chỉnh sửa cho phù hợp với yêu cầu của dự án.

Bảng 3 Ví dụ về Ma trận kiểm tra va chạm

![Image](images/image_000006_f6bd04c74ed7d1debce86368fd934d382b027a175b9ce76a0c3e3a4fe8fae245.png)

## c. Các đối tượng không cần kiểm tra xử lý va chạm

Trong quá trình phát hiện và xử lý xung đột, một số cặp đối tượng không cần thực hiện xử lý va chạm. Các va chạm này có thể trực tiếp xử lý tại công trường mà không cần chỉnh sửa lại mô hình. Một số va chạm có thể bỏ qua như sau:

- -Các đường ống có đường kính &lt;50mm sẽ không được kiểm tra va chạm;
- -Cốt thép sẽ không được kiểm tra va chạm;
- -Miệng gió (Air Terminal) không cần kiểm tra va chạm với trần (Ceiling);
- -Đèn âm trần (Recessed Lighting) không cần kiểm tra va chạm với trần (Ceiling);
- -Thiết  bị  báo  cháy  (Fire  Alarm  Device)  không  cần  kiểm  tra  va  chạm  với  trần (Ceiling);
- -Rãnh, lỗ thoát nước (Floor Drain / Channel &amp; Trench Drain) không cần kiểm tra va chạm với sàn (Floor/Slab);

## 5.

- -Cột (kiến trúc/ kết cấu) không cần kiểm tra va chạm với sàn/ trần trong trường hợp đổ tại chỗ.

## d. Thiết lập các nhóm va chạm

Trong quá trình thực hiện phối hợp đa bộ môn, Quản lý BIM cần thiết lập quy tắc với từng nhóm đối tượng. Các loại va chạm bao gồm 1 :

- -Va chạm cứng là khi hai vật thể có các bộ phận giao nhau trực tiếp (ví dụ các đường ống đâm xuyên qua dầm…). Các va chạm này thường sẽ rất tốn kém để khắc phục trên công trường nếu không được xử lý tốt trong giai đoạn thiết kế;
- -Va chạm mềm là khi một đối tượng nằm trong phạm vi ảnh hưởng của đối tượng khác và sẽ gây ảnh hưởng đến việc sử dụng, bảo trì của các đối tượng (ví dụ:va chạm mở cửa và tường hoặc kết cấu; các hệ thống HVAC cần không gian để thực hiện bảo trì, nếu trong khi thiết kế các vùng không gian không đủ sẽ gây ảnh hưởng đến công tác bảo trì hệ thống);
- -Va chạm 4D là xung đột liên quan đến quá trình xây dựng, khi các công việc không được lên kế hoạch thực hiện hợp lý, các đối tượng được xây dựng trước sẽ gây khó khăn trong quá trình thực hiện đối tượng sau đó (ví dụ: bố trí không gian không hợp lý dẫn đến quá trình vận chuyển thiết bị vào vị trí lắp đặt không thực hiện được).

Việc phân chia loại va chạm để phục vụ cho việc thiết lập quy tắc (Rules) kiểm tra và tìm kiếm trong quá trình tìm kiếm tự động và quản lý va chạm bằng phần mềm.

## e. Quy tắc đặt tên

Việc đặt tên góc nhìn, tên va chạm, báo cáo, ghi chú… tuân thủ yêu cầu về quy tắc đặt tên của chủ đầu tư hoặc quy định của cơ quan nhà nước có thẩm quyền (nếu có).

## f. Định dạng tập tin trong quá trình xử lý xung đột

- -Mô hình phối hợp cần được định dạng theo hướng 'chỉ đọc' nhằm cho các bên không phải là tác giả sẽ không thể điều chỉnh tập tin mô hình;
- -Báo cáo va chạm, ghi chú, đánh dấu có thể được định dạng dưới hình thức 2D hoặc 3D hoặc kết hợp cả hai.

## Yêu cầu thông tin trao đổi đối với bộ môn kiến trúc

## 5.1. Trong giai đoạn thiết kế sơ bộ

## a. Yêu cầu đầu vào

- -Hiểu rõ yêu cầu về công năng sử dụng, yêu cầu áp dụng BIM đối với công trình;
- -Thông tin dự kiến thời gian thực hiện dự án;
- -Các điều kiện hiện có (ví dụ: địa chất, địa hình khu đất, công trình hiện có);
- -Thông tin vị trí khu đất, kinh độ, vĩ độ;
- -Quy chuẩn, tiêu chuẩn kỹ thuật có liên quan.

1 Petr Matejka, Daniel Sabart, 2018, Categoriza of clashes and their impacts on Construction Projects

## b. Yêu cầu về mô hình thông tin

- -Tạo mô hình thiết kế sơ bộ có thể tính toán diện tích, khối tích của công trình;
- -Hình ảnh 3D để trực quan ý tưởng thiết kế;
- -Chuẩn bị các phương án thiết kế ý tưởng khác nhau để thảo luận;
- -Phân chia không gian, khu vực, phòng;
- -Thông tin về vị trí, đường bao khu đất, hệ lưới trục, cao độ trong mô hình;
- -Khối mở, khối đặc, khối rỗng.

## c. Đầu ra / Sản phẩm

- -Mô hình và bản vẽ hiện trạng (hạ tầng xung quanh, cao độ quy hoạch, chỉ giới xây dựng, phân chia khu vực,…);
- -Mô hình khối (diện tích xây dựng, diện tích sàn,…);
- -Bộ hồ sơ bản vẽ thiết kế sơ bộ trích xuất trực tiếp từ mô hình khối bao gồm: tổng mặt bằng dự án, mặt bằng, mặt đứng, mặt cắt chính của công trình.

Hình 7 Mô hình khối (massing)

![Image](images/image_000007_ef4e0ac2199affbc1f1b9ec1b57282485ffbc9d29df750daf8c45e64a3e59df9.png)

Hình 8 Mô hình địa hình

![Image](images/image_000008_0fbc2824cc670ab7c9a4bab5805db264839eddf219e63643f16a204ce0299d15.png)

## 5.2. Trong giai đoạn thiết kế cơ sở

## a. Yêu cầu đầu vào

- -Phương án thiết kế sơ bộ và sơ bộ tổng mức đầu tư, sản phẩm đầu ra thiết kế sơ bộ (nếu có);
- -Hồ sơ khảo sát xây dựng phục vụ lập dự án (ví dụ: địa chất, địa hình khu đất, công trình hiện có, thông tin vị trí khu đất, kinh độ, vĩ độ);
- -Hiểu rõ yêu cầu về thực hiện BIM đối với công trình;
- -Quy chuẩn, tiêu chuẩn kỹ thuật có liên quan.

## b. Yêu cầu về mô hình thông tin

- -Tạo mô hình thiết kế kiến trúc cơ sở;
- -Mô hình thể hiện chính xác hệ lưới trục và đảm bảo các bộ môn khác sử dụng hệ lưới trục này;
- -Thể hiện rõ vị trí khu vực, không gian, phòng phù hợp với yêu cầu về công năng sử dụng;
- -Thể hiện mặt bằng, mặt cắt, mặt đứng đảm bảo tiêu chuẩn, quy chuẩn kỹ thuật phù hợp với giai đoạn thiết kế cơ sở;
- -Thể hiện yêu cầu thông tin cơ bản về PCCC (thang máy PCCC, bể nước PCCC, cửa thoát hiểm,…);
- -Đảm bảo yêu cầu phối hợp mô hình kiến trúc với mô hình kết cấu và cơ điện;
- -Mô hình về các kết cấu, bộ phận chính của công trình, có thể bao gồm:
+ Tường (ở mức chiều dày, loại tường)

+ Cửa đi (cửa phòng chính, cửa vệ sinh, cửa thoát hiểm…)
+ Cửa sổ (vị trí, kích thước)
+ Sàn (độ dày hoàn thiện, sàn chính, sàn vệ sinh, lỗ mở…)
+ Mái (độ dốc, độ dày, loại mái…)
+ Thang máy (vị trí, kích thước chủ yếu)
+ Lan can
+ Cầu thang
+ Bộ phận kết cấu, thông tin vật liệu chủ yếu khác.

## c. Đầu ra / Sản phẩm

- -Mô hình thiết kế cơ sở đã được phối hợp giữa các bộ môn phù hợp với BEP;
- -Bảng diện tích phòng;
- -Các bảng thống kê liên quan;
- -Bộ hồ sơ bản vẽ phục vụ phẩm duyệt thẩm duyệt phòng cháy chữa cháy trích xuất trực tiếp từ mô hình;
- -Bộ hồ sơ bản vẽ thiết kế cơ sở trích xuất trực tiếp từ mô hình đảm bảo yêu cầu theo quy định của pháp luật hiện hành.

Hình 9 Mô hình kiến trúc của Dự án D26 Trụ sở Viettel trong giai đoạn thiết kế cơ sở

![Image](images/image_000009_7f10da4380e5343f14bdf858f5aa760ea42f4dae0c89253faea065fda06ad5c0.png)

## 5.3. Trong giai đoạn thiết kế kỹ thuật

## a. Yêu cầu đầu vào

- -Mô hình kiến trúc giai đoạn thiết kế cơ sở (nếu có);
- -Hồ sơ giai đoạn thiết kế cơ sở kèm các quyết định phê duyệt dự án;
- -Kế hoạch thực hiện BIM (BEP);

## b.

- -Hồ sơ khảo sát xây dựng phục vụ lập thiết kế kỹ thuật (ví dụ: địa chất, địa hình khu đất, công trình hiện có, thông tin vị trí khu đất, kinh độ, vĩ độ);
- -Yêu cầu kỹ thuật khác của Chủ đầu tư (nếu có).

## Yêu cầu về mô hình thông tin

- -Tạo mô hình thiết kế kiến trúc giai đoạn thiết kế kỹ thuật đảm bảo các yêu cầu về mức độ thể hiện thông tin, thể hiện chính xác ý định thiết kế, giải pháp thiết kế;
- -Thể hiện mặt bằng, mặt cắt, mặt đứng đảm bảo tiêu chuẩn, quy chuẩn kỹ thuật phù hợp với giai đoạn thiết kế kỹ thuật;
- -Thông tin chi tiết khu vực, không gian, phòng phù hợp với yêu cầu về công năng
- của Chủ đầu tư;
- -Đảm bảo yêu cầu về phối hợp mô hình kiến trúc với mô hình kết cấu và cơ điện; xử lý các xung đột;
- -Mô hình đầy đủ các thành phần, cấu kiện của công trình đảm bảo yêu cầu về mức độ thể hiện thông tin. Yêu cầu đối với một số cấu kiện, bộ phận công trình cụ thể như sau:
+ Tường (chính xác kích thước, các lớp vật liệu)
+ Cửa đi (chính xác kích thước, vật liệu cửa phòng chính, cửa vệ sinh, cửa thoát hiểm…)
- +
- +
- +
- Cửa sổ (chính xác kích thước, vật liệu…)
- Sàn hoàn thiện (chính xác độ dày, các lớp vật liệu)
- Mái (chính xác về độ dốc, độ dày, loại mái, các lớp vật liệu…)
+ Thang máy (kích thước cửa, hố thang máy…)
+ Lan can
- +
- Cầu thang

+

…

## c. Đầu ra / Sản phẩm

- -Mô hình đầy đủ thông tin phối hợp hoàn chỉnh giữa các bộ môn với nhau phù hợp với BEP;
- -Bộ bản vẽ thiết kế kỹ thuật phần kiến trúc trích xuất trực tiếp từ mô hình;
- -
- Bảng khối lượng các cấu kiện kiến trúc.

Hình 10 Mô hình kiến trúc của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình trong giai đoạn thiết kế kỹ thuật

![Image](images/image_000010_e44ae132d65fc4665a7f0940499aa3d04b04ed3aa5f8ebd7b893eaeaca299f7b.png)

## 5.4. Trong giai đoạn thiết kế bản vẽ thi công

## a. Yêu cầu đầu vào

- -Kế hoạch thực hiện BIM (BEP);
- -Mô hình kiến trúc giai đoạn thiết kế kỹ thuật (nếu có);
- -Hồ sơ thiết kế kỹ thuật;
- -Chỉ dẫn kỹ thuật có liên quan (nếu có).

## b. Yêu cầu về mô hình thông tin

- -Mô hình thiết kế bản vẽ thi công được phát triển từ mô hình thiết kế kỹ thuật, với mức độ phát triển thông tin cao hơn, thể hiện chi tiết các thành phần, cấu kiện công trình phù hợp với giai đoạn thiết kế bản vẽ thi công;
- -Phối hợp đa bộ môn xử lý triệt để xung đột đảm bảo cho quá trình thi công ngoài công trường;
- -Trích xuất khối lượng chi tiết các thành phần cấu kiện trong mô hình.

## c. Đầu ra / Sản phẩm

- -Mô hình đầy đủ thông tin phối hợp hoàn chỉnh giữa các bộ môn với nhau phù hợp với BEP;
- -Bộ hồ sơ bản vẽ thiết kế bản vẽ thi công trích xuất trực tiếp từ mô hình;
- -Bảng khối lượng các cấu kiện kiến trúc chi tiết.

Hình 11 Mô hình của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình hoàn thiện phối hợp đa bộ môn giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000011_5a3e4f72b60c1aeec260056d1bc9b2303a48d99b35c1960750784d4593e6b1c4.png)

## 5.5. Nội dung kiểm tra chủ yếu mô hình kiến trúc

| Nội dung                                                                                                                                                                | Đạt   | Không đạt   | Ghi chú   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------------|-----------|
| Đáp ứng các yêu cầu chung trong việc mô hình hoá đối tượng                                                                                                              |       |             |           |
| Mô hình ở định dạng đã được thống nhất, bao gồm các tầng đã được xác định. Các thành phần được thể hiện riêng biệt, sử dụng chính xác đối tượng thuộc hệ thống phù hợp. |       |             |           |
| Mô hình bao gồm các bộ phận công trình cần thiết                                                                                                                        |       |             |           |
| Bộ phận công trình được mô hình hóa bằng cách sử dụng đúng đối tượng đã được thống nhất cho dự án.                                                                      |       |             |           |
| Không có thành phần thừa, chồng chéo hoặc trùng lặp                                                                                                                     |       |             |           |
| Không có xung đột đáng kể hoặc có nhưng trong phạm vi dung sai cho phép đã được thống nhất giữa các đối tượng.                                                          |       |             |           |
| Tên và loại không gian theo sự thống nhất cho toàn dự án                                                                                                                |       |             |           |
| Không gian, tường và cột khớp với tổng diện tích sàn.                                                                                                                   |       |             |           |
| Dự kiến trước không gian cho việc bố trí hệ thống cơ điện và các bộ phận kết cấu                                                                                        |       |             |           |
| Chiều cao không gian được xác định phù hợp (bao gồm cả trần treo)                                                                                                       |       |             |           |
| Hình dạng và kích thước của không gian phù hợp với tường, vách                                                                                                          |       |             |           |
| Các khoảng không gian không chồng lấn nhau                                                                                                                              |       |             |           |
| Tất cả các không gian đều có định danh                                                                                                                                  |       |             |           |

## 6. Yêu cầu thông tin trao đổi đối với bộ môn kết cấu

## 6.1. Trong giai đoạn thiết kế sơ bộ

## a. Yêu cầu đầu vào

- -Mô hình kiến trúc sơ bộ;
- -Thông tin dự kiến thời gian thực hiện dự án;
- -
- Các điều kiện hiện có (ví dụ: địa chất, địa hình khu đất, công trình hiện có);
- -
- Thông tin vị trí khu đất, kinh độ, vĩ độ.

## b. Yêu cầu về mô hình thông tin

- -Đưa ra được kích thước sơ bộ ban đầu của các phần tử chịu lực chính;
- -Mô hình kết cấu sơ bộ, trong đó các cấu kiện kết cấu chính chứa các tham biến để cập nhật vào giai đoạn sau;
- -Chuẩn bị các phương án kết cấu để thảo luận.

## c. Đầu ra / Sản phẩm

- -Trong giai đoạn thiết kế sơ bộ, đơn vị thiết kế kết cấu không bắt buộc phải mô hình hóa kết cấu công trình. Tùy thuộc vào từng dự án cụ thể đơn vị thiết kế kết cấu có thể lập mô hình để tăng khả năng tương tác hoặc theo yêu cầu của dự án. Mức độ chi tiết và độ chính xác của mô hình trong giai đoạn này dựa theo mục đích của việc dựng mô hình;
- -Ngoài ra, trong giai đoạn này việc mô hình hóa có thể sử dụng để mô phỏng các giải pháp kết cấu khác nhau nhằm xác định chi phí. Mức độ chi tiết và độ chính các của mô hình phải tuân thủ;
- -Bộ hồ sơ bản vẽ sơ bộ trích xuất từ mô hình bao gồm: mặt bằng, mặt đứng, mặt cắt chính của công trình.

## 6.2. Trong giai đoạn thiết kế cơ sở

## a. Yêu cầu đầu vào

- -Phương án thiết kế sơ bộ, sản phẩm đầu ra thiết kế sơ bộ (nếu có);
- -Hồ sơ khảo sát xây dựng phục vụ lập dự án (ví dụ: địa chất, địa hình khu đất, công trình hiện có, thông tin vị trí khu đất, kinh độ, vĩ độ);
- -Hiểu rõ yêu cầu về thực hiện BIM đối với công trình;
- -Hệ lưới trục chung;
- -
- Quy chuẩn, tiêu chuẩn kỹ thuật có liên quan.

## Yêu cầu về mô hình thông tin

- -Tạo mô hình kết cấu theo yêu cầu trong giai đoạn thiết kế cơ sở;
- -Thể hiện rõ vị trí định vị cọc, cột, dầm…;
- -Thể hiện các phương án sơ bộ kết cấu chính, nền móng cho công trình;
- -
- Đảm bảo phối hợp mô hình kết cấu với mô hình phân tích tính toán kết cấu;
- -Thể hiện yêu cầu thông tin cơ bản về PCCC;

## b.

- -Mô hình về các kết cấu, bộ phận chính của công trình.

## c. Đầu ra / Sản phẩm

- -Mô hình thiết kế cơ sở đã được phối hợp giữa các bộ môn phù hợp với BEP;
- -Bộ hồ sơ bản vẽ phục vụ thẩm duyệt phòng cháy chữa cháy trích xuất trực tiếp từ mô hình;
- -Bộ hồ sơ bản vẽ thiết kế cơ sở trích xuất trực tiếp từ mô hình đảm bảo yêu cầu theo quy định của pháp luật hiện hành.

Hình 12 Mô hình kết cấu của Dự án D26 Trụ sở Viettel trong giai đoạn thiết kế cơ sở

![Image](images/image_000012_d36350975f113b3e35c61254b2c5c3d4468fcac6c853c58bd92f2c94c72e4d50.png)

## 6.3. Trong giai đoạn thiết kế kỹ thuật

## a. Yêu cầu đầu vào

- -Mô hình kết cấu giai đoạn thiết kế cơ sở (nếu có);
- -Hồ sơ giai đoạn thiết kế cơ sở kèm các quyết định phê duyệt dự án;
- -Hồ sơ khảo sát xây dựng phục vụ lập thiết kế kỹ thuật (ví dụ: địa chất, địa hình khu đất, công trình hiện có, thông tin vị trí khu đất, kinh độ, vĩ độ);
- -Yêu cầu kỹ thuật khác của Chủ đầu tư (nếu có).

## b. Yêu cầu về mô hình thông tin

- -Phù hợp với thiết kế cơ sở được duyệt;
- -Thể hiện các giải pháp kết cấu công trình phải bảo đảm an toàn, phù hợp với nội dung dự án được duyệt và phù hợp tiêu chuẩn kỹ thuật;
- -Thể hiện đầy đủ các thông số kỹ thuật của tất cả các phần tử. Là cơ sở để triển khai thiết kế thi công;
- -Đảm bảo yêu cầu phối hợp mô hình kết cấu với mô hình kiến trúc và mô hình cơ điện, phát hiện và xử lý các xung đột;
- -Mô hình về các kết cấu, bộ phận của công trình, có thể bao gồm:
+ Phần móng (chính xác kích thước, vật liệu...)

## c.

- o

- Cọc

- o

- Đài móng

- o

- Dầm móng

- o

- Bê tông lót

- o

- Móng cọc

- o

- Móng bè

- o

- Tường móng chịu lực

- o

- Hố thang máy

- o Sàn tấm

o

…

+ Phần khung (chính xác kích thước, vật liệu...)

- o

- Cột

- o Dầm

- o Sàn

- o

- Cầu thang

- o

- Tường chịu lực

- o

- Hệ giằng liên kết

- o

- Dầm giàn

o

…

- -Trích xuất khối lượng chủ yếu từ mô hình.

## Đầu ra / Sản phẩm

- -Trong giai đoạn thiết kế kỹ thuật, đơn vị thiết kế kết cấu xây dựng mô hình nhằm đảm bảo sự an toàn, đầy đủ thông tin phù hợp với thiết kế cơ sở đã được phê duyệt, đảm bảo điều kiện để triển khai mô hình thiết kế thi công;
- -Mô hình đầy đủ thông tin phối hợp hoàn chỉnh giữa các bộ môn với nhau phù hợp với BEP;
- -
- Bộ bản vẽ thiết kế kỹ thuật trích xuất trực tiếp từ mô hình;
- -Bảng khối lượng chi tiết các cấu kiện kết cấu (nếu có).

Hình 13 Mô hình kết cấu của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình trong giai đoạn thiết kế kỹ thuật

![Image](images/image_000013_729413fa5170980c1cb68a8fc644d69337b2c4b1cf03a3625786a993fa59c2af.png)

## 6.4. Trong giai đoạn thiết kế bản vẽ thi công

## a. Yêu cầu đầu vào

- -Mô hình kết cấu giai đoạn thiết kế kỹ thuật (nếu có);
- -Hồ sơ thiết kế kỹ thuật;
- -Chỉ dẫn kỹ thuật có liên quan (nếu có).

## b. Yêu cầu về mô hình thông tin

- -Thể hiện đầy đủ vị trí, các thông số kỹ thuật, vật liệu sử dụng và chi tiết cấu tạo của tất cả các phần tử;
- -Gia cố xử lý nền - móng, kết cấu chịu lực chính, hệ thống kỹ thuật công trình, công trình xây dựng dân dụng… (nếu có);
- -Chi tiết thiết kế các liên kết chính, liên kết quan trọng của kết cấu chịu lực chính và các cấu tạo bắt buộc (cấu tạo để an toàn khi sử dụng - vận hành - khai thác, cấu tạo để kháng chấn, cấu tạo để chống ăn mòn, xâm thực);
- -Thể hiện mặt bằng, mặt cắt, mặt đứng đầy đủ thông tin đảm bảo tiêu chuẩn xây dựng của Việt Nam ở giai đoạn thiết kế bản vẽ thi công;
- -Phối hợp mô hình kết cấu với mô hình kiến trúc và mô hình cơ điện và xử lý triệt để xung đột;

- -Mô hình về các kết cấu, bộ phận của công trình đảm bảo mức độ phát triển thông tin phù hợp trong giai đoạn triển khai thi công.

## c. Đầu ra / Sản phẩm

- -Mô hình thiết kế bản vẽ thi công phần kết cấu là cơ sở để triển khai quá trình thi công xây dựng công trình phù hợp với BEP;
- -Bộ bản vẽ thiết kế bản vẽ thi công trích xuất trực tiếp từ mô hình;
- -Bảng khối lượng chi tiết.

Hình 14 Mô hình kết cấu của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình trong giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000014_9e71cd44056342d3dcbb1bd747aaed1adaad77d8a45c84f37b7e0cfb04df5614.png)

## 6.5. Danh sách kiểm tra chủ yếu cho mô hình kết cấu

| Nội dung kiểm tra                                                                                                       | Đạt   | Không đạt   | Ghi chú   |
|-------------------------------------------------------------------------------------------------------------------------|-------|-------------|-----------|
| Đáp ứng các yêu cầu chung trong việc mô hình hoá đối tượng                                                              |       |             |           |
| Mô hình ở định dạng đã được thống nhất.                                                                                 |       |             |           |
| Các cấu kiện được mô hình hoá bằng chính xác loại đối tượng được quy định trong phần mềm hoặc trong quy định của dự án. |       |             |           |
| Mô hình bao gồm các bộ phận công trình cần thiết                                                                        |       |             |           |
| Không có thành phần thừa, chồng chéo hoặc trùng lặp                                                                     |       |             |           |
| Không có va chạm giữa mô hình kết cấu và các mô hình khác                                                               |       |             |           |
| Không có xung đột giữa các cấu trúc và sự xuyên qua trong các mô hình kiến trúc/ kết cấu                                |       |             |           |
| Các lỗ mở và vị trí dành riêng cho hệ thống cơ điện trong các cấu kiện kết cấu                                          |       |             |           |

## 7. Yêu cầu thông tin trao đổi đối với bộ môn cơ điện

## 7.1. Trong giai đoạn thiết kế cơ sở

## 7.1.1. Hệ thống HVAC

- a. Yêu cầu đầu vào
2. -Phương án thiết kế sơ bộ, sản phẩm đầu ra thiết kế sơ bộ (nếu có);
3. -
4. Hệ lưới trục chung;
5. -Hiểu rõ yêu cầu về thực hiện BIM đối với công trình;
6. -
7. Điện chiếu sáng và nguồn điện (nếu có).

## Yêu cầu về mô hình thông tin

- -Thiết lập mô hình năng lượng, đánh dấu khu vực và luồng không khí (nếu có);
- -Mô hình hệ thống HVAC cơ sở và xác định các yêu cầu đặc biệt (nếu có);
- -
- Xác nhận yêu cầu không gian phòng/ vị trí và tuyến ống;
- -
- Xác định các yêu cầu giao diện với các mô hình khác.

## Đầu ra/ sản phẩm

## b.

## c.

- -
- Bản vẽ thiết kế cơ sở (sơ đồ nguyên lý) đầy đủ thông tin theo yêu cầu.

## 7.1.2. Hệ thống điện

## a. Yêu cầu đầu vào

- -
- Phương án thiết kế sơ bộ, sản phẩm đầu ra thiết kế sơ bộ (nếu có);
- -
- Hiểu rõ yêu cầu về thực hiện BIM đối với công trình;
- -Điện chiếu sáng và nguồn điện (nếu có).

## Yêu cầu về mô hình thông tin

- -Xây dựng sơ đồ hệ thống cơ sở và xác định các yêu cầu đặc biệt (nếu có);
- -Xác nhận yêu cầu không gian phòng/ vị trí và yêu cầu đường truyền điện;
- -
- Kích thước dự tính phòng máy chính (máy biến áp, máy phát điện, máy tổng);
- -
- Xác định các yêu cầu giao diện với các mô hình khác;
- -
- Phương pháp phân phối điện khu vực.

## c.

## Đầu ra / Sản phẩm

Bản vẽ thiết kế cơ sở (sơ đồ nguyên lý) đầy đủ thông tin theo yêu cầu.

## 7.1.3.

## Hệ thống phòng cháy chữa cháy

## a. Yêu cầu đầu vào

- -Phương án thiết kế sơ bộ, sản phẩm đầu ra thiết kế sơ bộ (nếu có);
- -
- Hiểu rõ yêu cầu về thực hiện BIM đối với công trình;
- -
- Cập nhật báo cáo kỹ thuật PCCC (nếu có), đặc biệt là khói.

## b. Yêu cầu về mô hình thông tin

- -Thiết lập vị trí bể chứa nước cứu hỏa;
- -Xây dựng sơ đồ hệ thống và xác định các yêu cầu đặc biệt (nếu có);
- -
- Xác nhận yêu cầu không gian phòng/ vị trí và tuyến đường ống;
- -Xác định các yêu cầu giao diện với các mô hình khác.

## b.

## c. Đầu ra / Sản phẩm

Bản vẽ thiết kế cơ sở (sơ đồ nguyên lý) đầy đủ thông tin theo yêu cầu.

## 7.1.4. Hệ thống cấp thoát nước

- a. Yêu cầu đầu vào
2. -Phương án thiết kế sơ bộ, sản phẩm đầu ra thiết kế sơ bộ (nếu có);
3. -
4. Hiểu rõ yêu cầu về thực hiện BIM đối với công trình.

## b. Yêu cầu về mô hình thông tin

- -
- Thông tin sơ bộ bể chứa nước, vị trí và dung tích;
- -
- -
- Thiết kế cơ sở hệ thống và xác định các yêu cầu đặc biệt (nếu có);
- Xác nhận yêu cầu không gian phòng/ vị trí và tuyến đường ống;
- -Xác định các yêu cầu giao diện với các mô hình khác.

## c. Đầu ra / Sản phẩm

Bản vẽ thiết kế cơ sở (sơ đồ nguyên lý) đầy đủ thông tin theo yêu cầu.

## 7.2. Trong giai đoạn thiết kế kỹ thuật

## 7.2.1. Hệ thống HVAC

- a. Yêu cầu đầu vào
2. -
3. Mô hình cơ điện giai đoạn thiết kế cơ sở (nếu có);
4. -Hồ sơ giai đoạn thiết kế cơ sở kèm các quyết định phê duyệt dự án;
5. -Kế hoạch thực hiện BIM (BEP).

## b. Yêu cầu về mô hình thông tin

- -Phối hợp với mô hình kiến trúc, kết cấu và các mô hình khác, phát hiện và xử lý xung đột;
- -Kết hợp các yêu cầu báo cáo phòng cháy, âm thanh hoặc báo cáo khác có liên quan (nếu có);
- -
- Kiểm tra và xem xét các giao diện cơ / điện, ví dụ như tải;
- -Phối hợp xung đột đa bộ môn để nhận dạng và đánh giá với dung sai +/- 100mm.

## c. Đầu ra / Sản phẩm

Bản vẽ và mô hình đầy đủ thông tin liên quan đến hệ thống HVAC phù hợp với BEP.

## 7.2.2.

## Hệ thống điện

## a. Yêu cầu đầu vào

- -Mô hình cơ điện giai đoạn thiết kế cơ sở (nếu có);
- -
- Hồ sơ giai đoạn thiết kế cơ sở kèm các quyết định phê duyệt dự án;
- -
- Kế hoạch thực hiện BIM (BEP).

## b. Yêu cầu về mô hình thông tin

- -
- Phối hợp với Kết cấu, Kiến trúc và các mô hình khác, phát hiện và xử lý xung đột;
- -
- Thể hiện rõ kích thước thiết bị và máy móc;
- -Thể hiện rõ số lượng thiết bị điện trên khu vực dựa theo bảng dữ liệu phòng;
- -
- Phối hợp xung đột đa ngành để nhận dạng và đánh giá với dung sai +/- 100mm.

## c. Đầu ra / Sản phẩm

Bản vẽ và mô hình đầy đủ thông tin liên quan đến hệ thống điện phù hợp với BEP.

## 7.2.3. Hệ thống phòng cháy chữa cháy

## a. Yêu cầu đầu vào

- -
- -
- Mô hình cơ điện giai đoạn thiết kế cơ sở (nếu có);
- Hồ sơ giai đoạn thiết kế cơ sở kèm các quyết định phê duyệt dự án;
- -Kế hoạch thực hiện BIM (BEP).

## b. Yêu cầu về mô hình thông tin

- -Thể hiện rõ bố trí hệ thống đường ống phun nước, bao gồm các kích cỡ;
- -
- Phối hợp với kết cấu, kiến trúc và các mô hình khác, phát hiện và xử lý xung đột;
- -Kết hợp các yêu cầu Báo cáo phòng cháy, âm thanh hoặc báo cáo khác có liên quan (nếu có);
- -Phối hợp xung đột đa bộ môn để nhận dạng và đánh giá với dung sai +/- 100mm.

## c. Đầu ra / Sản phẩm

Bản vẽ và mô hình đầy đủ thông tin liên quan đến hệ thống PCCC phù hợp với BEP.

## 7.2.4. Hệ thống cấp thoát nước

## a. Yêu cầu đầu vào

- -Mô hình cơ điện giai đoạn thiết kế cơ sở (nếu có);
- -Hồ sơ giai đoạn thiết kế cơ sở kèm các quyết định phê duyệt dự án;
- -
- Kế hoạch thực hiện BIM (BEP).

## b. Yêu cầu về mô hình thông tin

- -Thể hiện bố trí đường ống, bao gồm các kích cỡ;
- -
- Phối hợp với kết cấu, kiến trúc và các mô hình khác, phát hiện và xử lý xung đột;
- -Kết hợp các yêu cầu báo cáo phòng cháy, âm thanh hoặc báo cáo khác có liên quan
- (nếu có);
- Phối hợp xung đột đa ngành để nhận dạng và đánh giá với dung sai +/- 100mm.
- -
- Đầu ra / Sản phẩm Bản vẽ và mô hình đầy đủ thông tin liên quan đến hệ thống phù hợp với BEP.

## c.

## 7.3. Trong giai đoạn thiết kế bản vẽ thi công

## 7.3.1.

## Hệ thống HVAC

## a. Yêu cầu đầu vào

- -Mô hình cơ điện giai đoạn thiết kế kỹ thuật (nếu có)
- -
- -
- Hồ sơ thiết kế kỹ thuật.;
- Chỉ dẫn kỹ thuật có liên quan (nếu có).

## b. Yêu cầu về mô hình thông tin

- -Thể hiện hệ thống chi tiết bao gồm thiết bị, ống dẫn và đường ống;
- Phối hợp với mô hình kiến trúc, kết cấu và các mô hình khác, xử lý triệt để các xung
- -đột;
- -
- Kiểm tra và xem xét các giao diện cơ / điện;

- -Phối hợp xung đột đa ngành với dung sai đến +/- 50mm.

## c. Đầu ra / Sản phẩm

Bản vẽ và mô hình đầy đủ thông tin đảm bảo khả năng thi công ngoài công trường phù hợp với BEP.

Hình 15 Mô hình hệ thống HVAC của Dự án Bệnh viện Hồng Ngọc- Mỹ Đình trong giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000015_f89a56790112d42d46a92dea7c454e8bef651ab4ecf305712494a0932d23de0f.png)

## 7.3.2. Hệ thống điện

## a. Yêu cầu đầu vào

- -Mô hình cơ điện giai đoạn thiết kế kỹ thuật (nếu có);
- -Hồ sơ thiết kế kỹ thuật;
- -Chỉ dẫn kỹ thuật có liên quan (nếu có).

## b. Yêu cầu về mô hình thông tin

- -Phối hợp với kết cấu, kiến trúc sư và các mô hình khác, xử lý triệt để các xung đột;
- -Hoàn thiện sơ đồ hệ thống và xác định các yêu cầu đặc biệt (nếu có);
- -Thể hiện chi tiết các kích thước và chủng loại;
- -Hoàn thiện bố trí cho các thiết bị điện và chiếu sáng;
- -Kiểm tra và xem xét các giao diện cơ/ điện;
- -Phối hợp xung đột đa bộ môn với dung sai đến +/- 50mm.

## c. Đầu ra / Sản phẩm

Bản vẽ và mô hình đầy đủ thông tin đảm bảo khả năng thi công ngoài công trường phù hợp với BEP.

Hình 16 Mô hình hệ thống điện của Dự án Bệnh viện Hồng Ngọc - Mỹ đình trong giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000016_fd2cbdb192f5dd5baba03fe2404d7378afcdbbea8dc1885998af5eed30538f5a.png)

## 7.3.3. Hệ thống phòng cháy chữa cháy

## a. Yêu cầu đầu vào

- -Mô hình cơ điện giai đoạn thiết kế kỹ thuật (nếu có);
- -Hồ sơ thiết kế kỹ thuật;
- -Chỉ dẫn kỹ thuật có liên quan (nếu có).

## b. Yêu cầu về mô hình thông tin

- -Thể hiện hệ thống chi tiết bao gồm thiết bị và đường ống;
- -Phối hợp với kết cấu, kiến trúc và các mô hình khác, xử lý triệt để các xung đột;
- -Kiểm tra và xem xét các giao diện cơ/ điện;
- -Thể hiện rõ vị trí bố trí vòi phun nước, kèm các ghi chú, yêu cầu thông tin cụ thể khác;
- -Phối hợp xung đột đa bộ môn với dung sai đến +/- 50mm.

## c. Đầu ra / Sản phẩm

Bản vẽ và mô hình đầy đủ thông tin đảm bảo khả năng thi công ngoài công trường phù hợp với BEP.

Hình 17 Mô hình hệ thống phòng cháy chữa cháy của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình trong giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000017_c2d5b624003082d323ac72a111d35966ee5e13f5df05f79c39c794addd19358f.png)

## 7.3.4. Hệ thống cấp thoát nước

## a. Yêu cầu đầu vào

- -Mô hình cơ điện giai đoạn thiết kế kỹ thuật (nếu có);
- -Hồ sơ thiết kế kỹ thuật;
- -Chỉ dẫn kỹ thuật có liên quan (nếu có).

## b. Yêu cầu về mô hình thông tin

- -Thể hiện hệ thống chi tiết bao gồm thiết bị và đường ống;
- -Phối hợp với kết cấu, kiến trúc sư và các mô hình khác, xử lý triệt để các xung đột;
- -Kiểm tra và xem xét các giao diện cơ/ điện;
- -Thể hiện rõ vị trí bố trí đường ống, các thông tin liên quan khác;
- -Phối hợp xung đột đa bộ môn với dung sai đến +/- 50mm.

## c. Đầu ra / Sản phẩm

Bản vẽ và mô hình đầy đủ thông tin đảm bảo khả năng thi công ngoài công trường phù hợp với BEP.

Hình 18 Mô hình hệ thống cấp thoát nước của Dự án Bệnh viện Hồng Ngọc - Mỹ Đình trong giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000018_299dc9b3cade0bed40e26fabf0fe0c06237c583b084c5d6f22f562f93c688f7b.png)

Hình 19 Mô hình phòng máy của Dự án D26 Trụ sở Viettel trong giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000019_c5a5051c3de03e0e97a60dd2c3feccc33f9fba44d5940a22de59a1e6e6dac7dd.png)

Hình 20 Mô hình hệ thống cơ điện của Dự án D26 Trụ sở Viettel trong giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000020_b6a2f43d836c37e632b84e07e24bf678f6adfaaf12bc29e2bddbeaa23b3308a5.png)

Hình 21 Mô hình phối hợp các hệ thống cơ điện của Dự án Bệnh viện Hồng Ngọc - Mỹ đình trong giai đoạn thiết kế bản vẽ thi công

![Image](images/image_000021_1d7d7eb44aeff2caa820d779c6e4405faea214d40f2d7ee7a09696e097c63f10.png)

## 7.4. Mức độ mô hình hoá đối với hệ thống cơ điện

| Giai đoạn          | Mức độ mô hình hoá   | Nội dung                                                                                                                           | Yêu cầu kiểm tra xung đột             |
|--------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Thiết kế sơ bộ     | 10%                  | Phòng máy và không gian thiết bị chính                                                                                             | Không                                 |
| Thiết kế cơ sở     | 30%                  | Các hạng mục chính, phòng máy và các tuyến, lưới tuyến chính được mô hình hóa để phối hợp                                          | Không                                 |
| Thiết kế kỹ thuật  | 60%                  | Các hạng mục chính, phụ, phòng máy, các tuyến, lưới tuyến chính và các tuyến nhỏ được mô hình hóa để phối hợp ở cấp độ trung bình. | Phát hiện va chạm đến dung sai 100mm. |
| Giai đoạn đấu thầu | 90%                  | Các hạng mục chính, phụ, phòng máy, các tuyến, lưới tuyến chính và các tuyến nhỏ được mô hình hóa để phối hợp ở cấp độ cao.        | Phát hiện xung đột đến dung sai 50mm. |
| Giai đoạn thi công | 100%                 | Theo chi tiết giai đoạn đấu thầu được cập nhật để chuẩn bị cho giai đoạn thi công.                                                 | Xử lý triệt để các xung đột           |

## 7.5. Danh sách kiểm tra chủ yếu cho mô hình cơ điện

| Nội dung                                                        | Đạt   | Không đạt   | Ghi chú   |
|-----------------------------------------------------------------|-------|-------------|-----------|
| Mô hình ở định dạng đã được thống nhất                          |       |             |           |
| Tiêu chuẩn BIM của dự án                                        |       |             |           |
| Mô hình có tuân thủ định dạng file của dự án                    |       |             |           |
| Mô hình có sàn                                                  |       |             |           |
| Các cấu kiện được gắn với sàn                                   |       |             |           |
| Các cấu kiện được yêu cầu ứng với giai đoạn đã được mô hình hoá |       |             |           |
| Các cấu kiện được mô hình hoá bằng đúng công cụ trong phần mềm  |       |             |           |
| Hệ thống được định nghĩa với tất cả các cấu kiện của chúng      |       |             |           |
| Tên hệ thống được đặt theo quy định                             |       |             |           |
| Màu sắc của hệ thống được đặt theo đúng quy định                |       |             |           |
| Mô hình không chứa các loại cấu kiện khác                       |       |             |           |
| Mô hình không chứa các cấu kiện bị trùng lặp                    |       |             |           |
| Không có va chạm với mô hình kiến trúc/ kết cấu                 |       |             |           |
| Hệ thống có các thông tin cần thiết theo từng giai đoạn         |       |             |           |

## PHẦN 2: MỘT SỐ NỘI DUNG TRIỂN KHAI BIM TRONG CÔNG TRÌNH HẠ TẦNG KỸ THUẬT ĐÔ THỊ

## 1. Định dạng trao đổi dữ liệu

Trong quá trình thực hiện dự án, định dạng sử dụng để trao đổi dữ liệu của từng loại mô hình cần được thống nhất giữa các đơn vị tham gia thực hiện, đảm bảo trao đổi thông tin được xuyên suốt.

Một số định dạng trao đổi dữ liệu thông dụng sử dụng trong các dự án đầu tư xây

dựng hạ tầng kỹ thuật đô thị:

- Đám mây điểm (LAS, E57, XYZ, PTS)
- Dữ liệu GIS (LANDXML, CityGML, NAS)
- Dữ liệu quy hoạch (PDF, DXF, OBJ, FBX)
- Ảnh (TIFF, BMP, GEOTIFF)
- Mô hình hiện trạng (IFC, OKSTRA)
- Mô hình địa hình (XYZ, IFC, LANDXML)
- Mô hình đất (GNDXML, AGS, LANDXML)
- Mô hình GIS (GML, LANDXML, ARCGIS)
- Mô hình cầu, hầm (IFC)
- Mô hình phục vụ lập tiến độ thi công, bóc tách khối lượng-chi phí, phân tích (IFC)

## 2. Mức độ phát triển thông tin

Mức độ phát triển thông tin một số bộ phận cấu kiện công trình hạ tầng kỹ thuật đô thị tham khảo Phụ lục 03: Mức độ phát triển thông tin của một số loại cấu kiện trong công trình hạ tầng kỹ thuật đô thị (giao thông, cấp thoát nước).

Mức độ phát triển thông tin phi hình học cho các bộ phận của cầu tham khảo Phụ lục 04: Mức độ phát triển thông tin phi hình học của một số cấu kiện trong công trình cầu.

## 3. Bảng gán mã màu hệ thống

Để phân biệt các hệ thống trong tổng thể dự án, cần thống nhất về mã màu cho từng hệ thống. Mã màu tuân thủ theo quy định của cơ quan có thẩm quyền (nếu có).

Dưới đây là Bảng mã màu cho một số hệ thống để tham khảo (Bảng 4).

Bảng 4 Bảng mã màu cho một số hệ thống

| Hạng mục                     | Màu sắc   |   R |   G |   B |
|------------------------------|-----------|-----|-----|-----|
| Hệ thống đường giao thông    |           | 220 | 220 | 220 |
| Mạng lưới thoát nước mưa     |           |   0 |   0 | 255 |
| Mạng lưới thoát nước thải    |           | 100 |  50 | 150 |
| Mạng lưới cấp nước           |           |   0 | 180 | 255 |
| Mạng lưới chiếu sáng         |           | 255 | 150 |   0 |
| Mạng lưới cấp điện           |           | 255 | 250 |   0 |
| Mạng lưới thông tin liên lạc |           |   0 | 255 |   0 |

## 4. Một số yêu cầu đối với mô hình hoá bề mặt

## 4.1. Các yêu cầu độ chính xác của đối tượng là bề mặt ( bao gồm đường, địa hình)

Các yêu cầu độ chính xác của mô hình thiết kế gồm:

- -Các yêu cầu nội dung về thông tin và thuộc tính;
- -Yêu cầu tính liên tục đối với các Breaklines và Surface (đường ngắt (đường dẫn) và bề mặt) : tại các vị trí bề mặt có sự thay đổi theo dạng dải như lề đường, chân taluy thì phải có đường breakline (đường dẫn hướng) để đảm bảo mô hình bề mặt được chính xác, đảm bảo lưới tam giác không được cắt qua đường breakline;
- -Yêu cầu hình học đối với đường ngắt, bề mặt, các đối tượng và các đối tượng điểm, cũng như tính đều đặn của lưới tam giác. Các vị trí đường ngắt phải trùng với khoảng cách ngắn nhất là 0.5m, các vị trí điểm đặt biệt, các vị trí nút giao, vị trí cong nằm trên mặt bằng và cong đứng trên trắc dọc.

## 4.2. Tính liên tục của các đối tượng đường ngắt (Breaklines) và bề mặt (Surface)

## Yêu cầu

Tất cả các đường ngắt và bề mặt trong thiết kế cuối cùng phải cần liên tục nhất có thể. Các bề mặt không được có các thay đổi theo chiều thẳng đứng và không cho phép có các đường ngắt trùng lặp trên bề mặt.

## Hướng dẫn

Các đường ngắt (Breaklines) phải liên tục. Không được có bất kỳ giật cấp (bậc đứng) giữa các đường ngắt trên bề mặt tại vị trí có khoảng hở. Tính liên tục của bề mặt có thể được đánh giá nhờ hỗ trợ của các đường đồng mức, các mặt cắt ngang và các mô hình (3D views). Lý do của việc không có bất kỳ giật cấp của các đường breakline vì trong các thuật toán xây dựng mô hình từ các điểm và đường thẳng không cho phép xây dựng các bề mặt thẳng đứng. Như ví dụ dưới đây, đường bó vỉa không được thẳn đứng với đường chân lề mà phải lùi vào 1-3mm.

Hình 22 Ví dụ tính liên tục lý tưởng của các đường ngắt và bề mặt trong một nút giao

![Image](images/image_000022_403d957090203e0545281330091bcefa2b7c7d754e4d1df7021577439e3f53a8.png)

## 4.3. Tính đều đặn của lưới tam giác

Lưới tam giác trong các mô hình thiết kế cuối cùng cần phải đều nhất có thể, nghĩa là các tam giác phải được kết nối với cùng một đường ngắt theo cự ly bằng nhau. Cách tốt nhất để đáp ứng yêu cầu này là cài đặt những điểm đường ngắt ở những lý trình đều, ví dụ năm hay mười mét. Mô hình tam giác đều cho phép dễ dàng nhận biết bề mặt kết cấu. Tư liệu đường nét và lưới tam giác phải tương ứng với nhau sao cho một tam giác được đặt ở từng điểm đường nét. Đường nét không được chứa những điểm không thuộc phần của lưới tam giác.

Yêu cầu tính đều đặn của lưới tam giác được thỏa mãn nếu tuân thủ các chiều dài đường ngắt được quy định trong hướng dẫn này.

Hình 23 Ảnh phối cảnh của một mô hình tam giác bề mặt đường

![Image](images/image_000023_e4758dbb9f35a774eb5d8c97ad0d878c1c3ab66c63f872d138c5670fba2b8a3e.png)

## 4.4. Độ chính xác hình học của mô hình bề mặt Yêu cầu

Các đường ngắt không được lệch ra khỏi đường hình học đã tính nhiều hơn 3mm và cự ly điểm đường nét không được vượt quá 10m.

## Hướng dẫn

Các vùng lệch ra khỏi đường hình học đã được tính được mô hình trong những đường cong tròn (đường cong đứng và đường cong bình diện). Độ chính xác lý thuyết khoảng 3mm được coi là phù hợp.

Khi lập các mô hình tuyến, cả hai giá trị hình học bình diện và thẳng đứng đều phải được xem xét. Giá trị bán kính thấp hơn là giá trị được quy định.

Cự ly điểm của các đường nét tối thiểu là 0,5m, trừ khi một đối tượng cụ thể (ví dụ một đường cong trên đỉnh cần yêu cầu đường ngắt bố trí dày hơn để đảm bảo mô hình hóa có chất lượng).

Bảng 5 Cự ly điểm đường ngắt tối đa ở các bán kính cong khác nhau (R) và bán kính đường tròn

| Bán kính cong R / Bán kính đường tròn S   | Cự ly điểm đường ngắt tối đa (m)   |
|-------------------------------------------|------------------------------------|
| 1 - 39                                    | R / 40 (tối thiểu 0.5 m)           |
| 40 - 149                                  | 1 m                                |
| 150 - 999                                 | 2 m                                |
| 1,000 - 3,999                             | 5 m                                |
| >4,000                                    | 10 m                               |

## Các giá trị (S)

Bán kính đường cong nói trên cũng được áp dụng cho đường 'clothoids'. Bảng 3.13 thể hiện các giá trị tối đa đáp ứng yêu cầu độ chính xác.

Bảng 6 Chiều dài tối đa của các đường ngắt song song với tuyến bình đồ theo các giá trị đường "clothoids" khác nhau

| Giá trị đường Clothoid A (m)   | Chiều dài tối đa của các đường ngắt (m)   |
|--------------------------------|-------------------------------------------|
| 40 - 79                        | 1 m                                       |
| 80 - 499                       | 2 m                                       |
| 500 - 999                      | 5 m                                       |
| > 1,000                        | 10 m                                      |

Đối với những đường ngắt được giới hạn bề mặt đất (ví dụ mép trên cùng của một mái dốc đào hoặc mép dưới cùng của một nền đắp), cự ly điểm đường ngắt vào khoảng 1m có thể được dùng để đảm bảo rằng đường ngắt sẽ đi theo địa hình với độ chính xác cần thiết.

## 5. Yêu cầu thông tin trao đổi đối với công trình giao thông (cầu, đường)

## 5.1. Dữ liệu ban đầu

Dữ liệu ban đầu được thu thập hoặc khảo sát từ nhiều nguồn khác nhau (từ quá trình thiết kế, thi công, bảo trì, vận hành,...). Dữ liệu này có thể bao gồm:

- -Mô hình quy hoạch;
- -Mô hình địa hình;
- -Mô hình địa chất và địa kỹ thuật;
- -Mô hình từ các giai đoạn trước;
- -Mô hình công trình hiện trạng…

Tài liệu liên quan khác như: Văn bản pháp lý, hồ sơ thông tin ở các giai đoạn trước, hồ sơ công trình hiện trạng...

Mô hình dữ liệu được thu thập từ các nguồn tài liệu khác nhau nên cần có biện pháp tổng hợp, phân loại và hiệu chỉnh nhằm hỗ trợ tốt nhất nhiệm vụ thiết kế dựa trên mô hình.

Mô hình sẽ liên tục được cập nhật các số liệu mới qua các giai đoạn dự án, trong suốt vòng đời công trình.

Công tác tổng hợp, phân loại, hiệu chỉnh thường gồm các công việc sau:

- -Chuyển đổi hệ tọa độ và hệ cao độ phù hợp với dự án;
- -Chuyển đổi định dạng các tập tin số liệu;
- -Tổng hợp các tập tin số liệu thành tập tin chung;
- -Cắt bỏ để phân định khu vực dự án;
- -Mô hình hóa bề mặt khảo sát, địa chất công trình, công trình hiện hữu... khu vực dự án.

Người hiệu chỉnh cần trình bày thuyết minh chi tiết phương pháp hiệu chỉnh dữ liệu thô, phần mềm công cụ và các phiên bản được sử dụng trong quá trình tạo lập mô hình dữ liệu trong Hồ sơ mô hình dữ liệu.

Hồ sơ mô hình dữ liệu ban đầu gồm: danh mục dữ liệu đầu vào và thuyết minh mô hình dữ liệu.

## 5.2. Giai đoạn lập quy hoạch

Trong giai đoạn lập quy hoạch, mục tiêu mô hình hóa là thể hiện hiện trạng và chiếm dụng không gian của các công trình,  gồm:

- -Mô hình hiện trạng trên nền hệ thống thông tin địa lý GIS như bề mặt địa hình, hình khối các công trình hiện hữu, hệ thóng giao thông, hạ tầng, nước, sử dụng đất...;
- -Mô hình các bộ môn kỹ thuật trong quy hoạch: Thể hiện các đối tượng hình học, hình khối 3D;
- -Quy định và mô tả màu sắc để phân biệt các bộ môn kỹ thuật, hệ thống và các thành phần khác nhau;

Mức độ chi tiết LOD tương ứng khoảng 100~200.

## 5.3. Thiết kế cơ sở

Mô hình khảo sát bao gồm các thông tin: Hiện trạng và điều kiện tự nhiên khu vực, hiện trạng các công trình, khu vực, khu vực địa chất đặc biệt...Mô hình khảo sát, hồ sơ đánh giá và phân tích các thông tin thu thập đều được chuyển giao và trở thành mô hình dữ liệu ban đầu cho giai đoạn thiết kế tiếp theo.

Mô hình hóa bước thiết kế cơ sở nhằm phục vụ phân tích và đánh giá sự cần thiết đầu tư dự án, phân tích so sánh các phương án và tính khả thi của các giải pháp. Mô hình có thể cung cấp các dữ liệu thông tin về: khối lượng - chi phí ước tính, sự tác động tới môi trường và các thông tin liên quan khác ảnh hưởng đến dự án.

Mô hình thiết kế cơ sở thể hiện các giải pháp thiết kế (vị trí, quy mô, cao trình, chức năng hệ thống...). Đồng thời xác định phạm vi sử dụng của công trình và phạm vi giải phóng mặt bằng nhằm đảm bảo công trình sẽ được xây dựng phù hợp với việc sử dụng đất và hệ thống giao thông ở các khu vực xung quanh. Ngoài ra, đánh giá tác động về môi trường cũng là ứng dụng cơ bản khi sử dụng mô hình ở giai đoạn này.

Mô hình thiết kế cơ sở đáp ứng được các yêu cầu về thiết kế cơ sở trong Luật Xây dựng, các nghị định, thông tư hiện hành và yêu cầu kỹ thuật của dự án

## Mô hình các phương án

Thiết kế, phân tích so sánh các phương án khác nhau và lựa chọn phương án khả thi là phần quan trọng thiết kế cơ sở. Việc mô hình hóa các phương án thiết kế khác nhau để dễ dàng so sánh về các chỉ tiêu kinh tế - kỹ thuật của các phương án là cần thiết. Do vậy độ chính xác của mô hình phải được xem xét, điều chỉnh tùy theo từng dự án cụ thể. Mô

hình hiện trạng khu vực có ảnh hưởng đến độ chính xác của mô hình thiết kế. Cần cẩn trọng xem xét vấn đề này trong quá trình đấu thầu và các giai đoạn hợp đồng.

Mô hình thiết kế cơ sở trong giai đoạn nghiên cứu khả thi có thể được tinh giản nhưng để sử dụng được phải đảm bảo đầy đủ các yếu tố hình học chủ yếu. Bề mặt hoàn thiện của mô hình cũng có thể được xem xét thực hiện để phục vụ báo cáo trình diễn trực quan.

Hình 24 Phối cảnh và minh hoạ phương án sử dụng đất

![Image](images/image_000024_2c0d24f90d0e1b4e90bc0083fddd9c814e58a89349683fe628860a7948ddf12b.png)

Các phương án và thông tin so sánh được mô hình hóa trong mô hình thiết kế cơ sở là những vấn đề có ảnh hưởng lớn khi so sánh giá thành xây dựng và tác động về môi trường giữa các phương án.

Mô hình hóa các bộ môn thiết kế trong giai đoạn thiết kế cơ sở (đường bộ, đường sắt, phố và quảng trường, công trình, cảnh quan,...) phải hỗ trợ chủ yếu cho những mục tiêu quan trọng trong giai đoạn thiết kế như mục đích tính toán chi phí đầu tư, đánh giá sử dụng dự án, do vậy các giải pháp thiết kế phải thể hiện đủ chính xác về các yếu tố hình học, không gian bố trí công trình đủ chi tiết và phù hợp với môi trường và những yêu cầu liên quan. Việc thiết kế dựa trên mô hình sẽ hỗ trợ việc xem xét, đảm bảo công trình phù hợp chức năng, có thể dễ dàng đánh giá và so sánh các phương án .

Tuy nhiên trong giai đoạn thiết kế cơ sở, các mô hình thiết kế của các chuyên ngành khác nhau không cần thiết được hoàn thiện đầy đủ.

Khái toán chi phí công trình dựa trên mô hình cho phép so sánh nhanh và chính xác hơn giữa các phương án. Các mô hình có tính liên tục cho phép xác định chính xác nhu cầu diện tích đất chiếm dụng. Mặt khác, thiết kế trên mô hình có thể đảm bảo công trình có thể khớp với công trình hiện trạng. Chi phí cho kết cấu, thiết bị và các chi phí có liên quan có thể được khái toán theo khối lượng tính toán dựa trên mô hình cho kết quả nhanh và đáng tin cậy.

Mô hình phương án được lựa chọn trong dự án phải được hoàn thiện để chuyển giao. Các mô hình phương án so sánh không cần thiết hoàn thiện đầy đủ, chỉ cần chuyển tất cả

những thông tin liên quan để có thể đưa ra các quyết định. Độ chính xác của các mô hình phương án so sánh được đưa vào trong báo cáo mô hình thông tin.

Mô hình phối hợp phải được xem xét không có các xung đột trong các bộ môn thiết kế theo các đối tượng và kết cấu. Các đường biên khu vực có ảnh hưởng về pháp lý, phải được hoàn thiện trong giai đoạn thiết kế này.

Hình 25 Mô hình thiết kế Dự án cầu Cửa Đại - Quảng Ngãi trong giai đoạn thiết kế cơ sở

![Image](images/image_000025_78930265bbb5296d9bf58a2938e294e6dcb779ca89757ce6ee72885c47eec81b.png)

## 5.4. Thiết kế kỹ thuật và thiết kế bản vẽ thi công

Trong các giai đoạn thiết kế này, tất cả các phần được yêu cầu cho việc hoàn chỉnh dự án xây dựng đều được mô hình hóa. Tuy nhiên, yêu cầu sử dụng BIM của mỗi dự án khác nhau tùy thuộc vào quy mô dự án nên có thể thống nhất trước một số hạng mục không cần mô hình hóa (Ví dụ: các công tác tạm, công trình phụ trợ, …)

Những chi tiết kỹ thuật được thiết kế cần mô hình đạt được độ chi tiết và độ chính xác phù hợp với giai đoạn thiết kế. Độ chính xác của mô hình bàn giao luôn phải tương ứng với hồ sơ thiết kế cuối cùng.

Các mô hình thiết kế cuối cùng của dự án là những sản phẩm cuối cùng của giai đoạn thiết kế và chúng được dùng làm cơ sở cho xây dựng hồ sơ lựa chọn nhà thầu cũng như hồ sơ phục vụ quá trình thi công. Các mô hình thiết kế cuối cùng có thể được điều chỉnh, cập nhật thêm ví dụ các mô hình phục vụ thi công cho phép tổ chức xây dựng dựa trên mô hình.

Mô hình thiết kế phải chứa các thông tin hình học và thuộc tính của các cấu kiện công trình (các lớp mặt đường và kết cấu nền đường, kết cấu cầu và công trình phụ trợ, hệ thống tuyến đường ống....). Và những kết cấu khác có liên quan đã được thống nhất trong thiết kế.

Hình 26 Mô hình dự án cầu Thủ Thiêm 2 trong giai đoạn thiết kế kỹ thuật

![Image](images/image_000026_ce8306731551bf160bccdda5d7bb0ef70ea231c98e7f10dea1758eb23ddfb1f6.png)

Tại giai đoạn thiết kế kỹ thuật, khối lượng thông tin được biểu diễn không quá phức tạp như ở giai đoạn thiết kế bản vẽ thi công/tổ chức thi công. Tuy nhiên, việc tham số hóa những thông tin hình học cho đối tượng BIM phải đại diện cho nhiều giải pháp trong một mô hình duy nhất. Yêu cầu thông tin cho đối tượng BIM như sau:

- Thông tin về các thành phần cấu thành: các thành phần chính;
- Thông tin về vật liệu cấu thành: Bao gồm vật liệu cấu thành, có thể thêm các thông tin về chất liệu hoàn thiện, loại, kích cỡ, cường độ…;
- Thông tin nhà sản xuất: có thể bao gồm nhiều nhà sản xuất khác nhau.

Thiết kế bản vẽ thi công có thể do nhà thầu nhưng cũng có thể do tư vấn thiết kế lập. Trong giai đoạn thiết kế bản vẽ thi công, các thông tin cần chi tiết hơn, cụ thể:

- Thông tin về các thành phần cấu thành: các thành phần chính và thành phần phụ;
- Thông tin về vật liệu cấu thành: Bao gồm vật liệu cấu thành, có thể thêm các thông tin về chất liệu hoàn thiện, loại, kích cỡ, cường độ…;

- Thông tin nhà sản xuất: có thể bao gồm nhiều nhà sản xuất khác nhau hoặc chỉ gồm thông tin của một nhà sản xuất cụ thể;
- Các thông tin, chỉ dẫn khác cho việc thi công.

## 5.5. Mô hình hóa giai đoạn thi công xây dựng (nhà thầu thi công)

Thiết kế tổ chức thi công sẽ do nhà thầu thi công trực tiếp lập. Thiết kế dựa trên mô hình cho phép mô hình hóa các giai đoạn công việc khác nhau trong thi công, tiến độ các công tác cũng có thể được đưa vào mô hình. Phải luôn xem xét đến mục đích của mô hình khi tiến hành mô hình hóa kế hoạch công việc trong thi công, ví dụ: mô hình hóa kế hoạch công việc thi công có tính đến yêu cầu về không gian của các đợt thi công khác nhau, mô hình hóa để quản lý, kiểm soát khối lượng, chi phí…

Sự khác biệt về yêu cầu chi tiết của các thành phần mô hình giữa hai giai đoạn thiết kế bản vẽ thi công và thiết kế tổ chức thi công được thực hiện nhằm xác định phạm vi xây dựng trên công trường sẽ được quản lý bởi một hoặc một vài nhà thầu thi công xây lắp. Theo đó, đối tượng BIM cung cấp thông tin cần thiết của một loại vật liệu, thiết bị đã được chỉ định do một nhà sản xuất cung cấp.

## PHỤ LỤC 01: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN HÌNH HỌC CỦA MỘT SỐ LOẠI CẤU KIỆN TRONG CÔNG TRÌNH XÂY DỰNG DÂN DỰNG DÂN DỤNG

Ghi chú: Bảng trên chỉ hướng dẫn thêm Mức độ phát triển thông tin của một số loại cấu kiện theo từng giai đoạn thực hiện dự án có tính chất thông dụng. Đối với các loại cấu kiện khác Chủ đầu tư lựa chọn LOD cho phù hợp với mục tiêu.

| Tên mô hình             | Các phần tử của mô hình   | Giai đoạn dự án          | LOD     |
|-------------------------|---------------------------|--------------------------|---------|
| Mô hình hạ tầng khu vực | f1, f2                    | Thiết kế cơ sở           | 100     |
| Mô hình hạ tầng khu vực | f1-f3                     | Thiết kế kỹ thuật        | 200     |
| Mô hình hạ tầng khu vực | f1-f3                     | Thiết kế bản vẽ thi công | 300/350 |
| Mô hình kết cấu         | b1                        | Thiết kế cơ sở           | 100     |
| Mô hình kết cấu         | b1-b3, b5                 | Thiết kế kỹ thuật        | 200     |
| Mô hình kết cấu         | b1-b3, b5                 | Thiết kế bản vẽ thi công | 300     |
| Mô hình kiến trúc       | a1, a2, a4, a5            | Thiết kế cơ sở           | 100     |
| Mô hình kiến trúc       | a1-a7                     | Thiết kế kỹ thuật        | 200     |
| Mô hình kiến trúc       | a1-a7                     | Thiết kế bản vẽ thi công | 350/400 |
| Mô hình cơ điện         | c1-c5, d1-d3, e1-e5       | Thiết kế kỹ thuật        | 200     |
| Mô hình cơ điện         | c1-c5, d1-d3, e1-e5       | Thiết kế bản vẽ thi công | 300/400 |

## 1. Mô hình kiến trúc

## a. Các hệ thống kiến trúc

Mô hình hóa các cấu kiện kiến trúc đến một mức độ thể hiện ý định thiết kế và thể hiện chính xác giải pháp thiết kế.

## a1. Bề mặt khu đất:

Mặt đường, vỉa hè, lề đường, các tiện nghi và các yếu tố xây dựng trong vùng lân cận của tòa nhà.

- a2. Tường nội thất và tường ngoại thất bao gồm:
- -Cửa đi, cửa sổ, lỗ mở;
- -Bề mặt gỗ veneer, vật liệu cách nhiệt và các cấu kiện theo phương đứng khác dày hơn 1cm (có thể là 1 phần của cấu kiện vật liệu tổng hợp hoặc cấu kiện lắp ráp);
- -Soffit nội thất và ngoại thất, mái hắt, các cấu kiện kiểm soát ánh nắng mặt trời;
- -Rào chắn, các cấu kiện che chắn;
- -Cấu kiện kiến trúc đúc sẵn.
- a3. Hệ thống sàn, trần, mái nhà bao gồm:

- -Các hạng mục kết cấu phù hợp được liệt kê dưới đây nếu không được kỹ sư kết cấu cung cấp và tích hợp vào mô hình kiến trúc để phối hợp và tạo hồ sơ bản vẽ;
- -Hệ thống cách nhiệt, hệ thống trần, gạch lát sàn và các cấu kiện theo phương ngang dày hơn 1cm (có thể là 1 phần của cấu kiện vật liệu tổng hợp hoặc lắp ráp);
- -Những phần dốc của mái nhà, sàn và trần nếu cần sẽ được mô hình.
- a4. Thang máy, cầu thang, ram dốc bao gồm hệ thống lan can
- a5. Tủ, kệ, lò sưởi và các cấu kiện kiến trúc nội thất khác
- a6. Dụng cụ nội thất, trang thiết bị và tài sản nếu không được các đơn vị khác cung
- cấp và tích hợp vào mô hình kiến trúc để phối hợp và tạo hồ sơ bản vẽ.
- -Nội thất (gắn vĩnh viễn);
- -Thiết bị chuyên dụng (Dịch vụ ăn uống, y tế, v.v.);
- -Mô hình cơ điện liên quan đến không gian kiến trúc (Nhà vệ sinh / bồn rửa / v.v.), yêu cầu lựa chọn màu sắc hoặc ảnh hưởng đến hình ảnh 3D (Thiết bị chiếu sáng) trừ khi được cung cấp bởi các kỹ sư.
- a7. Các khu vực cho người tàn tật, cửa tự động, các yêu cầu về không gian cho dịch vụ và các khu vực cho hoạt động khác phải được mô hình hóa như một phần của tất cả các thiết bị và kiểm tra va chạm với các cấu kiện khác.
- a8. Các mục này có thể được mô hình hóa ở tùy vào yêu cầu của Chủ đầu tư:
- -
- Trang trí tường ngoại thất và nội thất;
- -Tấm kim loại hoặc các cấu kiện mỏng khác;
- -Phần hoàn thiện khác.

## 2. Mô hình kết cấu

## b. Hệ thống kết cấu

- b1. Móng:
- -Móng bè;
- -Móng cọc khoan nhồi;
- -Móng cọc ép;
- -
- Móng đơn;
- -
- Móng băng.

## b2. Cấu kiện dạng thanh:

- -Cột thép (với hình dạng và kích thước chính xác);
- -Sàn thép Joists;
- -Hệ dầm dàn thép (mô hình các thanh giằng cho mục đích trực quan, nhưng không cần phải chính xác);
- -
- Dầm thép (với hình dạng và kích thước chính xác);
- -Cấu kiện bê tông đúc sẵn (tấm lõi rỗng có thể được mô hình hóa như dạng tấm);

## 3.

- -Cấu kiện bê tông đổ tại chỗ (không yêu cầu mô hình những phần vát và cắm vào cấu kiện);
- -
- Sàn bao gồm toàn bộ khu vực và lỗ mở (đổ tại chỗ, đúc sẵn, gỗ);
- -Mô hình độ dày tổng thể của hệ thống sàn gỗ (hệ thống dầm không cần phải được
- mô hình hóa);
- -Cột gỗ, cây chống gỗ;
- -
- Xà gồ gỗ;
- -Hệ giàn gỗ (bao gồm các thanh giằng cho mục đích trực quan, nhưng không cần phải chính xác);
- -Dầm gỗ hoặc dầm mỏng.
- b3. Các loại tường chịu lực bao gồm lỗ mở:
- -Tường chịu lực (thép gia cường, bê tông, thép, gỗ). Mô hình chiều dày tổng thể của tường thép và tường gỗ (Không yêu cầu mô hình các cấu kiện đơn lẻ);
- -
- Tường móng kết cấu.

b4. Các mục này có thể được mô hình hóa tùy vào yêu cầu của Chủ đầu tư:

- -
- -
- -
- -
- Cốt thép trong bê tông ;
- Các phần tử trong bê tông;
- Liên kết thép (tấm, bu lông, hàn góc,...);
- Những chi tiết thép khác.
- b5. Những chi tiết gỗ khác:
- -Đinh tán;
- -Mộng gỗ (trừ khi được coi là thành phần chính).

## Mô hình CƠ ĐIỆN

## c. Hệ thống HVAC:

## c1. Trang thiết bị:

Quạt thông gió, Hệ thống biến đổi lưu lượng gió, Các loại máy nén khí... c2. Hệ thống phân phối:

- -Cung cấp, tuần hoàn, xả, cứu trợ và hệ thống ống dẫn khí bên ngoài được mô hình hóa cho kích thước mặt bên ngoài hoặc phần cách nhiệt ống dẫn (tùy thuộc theo cái nào lớn hơn);
- -
- Khớp nối;
- -Máy khuếch tán, lưới tản nhiệt, miệng gió chắn mưa/ miệng lấy/ thải gió ngoài trời, chụp hút, bộ tản nhiệt sưởi .
- c3. Các ống có kích thước đường kính lớn hơn 5cm, bao gồm các lớp cách nhiệt trong mô hình

- c4. Các yêu cầu lối vào khu vực, không gian mở cửa, yêu cầu không gian hệ thống và không gian hoạt động khác phải được mô hình hóa như một phần của thiết bị HVAC và kiểm tra va chạm với các yếu tố khác.

## c5. Phần loại trừ:

Phụ kiện đường ống và các mối nối ống.

## d. Hệ thống điện:

- d1. Nguồn điện:
- -Máy biến áp nội thất và ngoại thất và các thiết bị khác;
- -Hộp kỹ thuật điện bao gồm cả không gian sử dụng;
- -Ống dẫn diện có kích thước trên 5cm sẽ được mô hình;
- -
- Đầu ra, công tắc, hộp nối.
- d2. Hệ thống chiếu sáng:

Thiết bị chiếu sáng được gắn vĩnh viễn (Không thể di chuyển, thiết bị cắm thêm không cần được mô hình hóa như một phần của hệ thống điện).

- d3. Các yêu cầu lối vào khu vực, không gian mở, các yêu cầu về không gian cho hệ thống và các khu vực cho hoạt động khác phải được mô hình hóa như một phần của các thiết bị điện để kiểm tra va chạm.

## e. Hệ thống cấp thoát nước và Phòng cháy chữa cháy:

- e1. Thoát nước thải và chụp thông hơi vent:
- -Đường ống có kích thước đường kính lớn hơn 5cm, bao gồm bất kì lớp bao bọc nào trong mô hình;
- -Thoát nước trên mái và sàn, đường dẫn, hố ga, thiết bị chặn dầu mỡ, bể chứa, xử lý nước và các hạng mục chính khác.

## e2. Đường ống cấp nước:

Đường ống có kích thước đường kính lớn hơn 5cm, bao gồm bất kì lớp bao bọc nào trong mô hình.

- e3. Đồ đạc: bồn rửa, đồ vệ sinh, bể nước, bồn rửa sàn
- e4. Phòng cháy chữa cháy:
- -Đường ống của hệ thống Sprinkler có kích thước trên 5cm;
- -Đầu phun Sprinkler;
- -Ống nước đứng Stand\_Pipe, trụ cứu hoả, đường ống nước chữa cháy  bao gồm không gian sử dụng.
- e5. Các yêu cầu lối vào khu vực, yêu cầu không gian của hệ thống, khoảng cách của van và không gian hoạt động khác phải được mô hình hóa như một phần của hệ thống cấp thoát nước

## 4. Mô hình hạ tầng khu vực

## f. Công trình hạ tầng khu vực:

Mô hình các cấu kiện của công trình hạ tầng khu vực sau đây ở mức tối thiểu f1. Địa hình:

Địa hình 3D của tất cả công trường xây dựng như được thiết kế, bao gồm tường chắn. Mô hình này phải bao gồm địa điểm và các khu vực xung quanh góp phần vào hệ thống thoát nước của khu vực hoặc tác động đến công trường xây dựng. Trong hầu hết các trường hợp, điều này sẽ yêu cầu các tuyến đường liền kề phải được mô hình hóa.

## f2. Yếu tố cảnh quan:

Các khu vực cơ sở hạ tầng, đất trống và khu vực trồng cây, khu vực đậu xe, ao hồ, đồi núi và các thành phần khác không được bao gồm trong mô hình.

## f3. Công trình hạ tầng kỹ thuật vá các bộ phận chi tiết:

Mô hình hóa tất cả các kết cấu của trạm bơm, hệ thống nhiên liệu, hố ga và các hạng mục chính khác ảnh hưởng đến thông tin đầu vào của dự án hoặc có thể trở thành hạn chế thiết kế của dự án. Tất cả các mục phải được tham chiếu địa lý sao cho tất cả các hạng mục có thể được xem dưới dạng lớp phủ trong mô hình thông tin tòa nhà.

- -Hệ thống Điện;
- -Hệ thống chiếu sáng (Cột điện...);
- -Hệ thống viễn thông;
- -Hệ thống truyền dữ liệu;
- -Hệ thống cấp nước (Nước sinh hoạt, nước phòng cháy chữa cháy, vòi lấy nước...);
- -Hệ thống thoát nước mưa;
- -Hệ thống thoát nước thải/ vệ sinh;
- -Hệ thống khí Gas;
- -Hệ thống điều hoà không khí (Chiller giải nhiệt nước và làm nóng nước).

PHỤ LỤC 02: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN PHI HÌNH HỌC CỦA MỘT SỐ CẤU KIỆN TRONG CÔNG TRÌNH XÂY DỰNG DÂN DỤNG

## BẢNG MỨC ĐỘ PHÁT TRIỂN THÔNG TIN PHI HÌNH HỌC BỘ MÔN KIẾN TRÚC - KẾT CẤU

![Image](images/image_000027_f3b98711deb6310e926173ed040c4651a59c994e96f63af200bcb53eafae1ea2.png)

![Image](images/image_000028_f56dc5bf124eaaad0eff9d433ef68532d8074b9a82f912a8599547e6345e4182.png)

![Image](images/image_000029_f226cd965934f928cdc19710548c3a4e19f12ad55608a3259cf641b05526973e.png)

![Image](images/image_000030_f61a1eef1d06193d09ac9d687e63ea3c620e4b66e9ad33b1500a36ffd88fb928.png)

![Image](images/image_000031_d4fdcaada917e912fb8c238578edc17c6e87fad9ca37cd64b7e92dae41bfdb62.png)

![Image](images/image_000032_add47527f0695c6d37f21ae4415916410d7518ad9cee6e3cf929470ae42d5f58.png)

![Image](images/image_000033_14ff1a3ad03b41fba4b88f9bf6a3c17eef0553070b76968c0b261e6f4390810f.png)

![Image](images/image_000034_a6e9fc65fa825a40c67259c521f3386e5a9162563ba6b2597e311387ef98da92.png)

![Image](images/image_000035_248ec8658f9225ea80f7128872119fb3735541aa67e837434e4c12c5d1ea421d.png)

![Image](images/image_000036_b2ce202dae628b452c18a15d913cf38aff0cb1768bc7845ecd8597339095a82e.png)

![Image](images/image_000037_fd6205651475711f6352bd6388ecc2e79104dc823a6efc186a3df1a01d806d48.png)

![Image](images/image_000038_e5e9ea230fcbbc99c3a28325d39fd0c9ab8b99fe306cf11bc930ca1e22b8baef.png)

![Image](images/image_000039_02e0662be6501f2325b97bf8231fe5c7b1152078b078fc92636095a156142bdb.png)

![Image](images/image_000040_1a89023bae95dbd2b1e6384100e10896a69c8a82528f7394771940d6e7063886.png)

![Image](images/image_000041_c7af644943372a2196ccf1e1dfeef513a0c93951d443789ffab3418ac0881944.png)

![Image](images/image_000042_c3048fcb4418d7f1dcf89fc5947a04ed73d4e74c50d94feca0de7833c3fcdc6e.png)

![Image](images/image_000043_629c1898addd4a73dc74ed315ae6bae25e4f0dbbf1adb28c47e623587908499d.png)

![Image](images/image_000044_d6d7570d0818c47089849a9b9f0ec5829c58418d3785fdb996f4e35e6ef5db96.png)

![Image](images/image_000045_9ec0e749b3f9be8f17470d1ae36c2410ad6324c0e644b48fef71dbaf04841ce8.png)

![Image](images/image_000046_7668f311a0d876ab373464fa42a1a100b4cf07acb1432fe929f7dcd4f12e047e.png)

![Image](images/image_000047_d00e0f01d55f65868343eba8476a8bac38ba88abc2ea462c67812cadd9a4c535.png)

![Image](images/image_000048_d4a1dfdbf41aa4dd618836ca0725264e9da253476e2bdedda887f7bee89c04a0.png)

![Image](images/image_000049_2b453c15bbedb9fb7a137fd3e8f34868efd3ca47d2aa67636bdb160158594bb4.png)

![Image](images/image_000050_97b3beb3f4a07083cd6cb0a60ed3d1dc4f8edf7b2c9d3cb02aa0165ea20646ae.png)

![Image](images/image_000051_f5a35c904365f4f580a3a66fcdea6af2e2bd79eec5c676eb138d42899512c8a9.png)

![Image](images/image_000052_f6cf20cc5f2f1660a73c94bedcb50cc5cd42a2749b043a99f9820eeb41c70af4.png)

![Image](images/image_000053_1b0c58184b6ca9cce3e86ba00d9ffe527c3a0e0def49fd8287381b934967a4e5.png)

![Image](images/image_000054_f8be968c2c3de54591fedc7ce8bb99942c0182d0f8a97e719df485c91e9197a8.png)

![Image](images/image_000055_f92131dbb6d560df1ac9e11b9c03522b6d361ee0f155c7978c67bd89a5789494.png)

![Image](images/image_000056_8b5a9bebad21907f93f2ddb851e9f05b36cf70b77f1d9aa01157b1afd7346ccb.png)

![Image](images/image_000057_84a1bd8db299dd223baea4cc0a5c6e757d76d295a79a5c00a1fe9d8610ec2b2e.png)

![Image](images/image_000058_3ac12130c7bc627dff8fdc16b773a9782cc521ecafa0c8341c4d59692dcdc211.png)

![Image](images/image_000059_f505b3f5e37ca232db39ccf6cc171601bade84b5b6d25d4498ee7f1400c3993b.png)

## BẢNG MỨC ĐỘ PHÁT TRIỂN THÔNG TIN PHI HÌNH HỌC BỘ MÔN MEP

![Image](images/image_000060_8d14e441d05d541ce9e5f94e532ae42dba89fefbc40752b67be2a99bbc0d576e.png)

![Image](images/image_000061_b326d0567f84cb27b978c497dbb90a103ab47b13e7e4b75989efc420c1250321.png)

![Image](images/image_000062_533ea6dde0342e8320ad8db9f7ff06edfd08f5ad4b32e3c3c37a2e13c19df77f.png)

![Image](images/image_000063_d673faa4609a67240a11733e9b185a002b9ca60b9210067eaad1a53f7feefc65.png)

![Image](images/image_000064_b39f1c3d4c9fddfdb58ffd164c089899541c2da556c571495089d7f17f8112d1.png)

![Image](images/image_000065_0d43ce569cc0e5ff83b2cafd3a79ab53a0a337302d0be992ece974a4cf44da02.png)

![Image](images/image_000066_16f7ac0008992edcadc3a1c78eff456b4685b09898efb77cd1cd36fef1726a68.png)

![Image](images/image_000067_6d9d961f3e3b33593c01cd7d8ef9b4befcd2ff44b36fc9391e80f36396b3c650.png)

![Image](images/image_000068_1a5d7cf58e079929f662c8ca4ad5c43cd9b9de68ddcfe7f0b1852c6cec96485d.png)

![Image](images/image_000069_f58bf5ea5a31e8f6efa6a8c9c7a9843b18021fd6a1d2aacce773007c3dcf9320.png)

![Image](images/image_000070_5267228f7152fb012dc83e5a9b1d0a7fc7cad65d8e4c82d77b65f73cfc15233a.png)

![Image](images/image_000071_14fddc7b574f47c143a8f07e8205b6714544e9a376de17b6bfbb2cd8b0205847.png)

![Image](images/image_000072_cc006872d93682521f425ac5a85accdc426f693d10c728102b7ca14b0f938f67.png)

![Image](images/image_000073_2316c7d4e789a49e8e6ec9abaa23bc6179de4bdfe2dd646d8ead5281cffb8399.png)

![Image](images/image_000074_a6c072ce031d8f5ad5cd1865fb3505c88d03e035bafed18e65bd201b8be49c2e.png)

![Image](images/image_000075_390f2c43c4576642f0264936c658de2d4b8330111e3e9d2763590648ce759dc5.png)

![Image](images/image_000076_1e13bffbe33062af57480e837910c7dc1f121305c1fd4d319c4ac782d77ea73c.png)

![Image](images/image_000077_b6dca4f2bf9f4bf0f9c1f480a94168d359e2a684fda6d8d8ca7bb13f7c3d6a20.png)

![Image](images/image_000078_c4011d754353feeebe3a960233e1d609a26594f3b9d3b51c094ad58a61880d5e.png)

![Image](images/image_000079_4703884d877f65e9d42f8a2944abf6a93feaa28d4bfbaceafc9b16e6c641aaa0.png)

![Image](images/image_000080_f7f05d340ce5889e54dbd78828fc210233095bb5ac745936c085279f98f78e7c.png)

![Image](images/image_000081_66aa9552b338b86ab98b6813b2d1bbfa888d29b5c55c5073d198141cd6cc06c9.png)

![Image](images/image_000082_dfaa335c15b3fa40d5b6be3930b6921847b0d5e854e81cc4f57d00ea57cf18ac.png)

![Image](images/image_000083_a4f0a5d7564de044df3cda2a42aaf8fc6f8997728773582d1884c02bd62d3091.png)

![Image](images/image_000084_7656d5780fb38c158dad8c8351e54b2645578df2e5e7835885684671569a6e25.png)

![Image](images/image_000085_d0dfc6958c23c048ce8fec76d447042d353a19e3713c7416e8dfad7c5032d03e.png)

![Image](images/image_000086_7bb48650aad1d91185f7ea6bb047b61530862672404e284e5d3224fd9d04636f.png)

![Image](images/image_000087_020ebb7714b40ba852d1b82ecacf20599ec65619d29744df52f6b704a3339caa.png)

![Image](images/image_000088_1e5dcaffd29eb5d18a0129f8ce85a9854e02bf359d8d3a3d6a816644b79a488e.png)

![Image](images/image_000089_fdcf1d73c4325ecba097421d7bdb7458dd6243197db67c7f25d0f4ca6b7b702e.png)

![Image](images/image_000090_a1bd07728dd4c1e5d4d6a8843e3307826e85b9752c1810a9588576da3cbfebc6.png)

|   Table |   Code 1 |   Code 2 |   Code 3 Code 4 | Description                                             | Ghi chú: 2 - Thông tin được xuất hiện từ bước Thiết kế cơ sở 3 - Thông tin được nhập từ bước Thiết kế kỹ thuật 4 - Thông tin được nhập từ bước thiết kế bản vẽ thi công 5 - Thông tin được nhập tại bước thi công   |   Tên cấu kiện Tên cấu kiện Tên của loại Ký hiệu của loại Ký hiệu của cấu kiện Mã số phân loại (Omni) Tên phân loại (Omni) Mô tả cấu kiện Số Seri Số Mô đen Đơn vị sản xuất Tên tầng Offset Phân loại hệ thống Loại hệ thống Tên hệ thống Hạng mục Chiều dài Chiều rộng Chiều cao |
|---------|----------|----------|-----------------|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         |          |          |                 |                                                         | Định danh thiết bị do nhà sản xuất đưa ra                                                                                                                                                                           |                                                                                                                                                                                                                                                                                 5 |
|      21 |       04 |       70 |              90 | Electronic Safety and Security Supplementary Components | Hệ thống an toàn và an ninh phụ trợ khác                                                                                                                                                                            |                                                                                                                                                                                                                                                                                   |
|      21 |       04 |       80 |                 | INTEGRATED AUTOMATION                                   | HỆ THỐNG TÍCH HỢP TỰ ĐỘNG                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                   |

## PHỤ LỤC 03: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN CỦA MỘT SỐ LOẠI CẤU KIỆN TRONG CÔNG TRÌNH HẠ TẦNG KỸ THUẬT ĐÔ THỊ (GIAO THÔNG, CẤP THOÁT NƯỚC)

## 1. Ví dụ Bảng mức độ phát triển mô hình theo giai đoạn trình tự đầu tư

| Loại đối tượng                |   Giai đoạn thiết kế cơ sở |   Giai đoạn thiết kế kỹ thuật |   Giai đoạn thiết kế BVTC |
|-------------------------------|----------------------------|-------------------------------|---------------------------|
| Địa hình                      |                        200 |                           300 |                       300 |
| San lấp mặt bằng              |                        200 |                           300 |                       350 |
| Đào móng                      |                        200 |                           300 |                       300 |
| Cọc                           |                        200 |                           300 |                       350 |
| Đường bộ, đường sắt           |                        300 |                           350 |                       400 |
| Trang thiết bị phụ trợ        |                        200 |                           300 |                       350 |
| Hệ thống đường ống hiện trạng |                        200 |                           300 |                       300 |
| Hệ thống cấp thoát nước       |                        200 |                           300 |                       350 |

## 2. Địa hình

|   LOD | Mô tả                                                                                                                                                             | LOI                                         | Hình ảnh*   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|-------------|
|   100 | Dạng địa hình được thể hiện dưới dạng mặt phằng 2D với các điểm tham chiếu (cao độ), thể hiện hình dạng và diện tích của bề mặt                                   | Loại Tên mặt phằng Cao độ Tên lớp           |             |
|   200 | Dạng địa hình được thể hiện dưới dạng mặt phẳng 3D, được hình thành dựa trên các điểm được bố trí thủ công. Các điểm được đo dựa trên cao độ của điểm đó.         | Loại Tên mặt phằng Cao độ Tên lớp Phân loại |             |
|   300 | Dạng địa được thể hiện dưới dạng mặt phằng 3D được hình thành dựa trên một mạng lưới là tập hợp của các điểm. Mạng lưới các điểm này được scan hoặc là dùng laser | Loại Tên mặt phằng Cao độ Tên lớp Phân loại |             |

![Image](images/image_000091_83c2c99d99f723d7f95a4816616dc0cecd7831232129407a87bf9e42710c0630.png)

![Image](images/image_000092_36ffd0e4f0108355d1577495bb4ccb6e086d12d93800c57755bd4b331fdd9152.png)

![Image](images/image_000093_18055ee75fa85f39b0e922ca6c696456f2894b0af2e813c98f785b55161f7f72.png)

![Image](images/image_000094_bf5fc4811620b15a9c1c7f2e26bc8bb9029e1ad32e70495f4485dbca9f375e9a.png)

![Image](images/image_000095_c0c574a238c87246e793a883450c91684451c0a49cf76d20d2d358101070b578.png)

![Image](images/image_000096_d2186889ba9456c1c8aa85a46bf0bf8403df32b3dd3e4403426b91f8112de2b3.png)

![Image](images/image_000097_d7d275f06c16f4bf8dfc21d4c9ac877035f0efd57d2ea9760907f85d404ec17b.png)

![Image](images/image_000098_729a873f51cda7feb22525573f7d48d10e63c46522c009591f7bf7b203d75ed4.png)

| 350   | Dạng địa hình được thể hiện dưới dạng mặt phằng 3D được hình thành dựa trên một mạng lưới là tập hợp của các điểm. Mạng lưới các điểm này được tạo lập bằng cách sử dụng các công nghệ như laser scan. Các lớp bề mặt bên dưới như đất sét, cát… được hiển thị dưới dạng mặt phẳng 3D được lấy dữ liệu từ các mẫu khoan tham dò trước đó   | Loại Tên mặt phằng Cao độ Tên lớp Phân loại   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|

## 3. San lấp mặt bằng

|   LOD | Mô tả                                                                          | LOI                                                      | Hình ảnh*   |
|-------|--------------------------------------------------------------------------------|----------------------------------------------------------|-------------|
|   100 | Hiển thị bề mặt san lấp mặt bằng dưới dạng bề mặt 2D                           | Loại Tên bề mặt Độ cao Tên lớp                           |             |
|   200 | Hiển thị bề mặt san lấp theo phương thẳng góc liên kết với các bề mặt khác.    | Loại Tên bề mặt Độ cao Tên lớp Phân loại                 |             |
|   300 | Hiển thị bề mặt san lấp với độ dốc với các bề mặt khác.                        | Loại Tên bề mặt Độ cao Tên lớp Phân loại Hiển thị độ dốc |             |
|   350 | Hiển thi san lấp mặt bằng với mức độ chính xác với độ dốc với các bề mặt khác. | Loại Tên bề mặt Độ cao Tên lớp Phân loại Hiển thị độ dốc |             |

## 4. Hố móng

| LOD   | Mô tả   | LOI   | Hình ảnh*   |
|-------|---------|-------|-------------|

![Image](images/image_000099_6a3f7502e01d8d49f29daab1f81e9b73987b9585e8ba5cbdd646af6a42c6af48.png)

![Image](images/image_000100_8e62f065df50fd6547ba12cb9fa8bbb1f3d5309ef9cc55011cd2641c4f2fd870.png)

![Image](images/image_000101_95f6a2fd9cf985815cec0a32f184a4f6eafcee9607f4428577a465681d7dd868.png)

![Image](images/image_000102_563428adbe61c22d3be6ab0fab6f2dbbdb096b62b67ad819ed44d1f0300e8286.png)

|   100 | Hiển thị thô phần đào đất đưới dạng bề mặt cho một mặt phẳng cố định.                                                         | Loại Tên bề mặt Độ cao Tên lớp                           |
|-------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
|   200 | Hiển thị thô phần đào đất dưới dạng bề mặt cho một mặt phằng cố định với mức độ hiển thị liên kết với các dạng địa hình khác. | Loại Tên bề mặt Độ cao Tên lớp Hiển thị độ dốc Phân loại |
|   300 | Hiển thị mặt bằng đào đất cho móng dưới dạng bề mặt 3D với các mặt phẳng thằng đứng                                           | Loại Tên bề mặt Độ cao Tên lớp Hiển thị độ dốc Phân loại |
|   350 | Hiển thị mặt bằng đào đất cho móng dưới dạng bề mặt 3D với các độ dốc chi tiết.                                               | Loại Tên bề mặt Độ cao Tên lớp Hiển thị độ dốc Phân loại |

## 5. Đào đất dạng tuyến

|   LOD | Mô tả                                        | LOI                                  | Hình ảnh*   |
|-------|----------------------------------------------|--------------------------------------|-------------|
|   100 | Hiện thị phần đào đất dưới dạng đường thằng. | Loại Độ cao Độ dốc Tên lớp           |             |
|   200 | Hiển thị phần đào đất dưới dạng 3D           | Loại Độ cao Độ dốc Tên lớp Phân loại |             |
|   300 | Hiển thị phần đào đất cho ống dưới dạng 3D.  | Loại Độ cao Độ dốc Tên lớp           |             |

|     |                                                                                              | Phân loại Tên bề mặt Độ dốc                                                 |
|-----|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 350 | Hiển thị phần đào đất cho ống dưới dạng 3D với bề mặt đào được liên kết với các bề mặt khác. | Loại Độ cao Độ dốc Tên lớp Phân loại Tên bề mặt Hiển thị độ dốc Tên bình đồ |

## 6. Đường bộ và đường sắt

|   LOD | Mô tả                                                             | LOI                                                        | Hình ảnh*   |
|-------|-------------------------------------------------------------------|------------------------------------------------------------|-------------|
|   100 | Hiển thị đường trung tâm của đường hoặc là đường sắt dưới dạng 2D | Loại Kích thước Tên lớp                                    |             |
|   200 | Hiển thị bề mặt 2D cho bề mặt đường hoặc là đường sắt.            | Loại Kích thước Tên lớp Độ cao Phân loại                   |             |
|   300 | Hiển thị bề mặt 3D liên kiết với các mặt phằng khác               | Loại Kích thước Tên lớp Độ cao Phân loại Tên bề mặt Độ dốc |             |
|   350 | Hiển thị bề mặt với độ dốc địa hình.                              | Loại Kích thước Tên lớp Độ cao Phân loại Tên bề mặt Độ dốc |             |

![Image](images/image_000103_71605d38dcf6343b5a14433dc9e0b529eef5f77feb48b14395af1bb12a8efd60.png)

![Image](images/image_000104_4f5b6e489962dab2336ddca4a17881b7f02095129c5a663e6b20886307c6c467.png)

![Image](images/image_000105_594f6fdd5a0990d8ba180d06723d26c582e85edeaeadd675e6cdd4b490c62e72.png)

![Image](images/image_000106_88f2689dc2ce77ccd653885b3c4808b502f1de6b24334bf988c2ec4fb492da09.png)

| 400   | Hiển thị lớp đất, kết cấu đường, cống rãnh với độ dốc địa hình.   | Loại Kích thước Tên lớp Độ cao Phân loại Tên bề mặt Độ dốc Tên bình đồ   |
|-------|-------------------------------------------------------------------|--------------------------------------------------------------------------|

## 7. Trang thiết bị của đường bộ và đường sắt

|   LOD | Mô tả                                                                                  | LOI                    | Hình ảnh*   |
|-------|----------------------------------------------------------------------------------------|------------------------|-------------|
|   100 | Đặc điểm kỹ thuật của vị trí thiết bị đường bộ và đường sắt.                           | Loại Tên lớp           |             |
|   200 | Đặc điểm kỹ thuật, kích thước, vị trí của đường và các thiết bị đường sắt.             | Loại Tên lớp Phân loại |             |
|   300 | Hiển thị đường và các thiết bị đường sắt dưới định dạng 3D.                            | Loại Tên lớp Phân loại |             |
|   350 | Hiển thị 3D của đường và các thiết bị đường sắt kể cả các khối được ẩn đi như là móng… | Loại Tên lớp Phân loại |             |
|   400 | Các chi tiết cụ thể được mô hình hóa trong mô hình ví dụ như các liên kết.             | Loại Tên lớp Phân loại |             |

## 8. Hệ thống đường ống hiện trạng

|   LOD | Mô tả                                                                                                                                                    | LOI                                             | Hình ảnh*   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|-------------|
|   100 | Vị trí tương đối của đường ống dưới dạng đường thằng 2D.                                                                                                 | Loại Kích thước Độ cao Độ dốc Tên lớp           |             |
|   200 | Vị trí tương đối của đường ống đưới dạng đường thằng 3D                                                                                                  | Loại Kích thước Độ cao Độ dốc Tên lớp Phân loại |             |
|   300 | Vị trí tương đối, độ đốc, kích thước và hướng phân phối chính của đường ống.                                                                             | Loại Kích thước Độ cao Độ dốc Tên lớp Phân loại |             |
|   350 | Khoảng cách, vị trí, thiết kế, vật liệu, công suất và hệ thống được thể hiện trên mô hình.                                                               | Loại Kích thước Độ cao Độ dốc Tên lớp Phân loại |             |
|   400 | Hình dạng chuẩn xác bao gồm chiều dày của vật liệu, chiều dài của đường ống. Vị trí của van, vật liệu, công suất và hệ thống được thế hiện trên mô hình. | Loại Kích thước Độ cao Độ dốc Tên lớp Phân loại |             |

## 9. Hệ thống thoát nước

|   LOD | Mô tả                                                                                                                                               | LOI                                                                              | Hình ảnh*   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-------------|
|   100 | Vị trí tương đối của đường ống đưới dạng các đường line                                                                                             | Loại Kích thước Tên lớp                                                          |             |
|   200 | Vị trí tương đối, kích thước và các đường phân tuyến và đường ống.                                                                                  | Loại Kích thước Tên lớp Phân loại Cao độ Độ dốc                                  |             |
|   300 | Vị trí tương đối và kích thước các đường phân tuyến của đường ống và các liên kết ống.                                                              | Loại Kích thước Tên lớp Phân loại Cao độ Độ dốc                                  |             |
|   350 | Khoảng các thực, vị trí và thiết kế.                                                                                                                | Loại Kích thước Tên lớp Phân loại Cao độ Độ dốc                                  |             |
|   400 | Hình dạng thực bao gồm chiều dày của các lớp vật liệu chiều dài của đường ống. Vật liêu,công suất và hệ thống được hiển thị thể hiện trong mô hình. | Loại Kích thước Tên lớp Phân loại Cao độ Độ dốc Vật liệu Tên hệ thống Công suất. |             |

## 10. Móng, cấu kiện bê tông đúc sẵn

|   LOD | Mô tả                                                                                                                                                                 | LOI                                                                                                                                                                      | Hình ảnh*   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
|   100 | Vị trí móng được thế hiện bởi các bề mặt mặt phẳng hình học.                                                                                                          | Loại Kích thước (tương đối)                                                                                                                                              |             |
|   200 | Móng được thể hiện dưới dạng hình khối, hình dạng tương đối, số lượng, kích thước, hình dạng vị trí và hướng đều được quy định trong mô hình.                         | Loại Kích thước Cao độ Phân loại Vật liệu                                                                                                                                |             |
|   300 | Móng được thể hiện với số lượng, các đường kích thước, hình dạng và vị trí và hướng quy định. Thêm vào đó có độ dốc, lỗ rỗng, cốt thép và các cấu kiện, các chi tiết. | Loại Kích thước Cao độ Phân loại Vật liệu Cốt thép                                                                                                                       |             |
|   350 | Móng gồm có các lỗ rỗng.Thể hiện các chi tiết thép trong khối móng.                                                                                                   | Loại Kích thước Cao độ Phân loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường Các lớp bị che khuất Bê tông, thô                                                    |             |
|   400 | Móng gồm có các lỗ rỗng.Thể hiện các chi tiết thép trong khối móng bao gồm chiều dài,chiều dày và các đoạn bẻ cong của cốt thép.                                      | Loại Kích thước Cao độ Phận loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường Các lớp bị che khuất Bê tông thô. Yêu cầu bề mặt/ Dung sai độ cao, quá trình làm khô |             |

![Image](images/image_000107_ae273d3e66cc7f5c0aede6a3f4515a99e40d56bf2e7279daf90747f65fa18a92.png)

![Image](images/image_000108_1871ab9b81f8ec5b2f8bb704df6a1c90213d22c18d02e7aae0b5665c8bc9091c.png)

| LOD   | Mô tả   | LOI                                            | Hình ảnh*   |
|-------|---------|------------------------------------------------|-------------|
|       |         | bê tông/tỷ trọng/nhà cung cấp và nhà sản xuất. |             |

## 11. Móng đổ tại chổ

|   LOD | Mô tả                                                                                                                                                                 | LOI                                                                                                                   | Hình ảnh*   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------|
|   100 | Vị trí móng được thế hiện bởi các bề mặt mặt phẳng hình học.                                                                                                          | Loại Kích thước (tương đối)                                                                                           |             |
|   200 | Móng được thể hiện dưới dạng hình khối, hình dạng tương đối, số lượng, kích thước, hình dạng vị trí và hướng đều được quy định trong mô hình.                         | Loại Kích thước Cao độ Phân loại Vật liệu                                                                             |             |
|   300 | Móng được thể hiện với số lượng, các đường kích thước, hình dạng và vị trí và hướng quy định. Thêm vào đó có độ dốc, lỗ rỗng, cốt thép và các cấu kiện, các chi tiết. | Loại Kích thước Cao độ Phân loại Vật liệu Cốt thép                                                                    |             |
|   350 | Móng gồm có các lỗ rỗng.Thể hiện các chi tiết thép trong khối móng bao gồm chiều dài,chiều dày và các đoạn bẻ cong của cốt thép.                                      | Loại Kích thước Cao độ Phân loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường Các lớp bị che khuất Bê tông, thô |             |
|   400 | Móng gồm có các lỗ rỗng.Thể hiện các chi tiết thép trong khối móng bao gồm chiều dài,chiều dày và các đoạn bẻ cong của cốt thép.                                      | Loại Kích thước Cao độ Phận loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường                                   |             |

![Image](images/image_000109_c12efbcd8bec24b52bea549a8ef878208a6d43e1e092c9d8783cab08f0a9fac5.png)

![Image](images/image_000110_4b34156dc2a0139cd7d39c812945194dd447a841afe3933e773f8c8ad246b039.png)

| Các lớp bị che khuất Bê tông thô. Yêu cầu bề mặt/ Dung sai độ cao , quá trình làm khô bê tông/tỷ trọng/nhà cung cấp và sản xuất.   |
|------------------------------------------------------------------------------------------------------------------------------------|

## 12. Tấm bê tông đổ tại chỗ

|   LOD | Mô tả                                                                                                                                                                                          | LOI                                                                                 | Hình ảnh*   |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------|
|   100 | Vị trí móng được thể hiện bởi các mặt phằng hình học.                                                                                                                                          | Loại Kích thước (tương đối)                                                         |             |
|   200 | Móng được thể hiện dưới dạng hình khối, hình dạng tương đối, số lượng, kích thước, hình dạng vị trí và hướng đều được quy định trong mô hình.                                                  | Loại Kích thước Độ cao Phân loại Vật liệu                                           |             |
|   300 | Móng được thể hiện với số lượng, các đường dim khích thước, hình dạng vị trí và các hướng quy định. Các lỗ rỗng >Ø500, cốt thép, các chi tiết công trình được làm rõ nhưng không được mô hình. | Loại Kích thước Độ cao Phân loại Vật liệu                                           |             |
|   350 | Cốt thép được thể hiện trong mô hình 3D thuận tiện cho quá trình thi công, vị trí kích thước của các bộ phận công trình được quy định từ trước.                                                | Loại Kích thước Độ cao Phân loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường |             |
|   400 | Các chi tiết bê tông cốt thép và các bộ phận khác của cồn trình được mô hình dưới dạng tổ hợp.                                                                                                 | Loại Kích thước Cao độ Phận loại Vật liệu                                           |             |

| Cốt thép Cường độ bê tông Dạng môi trường Các lớp bị che khuất Bê tông thô. Yêu cầu bề mặt/ Dung sai độ cao , quá trình làm khô bê tông/tỷ trọng/nhà cung cấp và sản xuất.   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 13. Tấm bê tông chế tạo sẵn

|   LOD | Mô tả                                                                                                                                                                                                                                                           | LOI                                                                                 | Hình ảnh*   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------|
|   100 | Tấm sàn được thể hiện bởi bề mặt ngoài của khối hình học, hình dạng bởi A geometric placeholder                                                                                                                                                                 | Loại Kích thước (tương đối)                                                         |             |
|   200 | Tấm sàn được thể hiện bởi các vật thể với những thiết kế tương đối, Số lượng, kích thước, hình dạng, vị trí và hướng.                                                                                                                                           | Loại Kích thước Độ cao Phân loại Vật liệu                                           |             |
|   300 | Móng được thể hiện với số lượng, các đường dim khích thước, hình dạng vị trí và các hướng quy định. Các lỗ rỗng >Ø500 xuất hiện trong khối hình học. Cốt thép, các chi tiết được làm rõ nhưng không được mô hình.                                               | Loại Kích thước Độ cao Phân loại Vật liệu                                           |             |
|   350 | Mô hình được chia nhỏ ra cho việc chế tạo trong nhà máy. Cốt thép được thể hiện trong mô hình 3D trực quan, với các lỗ rỗng thuận tiện cho quá trình lắp dựng, vị trí chính xác của các loại cấu kiện, các đường dim khoảng cách cũng được định nghĩa từ trước. | Loại Kích thước Độ cao Phân loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường |             |

![Image](images/image_000111_ff7fc99e6e90ec7462a23e7398b76b722f831fc39b2ac0a432f4471e45d202ab.png)

![Image](images/image_000112_4c1499069358f5cd1819b8edcfc451f6617d8554676c6c43311995796805d78c.png)

![Image](images/image_000113_f538b079d904f18b6cad475a3e4838f7bf52d4a8a080dfa08f1eb4f38924d7ed.png)

| 400   | Các chi tiết cụ thể được nhà sản xuất mô hình lại, ví dụ như các chi tiết cốt thép, cũng như các cấu liện khác của công trình.   | Loại Kích thước Cao độ Phận loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường Các lớp bị che khuất Bê tông thô. Yêu cầu bề mặt/ Dung sai độ cao , quá trình làm khô bê tông/tỷ trọng/nhà cung cấp và nhà sản xuất.   |
|-------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 14. Dầm bê tông, cấu kiện

|   LOD | Mô tả                                                                                                                                                                                            | LOI                                       | Hình ảnh*   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-------------|
|   100 | Vị trí của dầm được thể hiện bằng bề mặt bên ngoài của hình học hoặc là dưới dạng geometric place holder với những hình dạng tương đối.                                                          | Loại Kích thước (tương đối)               |             |
|   200 | Vị trí của dầm được thể hiện bằng các đối tượng có cùng chung tiết diện, cùng chung một thiết kế. Số lượng, kích thước và hình dạng thêm vào đó là vị trí và hướng của dầm cũng được định nghĩa. | Loại Kích thước Độ cao Phân loại Vật liệu |             |
|   300 | Dầm có các thông tin như số lượng, các đường kích thước, khoảng cách, hình dạng-vị trí và hướng của dầm đều được quy định. Độ dốc và các rỗ rỗng, cốt thép đều được thể hiện trong mô hình.      | Loại Kích thước Độ cao Phân loại Vật liệu |             |

![Image](images/image_000114_3099e2dcc9a42f19218aff92e6c6a99f96bbf780ee201f50ca63c67a325bcaf0.png)

![Image](images/image_000115_2549e27f3df96735ca1955ded3fc1ab75c7c27e649fe4b008e2dafa2760da88a.png)

|   350 | Dầm bao gồm chamfers, vị trí của các components, jonts và các casting joints. Hơn thế nữa các lỗ rỗng được được thể hiện trong mô hình.   | Loại Kích thước Độ cao Phân loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường                                                                                                                                  |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   400 | Dầm được chia ra thuận tiện cho quá trình đúc sẵn. Cốt thép được thể hiện chi tiết bao gồm các mối nối và các đoạn bẻ thép.               | Loại Kích thước Cao độ Phận loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường Các lớp bị che khuất Bê tông thô. Yêu cầu bề mặt/ Dung sai độ cao , quá trình làm khô bê tông/tỷ trọng/nhà cung cấp và sản xuất. |

## 15. Dầm bê tông đổ tại chỗ

|   LOD | Mô tả                                                                                                                                                                                            | LOI                                       | Hình ảnh*   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-------------|
|   100 | Vị trí của dầm được thể hiện bằng bề mặt bên ngoài của hình học hoặc là dưới dạng geometric place holder với những hình dạng tương đối.                                                          | Loại Kích thước (tương đối)               |             |
|   200 | Vị trí của dầm được thể hiện bằng các đối tượng có cùng chung tiết diện, cùng chung một thiết kế. Số lượng, kích thước và hình dạng thêm vào đó là vị trí và hướng của dầm cũng được định nghĩa. | Loại Kích thước Độ cao Phân loại Vật liệu |             |

![Image](images/image_000116_64bfe28849dbc0623aebf66a9fc9dc82f36b55fd4f5fcb54ff135a2cbefcb559.png)

![Image](images/image_000117_fe9a3adeb6b5aa62b84744cebab765b656eb3cf4b7f4e48ce2338c5bfda40e35.png)

![Image](images/image_000118_d3803d0cd9aafd01d5dd2488fef8dc006f1505f066632e4fa7908b7082cb675c.png)

|   300 | Dầm có các thông tin như số lượng, các đường dim khoảng cách, hình dạng-vị trí và hướng của dầm đều được quy định. Độ dốc và các rỗ rỗng, cốt thép đều được thể hiện trong mô hình.   | Loại Kích thước Độ cao Phân loại Vật liệu                                                                                                                                                                            |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   350 | Dầm bao gồm chamfers, vị trí của các components, jonts và các casting joints. Hơn thế nữa các lỗ rỗng được được thể hiện trong mô hình.                                               | Loại Kích thước Độ cao Phân loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường                                                                                                                                  |
|   400 | Cốt thép được thể hiện chi tiết bao gồm các mối nối và các đoạn bẻ thép.                                                                                                              | Loại Kích thước Cao độ Phận loại Vật liệu Cốt thép Cường độ bê tông Dạng môi trường Các lớp bị che khuất Bê tông thô. Yêu cầu bề mặt/ Dung sai độ cao , quá trình làm khô bê tông/tỷ trọng/nhà cung cấp và sản xuất. |

## 16. Dầm thép

|   LOD | Mô tả                                                                                                                                   | LOI                         | Hình ảnh*   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------|
|   100 | Vị trí của dầm được thể hiện bằng bề mặt bên ngoài của hình học hoặc là dưới dạng geometric place holder với những hình dạng tương đối. | Loại Kích thước (tương đối) |             |

![Image](images/image_000119_81df7ba02bd55c88ca664d68fd61ddcf4fddcbc4027746735b654c9a41f2c5a0.png)

![Image](images/image_000120_268ea8a3def1bf103266dcdf8218c09cc3c7f546fe04b17f4042ae3d8b583691.png)

![Image](images/image_000121_c01a162437d8da6094813e18241e63a7f71b8e6d7c4002ebbb45f5fe2b4a351e.png)

![Image](images/image_000122_40f6ad5f450755ce6326f6816d8d9119c5c14864f02d4fb066cff3974282343c.png)

|   200 | Vị trí của dầm được thể hiện bằng các đối tượng có cùng chung tiết diện, cùng chung một thiết kế. Số lượng, kích thước và hình dạng thêm vào đó là vị trí và hướng của dầm cũng được định nghĩa.   | Loại Kích thước (tương đối)                                                                                                                                             |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   300 | Dầm có các thông tin như số lượng, các đường dim khoảng cách, hình dạng-vị trí và hướng của dầm đều được quy định. Độ dốc và các rỗ rỗng, cốt thép đều được thể hiện trong mô hình.                | Loại Kích thước Cao độ Phân loại Vật liệu Yêu cầu chống cháy                                                                                                            |
|   350 | Dầm bao gồm chamfers, vị trí của các components, jonts và các casting joints. Hơn thế nữa các lỗ rỗng được được thể hiện trong mô hình.                                                            | Loại Kích thước Cao độ Phận loại Vật liệu Yêu cầu chống cháy Xử lý bề mặt                                                                                               |
|   400 | Dầm được chia ra thuận tiện cho quá trình đúc sẵn,chế tạo trong nhà máy.                                                                                                                           | Loại Kích thước Cao độ Phận loại Vật liệu Yêu cầu chống cháy Xử lý bề mặt Chiều dài tấm thép Khả năng chống ăn mòn Dung sai lắp đặt Neo dính Nhà cung cấp/ nhà sản xuất |

## 17. Cột thép

|   LOD | Mô tả                                                                                                                                                                                            | LOI                                                                                                       | Hình ảnh*   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------|
|   100 | Vị trí của cột được thể hiện bằng bề mặt bên ngoài của hình học hoặc là dưới dạng geometric place holder với những hình dạng tương đối.                                                          | Loại Kích thước (tương đối)                                                                               |             |
|   200 | Vị trí của cột được thể hiện bằng các đối tượng có cùng chung tiết diện, cùng chung một thiết kế. Số lượng, kích thước và hình dạng thêm vào đó là vị trí và hướng của cột cũng được định nghĩa. | Loại Kích thước Cao độ Phân loại Vật liệu                                                                 |             |
|   300 | Cột có các thông tin như số lượng, các đường dim khoảng cách, hình dạng-vị trí và hướng của dầm đều được quy định. Độ dốc và các rỗ rỗng, cốt thép đều được thể hiện trong mô hình.              | Loại Kích thước Cao độ Phân loại Vật liệu Yêu cầu chống cháy                                              |             |
|   350 | Cột bao gồm các end plates và brackets cũng như là các thanh sườn chịu lực. Các chi tiết tổ hợp, lỗ và các khớp gia cố được quy định.                                                            | Loại Kích thước Cao độ Phân loại Vật liệu Yêu cầu chống cháy Xử lý bề mặt Chiều dài tấm thép              |             |
|   400 | Cột được chia ra thuận tiện cho quá trình đúc sẵn,chế tạo trong nhà máy.                                                                                                                         | Loại Kích thước Cao độ Phận loại Vật liệu Yêu cầu chống cháy Xử lý bề mặt Chiều dài tấm thép Chống ăn mòn |             |

![Image](images/image_000123_feeeed68046f621909c986ba977667a58b25c4b1e51840b601a58886f8d9a394.png)

![Image](images/image_000124_30a1e09c84a72844b97eec333a9f8a4b8ea2168cdaa39c02730d15ae61b8ce2e.png)

| LOD Mô tả                              | LOI   | Hình ảnh*   |
|----------------------------------------|-------|-------------|
| Dung sai lắp đặt Nhà cung cấp/ nhà sản | xuất  |             |

## 18. Hệ thống phụ trợ, tiện ích

|   LOD | Mô tả                                                                                                                                                                                                                                | LOI                                                                                                    | Hình ảnh*   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-------------|
|   100 | Các khay các ống dẫn tuyến tĩnh được thể hiện bởi một hình khối với hình dạng hình học tương đối hoặc giản đồ. Các bộ phận được thể hiện bao gồm: hệ thống làm mát, hệ thống nhiệt, các sprinkler, hệ thống thông gió, các bảng điện | Loại Kích thước (tương đối) Tiêu thụ                                                                   |             |
|   200 | Vị trí, kích thước của các bộ phận chính và phụ của các tuyến lắp đặt. Không gian, các yêu cầu liên quan, các tiêu chuẩn đều phải được thể hiên trong mô hình. Thể hện vị trí của các bộ chuyển đổi, Boilers, máy bơm,…              | Loại Kích thước (tương đối) Cao độ Phân loại Tiêu thụ Tên hệ thống                                     |             |
|   300 | Các hình dạng thực tế, các thiết kế vị trí lặp đặt bao gồm các không gian cần thiết cần được thể hiện trong mô hình. Các loại liên kết, các loại ống tổ hợp đều được mô hình lại.                                                    | Loại Kích thước (tương đối) Cao độ Phân loại Tiêu thụ Tên hệ thống Vật liệu                            |             |
|   350 | Hình dạng chi tiết với kích thước chính xác, vị trí, thiết kế, các tiêu chuẩn yêu cầu cho công việc lắp đặt.                                                                                                                         | Loại Kích thước (tương đối) Cao độ Phân loại Tiêu thụ Tên hệ thống Vật liệu Nhà sản xuất/ nhà cung cấp |             |

| 400   | Các liên kiết và các chi tiết đều được thể hiện trong mô hình.   | Loại Kích thước (tương đối) Cao độ Phân loại Tiêu thụ Tên hệ thống Vật liệu Nhà sản xuất/ nhà cung cấp   |
|-------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|

## 19. Hệ thống đường ống

|   LOD | Mô tả                                                                                                                                                       | LOI                                                                               | Hình ảnh*   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------|
|   100 | Các đường ống dẫn chính được thể hiện bơi các geometric place holder với hình dạng hình học tương đối hoặc là các giản đồ.                                  | Loại Kích thước Tiêu thụ                                                          |             |
|   200 | Cách lắp đặt bố trí chúng, các vị trí kích thước của các đường ống chính và phụ trong quá trình lắp dựng bao gồm các van, các không gian tương đối          | Loại Kích thước (tương đối) Cao độ Phân loại Tên hệ thống Yêu cầu kỹ thuật.       |             |
|   300 | Khoảng cách, kích thước chính xác, vị trí, thiết kế của các đường ống chính phụ, vật liệu, chiều dày của đường ống các van đều được thể hiện trong mô hình. | Loại Kích thước Cao độ Phân loại Tên hệ thống Yêu cầu kỹ thuật Vật liệu           |             |
|   350 | Hình dạng chi tiết.                                                                                                                                         | Loại Kích thước Cao độ Phân loại Tên hệ thống Yêu cầu kỹ thuật Vật liệu Công suất |             |
|   400 | Các liên kết, các chi tiết đều được thể hiện trong mô hình 3D.                                                                                              | Loại Kích thước Cao độ Phân loại                                                  |             |

![Image](images/image_000125_e923c6f86079b42a8d56e6170fbe8bdaecba47c3f55b7dda7f5eac44488f21b3.png)

![Image](images/image_000126_70154afc1b1f3ca88ae7db67bbdda8f578be8e47cd83cf26d05f553eec7d9ceb.png)

![Image](images/image_000127_d15452f563cf20b7adbf62c2dcf9ccb14e7a3c5abf07b1fe575fe27e773f49e7.png)

![Image](images/image_000128_939272b09280b795af76ee0216b30d0ccef5f6042f5d1aeaec864b30f0583e76.png)

| Tên hệ thống Yêu cầu kỹ thuật Vật liệu Công suất Nhà sản xuất/ nhà cung cấp   |
|-------------------------------------------------------------------------------|

## 20. Hệ thống cấp, thoát nước

|   LOD | Mô tả                                                                                                                                                                                                 | LOI                                                                               | Hình ảnh*   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------|
|   100 | Đường định tuyến lắp đặt chính được thể hiện bơi các geometric place holder với hình dạng hình học tương đối hoặc là các giản đồ.                                                                     | Loại Kích thước Tên hệ thống                                                      |             |
|   200 | Vị trí, kích thước của các đường ống chính phụ, không gian xung quanh được thể hiện trên mô hình. Vị trí của tường và sàn.                                                                            | Loại Kích thước (tương đối) Cao độ Phân loại Tên hệ thống                         |             |
|   300 | Kích thước ống, ống cong bao gồm vị trí, thiết kế, độ cong, không gian cho đường ống đều được thể hiện trong mô hình. May bơm, các đường van, các vòi nước và các cấu kiện khác đều được mô hình hóa. | Loại Kích thước Cao độ Phân loại Tên hệ thống Vật liệu                            |             |
|   350 | Hình dạng chi tiết, kích thước, vị trí và thiết kế, các đường ống cong, van ốc vít, đường ống.                                                                                                        | Loại Kích thước Cao độ Phân loại Tên hệ thống Vật liệu Nhà sản xuất/ Nhà cung cấp |             |
|   400 | Các liên kết, chi tiết, giá đỡ, hệ thống treo và các giá đỡ đều được thể hiện trên mô hình.                                                                                                           | Loại Kích thước Cao độ Phân loại Tên hệ thống Vật liệu                            |             |

| Nhà sản xuất/ Nhà cung cấp   |
|------------------------------|

## 21. Máng cáp

|   LOD | Mô tả                                                                                                                                                                                                          | LOI                                                                                          | Hình ảnh*   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------|
|   100 | Khay cáp, bảng đen, các đường dim kích thước, vị trí và thiết kế, không gian cho việc lắp đặt.                                                                                                                 | Loại Kích thước                                                                              |             |
|   200 | Khay cáp, bảng đen, các đường dim kích thước, vị trí và thiết kế, không gian cho việc lắp đặt, vị trí tường và trần sàn.                                                                                       | Loại Kích thước (tương đối) Cao độ Phân loại Tên hệ thống                                    |             |
|   300 | Các đường dim kích thước thực tế, vị trí của các đường ống cong các mối nối. vị trí, kích thước của fixture, công tắc điện, các đường ống cùng các cấu kiện bê tông cốt thép. vị trí của các khay cáp thứ cấp. | Loại Kích thước (tương đối) Cao độ Phân loại Tên hệ thống Vật liệu                           |             |
|   350 | Hình dạng chi tiết, kích thước thực tế, vị trí, thiết kế, không gian xung quanh.                                                                                                                               | Loại Kích thước (tương đối) Cao độ Phân loại Tên hệ thống Vật liệu Đơn vị sản xuất/ cung cấp |             |
|   400 | Liên kết và chi tiết, giá đỡ được thể hiện trong mô hình 3D                                                                                                                                                    | Loại Kích thước (tương đối) Cao độ Phân loại Tên hệ thống Vật liệu Đơn vị sản xuất/ cung cấp |             |

## 22. Một số loại hố ga

## 22.1. Hố ga loại 1

|   LOD | Mô tả                                                                                                                                                                                                                                                                                                                                                                             | LOI                      | Hình ảnh   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|
|   100 | Mô hình cấu kiện có thể biểu thị trong mô hình dưới dạng ký hiệu hoặc biểu thị tương tự khác                                                                                                                                                                                                                                                                                      | Loại hệ thống thoát nước |            |
|   200 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng hệ thống chung, cấu kiện lắp ráp với số lượng và kích thước, hình dạng, vị trí và hướng gần đúng, Thông tin phi hình học cũng có thể được đính kèm vào mô hình cấu kiện                                                                                                                                                    | Cao độ cống thoát nước   |            |
|   300 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấu kiện lắp ráp với số lượng, kích thước, hình dạng, vị trí và hướng. Thông tin phi hình học có thể được đính kèm vào mô hình cấu kiện. Phần tử trong mô hình nên bao gồm: - Sàn bê tông - Tường - Đầu ống nối - Khung và nắp cống                                                                          | Mác bê tông              |            |
|   400 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấi kiện láp ráp với số lượng, kích thước, hình dạng, vị trí và thông tin chi tiết về chế tạo, lắp ráp, lắp đặt. Thông tin phi hình học cũng có thể được đính kèm với mô hình cấu kiện Phần tử trong mô hình nên bao gồm: - Sàn bê tông - Tường - Đầu ống nối - Chi tiết khung và nắp cống - Rãnh thoát nước | Ngày bàn giao            |            |

![Image](images/image_000129_5fc08a54a801cec60df0499ebe963439f833e02f85f4368ce8fec6c63c376fec.png)

![Image](images/image_000130_751297d9e8c793a37a0c16eb63babd178db17da8d8f1167a7d175f8a841785e3.png)

![Image](images/image_000131_68971ba71c034bb187b12cf54a9c8ef3b29bc04de995b13fdcf2c3c062873082.png)

![Image](images/image_000132_d61eaaf7101c0017767a549d71b18af927e34cdb112e787bf0f7f307725b7b8d.png)

22.2. Hố ga loại 2

|   LOD | Mô tả                                                                                                                                                                                                                                                                                                                                                                             | LOI                      | Hình ảnh   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|
|   100 | Mô hình cấu kiện có thể biểu thị trong mô hình dưới dạng ký hiệu hoặc biểu thị tương tự khác                                                                                                                                                                                                                                                                                      | Loại hệ thống thoát nước |            |
|   200 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng hệ thống chung, cấu kiện lắp ráp với số lượng và kích thước, hình dạng, vị trí và hướng gần đúng, Thông tin phi hình học cũng có thể được đính kèm vào mô hình cấu kiện                                                                                                                                                    | Cao độ cống thoát nước   |            |
|   300 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấu kiện lắp ráp với số lượng, kích thước, hình dạng, vị trí và hướng. Thông tin phi hình học có thể được đính kèm vào mô hình cấu kiện. Phần tử trong mô hình nên bao gồm: - Sàn bê tông - Tường - Đầu ống nối - Khung và nắp cống                                                                          | Mác bê tông              |            |
|   400 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấi kiện láp ráp với số lượng, kích thước, hình dạng, vị trí và thông tin chi tiết về chế tạo, lắp ráp, lắp đặt. Thông tin phi hình học cũng có thể được đính kèm với mô hình cấu kiện Phần tử trong mô hình nên bao gồm: - Sàn bê tông - Tường - Đầu ống nối - Chi tiết khung và nắp cống - Rãnh thoát nước | Ngày bàn giao            |            |

![Image](images/image_000133_ca6e5212a5750a3236cf1b0edfe3dc197eaec453d52a42503ccaa6f58b5bf95c.png)

![Image](images/image_000134_21e7f7fffa6727c6499dc9078eac00f8f6dfad1466d674e09a83340ebef822b5.png)

![Image](images/image_000135_9aa9fecbc1b6286efdd5e2653a7a2f3227debd120f06a64a3ebacd89694a3275.png)

| - Thang bậc bằng thép   |
|-------------------------|

## 22.3. Hố ga loại 3

|   LOD | Mô tả                                                                                                                                                                                                                                                                                                                                                           | LOI                      | Hình ảnh   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|
|   100 | Mô hình cấu kiện có thể biểu thị trong mô hình dưới dạng ký hiệu hoặc biểu thị tương tự khác                                                                                                                                                                                                                                                                    | Loại hệ thống thoát nước |            |
|   200 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng hệ thống chung, cấu kiện lắp ráp với số lượng và kích thước, hình dạng, vị trí và hướng gần đúng, Thông tin phi hình học cũng có thể được đính kèm vào mô hình cấu kiện                                                                                                                                  | Cao độ cống thoát nước   |            |
|   300 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấu kiện lắp ráp với số lượng, kích thước, hình dạng, vị trí và hướng. Thông tin phi hình học có thể được đính kèm vào mô hình cấu kiện. Phần tử trong mô hình nên bao gồm: - Sàn bê tông - Tường - Đầu ống nối - Khung và nắp cống                                                        | Mác bê tông              |            |
|   400 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấi kiện láp ráp với số lượng, kích thước, hình dạng, vị trí và thông tin chi tiết về chế tạo, lắp ráp, lắp đặt. Thông tin phi hình học cũng có thể được đính kèm với mô hình cấu kiện Phần tử trong mô hình nên bao gồm: - Sàn bê tông - Tường - Đầu ống nối - Chi tiết khung và nắp cống | Ngày bàn giao            |            |

![Image](images/image_000136_bd4d40a410f3cb9da97340c15cdc12115d7f07a34a914818fd3876f7aa93af74.png)

![Image](images/image_000137_051821e0ea43db91727e32dded778f539aa1450d063c6af9dc53533a1be2966d.png)

![Image](images/image_000138_096f8604ef30d9ced58e7b92f825b223f9cba391f3cb9136acbbb36236cd2201.png)

| - Rãnh thoát nước   |
|---------------------|
| - Dây thừng         |
| - Móc thép          |

## 22.4. Hố ga loại 4

|   LOD | Mô tả                                                                                                                                                                                                                                                                                                                                                                                 | LOI                      | Hình ảnh   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|
|   100 | Mô hình cấu kiện có thể biểu thị trong mô hình dưới dạng ký hiệu hoặc biểu thị tương tự khác                                                                                                                                                                                                                                                                                          | Loại hệ thống thoát nước |            |
|   200 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng hệ thống chung, cấu kiện lắp ráp với số lượng và kích thước, hình dạng, vị trí và hướng gần đúng, Thông tin phi hình học cũng có thể được đính kèm vào mô hình cấu kiện                                                                                                                                                        | Cao độ cống thoát nước   |            |
|   300 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấu kiện lắp ráp với số lượng, kích thước, hình dạng, vị trí và hướng. Thông tin phi hình học có thể được đính kèm vào mô hình cấu kiện. Phần tử trong mô hình nên bao gồm: - Sàn bê tông - Tường - Đầu ống nối - Khung và nắp cống - Tấm bê tông đúc sẵn                                                        | Mác bê tông              |            |
|   400 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấi kiện láp ráp với số lượng, kích thước, hình dạng, vị trí và thông tin chi tiết về chế tạo, lắp ráp, lắp đặt. Thông tin phi hình học cũng có thể được đính kèm với mô hình cấu kiện Phần tử trong mô hình nên bao gồm: - Sàn bê tông - Tường - Đầu ống nối - Chi tiết khung và nắp cống - Tấm bê tông đúc sẵn | Ngày bàn giao            |            |

![Image](images/image_000139_6c2d028a0fbf1714080824887b9fc0f363bf91b9fb97db48e58fa5e43befdae2.png)

![Image](images/image_000140_a8da66b6675262c10acb688c7907147fefed99b6c4838a72c2b3d2621d1f5bdd.png)

![Image](images/image_000141_d46b1bc779b215965d053d10e79af99ef49b7043df9e5d172310b43fb44d5e36.png)

![Image](images/image_000142_3c629ea78a6a078977b4ea8cb3984f172bd970cbd0066e8740938a64c3ac33d7.png)

| - Thang bậc bằng thép   |
|-------------------------|

## 23. Một số loại nắp hố ga

## 23.1. Nắp hố ga loại 1

|   LOD | Mô tả                                                                                                                                                                                                                                                                                                                                                                                  | LOI                      | Hình ảnh   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------|
|   100 | Mô hình cấu kiện có thể biểu thị trong mô hình dưới dạng ký hiệu hoặc biểu thị tương tự khác                                                                                                                                                                                                                                                                                           | Loại hệ thống thoát nước |            |
|   200 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng hệ thống chung, cấu kiện lắp ráp với số lượng và kích thước, hình dạng, vị trí và hướng gần đúng, Thông tin phi hình học cũng có thể được đính kèm vào mô hình cấu kiện                                                                                                                                                         | Vật liệu                 |            |
|   300 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấu kiện lắp ráp với số lượng, kích thước, hình dạng, vị trí và hướng. Thông tin phi hình học có thể được đính kèm vào mô hình cấu kiện. Phần tử trong mô hình nên bao gồm: - Khung và nắp công - Prising slot                                                                                                    | Hình dạng                |            |
|   400 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấi kiện láp ráp với số lượng, kích thước, hình dạng, vị trí và thông tin chi tiết về chế tạo, lắp ráp, lắp đặt. Thông tin phi hình học cũng có thể được đính kèm với mô hình cấu kiện Phần tử trong mô hình nên bao gồm: - Chi tiết khung và nắp cống - Móc nâng - Lỗ khoá - Tăng đinh (Raised stud) - Nhãn hiệu | Ngày bàn giao            |            |

![Image](images/image_000143_f191bc2dbdb858677c8d96229c42ef03c42c394a28add04ef45c9fa6f531656f.png)

![Image](images/image_000144_e6f2333ac812bcd3553cd3c38752c53f22615084b945eb79998723ddb5f69840.png)

![Image](images/image_000145_7a41a6480df286d6a550ef306674b0a54bdfdb1c4529522e6631160dd4302bd2.png)

![Image](images/image_000146_88cfd7cd937381535daff95f62d0a0c0aba34b7ee3bc8266680a7c0900862c1b.png)

## 23.2. Nắp hố ga loại 2

|   LOD | Mô tả                                                                                                                                                                                                                                                                                                                                                                      | LOI   | Hình ảnh   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------|
|   100 | Mô hình cấu kiện có thể biểu thị trong mô hình dưới dạng ký hiệu hoặc biểu thị tương tự khác                                                                                                                                                                                                                                                                               |       |            |
|   200 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng hệ thống chung, cấu kiện lắp ráp với số lượng và kích thước, hình dạng, vị trí và hướng gần đúng, Thông tin phi hình học cũng có thể được đính kèm vào mô hình cấu kiện                                                                                                                                             |       |            |
|   300 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấu kiện lắp ráp với số lượng, kích thước, hình dạng, vị trí và hướng. Thông tin phi hình học có thể được đính kèm vào mô hình cấu kiện. Phần tử trong mô hình nên bao gồm: - Khung và nắp cống - Móc nâng                                                                                            |       |            |
|   400 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấi kiện láp ráp với số lượng, kích thước, hình dạng, vị trí và thông tin chi tiết về chế tạo, lắp ráp, lắp đặt. Thông tin phi hình học cũng có thể được đính kèm với mô hình cấu kiện Phần tử trong mô hình nên bao gồm: - Chi tiết khung và nắp cống - Móc nâng - Lỗ khoá - Tăng đinh (Raised stud) |       |            |

![Image](images/image_000147_4a3424d942967bc0218e65f1a7c404bf5efb844876902cbe21da10173a357e60.png)

![Image](images/image_000148_50b6605062b9eedb9c833075bd74b2e691e898cd101f3454023c7ac81c059804.png)

## 24. Thang lên xuống

|   LOD | Mô tả                                                                                                                                                                                                                                                                                                                                        | LOI   | Hình ảnh   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------|
|   100 | Mô hình cấu kiện có thể biểu thị trong mô hình dưới dạng ký hiệu hoặc biểu thị tương tự khác                                                                                                                                                                                                                                                 |       |            |
|   200 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng hệ thống chung, cấu kiện lắp ráp với số lượng và kích thước, hình dạng, vị trí và hướng gần đúng, Thông tin phi hình học cũng có thể được đính kèm vào mô hình cấu kiện                                                                                                               |       |            |
|   300 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấu kiện lắp ráp với số lượng, kích thước, hình dạng, vị trí và hướng. Thông tin phi hình học có thể được đính kèm vào mô hình cấu kiện. Phần tử trong mô hình nên bao gồm: - Bậc thang - Thanh thép                                                                    |       |            |
|   400 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấi kiện láp ráp với số lượng, kích thước, hình dạng, vị trí và thông tin chi tiết về chế tạo, lắp ráp, lắp đặt. Thông tin phi hình học cũng có thể được đính kèm với mô hình cấu kiện Phần tử trong mô hình nên bao gồm: - Bậc thang - Thanh thép - Các bộ phận hỗ trợ |       |            |

![Image](images/image_000149_b124b489d12ed158d488bdcdc582597fa5ca7c1c9c7dddebadb86c6da46ba844.png)

![Image](images/image_000150_93297c4545f5d5ad24b4ae6818dcd76599553b2b10e85b793fb6b263e7efca7b.png)

![Image](images/image_000151_9feb488e97fa35aa9a48eb6668dbb460742396ba89e9b63e72e9643020b90281.png)

## 25. Biển báo

|   LOD | Mô tả                                                                                                                                                                                                                                                                                                                                       | LOI   | Hình ảnh   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------|
|   100 | Mô hình cấu kiện có thể biểu thị trong mô hình dưới dạng ký hiệu hoặc biểu thị tương tự khác                                                                                                                                                                                                                                                |       |            |
|   200 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng hệ thống chung, cấu kiện lắp ráp với số lượng và kích thước, hình dạng, vị trí và hướng gần đúng, Thông tin phi hình học cũng có thể được đính kèm vào mô hình cấu kiện                                                                                                              |       |            |
|   300 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấu kiện lắp ráp với số lượng, kích thước, hình dạng, vị trí và hướng. Thông tin phi hình học có thể được đính kèm vào mô hình cấu kiện. Phần tử trong mô hình nên bao gồm: - Tấm và bảng thông báo - Đế và cột                                                        |       |            |
|   400 | Mô hình cấu kiện được biểu thị trong mô hình dưới dạng một hệ thống, cấi kiện láp ráp với số lượng, kích thước, hình dạng, vị trí và thông tin chi tiết về chế tạo, lắp ráp, lắp đặt. Thông tin phi hình học cũng có thể được đính kèm với mô hình cấu kiện Phần tử trong mô hình nên bao gồm: - Chi tiết tấm và bảng thông báo - Đế và cột |       |            |

![Image](images/image_000152_5671fe0318ef6a812e8b38c7ce689abc87a62bb0a6fe6d1d9eae186a2e564c57.png)

![Image](images/image_000153_f05f1c8b9ae862918de2fc9722fd82932ee05174a0452ae97dafbe218e85ac39.png)

* Hình ảnh minh hoạ được sử dụng trong Hướng dẫn này được tham khảo từ hướng tài liệu Building Component Catalogue with Level of Development Specification (LOD) MT Højgaard

## PHỤ LỤC 04: MỨC ĐỘ PHÁT TRIỂN THÔNG TIN PHI HÌNH HỌC CỦA MỘT SỐ CẤU KIỆN TRONG CÔNG TRÌNH CẦU

## 1. Cọc đóng/ ép

| Giai đoạn                                      | Tham số                                         |
|------------------------------------------------|-------------------------------------------------|
| Thông tin trong giai đoạn thiết Tên và Số hiệu | Thông tin trong giai đoạn thiết Tên và Số hiệu  |
| kế                                             | Hạng mục                                        |
|                                                | Độ bền nén thiết kế (MPa)                       |
|                                                | Lớp bê tông bảo vệ                              |
|                                                | Mác bê tông                                     |
|                                                | Cao độ đầu cọc theo thiết kế                    |
|                                                | Cao độ mũi cọc                                  |
|                                                | Chiều dài cọc                                   |
|                                                | Vị trí theo trục Đông - Tây                     |
|                                                | Vị trí theo trục Bắc - Nam                      |
|                                                | Sức chịu tải thiết kế của cọc theo đất nền (kN) |
|                                                | Sức chịu tải thiết kế của cọc (kN)              |
|                                                | Loại cọc (Đại trà/Thí nghiệm)                   |
|                                                | Loại cọc (Đại trà/Thí nghiệm)                   |
|                                                | Cường độ nén thiết kế của bê tông (MPa)         |
|                                                | Loại cọc (Đại trà/Thí nghiệm)                   |
|                                                | Khối lượng (Tấn)                                |
|                                                | Tiêu chuẩn thiết kế                             |
| Thông tin phục vụ sản xuất                     | Tên và Số hiệu                                  |
|                                                | Số lượng                                        |
|                                                | Cường độ nén bê tông khi giao (MPa)             |
|                                                | Phê duyệt cấp phối bê tông                      |
|                                                | Hồ sơ kiểm tra bê tông                          |
|                                                | Biểu đồ nhiệt độ trong quá trình đóng rắn       |
|                                                | Ngày sản xuất                                   |
|                                                | Bản vẽ sản xuất                                 |
|                                                | Số lô sản xuất                                  |
|                                                | Đơn vị sản xuất                                 |
|                                                | Độ lệch chuẩn (loại phần tử)                    |
| Thông tin trong giai đoạn thi công             | Hồ sơ kiểm tra ứng suất                         |
|                                                | Tiêu chuẩn sản xuất                             |
|                                                | Biện pháp đổ bê tông                            |
|                                                | Điều kiện thi công                              |

| Sức chịu tải thực tế(kN)                                        |
|-----------------------------------------------------------------|
| Cao độ đầu cọc thực tế                                          |
| Bản vẽ thi công thực tế                                         |
| Vị trí theo trục Đông - Tây                                     |
| Vị trí theo trục Bắc - Nam                                      |
| Cường độ nén trung bình của bê tông sau 28 ngày (MPa)           |
| Cường độ nén trung bình sau 28 ngày trên toàn bộ cấu kiện (MPa) |
| Cao độ mũi cọc thực tế                                          |
| Mã cấu kiện                                                     |
| Hồ sơ thi công                                                  |
| Ngày thi công                                                   |
| Loại búa đóng                                                   |
| Quy trình đóng cọc đã được phê duyệt                            |

## 2. Cọc khoan nhồi

| Giai đoạn          | Tham số                                               |
|--------------------|-------------------------------------------------------|
| thiết kế           | Mã số cấu kiện                                        |
|                    | Cường độ chịu nén thiết kế (MPa)                      |
|                    | Lớp bê tông bảo vệ                                    |
|                    | Mác bê tông                                           |
|                    | Chiều dài thiết kế                                    |
|                    | Cao độ mũi cọc thiết kế                               |
|                    | Vị trí theo trục Đông - Tây                           |
|                    | Vị trí theo trục Bắc - Nam                            |
|                    | Cường độ chịu tải cọc theo đất nền(kN)                |
|                    | Cường độ chịu tải của cọc theo thiết kế (kN)          |
|                    | Cao độ mũi cọc theo thiết kế                          |
|                    | Đường kính cọc                                        |
|                    | Chiều dài cọc                                         |
|                    | Loại cọc                                              |
|                    | Loại thép dai chính                                   |
|                    | Loại thép chính của cọc                               |
| Thông tin thi công | Quy trình đóng cọc đã được phê duyệt                  |
| Thông tin thi công | Bản vẽ thi công thực tế                               |
| Thông tin thi công | Vị trí theo trục Đông - Tây                           |
| Thông tin thi công | Vị trí theo trục Bắc - Nam                            |
| Thông tin thi công | Cao độ mũi cọc thực tế                                |
| Thông tin thi công | Cường độ nén trung bình của bê tông sau 28 ngày (MPa) |

| Cường độ nén trung bình sau 28 ngày của cấu kiện (MPa) Mã số cấu kiện Ngày đổ Khối lượng bê tông (m 3 )   |
|-----------------------------------------------------------------------------------------------------------|
| Hồ sơ thi công                                                                                            |

## 3. Rào chắn

| Giai đoạn                  | Tham số                 |
|----------------------------|-------------------------|
| Thông tin thiết kế         | Mã số cấu kiện          |
| Thông tin thiết kế         | Chiều dài               |
| Thông tin thiết kế         | Chỉ dẫn kỹ thuật        |
| Thông tin phục vụ sản xuất | Mã số cấu kiện          |
| Thông tin phục vụ sản xuất | Ngày sản xuất           |
| Thông tin phục vụ sản xuất | Số lô sản xuất          |
| Thông tin phục vụ sản xuất | Đơn vị sản xuất         |
| Thông tin phục vụ sản xuất | Bản vẽ sản xuất         |
| Thông tin thi công         | Bản vẽ thi công thực tế |
| Thông tin thi công         | Mã số cấu kiện          |
| Thông tin thi công         | Ngày thi công           |

## 4. Bê tông vỉa hè

| Giai đoạn          | Tham số                                               |
|--------------------|-------------------------------------------------------|
| thiết kế           | Mã số cấu kiện                                        |
|                    | Độ bền nén thiết kế (MPa)                             |
|                    | Lớp bê tông bảo vệ                                    |
|                    | Mác bê tông                                           |
|                    | Khối lượng bê tông thiết kế                           |
|                    | Chiều dày                                             |
|                    | Chiều dài                                             |
|                    | Chiều rộng                                            |
|                    | Loại                                                  |
|                    | Chỉ dẫn kỹ thuật                                      |
|                    | Cốt thép dọc điển hình dưới                           |
|                    | Loại thép đai chính                                   |
|                    | Cốt thép điển hình trên                               |
| Thông tin thi công | Bản vẽ thi công thực tế                               |
| Thông tin thi công | Cường độ nén trung bình của bê tông sau 28 ngày (MPa) |

| Cường độ nén trung bình sau 28 ngày của cấu kiện (MPa)   |
|----------------------------------------------------------|
| Mã số cấu kiện                                           |
| Khối lượng bê tông thực tế (m³)                          |
| Hồ sơ thi công                                           |

## 5. Xà Mũ

| Giai đoạn          | Tham số                                                |
|--------------------|--------------------------------------------------------|
| thiết kế           | Mã số cấu kiện                                         |
|                    | Độ bền nén thiết kế (MPa)                              |
|                    | Lớp bê tông bảo vệ                                     |
|                    | Mác bê tông                                            |
|                    | Khối lượng bê tông thiết kế                            |
|                    | Chiều sâu                                              |
|                    | Chiều dài                                              |
|                    | Chiều rộng                                             |
|                    | Loại                                                   |
|                    | Loại cốt thép dưới bố trí theo phương dọc điển hình    |
|                    | Thép đai điển hình                                     |
|                    | Loại cốt thép trên bố trí theo phương dọc điển hình    |
|                    | Chỉ dẫn kỹ thuật                                       |
| Thông tin thi công | Bản vẽ thi công thực tế                                |
| Thông tin thi công | Cường độ nén trung bình của bê tông sau 28 ngày (MPa)  |
| Thông tin thi công | Mã số cấu kiện                                         |
| Thông tin thi công | Hồ sơ kiểm tra bê tông                                 |
| Thông tin thi công | Khối lượng bê tông thi công thực tế                    |
| Thông tin thi công | Cao độ xà mũ                                           |
| Thông tin thi công | Cường độ nén trung bình sau 28 ngày của cấu kiện (MPa) |
| Thông tin thi công | Hồ sơ thi công                                         |
| Thông tin thi công | Ngày đổ bê tông                                        |

## 6. Hàng rào bê tông

| Giai đoạn          | Tham số                   |
|--------------------|---------------------------|
| Thông tin thiết kế | Mã số cấu kiện            |
| Thông tin thiết kế | Độ bền nén thiết kế (MPa) |
| Thông tin thiết kế | Lớp bê tông bảo vệ        |

|                    | Mác bê tông                                            |
|--------------------|--------------------------------------------------------|
|                    | Khối lượng bê tông trong thiết kế (m ³ )               |
|                    | Chiều sâu                                              |
|                    | Chiều dài                                              |
|                    | Chiều rộng đáy hàng rào                                |
|                    | Chiều rộng đỉnh hàng rào                               |
|                    | Loại hàng rào                                          |
|                    | Loại cốt thép dưới bố trí theo phương dọc điển hình    |
|                    | Loại thép đai điển hình                                |
|                    | Loại cốt thép trên bố trí theo phương dọc điển hình    |
|                    | Chỉ dẫn kỹ thuật                                       |
| Thông tin thi công | Bản vẽ thi công thực tế                                |
| Thông tin thi công | Cường độ nén trung bình của bê tông sau 28 ngày (MPa)  |
| Thông tin thi công | Cường độ nén trung bình sau 28 ngày của cấu kiện (MPa) |
| Thông tin thi công | Mã số cấu kiện                                         |
| Thông tin thi công | Hồ sơ kiểm tra bê tông                                 |
| Thông tin thi công | Hồ sơ thi công                                         |
| Thông tin thi công | Khối lượng bê tông thực tế (m ³ )                      |
| Thông tin thi công | Ngày đổ bê tông                                        |

## 7. Sàn bê tông dự ứng lực

| Giai đoạn                  | Tham số                                 |
|----------------------------|-----------------------------------------|
| Thông tin thiết kế         | Mã số cấu kiện                          |
| Thông tin thiết kế         | Độ bền nén thiết kế (MPa)               |
| Thông tin thiết kế         | Lớp bê tông bảo vệ                      |
| Thông tin thiết kế         | Mác bê tông                             |
| Thông tin thiết kế         | Chiều sâu                               |
| Thông tin thiết kế         | Chiều dài                               |
| Thông tin thiết kế         | Chiều rộng                              |
| Thông tin thiết kế         | Loại                                    |
| Thông tin thiết kế         | Khối lượng (Tấn)                        |
| Thông tin thiết kế         | Cường độ nén thiết kế của bê tông (MPa) |
| Thông tin thiết kế         | Chỉ dẫn kỹ thuật                        |
| Thông tin phục vụ sản xuất | Mã số cấu kiện                          |
| Thông tin phục vụ sản xuất | Số lượng                                |
| Thông tin phục vụ sản xuất | Cường độ nén của bê tông khi giao (MPa) |

|                    | Phê duyệt cấp phối bê tông                             |
|--------------------|--------------------------------------------------------|
|                    | Hồ sơ kiểm tra bê tông                                 |
|                    | Biểu đồ nhiệt độ trong quá trình đóng rắn              |
|                    | Ngày sản xuất                                          |
|                    | Bản vẽ sản xuất                                        |
|                    | Số lô sản xuất                                         |
|                    | Đơn vị sản xuất                                        |
|                    | Độ lệch chuẩn (loại phần tử)                           |
|                    | Hồ sơ kiểm tra ứng suất                                |
| Thông tin thi công | Bản vẽ thi công thực tế                                |
| Thông tin thi công | Cường độ nén trung bình của bê tông sau 28 ngày (MPa)  |
| Thông tin thi công | Cường độ nén trung bình sau 28 ngày của cấu kiện (MPa) |
| Thông tin thi công | Mã số cấu kiện                                         |
| Thông tin thi công | Hồ sơ thi công                                         |

## 8. Sàn bê tông liên hợp

| Giai đoạn          | Tham số                                               |
|--------------------|-------------------------------------------------------|
| thiết kế           | Mã số cấu kiện                                        |
|                    | Độ bền nén thiết kế (MPa)                             |
|                    | Lớp bê tông bảo vệ                                    |
|                    | Mác bê tông                                           |
|                    | Khối lượng bê tông trong thiết kế (m³)                |
|                    | Cao độ sàn liên hợp                                   |
|                    | Chiều sâu                                             |
|                    | Chiều dài                                             |
|                    | Chiều rộng                                            |
|                    | Loại sàn                                              |
|                    | Loại cốt thép dưới bố trí theo phương dọc điển hình   |
|                    | Loại cốt thép trên bố trí theo phương dọc điển hình   |
|                    | Chỉ dẫn kỹ thuật                                      |
| Thông tin thi công | Bản vẽ thi công thực tế                               |
| Thông tin thi công | Cao độ sàn liên hợp thực tế                           |
| Thông tin thi công | Cường độ nén trung bình của bê tông sau 28 ngày (MPa) |
| Thông tin thi công | Mã số cấu kiện                                        |
| Thông tin thi công | Khối lượng bê tông thực tế (m³)                       |
| Thông tin thi công | Hồ sơ kiểm tra bê tông                                |
| Thông tin thi công | Hồ sơ thi công                                        |
| Thông tin thi công | Ngày đổ bê tông                                       |

## 9. Mặt đường- cầu

| Giai đoạn          | Tham số                                                |
|--------------------|--------------------------------------------------------|
| thiết kế           | Mã số cấu kiện                                         |
|                    | Độ bền nén thiết kế (MPa)                              |
|                    | Lớp bê tông bảo vệ                                     |
|                    | Mác bê tông                                            |
|                    | Chiều sâu                                              |
|                    | Chiều rộng                                             |
|                    | Chiều dài                                              |
|                    | Loại                                                   |
|                    | Chỉ dẫn kỹ thuật                                       |
|                    | Loại cốt thép dưới bố trí theo phương dọc điển hình    |
|                    | Loại cốt thép trên bố trí theo phương dọc điển hình    |
| Thông tin thi công | Bản vẽ thi công thực tế                                |
| Thông tin thi công | Cường độ nén trung bình của bê tông sau 28 ngày (MPa)  |
| Thông tin thi công | Cường độ nén trung bình sau 28 ngày của cấu kiện (MPa) |
| Thông tin thi công | Mã số cấu kiện                                         |
| Thông tin thi công | Hồ sơ kiểm tra bê tông                                 |
| Thông tin thi công | Hồ sơ thi công                                         |
| Thông tin thi công | Ngày đổ bê tông                                        |

## 10. Dầm Super T

| Giai đoạn                  | Tham số                                 |
|----------------------------|-----------------------------------------|
| Thông tin thiết kế         | Mã số cấu kiện                          |
| Thông tin thiết kế         | Độ bền nén thiết kế (MPa)               |
| Thông tin thiết kế         | Lớp bê tông bảo vệ                      |
| Thông tin thiết kế         | Mác bê tông                             |
| Thông tin thiết kế         | Chiều sâu                               |
| Thông tin thiết kế         | Chiều dài                               |
| Thông tin thiết kế         | Loại                                    |
| Thông tin thiết kế         | Khối lượng (Tấn)                        |
| Thông tin thiết kế         | Cường độ nén thiết kế của bê tông (MPa) |
| Thông tin thiết kế         | Chỉ dẫn kỹ thuật                        |
| Thông tin phục vụ sản xuất | Mã số cấu kiện                          |
| Thông tin phục vụ sản xuất | Số lượng                                |
| Thông tin phục vụ sản xuất | Cường độ nén của bê tông khi giao (MPa) |
| Thông tin phục vụ sản xuất | Phê duyệt cấp phối bê tông              |

|                    | Hồ sơ kiểm tra bê tông                                 |
|--------------------|--------------------------------------------------------|
|                    | Biểu đồ nhiệt độ trong quá trình đóng rắn              |
|                    | Ngày sản xuất                                          |
|                    | Bản vẽ sản xuất                                        |
|                    | Số lô sản xuất                                         |
|                    | Đơn vị sản xuất                                        |
|                    | Hồ sơ kiểm tra ứng suất                                |
| Thông tin thi công | Bản vẽ thi công thực tế                                |
| Thông tin thi công | Cường độ nén trung bình sau 28 ngày của cấu kiện (MPa) |
| Thông tin thi công | Cường độ nén trung bình của bê tông sau 28 ngày (MPa)  |
| Thông tin thi công | Mã số cấu kiện                                         |
| Thông tin thi công | Hồ sơ thi công                                         |