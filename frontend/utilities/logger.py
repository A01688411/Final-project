import logging

class CustomLogging:
    """
    Custom logging class to create a logger with specified configurations.
    """

    def create_logger(self, file_name: str, streamer: bool = False) -> logging:
        """
        Creates a logger with the specified configurations.

        Args:
            file_name (str): The name of the log file.
            streamer (bool, optional): Whether to enable streaming logs to the console. Defaults to False.

        Returns:
            logging: The created logger instance.
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')

        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        if streamer:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

        return logger