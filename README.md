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


### Administration Panel Pages

- To access Celery, use:
```bash
http://localhost:5555/
```

- To access RabbitMQ, use:
```bash
http://localhost:15672/
```

- To access Django Admin, use:
```bash
http://localhost:8000/
```
There are:

- Proposals:

```bash
http://0.0.0.0:8000/admin/core/proposal/
```

- Configuration by fields:

```bash
http://0.0.0.0:8000/admin/core/configurablefields/
```
On the configuration by fields page, it is possible to choose which fields will be requested in the form.
