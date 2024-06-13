import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Define a 3D object (modify these vertices for different shapes)
vertices = np.array([
    [1, 1, 1],  # Top front right
    [-1, 1, 1],  # Top back right
    [-1, -1, 1], # Bottom back right
    [1, -1, 1],  # Bottom front right
    [1, 1, -1],  # Top front left
    [-1, 1, -1], # Top back left
    [-1, -1, -1],# Bottom back left
    [1, -1, -1],  # Bottom front left
])

# Define functions for transformations (modify these for different effects)
def translate(vertices, tx, ty, tz):
  """
  Translates the object by the specified amounts in x, y, and z directions.
  """
  return vertices + np.array([tx, ty, tz])

def rotate_x(vertices, angle):
  """
  Rotates the object around the X-axis by the given angle in degrees.
  """
  theta = np.radians(angle)
  rotation_matrix = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
  return vertices.dot(rotation_matrix)

def rotate_y(vertices, angle):
  """
  Rotates the object around the Y-axis by the given angle in degrees.
  """
  theta = np.radians(angle)
  rotation_matrix = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
  return vertices.dot(rotation_matrix)

def rotate_z(vertices, angle):
  """
  Rotates the object around the Z-axis by the given angle in degrees.
  """
  theta = np.radians(angle)
  rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
  return vertices.dot(rotation_matrix)

def scale(vertices, sx, sy, sz):
  """
  Scales the object by the specified factors in x, y, and z directions.
  """
  return vertices * np.array([sx, sy, sz])

# Apply transformations (replace with desired operations)
transformed_vertices = translate(vertices, 2, 1, 0)  # Translate object
transformed_vertices = rotate_y(transformed_vertices, 60)  # Rotate around Y-axis

# Define viewing parameters (optional, adjust for better visualization)
view_elev = 15  # Elevation angle for viewing (in degrees)
view_azim = -60  # Azimuth angle for viewing (in degrees)

# Plot the original and transformed object
fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(121, projection='3d')
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='red', marker='o', label='Original')

ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")

ax = fig.add_subplot(122, projection='3d')
ax.scatter(transformed_vertices[:, 0], transformed_vertices[:, 1], transformed_vertices[:, 2], c='blue', marker='o', label='Transformed')

ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")

# Set viewing angles (optional)
ax.view_init(elev=view_elev, azim=view_azim)

plt.title("3D Transformation Demonstration")
plt.legend()
plt.show()
