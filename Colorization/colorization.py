import numpy as np
import cv2 as cv

if __name__ == '__main__':
    W_in = 224
    H_in = 224

    prototxt = "colorization_deploy_v2.prototxt.txt"
    caffemodel = "colorization_release_v2.caffemodel"
    kernel = "pts_in_hull.npy"
    input = "test1.jpg"

    # Select desired model
    net = cv.dnn.readNetFromCaffe(prototxt, caffemodel)

    pts_in_hull = np.load(kernel) # load cluster centers

    # populate cluster centers as 1x1 convolution kernel
    pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1)
    net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull.astype(np.float32)]
    net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, np.float32)]

    if input:
        cap = cv.VideoCapture(input)
    else:
        cap = cv.VideoCapture(0)

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    imshowSize = (width, height)

    while cv.waitKey(1) < 0:
        hasFrame, frame = cap.read()
        if not hasFrame:
            cv.waitKey()
            break

        img_rgb = (frame[:,:,[2, 1, 0]] * 1.0 / 255).astype(np.float32)

        img_lab = cv.cvtColor(img_rgb, cv.COLOR_RGB2Lab)
        img_l = img_lab[:,:,0] # L 채널 따로 꺼내기
        (H_orig,W_orig) = img_rgb.shape[:2] # 원본 이미지 크기

        # 네트워크 입력 사이즈에 맞게 이미지 크기를 재구성
        img_rs = cv.resize(img_rgb, (W_in, H_in))
        img_lab_rs = cv.cvtColor(img_rs, cv.COLOR_RGB2Lab)
        img_l_rs = img_lab_rs[:,:,0]
        img_l_rs -= 50 # 평균 중심화를 위해 전체적으로 50을 빼준다.

        net.setInput(cv.dnn.blobFromImage(img_l_rs))
        ab_dec = net.forward()[0,:,:,:].transpose((1,2,0)) # 결과물

        (H_out,W_out) = ab_dec.shape[:2]
        ab_dec_us = cv.resize(ab_dec, (W_orig, H_orig))
        img_lab_out = np.concatenate((img_l[:,:,np.newaxis],ab_dec_us),axis=2) # 원본 이미지의 L 채널과 연결
        img_bgr_out = np.clip(cv.cvtColor(img_lab_out, cv.COLOR_Lab2BGR), 0, 1)

        frame = cv.resize(frame, imshowSize)
        
        # 화면에 출력
        cv.imshow('origin', frame)
        cv.imshow('gray', cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
        cv.imshow('colorized', cv.resize(img_bgr_out, imshowSize))
