import logging

class CustomLogging():

    def Create_Logger(self, file_name: str, streamer: bool = False) -> logging:

        logger = logging.getLogger(__name__)  # Indicamos que tome el nombre del modulo
        logger.setLevel(logging.DEBUG)  # Configuramos el nivel de logging

        formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')  # Creamos el formato

        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)  # Configuramos el formato
        logger.addHandler(file_handler)  # Agregamos el archivo

        if (streamer):
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

        return logger