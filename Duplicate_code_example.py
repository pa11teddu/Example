def calculate_area(length, width):
  """Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """
  return length * width


def calculate_perimeter(length, width):
  """Calculates the perimeter of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The perimeter of the rectangle.
  """
  return 2 * (length + width)


def calculate_volume(length, width, height):
  """Calculates the volume of a rectangular prism.

  Args:
    length: The length of the rectangular prism.
    width: The width of the rectangular prism.
    height: The height of the rectangular prism.

  Returns:
    The volume of the rectangular prism.
  """
  return length * width * height


def calculate_surface_area(length, width, height):
  """Calculates the surface area of a rectangular prism.

  Args:
    length: The length of the rectangular prism.
    width: The width of the rectangular prism.
    height: The height of the rectangular prism.

  Returns:
    The surface area of the rectangular prism.
  """
  return 2 * (length * width + length * height + width * height)


def calculate_area_perimeter(length, width):
  """Calculates the area and perimeter of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    A tuple containing the area and perimeter of the rectangle.
  """

  # Extract the duplicate code into a separate function.
  def calculate_area_and_perimeter():
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    return area, perimeter

  # Return the result of the new function.
  return calculate_area_and_perimeter()
