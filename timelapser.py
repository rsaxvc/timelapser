import cv
#constants
outwidth = 1024
outheight = 768

#io setup
f = open('inputlist', 'r')
vidout = cv.CreateVideoWriter("output.avi", cv.CV_FOURCC('D','I','V','X'), 30, (outwidth,outheight), 1 ) 

#iteration
for line in f:
	line = line.strip()
	print "Processing:",line
	inframe = cv.LoadImage(line)
	outframe = cv.CreateImage((outwidth,outheight), cv.IPL_DEPTH_8U, 3);
	cv.Resize( inframe, outframe, cv.CV_INTER_AREA)
	cv.WriteFrame( vidout, outframe )
