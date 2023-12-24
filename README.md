
# DjangoChat Application

DjangoChat is a simple Django-based web application that allows users to join chat rooms, communicate with others, and have real-time conversations.

## Installation

Follow these steps to set up the DjangoChat application on your local machine:

1. Clone the repository:

    ```bash
    git clone https://github.com/amitpanwar789/djangoChat
    cd djangoChat
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

4. Start the development server:

    ```bash
    python3 manage.py runserver
    ```

5. Open your web browser and go to [http://localhost:8000](http://localhost:8000).

## Usage

1. Once the server is running, navigate to [http://localhost:8000](http://localhost:8000) in your web browser.

2. You will be directed to the login or signup page. If you don't have an account, sign up.

3. After logging in or signing up, you will be redirected to the main chat interface.

4. Create or join a chat room by entering the room name or selecting an existing room.

5. Start chatting with other users in real-time.

