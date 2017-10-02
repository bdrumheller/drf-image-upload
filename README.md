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

## Sample GET request
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "58bf512a-4a9b-492c-85af-58bc85344a83",
            "description": "Cool Animal Pics",
            "url": "https://drive.google.com/uc?export=download&id=0BzBCYWjiwiObUk9idGNjT3QzQkE",
            "images": [
                {
                    "id": "04e6ee37-20ee-4920-8155-9bc8cfcff6b6",
                    "image": {
                        "thumbnail": "http://127.0.0.1:8000/images/__sized__/39/95/06/15/5c/d8/4f/d0/9e/b2/ae/95/1e/e5/19/ac/doge-thumbnail-100x100-70.jpg",
                        "full_size": "http://127.0.0.1:8000/images/39/95/06/15/5c/d8/4f/d0/9e/b2/ae/95/1e/e5/19/ac/doge.jpg"
                    }
                },
                {
                    "id": "581ad6f1-be89-4c03-a5d9-86318f18af7c",
                    "image": {
                        "thumbnail": "http://127.0.0.1:8000/images/__sized__/52/56/8e/ed/cf/2c/48/33/be/e6/da/3d/ab/0c/f4/b4/panda-thumbnail-100x100-70.jpg",
                        "full_size": "http://127.0.0.1:8000/images/52/56/8e/ed/cf/2c/48/33/be/e6/da/3d/ab/0c/f4/b4/panda.jpg"
                    }
                },
                {
                    "id": "ccb0c22d-3ddf-45ec-9e06-e3a88277c769",
                    "image": {
                        "thumbnail": "http://127.0.0.1:8000/images/__sized__/30/57/e9/26/c0/b2/4e/e7/b0/76/56/0c/14/91/c0/c7/h9tiwncjw9pz-thumbnail-100x100-70.jpg",
                        "full_size": "http://127.0.0.1:8000/images/30/57/e9/26/c0/b2/4e/e7/b0/76/56/0c/14/91/c0/c7/h9tiwncjw9pz.jpg"
                    }
                }
            ]
        }
    ]
}
```

## Customizations
Images are viewable in the browser at `http://127.0.0.1:8000/images/`. Image files are stored locally in the `media_root` directory. The `media_root` and image sizes are configurable in `settings.py` in the `MEDIA_ROOT` and `VERSATILEIMAGEFIELD_RENDITION_KEY_SETS` respectively.
