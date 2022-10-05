# Polygonal Map Generation for RL Placement
> An adaption based on [Polygonal Map Generation](https://github.com/TheFebrin/Polygonal-Map-Generation-for-Games) for Games based on [http://www-cs-students.stanford.edu/~amitp/game-programming/
]()


## Setup

Install this library `polymap` locally with pip

```pip install -e .```

## Creating Maps

#### Creating a single map

The function ``polymap/new_map.py`` creates a new map, it can be run from the command line with options like this:

```
python polymap/new_map.py --n_cells=1000 --seed=$rep --fname test_map --export='all'
```

The options for ``export`` are:

- `json` export all polygons as a json file with name ``{fname}.json`` 
- `image` export map as an image with name ``{fname}.png`` 
- `all` export json and image
- `None` (or anything else) return the graph and the list of terrains (for notebooks, inside algorithms, etc.)


The new_map has several different generation parameters exposed that can be accessed when calling the function from the within python or the command line:
- `n_cell` how many polygons to generate
- `n_rivers` maximum number of rivers to generate
- `ocean_to_total_ratio` the amount of ocean
- `lake_to_total_ratio` the amount of lake 

Though has it is procedural all of these values (except the n_cell) are guidelines not hard constraints.

#### Creating a set of maps

The script `batch_map_gen.sh` generates a set of maps, you can set the parameters in this file or edit the defaults in `new_map.py`. I created several different sets and uploaded them here.

I didn't do anything fancy to produce them in parallel, just runnning processes in the background -- for optimal performance only run as many at a time as you have cores.


## Biomes

Each polygon has a biome type assigned to it defined by the combination of moisture and elevation. As many of these as you want can be defind, I kept it simple. You can see how these are defined in `polymap/custom_map.py` where I defined the graph.

```python
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
``` 

## Libraries
* Python - version 3.7.3
* numpy
* scipy
* shapely
* matplotlib
* plotly

## Status
Project: _finished_

## Credits
* [@MatMarkiewicz](https://github.com/MatMarkiewicz)
* [@jgrodzicki](https://github.com/jgrodzicki)
* [@SWi98](https://github.com/SWi98)
* [@TheFebrin](https://github.com/TheFebrin)
