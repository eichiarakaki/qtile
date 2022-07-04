from sys import path
from os.path import join
from .path import qtile_path
path.append(join(qtile_path, 'settings'))
from typing import Optional
from libqtile.bar import (
    BarType, 
    Bar, 
    Gap,
)



class __Error(Exception):
    """Base class for other exceptions"""
    pass


class _ConfigError(__Error):
    pass


class _Overflows(__Error):
    """ Exception raised for errors in the input integers. """

    def __init__(self, minimum, maximum, entered_value):
        self.__minimum = minimum
        self.__maximum = maximum
        self.__entered_value = entered_value


    def __str__(self):
        return '{} is not in the range of {} and {}'.format(self.__entered_value,
                                                            self.__minimum,
                                                            self.__maximum)


class NewBar:
    def __init__(self) -> None:
        self._widgets: list = None
        self._width: int = None 
        self._height: int = None 
        self._x_position: int = None 
        self._y_position: int = None 
        self._opacity: float = None
        self._margin_bottom: int = None


    def __verify(self) -> bool:
        flag = True
        for _, (k, v) in enumerate(vars(self).items()):
            if v == None:
                flag = False
        return flag


    def assembler(self) -> Optional[BarType]:
        if self.__verify():
            return Bar(
                    self._widgets,
                    self._height,
                    opacity = self._opacity,
                    margin = [
                        self._y_position,
                        1980-self._x_position-self._width, # only for 1980x1080 screens
                        self._margin_bottom,
                        self._x_position 
                    ])   
        else:
            return Gap(55)
                

    def positions(self, *pos: list) -> None:
        """ X - Y """
        if all(param == int for param in pos):
            raise _ConfigError('Parameters for the position must be integers.')
        if not len(pos) == 2:
            raise _ConfigError('Only 2 parameters are allowed.')

        self._x_position, self._y_position = pos


    def geometry(self, *geo: list) -> None:
        """Width - Height"""
        if all(param == int for param in geo):
            raise _ConfigError('Parameters for the geometry must be integers.')
        if not len(geo) == 2:
            raise _ConfigError('Only 2 parameters are allowed.')

        self._width, self._height = geo


    def widget(self, widgets: list) -> None:
        if type(widgets) is not list:
            raise _ConfigError('The widgets have to be in a list.')

        self._widgets = widgets


    def opacity(self, op: float) -> None:
        if type(op) is not float:
            raise ValueError('The shade of the opacity must be a float.')
        if not 0.0 <= op <= 1.0:
            raise _Overflows(minimum=0.0, maximum=1.0, entered_value=op) 
        
        self._opacity = op


    def margin(self, bottom: int) -> None:
        if type(bottom) is not int:
            raise ValueError('The shade of the opacity must be a float.')
        
        self._margin_bottom = bottom