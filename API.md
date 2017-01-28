Here is gonna be the API

#Structures

##Sequence of images
{

    "qr_size" : 4.25,
    
    "qr_height" : 2.3,
    
    "qr_distance" : 8.9,
    
    "horizontal_dimension" : 3,
    
    "vertical_dimension" : 5,
    
    "horizontal_lenght" : 3.2,
    
    "vertical_lenght" : 5.4,
    
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
    
    "qr_height" : 2.3,
    
    "qr_distance" : 8.9,
    
    "horizontal_dimension" : 3,
    
    "vertical_dimension" : 5,
    
    "horizontal_lenght" : 3.2,
    
    "vertical_lenght" : 5.4,
    
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
