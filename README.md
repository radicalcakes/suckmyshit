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

Database - redis

flask - `pip install flask`

redis - `pip install redis`

pillow - `pip install Pillow`

TODOs
--
 - Test crud for image
 - start thinking of thumbnail size and add thumbnail
 - use ajax to post images
 - explore foundation

Models
--
- id: hash of image id
- type: the mime type of the image request
- size: size of image in bytes
- url: url of the image to serve

GET (id)
```javascript
{
    "data": {
        "id": "vid23dflk",
        "type": "image/jpeg",
        "creation_date": datetime.utc.now(),
        "size": 521916,
        "url": "http://dumpon.us/vid23dflk.jpg"
    }
}
```

POST Parameters:
* image: A binary file, base64 data
* type: The type of the file that's being sent: file or base64
* name (optional): The name of the file, this is automatically detected if uploading a file with a POST and multipart / form-data

Tests
--
 - GET to the api gives the proper format and responses
 - POST to the api gives proper response
 - Hash function creates a truly unique image
 - 


Usage
--
