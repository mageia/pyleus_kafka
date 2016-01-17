import logging
import logging.config

from pyleus.storm import SimpleBolt

log = logging.getLogger("logging_example.logger_bolt")


class LoggerBolt(SimpleBolt):

    def process_tuple(self, tup):
        for k in tup.values:
            log.info("Received: %r", k)


if __name__ == '__main__':
    LoggerBolt().run()
