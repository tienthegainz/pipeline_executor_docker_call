# FastAPI Boilerplate

A template to start on FastAPI backend projects.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You'll need `python@3.8`, `docker` and `pydocker` installed on your system to run the project.

### Installing

Run the following command to install all the project dependencies.
```shell script
# TODO
```

### Running

After all the above mentioned steps, you can start the application using the following command:
```shell script
python -m app.main
```
or
```shell script
uvicorn --host 0.0.0.0 --port 8000 --workers 4 app:app
```
The application will be available at https://localhost:8000.

## Development

These instructions will provide you some useful information on developing this application.

## Testing

The application unit tests are inside the `app/tests` module.

Run the following command in the terminal to execute the application unit tests.
```shell script
pytest app/tests
```

## Deployment

The application can be deployed in production using `gunicorn`, you don't need to make any code changes for the same.
Head over to the [Uvicorn Deployment](https://www.uvicorn.org/deployment/) documentation for complete instructions.

## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The API framework used

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
