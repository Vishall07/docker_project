# Use official Nginx image as base
FROM nginx:alpine

# Copy static files to Nginx HTML folder
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
