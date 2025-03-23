# Stage 1: Build ứng dụng Node.js
FROM node:18 AS builder

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép package.json và package-lock.json để cài đặt dependencies
COPY package*.json ./

# Cài đặt dependencies
RUN npm install

# Sao chép mã nguồn vào container
COPY . .

# Build ứng dụng (nếu cần, ví dụ: nếu bạn sử dụng TypeScript, bạn có thể biên dịch ở đây)
RUN npm run build

# Stage 2: Chạy ứng dụng với image nhỏ gọn hơn
FROM node:18-alpine

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép các tệp đã build từ Stage 1 vào container
COPY --from=builder /app /app

# Cài đặt dependencies cho ứng dụng trong môi trường sản xuất
RUN npm install --production

# Expose port mà ứng dụng sẽ lắng nghe
EXPOSE 3000

# Chạy ứng dụng Node.js
CMD ["npm", "start"]
