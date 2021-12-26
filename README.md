# Dvor API

API for Dvor ("Двор") Project. 

> Damage to cultural property belonging to
any people whatsoever means damage to the
cultural heritage of all mankind, since each
people makes its contribution to the culture of
the world.

### Building

Prepare environment

```shell
python3 -m venv venv
```

```shell
source venv/bin/activate
```

```shell
pip3 install -r requirements.txt
```

Run server

```shell
./run_server.sh
```

Test server

```shell
pytest -v -s
```

API docs

```
GET $BASE_URL/docs

or

GET $BASE_URL/redoc
```

### Languages, libraries and tools used

* [python3](https://docs.python.org/3.9/)
* [FastAPI](https://fastapi.tiangolo.com)
* [uvicorn](https://github.com/encode/uvicorn)
* [pytest](https://docs.pytest.org/en/6.2.x/contents.html)
