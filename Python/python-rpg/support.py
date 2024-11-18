from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    
    terrain_map = []
    
    with open(path) as level_map:
        
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        
        return terrain_map

def import_folder(path):
    for _,__,img_files in walk(path):
        
        surface_list = []
        
        for image in img_files:
            full_path = path + '/' + image
            
            image_surf = pygame.image.load(full_path).convert_alpha()            
            surface_list.append(image_surf)            
            # print(full_path)
            
    return surface_list        
    
# import_folder('python/python-rpg/graphics/Grass')
# print(import_csv_layout('Python/python-rpg/map/map_FloorBlocks.csv'))
