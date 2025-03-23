# Sử dụng Golang base image để build ứng dụng
FROM golang:1.18-alpine AS builder

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các tệp Go vào container
COPY . .

# Build ứng dụng Go
RUN go build -o main .

# Tạo image cho ứng dụng sản phẩm cuối cùng, sử dụng một image nhẹ hơn
FROM alpine:latest

# Cài đặt các thư viện cần thiết để chạy ứng dụng Go
RUN apk --no-cache add ca-certificates

# Sao chép ứng dụng đã build từ container builder
COPY --from=builder /app/main /main

# Expose port 8080 để truy cập ứng dụng
EXPOSE 8080

# Chạy ứng dụng Go
CMD ["/main"]
