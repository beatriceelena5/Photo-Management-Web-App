# Photo-Management-Web-App

A web-based photo management app built with Python and Flask, allowing admins to securely upload, organize, and display images in a categorized gallery with thumbnail views and detailed descriptions.

## Features

- **Authentication**: Admin login with permissions for uploading and deleting images.
- **Image Upload**: Upload images across categories, with options to add names and descriptions.
- **Image Gallery**: Displays uploaded images as thumbnails organized by category, with options to view full-size images.
- **About Page**: Displays information about the site admin.
- **Image Deletion**: Enables admins to delete uploaded images.

## Project Structure

- **app.py**: The main Flask app code, defining routes and application logic.
  - **Key Routes**:
    - `/`: Homepage displaying the image gallery.
    - `/login`: Admin login page.
    - `/upload`: Enables image uploads (admin only).
    - `/delete/<category>/<filename>`: Allows image deletion (admin only).
    - `/logout`: Logs the user out.
    - `/about`: "About" page with admin information.
  - **allowed_file(filename)** function: Checks if the uploaded file has an allowed extension.
  - **create_thumbnail(image_path)** function: Generates a thumbnail of the uploaded image.
- **Dockerfile**: Configuration for containerizing the app with Docker.
- **requirements.txt**: Lists required Python dependencies.
- **templates/**: Directory containing Jinja2 HTML templates.
- **static/**: Directory for static files (CSS, uploaded images).
- **metadata/**: Directory containing JSON metadata for images.

The app dynamically generates HTML pages using Jinja2 and leverages the Bootstrap framework for styling. Images and metadata are stored in the server's file system.

## Challenges

- **Error Handling**: Managed potential issues during image upload and deletion.
- **Thumbnail Creation**: Configured the Pillow library to support thumbnail generation.

## Login Credentials

- **Username**: admin
- **Password**: password
