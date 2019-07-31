# import numpy as np
# import cv2
#
# # Load an color image in grayscale
# img = cv2.imread('C:/Users/kienk/OneDrive/Pictures/6.jpg',1)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# img=cv2.imread('C:/Users/kienk/OneDrive/Pictures/6.jpg')
# plt.imshow(img,cmap='Blues',interpolation='bicubic')
# plt.xticks([0,1600]), plt.yticks([0,1000])
# # Parameters:
# # # X : array-like or PIL image
# # # The image data. Supported array shapes are:
# # #
# # # (M, N): an image with scalar data. The data is visualized using a colormap.
# # # (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
# # # (M, N, 4): an image with RGBA values (0-1 float or 0-255 int), i.e. including transparency.
# # # The first two dimensions (M, N) define the rows and columns of the image.
# # #
# # # Out-of-range RGB(A) values are clipped.
# # #
# # # cmap : str or Colormap, optional
# # # The Colormap instance or registered colormap name used to map scalar data to colors. This parameter is ignored for RGB(A) data. Defaults to rcParams["image.cmap"].
# # #
# # # norm : Normalize, optional
# # # The Normalize instance used to scale scalar data to the [0, 1] range before mapping to colors using cmap. By default, a linear scaling mapping the lowest value to 0 and the highest to 1 is used. This parameter is ignored for RGB(A) data.
# # #
# # # aspect : {'equal', 'auto'} or float, optional
# # # Controls the aspect ratio of the axes. The aspect is of particular relevance for images since it may distort the image, i.e. pixel will not be square.
# # #
# # # This parameter is a shortcut for explicitly calling Axes.set_aspect. See there for further details.
# # #
# # # 'equal': Ensures an aspect ratio of 1. Pixels will be square (unless pixel sizes are explicitly made non-square in data coordinates using extent).
# # # 'auto': The axes is kept fixed and the aspect is adjusted so that the data fit in the axes. In general, this will result in non-square pixels.
# # # If not given, use rcParams["image.aspect"] (default: 'equal').
# # #
# # # interpolation : str, optional
# # # The interpolation method used. If None rcParams["image.interpolation"] is used, which defaults to 'nearest'.
# # #
# # # Supported values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'.
# # #
# # # If interpolation is 'none', then no interpolation is performed on the Agg, ps, pdf and svg backends. Other backends will fall back to 'nearest'. Note that most SVG renders perform interpolation at rendering and that the default interpolation method they implement may differ.
# # #
# # # See Interpolations for imshow/matshow for an overview of the supported interpolation methods.
# # #
# # # Some interpolation methods require an additional radius parameter, which can be set by filterrad. Additionally, the antigrain image resize filter is controlled by the parameter filternorm.
# # #
# # # alpha : scalar, optional
# # # The alpha blending value, between 0 (transparent) and 1 (opaque). This parameter is ignored for RGBA input data.
# # #
# # # vmin, vmax : scalar, optional
# # # When using scalar data and no explicit norm, vmin and vmax define the data range that the colormap covers. By default, the colormap covers the complete value range of the supplied data. vmin, vmax are ignored if the norm parameter is used.
# # #
# # # origin : {'upper', 'lower'}, optional
# # # Place the [0,0] index of the array in the upper left or lower left corner of the axes. The convention 'upper' is typically used for matrices and images. If not given, rcParams["image.origin"] is used, defaulting to 'upper'.
# # #
# # # Note that the vertical axes points upward for 'lower' but downward for 'upper'.
# # #
# # # See the origin and extent in imshow tutorial for examples and a more detailed description.
# # #
# # # extent : scalars (left, right, bottom, top), optional
# # # The bounding box in data coordinates that the image will fill. The image is stretched individually along x and y to fill the box.
# # #
# # # The default extent is determined by the following conditions. Pixels have unit size in data coordinates. Their centers are on integer coordinates, and their center coordinates range from 0 to columns-1 horizontally and from 0 to rows-1 vertically.
# # #
# # # Note that the direction of the vertical axis and thus the default values for top and bottom depend on origin:
# # #
# # # For origin == 'upper' the default is (-0.5, numcols-0.5, numrows-0.5, -0.5).
# # # For origin == 'lower' the default is (-0.5, numcols-0.5, -0.5, numrows-0.5).
# # # See the origin and extent in imshow tutorial for examples and a more detailed description.
# # #
# # # filternorm : bool, optional, default: True
# # # A parameter for the antigrain image resize filter (see the antigrain documentation). If filternorm is set, the filter normalizes integer values and corrects the rounding errors. It doesn't do anything with the source floating point values, it corrects only integers according to the rule of 1.0 which means that any sum of pixel weights must be equal to 1.0. So, the filter function must produce a graph of the proper shape.
# # #
# # # filterrad : float > 0, optional, default: 4.0
# # # The filter radius for filters that have a radius parameter, i.e. when interpolation is one of: 'sinc', 'lanczos' or 'blackman'.
# # #
# # # resample : bool, optional
# # # When True, use a full resampling method. When False, only resample when the output image is larger than the input image.
# # #
# # # url : str, optional
# # # Set the url of the created AxesImage. See Artist.set_url.
# # #
# # # Returns:
# # # image : AxesImage
# # # Other Parameters:
# # # **kwargs : Artist properties
# # # # These parameters are passed on to the constructor of the AxesImage artist.
# plt.show()

