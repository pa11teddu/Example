def calculate_area(length, width):
  return length * width

def calculate_perimeter(length, width):
  return 2 * (length + width)

def calculate_volume(length, width, height):
  return length * width * height

def calculate_surface_area(length, width, height):
  return 2 * (length * width + length * height + width * height)

# Extract the duplicate code from the `calculate_area_perimeter()` function into a
# separate function.
def calculate_area_and_perimeter(length, width):
  area = calculate_area(length, width)
  perimeter = calculate_perimeter(length, width)
  return area, perimeter

# Refactor the `calculate_area_perimeter()` function to call the new
# `calculate_area_and_perimeter()` function.
def calculate_area_perimeter(length, width):
  """Calculates the area and perimeter of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    A tuple containing the area and perimeter of the rectangle.
  """
  return calculate_area_and_perimeter(length, width)

