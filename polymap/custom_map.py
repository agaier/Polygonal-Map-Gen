"""Customized map graph"""

from polymap.map import Graph
from enum import Enum
from polymap.terrain import TerrainType

# class TerrainType(Enum):
#     OCEAN = 1
#     LAND = 2
#     LAKE = 3
#     COAST = 4

class BiomeType(Enum):
    OCEAN = 1
    LAKE = 2
    COAST = 3
    MOUNTAIN = 4
    FOREST = 5
    HILLS = 6
    WOODED_HILLS = 7
    PLAINS = 8
    DEEPOCEAN = 9



class FiteMap(Graph):
    def __init__(self, N: int = 25, iterations: int = 2):
        super().__init__(N, iterations)

    def assign_biomes(self):
        """Assigns biomes based on height and moisture

        -- Possible Terrains, lowest to highest --
        * Dry 
            - Plains
            - Hills
            - Mountain
        * Wet
            - Forest
            - Wooded Hills
            - Mountain
        * Ocean
            - Deep Ocean
            - Ocean
        * Coast
            - Coast
        * Lake
            - Lake
        """
        heights = [0.85, 0.6]
        moisture = [0.6]

        for center in self.centers:
            # Coast
            if center.terrain_type == TerrainType.COAST:
                center.biome = BiomeType.COAST

            # Ocean
            elif center.terrain_type == TerrainType.OCEAN:
                if any([n.terrain_type == TerrainType.COAST for n in center.neighbors]):
                    center.biome = BiomeType.OCEAN
                else:
                    center.biome = BiomeType.DEEPOCEAN

            # Lake     
            elif center.terrain_type == TerrainType.LAKE:
                center.biome = BiomeType.LAKE

            # Wet
            elif center.moisture > moisture[0]:
                if center.height > heights[0]:
                    center.biome = BiomeType.MOUNTAIN
                elif center.height > heights[1]:
                    center.biome = BiomeType.WOODED_HILLS
                else:
                    center.biome = BiomeType.FOREST

            else: # moisture < 0.5
                if center.height > heights[0]:
                    center.biome = BiomeType.MOUNTAIN
                elif center.height > heights[1]:
                    center.biome = BiomeType.HILLS
                else:
                    center.biome = BiomeType.PLAINS                   
                
    def _center_to_biome_color(self, center):
        if center.biome == BiomeType.OCEAN: color = 'deepskyblue'
        elif center.biome == BiomeType.LAKE: color = 'royalblue'
        elif center.biome == BiomeType.COAST: color = 'beige'
        elif center.biome == BiomeType.MOUNTAIN: color = 'slategray'
        elif center.biome == BiomeType.FOREST: color = 'forestgreen'
        elif center.biome == BiomeType.HILLS: color = 'darkkhaki'
        elif center.biome == BiomeType.WOODED_HILLS: color = 'darkgreen'
        elif center.biome == BiomeType.PLAINS: color = 'wheat'
        elif center.biome == BiomeType.DEEPOCEAN: color = 'dodgerblue'
        else:
            raise AttributeError(f'Unexpected biome type: {center.biome}')
        return color


