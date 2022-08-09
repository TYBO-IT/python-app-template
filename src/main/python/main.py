from getopt import getopt
import logging
import os
import sys

from dotenv import find_dotenv, load_dotenv
from flask import Flask

from com.ivanskodje.properties.application_properties import ApplicationProperties
from com.ivanskodje.config.logging_config import LoggingConfig
from com.ivanskodje.controller.hello_controller import HelloController


class Main:
    
    application_properties : ApplicationProperties
    logging_config : LoggingConfig

    def __init__(self) -> None:       
        load_dotenv(find_dotenv())
        self.application_properties = ApplicationProperties()
        self.logging_config = LoggingConfig(self.application_properties)

        app = Flask(__name__)
        hello_controller = HelloController(app)
        # Add initialized classes to components here for injection
        # ...

        if __name__ == "__main__":
            logging.info(f'Started app (Debug mode): {self.application_properties.get_name()}')
            app.run(debug=True)
        else:
            logging.info(f'Started app: {self.application_properties.get_name()}')
            app.run()

run = Main()