# List of Models

- Product
    - Product Name
    - Price
    - Category
    - Tags
    - Published by
- Order
    - Product (OneToOne)
    - User (ForeignKey)
    - status (Ordered, In Progress, Arrived, Cancelled)
- User
    - Username (Email)
- Profile
    - Profile Image
    - Thumbnail
    - User
- Tag
    - Name

# Actions
    
- Product
    - Add
    - Delete
    - Update
- Order
    - Product
    - User
- User
    - Registrate
    - Update
    - Delete account


Libraries that are being used in the project are,
* djoser
* pillow
* django-cors-headers
* stripe
