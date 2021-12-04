from mosaic import create_mosaic
import glob, concurrent.futures

files = glob.glob("/path/to/source/image/*.jpg")

def mosaic(file):
    create_mosaic(
        subject=file, 
        target=file + "_mosaic.png",
        tile_path="/path/to/tiles/folder",
        tile_ratio=800/600, # Crop tiles to be height/width ratio
        tile_width=300, # Tile will be scaled
        enlargement=5, # Mosiac will be this times larger than original
        reuse=True, # Should tiles be used multiple times?
        color_mode='RGB',  # RGB (color) L (greyscale)
    )

def main():
    # Change as per the number of CPUs
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as excuter:
        excuter.map(mosaic, files)

if __name__ == '__main__':
    main()