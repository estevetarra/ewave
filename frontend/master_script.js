//noinspection JSAnnotator
function myFunction(){
	
    var QRSize = document.getElementById ('qrsize').value;
    var QRheight= document.getElementById ('qrheight').value;
    var QRdist_first=document.getElementById('qrdistance').value;
    var image_w = document.getElementById('imgw').value
    var image_h=document.getElementById('imgh').value;
    var room_x= document.getElementById ('roomw').value;
    var room_y=document.getElementById ('roomh').value;
    var colorprimary = document.getElementById('color1').value;
    var RoomName = document.getElementById('roomname').value;
    var colorsecondary = document.getElementById('color2').value;
    var total_frames = document.getElementById('frames').value;
    var time_bw_frames =document.getElementById('time_bw_frames').value;

    var img_type = document.getElementById('type').value;



    if (img_type=="Vertical")    resultArray  = generateGraph_version1 (total_frames ,colorprimary,colorsecondary,image_w,image_h);
    else  resultArray  = generateGraph_version2 (total_frames ,colorprimary,colorsecondary,image_w,image_h);
    alert ("the form was submitted\n QR size : "+QRSize+"\n QRheight:"+QRheight
        +"\n Distance from first person"+QRdist_first+"\nimage_width:"+image_w+"\nimage height:"+image_h+"\ncolor1"+colorprimary+"\ncolor2"+colorsecondary+
        "\nroom width : "+room_x+"\nroom length:"+room_y+"\n frames : "+total_frames +"\n room name ="+RoomName

    );


    var objecteJson = {"qr_size": QRSize,
            "qr_center_height":QRheight,
            "qr_distance":QRdist_first,
            "image_width":image_w,
            "image_height":image_h,
            "room_x":room_x,
            "room_y":room_y,
            "time_frames":total_frames ,
            "data":resultArray,
            "name":RoomName,
            "time_between_frames":time_bw_frames
	};
    alert(JSON.stringify(objecteJson));
     

     // Sending and receiving data in JSON format using POST mothod
//
    xhr = new XMLHttpRequest();
    var url = "/set_scenario";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () { 
        if (xhr.readyState == 4 && xhr.status == 200) {
            var json = JSON.parse(xhr.responseText);
            alert(xhr.responseText)
        }
    }
    var data = JSON.stringify(objecteJson);

	
    xhr.send(data);

}
function generateGraph_version1(total_frames ,color1,color2, img_w,img_h){

	var imgArray = new Array();
	for (i=0; i<total_frames ; i++){
		imgArray[i] = new Array();
		for (j=0; j<img_h; j++){
			imgArray[i][j] = new Array();
			for (k=0; k<img_w;k++){
				currentcolor = getColor_version1 (i,total_frames ,j,img_h,color1,color2);
			
				imgArray[i][j][k]= currentcolor;
			} 
		}
	}
 	return imgArray;
}
function generateGraph_version2(total_frames ,color1,color2,img_w,img_h) {

    var imgArray = new Array();
    for (i=0; i<total_frames ; i++){
        imgArray[i] = new Array();
        for (j=0; j<img_h; j++){
            imgArray[i][j] = new Array();
            for (k=0; k<img_w;k++){
                currentcolor = getColor_version2 (i,total_frames ,k,img_w,color1,color2);

                imgArray[i][j][k]= currentcolor;
            }
        }
    }
    return imgArray;

}
function getColor_version1 (current_frame, time_frames, j,img_h, color1,color2){
	var percentage = current_frame/time_frames;
	var current_height = j/img_h;
	if (current_height<percentage) return color2;
	else return color1;
}
function getColor_version2 (current_frame,time_frames,i,img_w,color1,color2){
    var percentage = current_frame/time_frames;
    var current_height = i/img_w;
    if (current_height<percentage) return color2;
    else return color1;

}
