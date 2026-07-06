# Social Media REST API

**Student:** Gabriele Moschella  
**Project Type:** REST API  
**Framework used:** Django REST Framework

This application implements the backend (RESTful API) of a social network. It allows user to register, 
authenticate by JWT, publish contents (posts), interact via likes and comments and with other users following them. 
It also includes a private chat between users and a sistem of privileges based on the role of the user.

---

## Features

### Guest (Unauthenticated)
* **Sign up:** Creation of a new user profile.
* **Public access:** Visualization of the general feed (all post).
* **Consultation:** Visualization in detail of a specific post.

### User (Authenticated)
* **Authentication:** Login, refresh of token and logout.
* **Profile management:** Modification of user data.
* **Content Management (CRUD):** Creating posts, editing, and deleting them.
* **Interactions:** Add/remove comments and like to post.
* **Follow interactions:** Follow/unfollow other users.
* **Timeline (custom feed):** Visualization of a custom feed that contains only posts published by followed users.
* **Chat:** Send private messages to other users and view chat history.

### Moderator 
* **All the features of the standard User.**
* **Content moderation:** Deletion of any post or comment in the system.
* **User management (Ban):** Blocking/unlocking user accounts.

---

## Local installation instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gabriele04/social_api_project
   cd social_api_project
   ```
2. **Create virtual environment and activate it:**
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate
   # Linux/Mac: source venv/bin/activate
   ```
3. **Install dependencies and apply migrations:**
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```
4. **Start local server:**
   ```bash
   python manage.py runserver
   ```
The API will be available at: `http://127.0.0.1:8000/`

## Database and demo data
This project includes the database file SQLite preconfigured: `db.sqlite3`

---

## Database and demo data

The project includes a preconfigured SQLite database file: **db.sqlite3**.
the database already contains sample data (Demo Data), including posts, comments, follow relationships, and chat history, for easy testing.

### Demo accounts

| Username     | Password     | Role          | Description                                        |
|--------------|--------------|---------------|----------------------------------------------------|
| `mod_demo`   | `mod12345`   | **Moderator** | User Moderator to test blocks and global deletion. |
| `user_demo`  | `user12345`  | **User**      | Standard user with preloaded data and posts.       |
| `user2_demo` | `user212345` | **User**      | Standard user with preloaded data and posts.       |

---

## Online deployment link
**URL:** https://social-api-project-5yqu.onrender.com

---

## Main endpoints table

*Note: `Authorization: Bearer <access_token>` it's required for all endpoints where "Auth" is "Yes".*
*Note: `Role` indicates the user that can do that action (any or only the author for action like delete or modify). `Role: Mod` is present in every endpoint so is omitted.*


