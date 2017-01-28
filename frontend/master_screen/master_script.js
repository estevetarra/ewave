function myFunction(){
	
var QRSize = document.getElementById ('qrsize').value;
var QRheight= document.getElementById ('qrheight').value; 
var QRdist_first=document.getElementById('qrdistance').value;
var image_w = document.getElementById('imgw').value
var image_h=document.getElementById('imgh').value;
var room_x= document.getElementById ('roomw').value;
var room_y=document.getElementById ('roomh').value;
var colorprimary = document.getElementById('color1').value;

var colorsecondary = document.getElementById('color2').value;
var frames = 30;
	


resultArray  = generateGraph_version1 (frames,colorprimary,colorsecondary,image_w,image_h);
alert ("the form was submitted\n QR size : "+QRSize+"\n QRheight:"+QRheight
	+"\n Distance from first person"+QRdist_first+"\nimage_width:"+image_w+"\nimage height:"+image_h+"\ncolor1"+colorprimary+"\ncolor2"+colorsecondary+
	"\nroom width : "+room_x+"\nroom length:"+room_y+"\n frames : "+frames

);



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
