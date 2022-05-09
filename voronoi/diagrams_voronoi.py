import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay

from settings import COORDINATES, QNTD_POINTS, SCALA, MARGIN, PATH_SAVE


#COORDINATES = np.random.rand(QNTD_POINTS, 2)*SCALA
COLOR_BLUE = 'blue'
COLOR_BLACK = 'black'


def display_voronoi(points_x, points_y, COLOR_POINT):
  plt.plot(points_x, points_y,'o', color=COLOR_POINT)


def display_delaunay(points_x, points_y, points_indices, COLOR_POINT):
  plt.triplot(points_x, points_y, points_indices, color=COLOR_POINT)


def adjust_limit_axis(min_x, max_x, min_y, max_y):
  plt.xlim((min_x*MARGIN, max_x*MARGIN)) 
  plt.ylim((min_y*MARGIN, max_y*MARGIN))


def get_valid_region_voronoi(voronoi_regions):
  return [region for region in voronoi_regions if not -1 in region ]


def colorize_polygon_voronoi(area, voronoi_vertices):
  polygon = [voronoi_vertices[i] for i in area]        
  plt.fill(*zip(*polygon), alpha=0.6)


def colorize_diagrama_voronoi(voronoi_regions, voronoi_vertices):
  areas = get_valid_region_voronoi(voronoi_regions)

  for area in areas:
    colorize_polygon_voronoi(area, voronoi_vertices)


def get_max_points(coordinates):
  return max(i[0] for i in coordinates), max(i[1] for i in coordinates) 


def get_min_points(coordinates):
  return min(i[0] for i in coordinates) , min(i[1] for i in coordinates)


def save_image():
  plt.savefig(PATH_SAVE)


def limits_axis(max_x, max_y):
  WIDTH = max_x*2
  HEIGHT = max_y*2
  return [[WIDTH, HEIGHT], [-WIDTH, HEIGHT], [WIDTH, -HEIGHT], [-WIDTH, -HEIGHT]]


def diagrams_of_voronoi(coordinates):

  max_x, max_y = get_max_points(coordinates)
  min_x, min_y = get_min_points(coordinates)
  limits = limits_axis(max_x, max_y)

  # add 4 distant dummy points
  points = np.append(coordinates, limits, axis=0)
  delaunay = Delaunay(coordinates)

  # compute Voronoi tesselation
  voronoi = Voronoi(points)

  POINTS_X = points[:,0]
  POINTS_Y = points[:,1]
  INDICES_TRIANGULATION_POINTS = delaunay.simplices

  voronoi_plot_2d(voronoi, show_vertices=False)

  colorize_diagrama_voronoi(voronoi.regions, voronoi.vertices)

  adjust_limit_axis(min_x, max_x, min_y, max_y)

  display_delaunay(POINTS_X, POINTS_Y, INDICES_TRIANGULATION_POINTS, COLOR_BLACK)
  
  display_voronoi(POINTS_X, POINTS_Y, COLOR_BLUE)
  
  save_image()
  
  plt.show()



diagrams_of_voronoi(COORDINATES)