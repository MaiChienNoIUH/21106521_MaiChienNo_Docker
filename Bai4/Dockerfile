# Sử dụng Nginx làm base image
FROM nginx:latest

# Sao chép tệp index.html vào thư mục chứa các tệp web của Nginx
COPY index.html /usr/share/nginx/html/

# Expose cổng 80 để người dùng có thể truy cập trang web
EXPOSE 80

# Nginx sẽ tự động chạy khi container được khởi động
CMD ["nginx", "-g", "daemon off;"]
