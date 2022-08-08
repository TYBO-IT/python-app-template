import yaml

from com.ivanskodje.properties.logging_properties import LoggingProperties


class ApplicationProperties:
    application_properties: dict
    logger_properties: dict

    def __init__(self) -> None:
        with open("./src/main/resources/application.yml", "r") as file:
            self.application_properties = yaml.safe_load(file)
            self.logger_properties = LoggingProperties(self.application_properties["logging"])
    
    def get_profile(self):
        return self.application_properties["application"]["profile"]
    
    def get_name(self):
        return self.application_properties["application"]["name"]
    
    def get_logging_properties(self) -> LoggingProperties:
        return self.logger_properties
