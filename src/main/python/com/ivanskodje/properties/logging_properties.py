    
import logging


class LoggingProperties:
    logging_properties: dict

    def __init__(self, logging_properties) -> None:
        self.logging_properties = logging_properties

    
    def get_console_level(self):
        return self.logging_properties["console"]["level"]

    def get_file_level(self):
        return self._get_log_level(self.logging_properties["file"]["level"])
    
    def get_file_name(self):
        return self.logging_properties["file"]["name"]
    
    def get_file_path(self):
        return self.logging_properties["file"]["path"]
    
    def _get_log_level(self, logging_level):
        if(logging_level is None):
            raise Exception("Missing logging level from properties!")

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
            case "NOTSET":
                return logging.NOTSET
            case default:
                raise Exception("Invalid logging level loaded from properties")
