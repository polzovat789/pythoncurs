import logging
from logging.handlers import TimedRotatingFileHandler
import os


# Настройка логирования
def setup_logger():
    # Создаем каталог для логов, если он не существует
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Создаем логгер
    logger = logging.getLogger("user_logger")
    logger.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень логирования

    # Формат логов
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # Обработчик для записи в файл с ротацией (создание нового файла каждый день)
    file_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "user_actions.log"), when="midnight", interval=1,
        backupCount=7
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)  # Логирование действий на уровне INFO

    # Обработчик для вывода логов на консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)  # Логирование всех сообщений на консоль

    # Добавляем обработчики в логгер
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Функция для записи действия пользователя в лог
def log_user_action(logger, action, level=logging.INFO):
    if level == logging.INFO:
        logger.info(action)
    elif level == logging.ERROR:
        logger.error(action)
    elif level == logging.WARNING:
        logger.warning(action)
    else:
        logger.debug(action)


# Пример работы программы
if __name__ == "__main__":
    # Настройка логгера
    logger = setup_logger()

    # Пример логирования действий
    log_user_action(logger, "Пользователь вошел в систему.")
    log_user_action(
        logger, "Ошибка при попытке загрузить файл.", level=logging.ERROR
    )
    log_user_action(logger, "Пользователь изменил настройки.")
    log_user_action(
        logger, "Предупреждение: неправильный формат ввода.", level=logging.WARNING
    )
    log_user_action(logger, "Пользователь вышел из системы.")
