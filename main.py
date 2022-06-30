from modules import finger_detector
import cv2
import os


def main_fn():
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    detector = finger_detector.FingerDetector()

    play_sound = False

    while cap.isOpened():
        success, image = cap.read()
        play_sound = False

        if not success:
            continue

        result = detector.detect(image)
        for (landmarks, finger_stat) in result:
            if finger_stat == finger_detector.HandGesture.Mid:
                reg = detector.mid_finger_region(image, landmarks)
                play_sound = True
                cv2.line(image, reg[0], reg[1], (255, 255, 255), 64)
                cv2.line(image, reg[0], reg[1], (0, 0, 0), 48)
            else:
                play_sound = False
                detector.draw_landmarks(image, landmarks)

        if play_sound:
            os.system("python modules/play_sound.py  faack")

        cv2.imshow('Friendly Python', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()


if __name__ == "__main__":
    main_fn()
