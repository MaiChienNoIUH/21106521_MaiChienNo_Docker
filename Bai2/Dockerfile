# Sử dụng python:3.10 làm base image
FROM python:3.10

# Thiết lập thư mục làm việc trong container
WORKDIR /usr/src/app

# Sao chép tệp requirements.txt vào container
COPY requirements.txt ./

# Cài đặt các dependencies từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Mở cổng 5000
EXPOSE 5000

# Chạy ứng dụng Flask
CMD ["python", "app.py"]
