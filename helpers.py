# Filtering functions
operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]

def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                return name, operator_type[0].strip(), value

    return [None] * 3


# Styling functions
def style_title():
    title_style = {
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
    return title_style

def style_font():
    font_style = {
        'family': "Raleway"
    }
    return font_style

def network_layout_options():
    layout_types = ["random", "grid", "circle", "concentric", "breadthfirst", "cose", "cose-bilkent", "cola", "euler", "spread", "dagre", "klay"]
    options = [{'label' : layout.title(), 'value' : layout} for layout in layout_types]
    return options

def clique_sizes():
    return [2, 3, 4, 5]

def generate_options(option_arr):
    return [{'label' : str(option).title(), 'value' : option} for option in option_arr]

def generate_range_values(value_arr):
    return {i : str(value_arr[i]) for i in range(len(value_arr))}