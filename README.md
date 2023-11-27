# Django dynamic models
## 1.  Install requirements
Install project dependencies by command:

    pip install -r requirements/base.txt

## 2. Setup environment variables
Make a copy of `.envfile` and rename it to `.env` 
Then make important changes, set database variables and other things.
For `DJANGO_SETTINGS_MODULE` variable, you can write:
`core/settings/development` or `core/settings/production`

## 3. Make migrations
Make migrations to create tables in database:

    python manage.py makemigrations
    python manage.py migrate

## 4. Usage
Send CSV file to the `BASE_URL/common/upload/` api, use argument `file` in request data:

![enter image description here](https://i.ibb.co/F7h7rzM/Screenshot-from-2023-11-27-19-56-00.png)

It generates dynamic model if your csv file is valid, otherwise it returns error
Successful response would be like:

![enter image description here](https://i.ibb.co/9G5fL6h/Screenshot-from-2023-11-27-20-00-14.png)

It returns the name of the table so you can check it from database:

![enter image description here](https://i.ibb.co/M864sRk/Screenshot-from-2023-11-27-20-02-39.png)
As you can see it created table from your csv file.

## Feel free to contribute!

