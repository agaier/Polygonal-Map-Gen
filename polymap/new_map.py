from polymap.custom_map import FiteMap as Graph
from polymap.terrain import assign_terrain_types_to_graph
import numpy as np
import fire

def make_terrain_list(borders, biomes):
    """Creates a list of dictionaries with terrain data"""
    terrain_list = []
    for i in range(len(borders)):
        terrain_dict = { 'id'           : f"terrain-{i}",
                         'polygon'      : borders[i].tolist(),
                         'tags'         : ["location", "zone", biomes[i]],
                         'display_name' : biomes[i]}
        terrain_list += [terrain_dict]
    return terrain_list

def new_map(n_cells=150, n_rivers=10, min_river_height=0.6, 
              ocean_to_total_ratio=0.4, lake_to_total_ratio=0.05, seed=None,
              export=None, fname='map'):
    if seed is not None:
        np.random.seed(seed)
    g = Graph(N=n_cells, iterations=2)
    assign_terrain_types_to_graph(graph=g, 
                                  lake_to_total_ratio=lake_to_total_ratio,
                                  ocean_to_total_ratio=ocean_to_total_ratio)
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

    if (export == "json") or (export == "all"):
        import json
        with open(f'{fname}.json', 'w', encoding='utf-8') as f:
            json.dump(terrain_list, f, ensure_ascii=False, indent=4)

    
    if (export == "image") or (export == "all"):
        import matplotlib.pyplot as plt
        fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(12,12),dpi=100)
        ax = ax.flatten()

        plot_type = ['biome', 'terrain', 'moisture', 'height']

        for i, p_type in enumerate(plot_type):
            g.plot_full_map(plot_type=p_type, debug_height=False,  debug_moisture=False,  downslope_arrows=False, 
                rivers=True, ax = ax[i], edgecolor='gray', linewidth=0.2)
            ax[i].set_title(p_type.capitalize(), fontsize=18)
            
        plt.setp(ax.flat, xticks=[], yticks=[])
        plt.subplots_adjust(wspace=0.05, hspace=0.15)
        plt.savefig(f'{fname}.png')    

    else:
        return g, terrain_list

    print(f"[**] {fname} generated")

fire.Fire(new_map)


# if __name__ == '__main__':
#     g, terrain_list = new_map(n_cells=200, seed=0)
#     terrains = [center.terrain_type for center in g.centers]
#     biomes   = [center.biome.name for center in g.centers]
#     print(f"Biomes:\n {set(biomes)}")

#     print("Done")