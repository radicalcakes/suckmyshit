Dumpon.us
==

Simple image uploader

Methods for interacting with the api:

| HTTP method       | URI       | Action  |
| ------------- |:-------------:| -----:|
| GET     | http://dumpon.us/api/images | Retrieve list of images |
| GET     | http://dumpon.us/api/images/{id} | Retrieve an individual image |
| POST   | http://dumpon.us/api/images | Add an image 


Requirements
--

`pip install -r requirements.txt`

TODOs
--
 - Test crud for image
 - start thinking of thumbnail size and add thumbnail
 - use ajax to post images
 - explore foundation

Models
--

GET (id)
```javascript
{

  'data':  {
            "id": "vid23dflk",
            "title": "Monkey Socks",
            "type": "image/jpeg",
            "creation_date": "2014-04-09 19:31:53.355174",
            "size": 521916,
            "url": "http://dumpon.us/imgs/vid23dflk.jpg"
    },
    'status': 200
}
```

GET /api/images

```javascript
{
    'data': [
        {
            "id": "vid23dflk",
            "title": "Monkey Socks",
            "type": "image/jpeg",
            "creation_date": "2014-04-09 19:31:53.355174",
            "size": 521916,
            "url": "http://dumpon.us/imgs/vid23dflk.jpg"
        },
        {
            "id": "vid23dflk",
            "title": "Monkey Socks",
            "type": "image/jpeg",
            "creation_date": "2014-04-09 19:31:53.355174",
            "size": 521916,
            "url": "http://dumpon.us/imgs/vid23dflk.jpg"
      },
    ]
}

```

POST Parameters:
* image: A binary file, base64 data
* size: Size of the bin file
* type: The type of the file that's being sent: file or base64
* name (optional): The name of the file, this is automatically detected if uploading a file with a POST 
* title (optional): Title of the upload

Tests
--
 - GET to the api gives the proper format and responses
 - POST to the api gives proper response
 - Hash function creates a truly unique image
 - 


Usage
--

- GET /api/images/<image_id> - `curl -i -H "Accept: application/json" "localhost:5000/api/images/123"`

- GET /api/images - `curl -i -H "Accept: application/json" "localhost:5000/api/images"`


