import numpy as np
import matplotlib.pyplot as plt
import logging
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay

def diagrams_of_voronoi(coordinates):

  # make up data points
  max_x = max(i[0] for i in coordinates) 
  max_y = max(i[1] for i in coordinates)

  min_x = min(i[0] for i in coordinates) 
  min_y = min(i[1] for i in coordinates)

  WIDTH = max_x*2
  HEIGHT = max_y*2
  limits = [[WIDTH, HEIGHT], [-WIDTH, HEIGHT], [WIDTH, -HEIGHT], [-WIDTH, -HEIGHT]]

  # add 4 distant dummy points
  points = np.append(coordinates, limits, axis=0)
  tri = Delaunay(coordinates)

  # compute Voronoi tesselation
  vor = Voronoi(points)

  # plot
  voronoi_plot_2d(vor, show_vertices=False)

  # colorize
  OPACITY = 0.6
  for region in vor.regions:
    if not -1 in region:
      polygon = [vor.vertices[i] for i in region]        
      plt.fill(*zip(*polygon),alpha=OPACITY)


  # fix the range of axes
  MARGIN = 1.2
  plt.xlim((min_x*MARGIN, max_x*MARGIN)) 
  plt.ylim((min_y*MARGIN, max_y*MARGIN))


  # show diagrams of voronoi
  plt.triplot(points[:,0], points[:,1], tri.simplices, color='black')
  plt.plot(points[:, 0], points[:, 1],'o', color='blue')
  
  logging.info(f'Generate Image \m/')
  plt.savefig('./voronoi/images/diagram_of_voronoi.png')
  plt.show()

  logging.info(f'Finish programming')
  


coordinates = [[-2.4, -3.0], [4.0, 3.0], [-5.5, 2.5], [3.1, 2.1], [-1.0, 1.8], [4.2, -1.4], [2.4, 1.0]]
# QNTD_POINTS = 20
# coordinates = np.random.rand(QNTD_POINTS, 2)*100

diagrams_of_voronoi(coordinates)