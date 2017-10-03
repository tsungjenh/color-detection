from apscheduler.scheduler            import Scheduler

if __name__ == '__main__':
    search_color = Search_Color()
    img = cv2.imread('test2.jpg')
    print search_color.color_detection(img,'car')
