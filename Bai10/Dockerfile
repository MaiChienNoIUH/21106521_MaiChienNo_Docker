# Sử dụng php:8.2-apache làm base image
FROM php:8.2-apache

# Cài đặt bất kỳ extension PHP nào nếu cần
# Ví dụ: Cài đặt mysqli
RUN docker-php-ext-install mysqli

# Tạo thư mục trong container để mount mã nguồn
RUN mkdir /var/www/html/src

# Thiết lập Apache để phục vụ ứng dụng PHP
COPY ./src /var/www/html/

# Mở cổng 80
EXPOSE 80
