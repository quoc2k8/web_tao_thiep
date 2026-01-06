# web_tao_thiep
phát triển trang web tạo thiệp bằng django

file thiep_chuc là file tự code, chạy được

file web_chuc là file AI hỗ trợ làm, vẫn cần cấu hình để chạy được

# Hướng dẫn nhanh chạy dự án Django

## 1. Chuẩn bị môi trường

```bash
# Kiểm tra Python
python --version
```

# Tạo môi trường ảo
```
python -m venv venv
```

# Kích hoạt môi trường
# Windows
```
venv\Scripts\activate
```
# macOS / Linux
```
source venv/bin/activate
```
## 2. Cài đặt thư viện
```
pip install -r requirements.txt
```
## 3. Thiết lập cơ sở dữ liệu
### Tạo migrations cho app mới
```
python manage.py makemigrations
```
### Tạo bảng cơ sở dữ liệu
```
python manage.py migrate
```
### Tạo tài khoản quản trị (tùy chọn)
```
python manage.py createsuperuser 
```
## 4. Chạy dự án
```
python manage.py runserver
```
Mở trình duyệt và truy cập: http://127.0.0.1:8000
