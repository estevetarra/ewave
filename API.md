Here is gonna be the API

#Structures

##Sequence of images
{

    "qr_size" : 4.25,
    
    "qr_center_height" : 2.3,
    
    "qr_distance" : 8.9,
    
    "image_width" : 3,
    
    "image_height" : 5,
    
    "room_x" : 3.2,
    
    "room_y" : 5.4,
    
    "time_frames" : 30,
    
    // data[frame_number][vertical][horizontal]
    
    "data" : 
    
        [
        
            [
            
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"]
                
            ],
            
                        [
            
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"]
                
            ]
            
        ]
        
}

##Seguence of colors

{

    "time_frames" : 30,
    
    // data[frame_number]
    
    "data" : ["#EFDECD","#EFDECD","#EFDECD"]

    "time" : 108383209 (in millis, to synchronize)
    
}


#Api


##User

### Send QR

/send_qr

{

    "file" : image.png
    
}

{

    "time_frames" : 30,
    
    // data[frame_number]
    
    "data" : ["#EFDECD","#EFDECD","#EFDECD"]
    
}

## Master
/set_scenario

{

    "qr_size" : 4.25,

    "qr_center_height" : 2.3,

    "qr_distance" : 8.9,

    "image_width" : 3,

    "image_height" : 5,

    "room_x" : 3.2,

    "room_y" : 5.4,

    "time_frames" : 30,
    
    // data[frame_number][vertical][horizontal]
    
    "data" : 
    
        [
        
            [
            
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"]
                
            ],
            
                        [
            
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"],
                
                ["#EFDECD","#EFDECD","#EFDECD"]
                
            ]
            
        ]
        
}


{

    "url": ewave.com/1223456327
    
}
