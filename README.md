# Django Art Museum Website

This project is a Django-based website for stock art, where users can browse, search, and download high-quality images for their projects. 

## Screenshots

<img width="1496" alt="Screenshot 2024-03-16 at 8 20 35 PM" src="https://github.com/ameyagidh/DjangoArtMuseumWebsite/assets/65457905/55f7b55a-a26b-437d-b49d-446b73245b54">
<img width="1496" alt="Screenshot 2024-03-16 at 8 20 28 PM" src="https://github.com/ameyagidh/DjangoArtMuseumWebsite/assets/65457905/3b266f1f-4042-4a5c-8965-d4824777de8b">
<img width="1496" alt="Screenshot 2024-03-16 at 8 20 19 PM" src="https://github.com/ameyagidh/DjangoArtMuseumWebsite/assets/65457905/ba6812ee-d4ee-4e30-bcc5-5da7d7cf1827">
<img width="1496" alt="Screenshot 2024-03-16 at 8 20 09 PM" src="https://github.com/ameyagidh/DjangoArtMuseumWebsite/assets/65457905/3183a620-c85e-40de-b4c7-1cdabe986e8d">


## Features

- **User Authentication**: Users can register, log in, and log out.
- **Image Upload**: Admin users can upload new images to the platform.
- **Search**: Users can search for images based on keywords.
- **Categories**: Images are organized into categories for easier browsing.
- **Download**: Users can download images they like.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/ameyagidh/DjangoArtMuseumWebsite.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the admin interface:
   ```
   http://127.0.0.1:8000/admin/
   ```

7. Log in with the superuser credentials created in step 4.

## Usage

- **Browse Images**: Visit the homepage to browse available images.
- **Search**: Use the search bar to find images based on keywords.
- **Download**: Click on an image to view details and download it.
- **Admin Panel**: Access the admin panel to upload new images and manage existing ones.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
This project was created by [Your Name]. Special thanks to [anyone you want to credit].
