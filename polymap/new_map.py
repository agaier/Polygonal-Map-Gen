#from polymap.map import Graph
from polymap.custom_map import FiteMap as Graph
from polymap.terrain import assign_terrain_types_to_graph
import numpy as np



def make_terrain_list(borders, biomes):
    """Creates a list of dictionaries with terrain data"""
    terrain_list = []
    for i in range(len(borders)):
        terrain_dict = { 'id'           : f"terrain-{i}",
                         'polygon'      : borders[i],
                         'tags'         : ["location", "zone", biomes[i]],
                         'display_name' : biomes[i]}
        terrain_list += [terrain_dict]
    return terrain_list

def new_map(n_cells=150, n_rivers=10, min_river_height=0.6, 
              min_water_ratio=0.25, lake_to_total_ratio=0.05, seed=None):
    if seed is not None:
        np.random.seed(seed)
    g = Graph(N=n_cells, iterations=2)
    assign_terrain_types_to_graph(graph=g, 
                                  min_water_ratio=min_water_ratio, 
                                  lake_to_total_ratio=lake_to_total_ratio)
    g.assign_corner_elevations()
    g.redistribute_elevations()
    g.assign_center_elevations()
    g.create_rivers(n=n_rivers, min_height=min_river_height)
    g.assign_moisture()
    g.assign_biomes()
    
    # Get Polygons as 'dict' list for RL env
    borders  = [g._center_to_polygon(center, 'biome').get_xy() for center in g.centers]
    biomes   = [center.biome.name for center in g.centers]
    terrains = [center.terrain_type.name for center in g.centers]
    terrain_list = make_terrain_list(borders, biomes)
    
    return g, terrain_list
    
if __name__ == '__main__':
    g, terrain_list = new_map(n_cells=200, seed=0)
    terrains = [center.terrain_type for center in g.centers]
    biomes   = [center.biome.name for center in g.centers]
    print(f"Biomes:\n {set(biomes)}")

    print("Done")