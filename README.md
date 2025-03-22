# CartoonRenderingComparison
Comparison of cartoon rendering effects using OpenCV: Median/Gaussian blur with 4 edge filters (AdaptiveThreshold, Sobel, Canny, Laplacian)

OpenCV를 활용한 다양한 필터 기반 Cartoon Rendering 효과 비교 프로그램

# 주요 기능
이미지를 만화 스타일로 변환하는 알고리즘의 다양한 블러 - 필터 조합을 테스트해서 비교할 수 있다.

cv.imread()에 원하는 이미지의 경로를 입력해 만화 같은 느낌이 잘 표현되는 이미지와 잘 표현되지 않는 이미지를 비교할 수 있다.

총 8개의 조합으로 렌더링한 결과를 비교한다.
- Median Blur + Adaptive Threshold
- Median Blur + Sobel
- Median Blur + Canny
- Median Blur + Laplacian
- Gaussian Blur + Adaptive Threshold
- Gaussian Blur + Sobel
- Gaussian Blur + Canny
- Gaussian Blur + Laplacian
