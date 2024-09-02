import cv2

def capture(camera_port, save_path):
    # 카메라 초기화
    cap = cv2.VideoCapture(camera_port)

    # 카메라가 열려 있는지 확인
    if not cap.isOpened():
        # print("카메라를 열 수 없습니다.")
        return False

    # cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)  # 0.75는 수동 노출 모드
    # cap.set(cv2.CAP_PROP_EXPOSURE, 0.1)        # 수동 노출 값, 조정 필요

    # 프레임 캡처
    ret, frame = cap.read()

    # 프레임 캡처 성공 여부 확인
    if ret:
        # 이미지 저장
        cv2.imwrite(save_path, frame)
        # print(f"사진이 {save_path}에 성공적으로 저장되었습니다.")
        result = True
    else:
        print("사진을 캡처할 수 없습니다.")
        result = False

    # 카메라 자원 해제
    cap.release()
    return result

# 함수 호출 예제
# capture_and_save_image(camera_port=0, save_path="captured_image.jpg")
