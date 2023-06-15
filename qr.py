import qrcode
import time
import cv2


def func1():
    link_input = input("Enter data for QR\n")
    filename = input("Name a file.\n")
    time.sleep(1)
    creation = qrcode.make(link_input)
    creation.save(filename+".png")
    print("Done, saved in working dir")
    ask = input('Do you wanna read it?')
    if ask == 'yes':
        read_img = cv2.imread(filename+'.png')
        img_detect = cv2.QRCodeDetector()
        data, bbox , straight_qrcode= img_detect.detectAndDecode(read_img)
        if bbox is not None:
            print(f"QRCode data:\n{data}")
            n_lines = len(bbox)
    else:
        exit


def func2():
    import cv2
    # Cam ON
    cap = cv2.VideoCapture(0)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if bbox is not None:
            if data:
                print("[+] QR Code detected, data:", data)   
        # display the result
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


def menu():
    choice = input('Do yow wanna create Qr(1) or read from cam(2)')
    if choice == '1':
        func1()  
    else:
        func2()
    return menu()


menu()

