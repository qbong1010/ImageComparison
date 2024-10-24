import cv2
import os

# 이미지 파일 경로
##image1_path = 'C:/Users/dohwa/Desktop/MyPlugin/Image Comparison/위성이미지/W7_2013.jpg'
##image2_path = 'C:/Users/dohwa/Desktop/MyPlugin/Image Comparison/위성이미지/W7_2023.jpg'
image1_path = "C:\\Users\\dohwa\\Desktop\\MyPlugin\\Image Comparison\\sat_images\\TEST_original.jpg"
image2_path = "C:\\Users\\dohwa\\Desktop\\MyPlugin\\Image Comparison\\sat_images\\TEST_changed.jpg"
# 이미지 불러오기
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# 이미지 파일 존재 여부 확인
if not os.path.exists(image1_path):
    print(f"Error: Image 2013 not found at {image1_path}")
if not os.path.exists(image2_path):
    print(f"Error: Image 2023 not found at {image2_path}")

# 이미지가 제대로 불러와졌는지 확인 후 프로그램 종료
if image1 is None:
    print("Error: Image 2013 could not be loaded.")
    exit()  # 오류 발생 시 프로그램 종료

if image2 is None:
    print("Error: Image 2023 could not be loaded.")
    exit()  # 오류 발생 시 프로그램 종료

# 그레이스케일로 변환 (조도 및 색상 차이 최소화)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# 이미지 크기 맞추기 (이미지 크기가 다를 경우)
gray1 = cv2.resize(gray1, (gray2.shape[1], gray2.shape[0]))

# 이미지 차이 계산 (절대 차이)
diff = cv2.absdiff(gray1, gray2)

# 차이점을 강조하기 위한 임계 처리 (Thresholding)
_, thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

# 노이즈 제거 (모폴로지 연산)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
cleaned_diff = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 변경된 부분을 시각적으로 강조하기 위해 윤곽선을 그림
contours, _ = cv2.findContours(cleaned_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 변경된 영역에 윤곽선 그리기
for contour in contours:
    if cv2.contourArea(contour) > 100:  # 너무 작은 영역은 무시
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 255, 0), 2)  # 녹색 윤곽선

# # 결과 시각화
# cv2.imshow("Original Image", image1)
# cv2.imshow("Modified Image with Detected Changes", image2)
# cv2.imshow("Differences", cleaned_diff)

# # 키 입력 대기 후 모든 창 닫기
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 변환 완료 후 확인 메시지 출력
# print("Images successfully loaded and converted to grayscale.")


# 이미지 저장 경로 명시
cv2.imwrite("C:\\Users\\dohwa\\Desktop\\MyPlugin\\Image Comparison\\output_original.jpg", image1)
cv2.imwrite("C:\\Users\\dohwa\\Desktop\\MyPlugin\\Image Comparison\\output_modified.jpg", image2)
cv2.imwrite("C:\\Users\\dohwa\\Desktop\\MyPlugin\\Image Comparison\\output_diff.jpg", cleaned_diff)

print("Images have been saved successfully to 'C:\\Users\\dohwa\\Desktop\\MyPlugin\\Image Comparison\\'")




