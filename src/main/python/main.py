from getopt import getopt
import logging
import os
import sys

from dotenv import find_dotenv, load_dotenv

from com.ivanskodje.properties.application_properties import ApplicationProperties
from com.ivanskodje.config.logging_config import LoggingConfig


class Main:
    application_properties : ApplicationProperties
    logging_config : LoggingConfig

    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.application_properties = ApplicationProperties()
        self.logging_config = LoggingConfig(self.application_properties)

        # Add initialized classes to components here for injection
        # ...

        logging.info(f'Started app: {self.application_properties.get_name()}')

run = Main()