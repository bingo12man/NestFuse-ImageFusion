import cv2


def salient(index):
    img = cv2.imread("images/IV_images/IR"+str(index)+".png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
    
    # print(n_labels)
    
    
    vis_img = cv2.imread("images/IV_images/VIS"+str(index)+".png")
    size_thresh = 1
    for i in range(1, n_labels):
        if stats[i, cv2.CC_STAT_AREA] >= size_thresh:
            # print(stats[i, cv2.CC_STAT_AREA])
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            # print(y, x)
            # print(h,w)
            if(stats[i, cv2.CC_STAT_AREA] > 10000):
              for j in range(0,h):
                for k in range(0,w):
                  rgb = img[y+j,x+k]
                  if(rgb[0] > 130 and rgb[1] > 130 and rgb[2] > 130 and h < 3*w):
                      img[y+j,x+k] = tuple(13*ele1//16 + 3*ele2//16 for ele1, ele2 in zip(img[y+j,x+k], vis_img[y+j,x+k]))
                   # img[y+j, x+k] = vis_img[y+j, x+k]
    cv2.imwrite("images/IV_images/IRR"+str(index)+".png", img)
            # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)
            # print(h*w)
    
    # print(rgb[0])
    
if __name__ == '__main__':
    
    salient(1)
