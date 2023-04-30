import cv2

# Frame iterator from Henrik Midtiby
class FrameIterator():
    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)

    
    def frame_generator(self):
        # Define a generator that yields frames from the video
        while(1):
            ret, frame = self.cap.read()
            if ret is not True:
                break
            else:
                yield frame
            
        self.cap.release()

    def main(self):
        for frame in self.frame_generator():
            # Process frame
            cv2.imshow('frame',frame)

            # Deal with key presses
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
            elif k == ord('s'):
                cv2.imwrite("../output/ex00_stillimage.png", frame)

    def extract_images(self,frac=100):
        # Empty the output folder
        import shutil, os
        shutil.rmtree("output/disc")
        os.mkdir("output/disc")

        count:int = 0
        file:int = 0
        for frame in self.frame_generator():
            # save every n-th frame and disregard the first 1200 frames
            if count % frac == 0 and count > 1200:
                cv2.imwrite(f"output/disc/frame{file:03d}.jpg", frame)
                file += 1
            count += 1