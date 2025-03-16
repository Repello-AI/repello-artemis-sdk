import logging
import os


class ColoredFormatter(logging.Formatter):
    """
    A custom formatter that adds colors based on log level for console output.
    Colors work in most terminals but not in log files.
    """

    COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[41m",  # Red background
    }
    RESET = "\033[0m"  # Reset color

    def format(self, record):
        log_fmt = "%(colored_prefix)s %(message)s"
        formatter = logging.Formatter(log_fmt)

        # Add coloring to the entire bracket part
        levelname = record.levelname
        if levelname in self.COLORS:
            color_code = self.COLORS[levelname]
            record.colored_prefix = f"{color_code}[{record.name} {self.formatTime(record)} {levelname}]{self.RESET}"
        else:
            record.colored_prefix = (
                f"[{record.name} {self.formatTime(record)} {levelname}]"
            )

        result = formatter.format(record)
        return result

    def formatTime(self, record, datefmt=None):
        """Format the time using the default formatter"""
        return logging.Formatter().formatTime(record)


# Create the logger
artemis_logger = logging.getLogger("Artemis@Repello")
artemis_logger.setLevel(logging.DEBUG)
artemis_logger.addHandler(logging.NullHandler())
artemis_logger.propagate = False

# Regular formatter for file logging
file_formatter = logging.Formatter(
    fmt="[%(name)s %(asctime)s %(levelname)s] %(message)s"
)


def enable_console_logging(level=logging.INFO):
    """
    Enable logging to console with colored output.
    """
    # Remove existing console handlers to avoid duplicates
    for handler in artemis_logger.handlers[:]:
        if isinstance(handler, logging.StreamHandler) and not isinstance(
            handler, logging.FileHandler
        ):
            artemis_logger.removeHandler(handler)

    # Add new console handler with colored formatter
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter())
    handler.setLevel(level)
    artemis_logger.addHandler(handler)
    artemis_logger.setLevel(min(artemis_logger.level, level))


def enable_file_logging(filepath, level=logging.DEBUG):
    """
    Enable logging to a file with standard formatting (no colors).
    """
    # Remove existing file handlers with the same path to avoid duplicates
    for handler in artemis_logger.handlers[:]:
        if isinstance(
            handler, logging.FileHandler
        ) and handler.baseFilename == os.path.abspath(filepath):
            artemis_logger.removeHandler(handler)

    # Add new file handler with standard formatter
    handler = logging.FileHandler(filepath)
    handler.setFormatter(file_formatter)
    handler.setLevel(level)
    artemis_logger.addHandler(handler)
    artemis_logger.setLevel(min(artemis_logger.level, level))
