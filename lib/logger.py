class Log4j(object):

    def __init__(self,spark):
        # get spark app details with wich to prefix all messages 

        log4j = spark._jvm.org.apache.log4j
        self.logger = log4j.LogManager.getLogger("retail_analysis")

    def error(self,message):
        """ Log an Error.
        :params: Error message to write to log
        :return: None
        """
        self.logger.error(message)

    def warn(self, message):
        """ Log a Warning.
        :params: Warn message to write to log
        :return: None
        """
        self.logger.warn(message)

    def info(self, message):
        """ Log an Information.
        :params: Warn message to write to log
        :return: None
        """
        self.logger.info(message)