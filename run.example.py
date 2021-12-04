from mosaic import create_mosaic

create_mosaic(
    subject="/path/to/source/image", 
    target="/path/to/output/image", 
    tile_path="/path/to/tiles/folder",
    tile_ratio=800/600, # Crop tiles to be height/width ratio
    tile_width=500, # Tile will be scaled
    enlargement=3, # Mosiac will be this times larger than original
    reuse=True, # Should tiles be used multiple times?
    color_mode='RGB',  # RGB (color) L (greyscale)
) 