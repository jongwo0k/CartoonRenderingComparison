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

matplotlib을 사용해 결과를 시각화 하고 (cv.imshow()로도 시각화 할 수 있다)

cv.imwrite()에 원하는 저장 경로를 입력해 개별 이미지 8개를 각각 저장한다

# 렌더링 과정

## Grayscale - 흑백처리
명암 정보를 통해 윤곽선을 검출하기 위해 채널을 1개로 줄인다

## Blur - 노이즈 제거
Median Blur

-주변 픽셀의 중앙값을 사용하여 노이즈를 제거한다.
-salt & pepper 노이즈 제거에 효과적이며 윤곽선을 잘 보존한다.

Gaussian Blur

-gaussian kernel을 이용해 가중치를 적용하여 노이즈를 제거한다.
-연속적인 노이즈 감소에 유리하다.

## Edge Detection - 윤곽선 검출
AdaptiveThreshold

-이미지의 밝기에 따라 임계값을 적용하여 이진화해 윤곽선을 검출한다
-조명이 불균일한 경우나 그림자가 있을 때 유리하다.

Sobel Filter

-수평/수직 기울기를 이용하여 윤곽선을 검출한다
-밝기 변화가 큰 경우 유리하다.

Canny Filter

-gradient, 최대비 억제, hysteresis 여러 단계를 거쳐 윤곽선을 정교하게 검출한다.
-노이즈에 강하며 정확하고 깔끔한 윤곽선 검출에 유리하다.

Laplacian Filter

-두 번 미분을 통해 변곡점을 이용하여 윤곽선을 검출한다.
-노이즈에 민감하고 경계가 두드러지는 경우 유리하다.

## BilateralFilter
공간적 거리와 색상 거리를 고려한다.
윤곽선을 유지하면서 색상을 부드럽게 처리한다.

### Bitwise
윤곽선과 색상을 결합한다.
최종적으로 윤곽선은 뚜렷하고 내부 색상은 부드러운 카툰 렌더링 이미지를 완성한다.

# 결과 비교
### Median Blur


![Median Blur Filter Comparison](./images/dragonball/MedianD.png)

### Gaussian Blur


![Gaussian Blur Filter Comparison](./images/dragonball/GaussianD.png)


### Median Blur


![Median Blur Filter Comparison](./images/elephant/MedianE.png)


### Gaussian Blur


![Gaussian Blur Filter Comparison](./images/elephant/GaussianE.png)


### Median Blur


![Median Blur Filter Comparison](./images/sketch/MedianS.png)


### Gaussian Blur


![Gaussian Blur Filter Comparison](./images/sketch/GaussianS.png)
