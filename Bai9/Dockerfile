# Sử dụng redis:latest làm base image
FROM redis:latest

# Sao chép tệp redis.conf vào container
COPY redis.conf /usr/local/etc/redis/redis.conf

# Cấu hình Redis sử dụng tệp cấu hình tùy chỉnh
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
