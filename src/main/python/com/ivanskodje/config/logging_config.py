import logging
import os

from com.ivanskodje.properties.application_properties import ApplicationProperties
from com.ivanskodje.properties.logging_properties import LoggingProperties


class LoggingConfig:

    def __init__(self, application_properties: ApplicationProperties) -> None:
        logger_properties: LoggingProperties = application_properties.get_logging_properties()

        profile = application_properties.get_profile()
        log_formatter = logging.Formatter(
            f'%(asctime)s | {profile} | %(levelname)-8s | {application_properties.get_name()} | %(message)s')

        file_name = f"{logger_properties.get_file_path()}/{logger_properties.get_file_name()}.log"
        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(self._get_log_level(
            logger_properties.get_file_level()))

        file_name = f"{logger_properties.get_file_path()}/{logger_properties.get_file_name()}.error.log"
        file_error_handler = logging.FileHandler(file_name)
        file_error_handler.setFormatter(log_formatter)
        file_error_handler.setLevel(logging.ERROR)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        console_handler.setLevel(self._get_log_level(
            logger_properties.get_console_level()))

        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[file_handler, file_error_handler, console_handler]
        )

    def _get_log_level(self, logging_level):
        if(logging_level is None):
            print("No logging level set in application.yml, setting default to INFO")
            return logging.INFO

        match (logging_level.upper()):
            case "DEBUG":
                return logging.DEBUG
            case "INFO":
                return logging.INFO
            case "ERROR":
                return logging.ERROR
            case "WARN":
                return logging.WARN
            case "CRITICAL":
                return logging.CRITICAL
            case "NONE":
                return logging.NOTSET
            case default:
                raise Exception("Invalid logging level loaded from properties")
