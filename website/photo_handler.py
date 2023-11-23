import os
import random

def update_photo(photo_file):
    # Add logic to update the photo, e.g., save to a database or file system
    # This function can be more complex depending on your needs
    save_path = os.path.join('static/uploads', photo_file.filename)
    photo_file.save(save_path)
    return save_path

def updatePaperPhoto(fullness):
    """fullness should be a percentage between 0% and 100%"""
    if(0 <= fullness < 25):
        pass
    pass


def get_photos():
    # Add logic to retrieve a list of all photos
    # This could involve querying a database or listing files in a directory
    # print()
    # print(os.listdir())
    # print()
    # print()
    # print()
    photo_folder = 'website/static/bin_status_pics'
    all_photos = [f for f in os.listdir(photo_folder) if os.path.isfile(os.path.join(photo_folder, f))]
    # ONLY TO RANDOMIZE FOR RIGHT NOW: NEED TO FIX BEFORE DEMO 
    photos = []
    for i in range(3):
        photos.append(all_photos[random.randint(0, len(all_photos)-1)])
    return photos