##video##
#import cv2
# import numpy as np
# cap=cv2.VideoCapture('C:/Users/kienk/Downloads/1.mp4')
# while(True):
#     ret,frame=cap.read()
#     gray=cv2.cvtColor(frame,cv2.COLOR_HLS2RGB)
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(60)& 0xFF== 27:
#         break
# cap.release()
# cv2.destroyAllWindows()
##Drawing Functions##
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# img=np.zeros((512,512,3),np.uint8)
# img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
# img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
# img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(20,500), font,2,(255,255,255),2,cv2.LINE_AA)
# cv2.imshow('image',img )
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# # import numpy as np
# #
# # drawing = False # true if mouse is pressed
# # mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# # ix,iy = -1,-1
# #
# # # mouse callback function
# # def draw_circle(event,x,y,flags,param):
# #     global ix,iy,drawing,mode
# #
# #     if event == cv2.EVENT_LBUTTONDOWN:
# #         drawing = True
# #         ix,iy = x,y
# #
# #     elif event == cv2.EVENT_MOUSEMOVE:
# #         if drawing == True:
# #             if mode == True:
# #                 cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
# #             else:
# #                 cv2.circle(img,(x,y),5,(0,0,255),-1)
# #
# #     elif event == cv2.EVENT_LBUTTONUP:
# #         drawing = False
# #         if mode == True:
# #             cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
# #         else:
# #             cv2.circle(img,(x,y),5,(0,0,255),-1)
# # img = np.zeros((512,512,3), np.uint8)
# # cv2.namedWindow('image')
# # cv2.setMouseCallback('image',draw_circle)
# #
# # while(1):
# #     cv2.imshow('image',img)
# #     k = cv2.waitKey(1) & 0xFF
# #     if k == ord('m'):
# #         mode = not mode
# #     elif k == 27:
# #         break
# #
# # cv2.destroyAllWindows()
# import cv2
# import numpy as np
#
# drawing = False # true if mouse is pressed
# mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# img = np.zeros((512,512,3), np.uint8)
# ix,iy=-9,-9
# cv2.namedWindow('image')
# def nothing(x):
#     pass
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)
# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('size','image',-1,8,nothing)
# # mouse callback function
#
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode,r,g,b
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img,(ix,iy),(x,y),(r,g,b),-1)
#             else:
#                 cv2.circle(img,(x,y),s,(r,g,b),-1)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv2.rectangle(img,(ix,iy),(x,y),(r,g,b),-1)
#         else:
#             cv2.circle(img,(x,y),s,(r,g,b),-1)
#
# cv2.setMouseCallback('image',draw_circle)
#
# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
#     r = cv2.getTrackbarPos('R','image')
#     g = cv2.getTrackbarPos('G','image')
#     b = cv2.getTrackbarPos('B','image')
#     s = cv2.getTrackbarPos('size','image')
# cv2.destroyAllWindows()
## get track bar to control color
# import cv2
# import numpy as np
#
# def nothing(x):
#     pass
#
# # Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)
# cv2.namedWindow('image')
#
# # create trackbars for color change
# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)
#
# # create switch for ON/OFF functionality
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'image',0,1,nothing)
#
# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
#     # get current positions of four trackbars
#     r = cv2.getTrackbarPos('R','image')
#     g = cv2.getTrackbarPos('G','image')
#     b = cv2.getTrackbarPos('B','image')
#     s = cv2.getTrackbarPos(switch,'image')
#
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b,g,r]
#
# cv2.destroyAllWindows()