### Technologies Used:

- Django
- Celery
- Docker
- Docker Compose

### Purpose:

The purpose is to create a page for people to apply for loans from LFG_BANK. The page should be available at localhost:9000. The admin page is at :8080.

The aim is to develop a page to allow users to apply for loans from LFG_BANK. The page will be accessible at localhost:9000. In addition, the admin page can be accessed at :8080.

### Docker Architecture:

- db Container: it's the database.
- flower Container: where you have access to the Celery graphical interface to check if the asynchronous processes have been completed.
- lfg-bank Container: where Django is located.
- lfg-background Container: where the Celery logs are.
- broker Container: where RabbitMQ is.
