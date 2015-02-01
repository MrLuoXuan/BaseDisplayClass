__author__ = 'wuque'

class display_base_class:
    def __init__(self):
        print('This Is A Base Class, Can\'t Contruct')
    def get_all_attr(self):
        attr_list = []
        for item in self.__dict__:
            attr_list.append('{0} = {1}'.format(item, self.__dict__[item]))
        return ','.join(attr_list)
    def get_introduction_attr(self):
        str_attr = '{0}: {1}'.format(self.__class__.__name__, self.get_all_attr())
        return str_attr
    def __str__(self):
        return self.get_introduction_attr()

class base(display_base_class):
    pass
base_class = base()
print(base_class)
