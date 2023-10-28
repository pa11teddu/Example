def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def calculate_volume(length, width, height):
    return length * width * height

def calculate_surface_area(length, width, height):
    base_area = length * width
    lateral_area = 2 * (length * height + width * height)
    total_area = 2 * base_area + lateral_area
    return total_area

def calculate_area_and_perimeter(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    return area, perimeter

def calculate_area_perimeter(length, width):
    return calculate_area_and_perimeter(length, width)
