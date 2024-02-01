from datadog_checks.base import ConfigurationError, OpenMetricsBaseCheckV2


class Neo4jCheck(OpenMetricsBaseCheckV2):
    __NAMESPACE__ = "neo4j"

    def __init__(self, name, init_config, instances):
        super(Neo4jCheck, self).__init__(name, init_config, instances)

        self.metrics_map = [".*"]

    def get_default_config(self):
        return {"metrics": self.metrics_map}

    def configure_scrapers(self):
        """
        Creates a scraper configuration for each instance.
        """

        scrapers = {}

        for config in self.scraper_configs:
            host = config.get('host', '')
            port = config.get('port', '')

            if not isinstance(host, str):
                raise ConfigurationError('The setting `host` must be a string')
            if not isinstance(port, int):
                raise ConfigurationError('The setting `port` must be an integer')
            if not host:
                raise ConfigurationError('The setting `host` is required')
            if not port:
                raise ConfigurationError('The setting `port` is required')

            endpoint = f"http://{host}:{port}/metrics"

            config["openmetrics_endpoint"] = endpoint

            scrapers[endpoint] = self.create_scraper(config)

        self.scrapers.clear()
        self.scrapers.update(scrapers)