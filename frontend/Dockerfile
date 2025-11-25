# Use Nginx image
FROM nginx:latest

# Remove default Nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy your frontend files into Nginx web directory
COPY . /usr/share/nginx/html/

# Expose port 80 for Nginx
EXPOSE 80

# Nginx runs automatically via ENTRYPOINT
