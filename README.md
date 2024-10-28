# Photo-Management-Web-App
A web-based photo management app built with Python and Flask, enabling admins to securely upload, organize, and display images in a categorized gallery with thumbnail views and detailed descriptions.

This web-based photo management app allows the admin to upload, organize, and display images in a user-friendly gallery. Built using Python and Flask, the application features authentication, image uploading, and thumbnail display.

Features:

Authentication: Allows the admin to log in with permissions for uploading and deleting images.
Image Upload: The admin can upload images across different categories and add names and descriptions to each.
Image Gallery: Displays uploaded images as thumbnails organized by category. Each thumbnail can be opened to view the full-size image.
About Page: A page with information about the site admin.
Image Deletion: The admin can delete uploaded images.
Project Structure

app.py: The main Flask app code, defining routes and application logic.
Key Routes:
/: Displays the homepage with the image gallery.
/login: Allows admin login.
/upload: Enables image uploads (admin only).
/delete/<category>/<filename>: Allows image deletion (admin only).
/logout: Logs the user out.
/about: Displays the "About" page.
allowed_file(filename) function: Checks if the uploaded file has an allowed extension.
create_thumbnail(image_path) function: Generates a thumbnail of the uploaded image.
Dockerfile: Configuration for containerizing the app with Docker.
requirements.txt: List of required Python dependencies.
templates/: Directory containing Jinja2 HTML templates.
static/: Directory for static files (CSS, uploaded images).
metadata/: Directory containing JSON metadata for images.
The app dynamically generates HTML pages using Jinja2 and uses the Bootstrap framework for styling. Images and metadata are stored in the server's file system.

Challenges

Error Handling: Special attention was required to manage errors during image upload and deletion.
Thumbnail Creation: Configuring the Pillow library correctly was essential for implementing the thumbnail generation function.
Login Credentials:

Username: admin
Password: password
