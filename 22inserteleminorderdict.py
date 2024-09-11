# insert element at the beginning of ordered dict
from collections import OrderedDict
ord_dct = OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
ord_dct.update({'color4':'Orange'},last=False)
ord_dct.move_to_end('color4', last=False)
print(ord_dct)
