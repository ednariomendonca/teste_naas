### Color in negative and positive values

def color_negative_positive(values): 
    red = 'background-color: red;'
    orange = 'background-color: orange;'
    green = 'background-color: green;'
    default = ''
    
    return [red if x < 0 else orange if x == 0 else green if x > 0 else default for x in values]