import cv2 as cv
import matplotlib.pyplot as plt

# 불러오기
img = cv.imread(r"C:\CV\images\dragonball.png") # C:\CV\images\elephant.jpeg C:\CV\images\sketch.png

# 흑백처리
# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 노이즈 제거
# Median Blur
grayM = cv.medianBlur(gray, 5)

# Gaussian Blur
grayG = cv.GaussianBlur(gray, (5, 5), 0)

# 윤곽선(edge) 검출
# adaptiveThreshold
edge_M_AT = cv.adaptiveThreshold(grayM, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
edge_G_AT = cv.adaptiveThreshold(grayG, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

# sobel (dx)
edge_M_S = cv.Sobel(grayM, cv.CV_8U, 1, 0)
edge_G_S = cv.Sobel(grayG, cv.CV_8U, 1, 0)

# Canny
edge_M_C = cv.Canny(grayM, 100, 200)
edge_G_C = cv.Canny(grayG, 100, 200)

# Laplacian
edge_M_L = cv.Laplacian(grayM, cv.CV_8U)
edge_G_L = cv.Laplacian(grayG, cv.CV_8U)

# bilateralFilter - 색상을 부드럽게 처리
color = cv.bilateralFilter(img, 9, 300, 300)

# bitwise - 윤곽선, 색상 결합
cartoon_M_AT = cv.bitwise_and(color, color, mask=edge_M_AT)
cartoon_M_S = cv.bitwise_and(color, color, mask=edge_M_S)
cartoon_M_C = cv.bitwise_and(color, color, mask=edge_M_C)
cartoon_M_L = cv.bitwise_and(color, color, mask=edge_M_L)

cartoon_G_AT = cv.bitwise_and(color, color, mask=edge_G_AT)
cartoon_G_S = cv.bitwise_and(color, color, mask=edge_G_S)
cartoon_G_C = cv.bitwise_and(color, color, mask=edge_G_C)
cartoon_G_L = cv.bitwise_and(color, color, mask=edge_G_L)

# 그룹화
group_M = {
    "M_AdaptiveThreshold": cartoon_M_AT,
    "M_Sobel":  cartoon_M_S,
    "M_Canny":  cartoon_M_C,
    "M_Laplacian":  cartoon_M_L
}

group_G = {
    "G_AdaptiveThreshold": cartoon_G_AT,
    "G_Sobel":  cartoon_G_S,
    "G_Canny":  cartoon_G_C,
    "G_Laplacian":  cartoon_G_L
}

# Plots에 출력
plt.figure(figsize=(12, 6))
for i, (key, image) in enumerate(group_M.items(), 1):
    plt.subplot(2, 2, i)
    plt.title(f"MedianBlur + {key.split('_')[1]}")
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.axis("off")
plt.suptitle("Cartoon Rendering (Median Blur)", fontsize=14)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for i, (key, image) in enumerate(group_G.items(), 1):
    plt.subplot(2, 2, i)
    plt.title(f"GaussianBlur + {key.split('_')[1]}")
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.axis("off")
plt.suptitle("Cartoon Rendering (Gaussian Blur)", fontsize=14)
plt.tight_layout()
plt.show()

# 창으로 출력
# Display the cartoon image
"""
cv.imshow("Cartoon_M_AT", cartoon_M_AT) # M_S, G_C, ...
cv.waitKey(0)
cv.destroyAllWindows()
"""
# 이미지 저장
for key, image in {**group_M, **group_G}.items():

    cv.imwrite(f"cartoon_{key}.png", image)

