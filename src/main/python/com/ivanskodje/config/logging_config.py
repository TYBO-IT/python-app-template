import logging
import os

from com.ivanskodje.properties.application_properties import ApplicationProperties
from com.ivanskodje.properties.logging_properties import LoggingProperties


class LoggingConfig:

    logging_properties: LoggingProperties
    logger_properties: LoggingProperties

    def __init__(self, application_properties: ApplicationProperties) -> None:
        self._populate_local_variables(application_properties)
        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[
                self._file_handler(),
                self._file_error_handler(),
                self._console_handler()
            ]
        )

    def _populate_local_variables(self, application_properties: ApplicationProperties):
        app_name = application_properties.get_name()
        profile = application_properties.get_profile()
        self.formatter = logging.Formatter(
            f'%(asctime)s | {profile} | %(levelname)-8s | {app_name} | %(message)s'
        )

        logger_properties = application_properties.get_logging_properties()
        self.console_level = logger_properties.get_console_level()
        self.filename = f"{logger_properties.get_file_path()}/{logger_properties.get_file_name()}"
        self.file_level = logger_properties.get_file_level()

    def _console_handler(self):
        handler = logging.StreamHandler()
        handler.setFormatter(self.formatter)
        handler.setLevel(self.console_level)
        return handler

    def _file_handler(self):
        filename = f"{self.filename}.log"
        handler = logging.FileHandler(filename)
        handler.setFormatter(self.formatter)
        handler.setLevel(self.file_level)
        return handler

    def _file_error_handler(self):
        filename = f"{self.filename}.error.log"
        handler = logging.FileHandler(filename)
        handler.setFormatter(self.formatter)
        handler.setLevel(logging.ERROR)
        return handler
