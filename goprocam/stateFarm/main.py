# Go Pro Camera Info
# Name: StateFarm HERO 7 BLACK
# Password: zbz-hJm-4WN

from goprocam import GoProCamera, constants
import shutil
import asyncio

# create a Go Pro object
go_pro = GoProCamera.GoPro()
donwloaded_picture = 0 
downloaded_video = 0


def show_all_my_media():
    go_pro.listMedia(True)

def delete_media(file="all"):
    go_pro.delete(file)

def download_all_media_to_image_folder(): # This function will dowload all the media on the Go Pro
    all_media = go_pro.downloadAll()
    for file in all_media:
        shutil.move('./{}'.format(file), './images/{}'.format(file))
    delete_media()


def take_a_picture(timer_input=0, timelapse_activated = False): 
    if timelapse_activated:
        i = 0
        while i <10: # Take a picture every {timer_input} seconds
            go_pro.take_photo(timer=timer_input)
            filename = 'timelapse_photo_{}.JPG'.format(i) 
            go_pro.downloadLastMedia(custom_filename=filename)

            # Move the downloded file to the folder your choice
            shutil.move('./{}'.format(filename), './images/{}'.format(filename))
            i+=1
    else:
        go_pro.take_photo(timer=timer_input)
        filename= 'photo_{}.JPG'.format(donwloaded_picture)
        go_pro.downloadLastMedia(custom_filename=filename)

        # Move the downloded file to the folder your choice
        shutil.move('./{}'.format(filename), './images/{}'.format(filename))
        donwloaded_picture += 1

def take_a_video(duration_input=5):
    go_pro.shoot_video(duration=duration_input)
    filename= 'video_{}.mp4'.format(downloaded_video)
    go_pro.downloadLastMedia(custom_filename=filename)
    
    # Move the downloded file to the folder your choice
    shutil.move('./{}'.format(filename), './videos/{}'.format(filename))
    downloaded_video+=1

    


# take_a_picture(0.5,True)
take_a_video()

# download_all_media_to_image_folder()