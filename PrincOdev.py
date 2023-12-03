import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\Hamza\\princ.jpg")
import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread("C:\\Users\Hamza\\princ.jpg")  # Görüntü yolu buraya eklenmelidir

# Gri seviyeye dönüştür
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eşikleme
ret, thresh = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)

# Morfolojik işlemler (istenmeyen arka planları temizleme)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Etiketleme
ret, markers = cv2.connectedComponents(sure_bg)

# Toplam pirinç sayısı
num_rice_detected = ret - 1  # -1 çünkü arka planı saymıyoruz

# Sonuçları ekrana yazdır
print("Toplam Pirinç Sayısı:", num_rice_detected)

# Eşiklenmiş görüntüyü göster
cv2.imshow("Eşiklenmiş Görüntü", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
