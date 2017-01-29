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
    var framestime = 30;



    resultArray  = generateGraph_version1 (framestime,colorprimary,colorsecondary,image_w,image_h);
    alert ("the form was submitted\n QR size : "+QRSize+"\n QRheight:"+QRheight
        +"\n Distance from first person"+QRdist_first+"\nimage_width:"+image_w+"\nimage height:"+image_h+"\ncolor1"+colorprimary+"\ncolor2"+colorsecondary+
        "\nroom width : "+room_x+"\nroom length:"+room_y+"\n frames : "+framestime+"\n room name ="+RoomName

    );

    var objecteJson = {"qr_size": QRSize,
            "qr_center_height":QRheight,
            "qr_distance":QRdist_first,
            "image_width":image_w,
            "image_height":image_h,
            "room_x":room_x,
            "room_y":room_y,
            "time_frames":framestime,
            "data":resultArray,
            "name":RoomName
            };
    //alert(JSON.stringify(objecteJson));
     

     // Sending and receiving data in JSON format using POST mothod
//
    xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/set_scenario";
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
     
/*
    var xhr = new XMLHttpRequest();
    var url = 'http://127.0.0.1:5000/set_scenario';
    xhr.open('POST', url,true);
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    xhr.onreadystatechange = function() {
        if (xhr.readyState==XMLHttpRequest.DONE && xhr.status == 200) {
            alert('Ok ,now ' + xhr.responseText);
        }
        else if (xhr.status != 200) {
            alert('Request failed.  Returned status of ' + xhr.status);
        }
    };
    xhr.send(JSON.stringify(objecteJson));
    */


    /*xhr.onreadystatechange =function (){
        if (xhr.readyState==XMLHttpRequest.DONE && xhr.status==200){
            var json_ans = JSON.parse(xhr.responseText);
            console.log(json_ans.url);
            alert ("success!!");
        }
        else if (xhr.status == 400) alert ("There was an error 400");

    }*/
    //var data = JSON.stringify (objecteJson);
    //xhr.send(data);
//$.post ("127.0.0.1/set_scenario",objecteJson,function (data,status){	alert ("Data : " +data + "\nStatus: "+status);});
}
function generateGraph_version1(time_frames,color1,color2, img_w,img_h){

	var imgArray = new Array();
	for (i=0; i<time_frames; i++){
		imgArray[i] = new Array();
		for (j=0; j<img_h; j++){
			imgArray[i][j] = new Array();
			for (k=0; k<img_w;k++){
				currentcolor = getColor_version1 (i,time_frames,j,img_h,color1,color2);	
			
				imgArray[i][j][k]= currentcolor;
			} 
		}
	}
 	return imgArray;
}
function getColor_version1 (current_frame, time_frames, j,img_h, color1,color2){
	var percentage = current_frame/time_frames
	var current_height = j/img_h;
	if (current_height<percentage) return color2;
	else return color1;
}
