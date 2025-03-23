# Sử dụng image Python làm base image
FROM python:3.10-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép mã nguồn vào container
COPY app.py .

# Thiết lập biến môi trường APP_ENV với giá trị mặc định là 'development'
ENV APP_ENV=development

# Chạy ứng dụng Python
CMD ["python", "app.py"]
