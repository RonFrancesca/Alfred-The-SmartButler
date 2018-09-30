import logging
from os import listdir


def logError():
    logger = logging.getLogger('jasper')
    fh = logging.FileHandler('jasper.log')
    fh.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.error('Failed to execute module', exc_info=True)


class Brain(object):

    def __init__(self, mic, profile):
        def get_modules():

            folder = 'modules'

            def get_module_names():
                module_names = [m.replace('.py', '')
                                for m in listdir(folder) if m.endswith('.py')]
                module_names = map(lambda s: folder + '.' + s, module_names)
                return module_names

            def import_module(name):
                mod = __import__(name)
                components = name.split('.')
                for comp in components[1:]:
                    mod = getattr(mod, comp)
                return mod

            def get_module_priority(m):
                try:
                    return m.PRIORITY
                except:
                    return 0

            modules = map(import_module, get_module_names())
            modules = filter(lambda m: hasattr(m, 'WORDS'), modules)
            modules.sort(key=get_module_priority, reverse=True)
            return modules

        self.mic = mic
        self.profile = profile
        self.modules = get_modules()

    def query(self, text):

        for module in self.modules:
            if module.isValid(text):

                try:
                    module.handle(text, self.mic, self.profile)
                    break
                except:
                    logError()
                    self.mic.say(
                        "I'm sorry. I had some trouble with that operation. Please try again later.")
                    break
