class Config:
    __conf = {}

    @staticmethod
    def get_config_variable(name):
        if name in Config.__conf:
            try:
                int_repr = int(Config.__conf[name])
                return int_repr
            except ValueError:
                return Config.__conf[name]
        else:
            raise NameError("Config variable does not exist")

    @staticmethod
    def set_config_variable(name, value):
        Config.__conf[name] = value

