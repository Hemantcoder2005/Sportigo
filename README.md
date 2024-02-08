# Sportigo

### Sportigo is a web application designed to streamline sports equipment booking and availability tracking for college students. It aims to solve the common problem of students traveling to the sports block only to find their desired sport already taken. With Sportigo, students can check real-time availability, book equipment, and ensure the security of sports gear.

## Features

1. *Live Availability Tracking*:
   - Students can view the availability status of various sports and equipment online.
   - Real-time updates ensure accurate information.

2. *Equipment Booking*:
   - Users can reserve specific sports equipment through the platform.
   - Booking slots are time-bound to prevent conflicts.

3. *Secure Sign-Out Process*:
   - When returning equipment, students must sign out to verify the return.
   - This enhances security and accountability.

4.  *Making our own API*: 
   - We have created a custom API using JavaScript that interacts with Sqlite for data storage and to accept queries.

## Look at the Figma Design
``https://www.figma.com/file/tcvaxu6Qg2KwETBUb2CC9u/Hackathon?type=design&node-id=2-3&mode=design&t=uEbCvYsw7OpXXE68-0``


## Getting Started

Follow these steps to set up Sportigo locally:

1. *Clone the Repository*:
   
   git clone https://github.com/Hemantcoder2005/sportigo.git
   

2. *Install Dependencies*:
   
   ``pip install django``
   ``pip install django-browser-reload``
   
   

3. *Run the Application*:
   
   ``python manage.py runserver``
   
4. *Fake Login*:
-  Username: ``hemant2324``
-  Password:  ``sam``
## Tech Stack

- *Frontend*:
  - HTML, CSS, JavaScript
  - Django

- *Backend*:
  - Sqlite (for database)

- *Authentication & Authorization*:
  - Implementing  a custom user model for users and guard.

## Problems
- designing
- data gathering
- handling multiple types of facilities (like gym, swimming pool etc.)
- authentication system
- incorporating api into our code
- could not make interface for the guard 

## Future Goals
-  Improve UI/UX
-  Handling more than one type of facility
-  Making QR scanner accessible to make it easier to log in
-  Adding payment gateway integration

## Contributing

We welcome contributions! If you'd like to improve Sportigo, follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature-name.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature/your-feature-name.
5. Open a pull request.

## Team- ToteCodeKarenge
- Hemant Narula
- Gopal Tiwari
- Girik Aggarwal
- Aditya Verma
 
## Acknowledgments

- Inspired by the need to enhance sports facility management in colleges.
- Thanks to all contributors who make Sportigo better!



