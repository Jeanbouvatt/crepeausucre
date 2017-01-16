# Service s


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

    "Service": "Microservice s",
    "Version": "0.1"

}
```

## Request
GET /status

### Response

Return status 200 if user did not play, else 401

```json
{
    "msg":"ok"
}
```

