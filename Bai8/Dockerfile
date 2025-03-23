# Sử dụng postgres:15 làm base image
FROM postgres:15

# Sao chép tệp SQL vào thư mục /docker-entrypoint-initdb.d/
# PostgreSQL tự động thực thi tất cả các tệp SQL trong thư mục này khi container khởi động lần đầu tiên
COPY init.sql /docker-entrypoint-initdb.d/

# Thiết lập biến môi trường nếu cần
ENV POSTGRES_USER=my_user
ENV POSTGRES_PASSWORD=my_password
ENV POSTGRES_DB=my_database