| Method     | Name                 | URL                         | Auth | Role   | Request Body                                                                                  | Response Example                                                                                                                                                                               | Description                                          |
|------------|----------------------|-----------------------------|------|--------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| **POST**   | **Signup**           | `/api/auth/signup/`         | No   | Any    | `{"username": "user", "password": "1234", "email": "...", "bio": "...", "occupation": "..."}` | `{ "id": 1, "username": "user", "email": "...", "role": "user", "bio": "...", "occupation": "..." }`                                                                                           | Registration (create user)                           |
| **POST**   | **Login**            | `/api/auth/login/`          | No   | Any    | `{"username": "user", "password": "1234"}`                                                    | `{"refresh": "...", "access": "..."}`                                                                                                                                                          | Get token JWT.                                       |
| **POST**   | **Refresh Token**    | `/api/auth/token/refresh/`  | No   | Any    | `{"refresh": "..."}`                                                                          | `{"access": "..."}`                                                                                                                                                                            | Refresh your token JWT.                              |
| **GET**    | **Get User Profile** | `/api/auth/<username>`      | Yes  | Any    | *N/A*                                                                                         | `{ "id": 1, "username": "user", "bio": "...", "occupation": "..." }`                                                                                                                           | Get user information                                 |
| **PATCH**  | **Update profile**   | `/api/auth/update/`         | Yes  | Any    | `{ "username": "user", "email": "", "bio": "...", "occupation": "..." }`                      | `{ "username": "user", "email": "", "bio": "...", "occupation": "..." }`                                                                                                                       | Modify your user information                         |
| **POST**   | **Follow User**      | `/api/auth/users/2/follow/` | Yes  | Any    | *N/A*                                                                                         | `{"message": "started to follow user"}`                                                                                                                                                        | Follow/unfollow a user                               |
| **POST**   | **Block User**       | `/api/auth/users/2/block/`  | Yes  | Mod    | *N/A*                                                                                         | `{"message": "user unblocked"}`                                                                                                                                                                | Block/unblock a user                                 |
| **POST**   | **Logout**           | `/api/auth/logout/`         | Yes  | Any    | `{ "refresh": "..."}`                                                                         | `{"message": "logout successfull"}`                                                                                                                                                            | Logout (blacklist refresh token)                     |
| **POST**   | **Create Post**      | `/api/posts/`               | Yes  | Any    | `{ "title": "...", "description": "...", "media_url": "..." }`                                | `{ "id": 1, "author": 1, "author_username": "user", "title": "...", "description": "...", "media_url": "...", "created_at": "...", "updated_at": "...", "likes": 0, "comments": [] }`          | Create a post                                        |
| **PATCH**  | **Update Post**      | `/api/posts/1/`             | Yes  | Author | `{ "title": "...", "description": "...", "media_url": "..." }`                                | `{ "id": 1, "author": 1, "author_username": "user", "title": "...", "description": "...", "media_url": "...", "created_at": "...", "updated_at": "...", "likes": 0, "comments": [...] }`       | Modify a post                                        |
| **DELETE** | **Delte Post**       | `/api/posts/1/`             | Yes  | Author | *N/A*                                                                                         | *N/A*                                                                                                                                                                                          | Delete a post                                        |
| **GET**    | **Post Detail**      | `/api/posts/1/`             | No   | Any    | *N/A*                                                                                         | `{ "id": 1, "author": 1, "author_username": "user", "title": "...", "description": "...", "media_url": "...", "created_at": "...", "updated_at": "...", "likes": 0, "comments": [...] }`       | Retrieve single post informations                    |
| **GET**    | **General Feed**     | `/api/posts/`               | No   | Any    | *N/A*                                                                                         | `[{ "id": 1, "author": 1, "author_username": "user", "title": "...", "description": "...", "media_url": "...", "created_at": "...", "updated_at": "...", "likes": 0, "comments": [...] } ...]` | Retrieve all posts informations                      |
| **GET**    | **Custom Feed**      | `/api/posts/feed/`          | Yes  | Any    | *N/A*                                                                                         | `[{ "id": 1, "author": 1, "author_username": "user", "title": "...", "description": "...", "media_url": "...", "created_at": "...", "updated_at": "...", "likes": 0, "comments": [...] } ...]` | Retrieve posts informations based on user you follow |
| **POST**   | **Toogle Like**      | `/api/posts/1/like/`        | Yes  | Any    | *N/A*                                                                                         | `{ "message": "like added"}`                                                                                                                                                                   | Add/remove like to a post                            |
| **POST**   | **Create Comment**   | `/api/posts/1/comment/`     | Yes  | Any    | `{ "body": "..."}`                                                                            | `{ "id": 1, "post": 1, "author": 1, "author_username": "user", "body": "...", "created_at": "..." }`                                                                                           | Create a comment on a post                           |
| **GET**    | **Get Comment**      | `/api/posts/1/comment/1/`   | No   | Any    | *N/A*                                                                                         | `{ "id": 1, "post": 1, "author": 1, "author_username": "user", "body": "...", "created_at": "..." }`                                                                                           | Get comment information                              |
| **DELETE** | **Delete Comment**   | `/api/posts/1/comment/1/`   | Yes  | Author | *N/A*                                                                                         | *N/A*                                                                                                                                                                                          | Delete a comment                                     |
| **POST**   | **Send Message**     | `/api/chats/send/1/`        | Yes  | Any    | `{ "body": "..."}`                                                                            | `{ "id": 1, "sender": 1, "sender_username": "user", "receiver": 2, "receiver_username": "user2", "body": "...", "sent_at": "..." }`                                                            | Send a message to a user                             |
| **GET**    | **History Chat**     | `/api/chats/history/1/`     | Yes  | Any    | *N/A*                                                                                         | `[ { "id": 3, "sender": 5, "sender_username": "user_demo", "receiver": 8, "receiver_username": "user2", "body": "messaggione", "sent_at": "2026-07-06T14:40:09.253586Z" } ..]`                 | Retrieve the message history with a user             |



---

## Testing workflow and scenario (Postman)

In the project is included a Postman Collection `Social_Media_API.postman_collection.json`, which serves as a minimally documented client. To test, import the file into Postman and follow the scenario:

### 1. Login e setup
Do the **Login** with the `user_demo` credentials. Copy the `access` token value returned from the response and set it as the `Bearer Token` for subsequent requests.

### 2. Call public endpoint
Do the `GET` **General Feed** request (`/api/posts/`). It's a public endpoint so the server will return the list of posts without requiring any authorization.

### 3. Call authenticated endpoint
Do the `GET` **Custom Feed** request (`/api/posts/feed/`). The server will check the `user_demo` JWT token and return only posts created by users that he follow.

### 4. Create, update, delete data (CRUD)
* **Create:** Do a `POST` to `/api/posts/`, sending a JSON with `"title"` and `"description"` fields. The server will respond with *201 Created*.
* **Update:** Note the ID of the post you just created. Do the `PATCH` request to the URL `/api/posts/<id>/`, modifying the description/title. The server will save the change (*200 OK*).
* **Delete:** Do the `DELETE` request to the same URL. The post will be removed (*200 OK*).

### 5. Test forbidden action
The app also verify and blocks unauthorized actions (403 Forbidden).
* **Action:** Using the token of a standard user like `user_demo`, try performing an action that only moderators can do like the `POST` on `/api/auth/users/1/block/` that block a user.
* **Result:** The API will block the request, returning the status code **403 Forbidden** and the error message: `"you don't have moderator permissions"`


