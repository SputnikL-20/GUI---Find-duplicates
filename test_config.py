import configparser


config = configparser.ConfigParser()

config.read('./sample.ini', encoding='utf8')

# for key in config['APP']:  
print(config['APP']['log_txt'])
print(config['APP']['suffix'])
print(config['APP']['sear_dir'])