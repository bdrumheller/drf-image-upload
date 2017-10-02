# Django Rest Framework (DRF) Versatile Image Upload 
Upload images to a Django Rest endpoint by providing a public zip file url. From this image, create images of multiple sizes 
using [VersatileImageField](http://django-versatileimagefield.readthedocs.io/en/latest/overview.html).

## Initialize a Postgres Database and User 
Install [postgresql](https://www.postgresql.org/). As the postgres user run the following commands. The username and password provided match those in `api.env`.
```bash
  createuser -SdR image_user
  psql -c "ALTER ROLE image_user WITH PASSWORD 'image_password'"
  createdb image_db -O image_user
  ```

## Install required Python Packages
```bash
TODO (add requirements.py)
```

## Migrate the data model
```python
python3 manage.py migrate
```

## Start the API
```python
python3 manage.py runserver
```

## POST to the endpoint
Once the API has been started, you can send a `POST` request to the endpoint located at `http://127.0.0.1:8000/images/`.

For example:
```json
{
	"description" : "Cool Animal Pics",
	"url" : "https://drive.google.com/uc?export=download&id=0BzBCYWjiwiObUk9idGNjT3QzQkE"
}
```

## Customizations
Images are viewable in the browser at `http://127.0.0.1:8000/images/`. Image files are stored locally in the `media_root` directory. The `media_root` and image sizes are configurable in `settings.py` in the `MEDIA_ROOT` and `VERSATILEIMAGEFIELD_RENDITION_KEY_SETS` respectively.
