# Service i

The purpose of this service is to define if the player win something.
A price is ramdomly selected, and an image is generated with the id of the player.
The ourput is a json with the price and the image data.

## Dependencies

- Python 3
- Flask (python3-flask)
- Sqlite

## Configuration file

```
[i]
port=8090
debug=False
```

* Port: Tcp port number used by the server.
* debug: Add information to log file to debug the app.

## API

### Request
GET /

### Response

Return service name and version

```json
{

    "Service": "Microservice i",
    "Version": "0.1"

}
```

## Request
GET /login/id

### Response

Return status 200 if authenticated user, else 401

```json
{
    "msg":"ok"
}
```

