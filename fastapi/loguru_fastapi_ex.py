import logging
import sys
from pprint import pformat

from fastapi import FastAPI
from loguru import logger
from loguru._defaults import LOGURU_FORMAT
from starlette.requests import Request
import uvicorn


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where logged message originated
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def format_record(record: dict) -> str:
    """
    Custom format for loguru loggers.
    Uses pformat for log any data like request/response body during debug.
    Works with logging if using loguru handler.

    Example:
    >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
    >>> logger.bind(payload=).debug("users payload")
    >>> [   {   'count': 2,
    >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
    >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
    """
    format_string = LOGURU_FORMAT

    if record["extra"].get("payload") is not None:
        record["extra"]["payload"] = pformat(
            record["extra"]["payload"], indent=4, compact=True, width=88
        )
        format_string += "\n<level>{extra[payload]}</level>"

    format_string += "{exception}\n"
    return format_string


app = FastAPI(title="Logger Handler", debug=True)

# set loguru format for root logger
logging.getLogger().handlers = [InterceptHandler()]

# set format
logger.configure(
    handlers=[{"sink": "myfile.log", "level": logging.DEBUG, "format": format_record}]
)

# Also set loguru handler for uvicorn loger.

logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]


@logger.catch  # to catch any exceptions in the function
@app.get("/")
def index(request: Request) -> None:
    logger.info("loguru log")
    logging.info("logging log")
    logging.getLogger("fastapi").debug("fastapi info log")
    logger.bind(payload=dict(request.query_params)).debug("params with formating")
    return None


# code adapted from: https://github.com/tiangolo/fastapi/issues/1276
# see also: https://medium.com/1mgofficial/how-to-override-uvicorn-logger-in-fastapi-using-loguru-124133cdcd4e


if __name__ == "__main__":
    uvicorn.run("loguru_fastapi_ex:app", debug=True, reload=True)
