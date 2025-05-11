# 🐦 Mini Twitter Web App

A simple Twitter-like web application built using **Django**, where users can **register**, **log in**, and **post tweets with photos**. Users can also **edit** and **delete** their own tweets.

## 🚀 Features

- 🔐 User Registration and Authentication (Login/Logout)
- 📝 Create Tweets with Optional Photo Upload
- 🧾 Edit and Delete Your Own Tweets
- 🖼️ Image Upload Support for Tweets
- 🔍 Responsive and Minimal UI (Bootstrap-based)

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django DB)
- **Media Storage:** Local file storage for uploaded images

## 📸 Screenshots



## 🧑‍💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ab-malek/Twitter-app.git
cd chaiheadq
```
### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate

```

### 6. Run the Development Server

```bash
python manage.py runserver

```
Visit http://127.0.0.1:8000 in your browser.

## ⚙️ Configuration

Uploaded images are stored in the media/ folder.
Update MEDIA_URL and MEDIA_ROOT in settings.py if deploying to production.

##📌 TODO / Future Improvements
Like/Retweet Functionality

Follow/Unfollow System

Comments on Tweets

Pagination

Profile Page with User Bio



















