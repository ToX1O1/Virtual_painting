import cv2 
import mediapipe as mp 
import time
import math



class handDetector():
    def __init__(self,mode =False, maxHands=2,modelComplexity=1,detectionCon=0.5,trackCon=0.5): 
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.finger_tip_id= [4,8,12,16,20]
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.modelComplex,self.detectionCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils


    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)


        return img

    def findPosition(self, img , handNo=0 , draw =True):
        self.lmlist=[]
        
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myhand.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x * w),int(lm.y * h) 
                self.lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),7,(255,0,255),cv2.FILLED)

        return self.lmlist

    def fingerStatus(self):
            #if len(self.lm_list)!=0:    
            fingers=[]

            if (self.lmlist[self.finger_tip_id[0]][1] < self.lmlist[self.finger_tip_id[0] - 1][1]):
                fingers.append(1)
            else:
                fingers.append(0)
        
            for i in range(1,5):
                if (self.lmlist[self.finger_tip_id[i]][2] < self.lmlist[self.finger_tip_id[i] - 2][2]):
                    fingers.append(1)
                else:
                   fingers.append(0)
                
            return fingers    

        
    def fingersUp(self):#checking which finger is open 
        fingers = []#storing final result
        # Thumb < sign only when  we use flip function to avoid mirror inversion else > sign
        if self.lmlist[self.tipIds[0]][1] > self.lmlist[self.tipIds[0] - 1][1]:#checking x position of 4 is in right to x position of 3
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers
        for id in range(1, 5):#checking tip point is below tippoint-2 (only in Y direction)
            if self.lmlist[self.tipIds[id]][2] < self.lmlist[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            # totalFingers = fingers.count(1)

        return fingers

    def findDistance(self, p1, p2, img, draw=True,r=15,t=3):# finding distance between two points p1 & p2
        x1, y1 = self.lmlist[p1][1],self.lmlist[p1][2]#getting x,y of p1
        x2, y2 = self.lmlist[p2][1],self.lmlist[p2][2]#getting x,y of p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2#getting centre point

        if draw: #drawing line and circles on the points
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
        
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2, cx, cy]

def main():
    pTime=0
    cTime=0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img =cap.read()
        img = detector.findHands(img)
        lmlist =detector.findPosition(img)
        

        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)

        cv2.imshow("Image",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break




if __name__ == "__main__":
    main()