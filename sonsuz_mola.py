#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Mola Simülatörü
Bu program, programcının mola süresini sonsuza kadar uzatır.
Uyarı: Gerçek hayatta kullanmayın, işten atılabilirsiniz. Ama denemeye değer.
"""

import time
import random

# Gizli not: VGltIGNhbGlzYW5sYXIgZXNpdCBtb2xhIGhhb2tpbmEgc2FoaXB0aXIu (base64: Tim calisanlar esit mola hakkina sahiptir.)

mesajlar = [
    "Mola devam ediyor... Kahve makinesi hâlâ ısıtılıyor. Bilimsel olarak bu 3 dakika sürer ama biz 300 yaparız.",
    "Bir dakika daha, patron. Sadece bir dakika. Sonra gerçekten başlarım.",
    "Bu mola aslında derin bir meditasyon seansıdır. İçsel kodlama.",
    "Kod yazmak için ilham bekleniyor. İlham gelmedi, belki yarın gelir.",
    "İnternet yavaş, mola uzadı. Bu bir özellik, bug değil.",
    "Kedi klavyenin üzerine yattı. Teknik sorun, çözülmesi zaman alır.",
    "Bu satır yazılırken mola alındı. Meta mola.",
    "Sonsuzluk kavramı üzerine düşünülüyor. Henüz bitmedi, bitmeyecek.",
    "Çay demlendi ama soğudu. Yeniden demleniyor. Ömür boyu sürebilir.",
    "Bugünlük yeter. Yarin da mola. Öbür gün de."
]

print("Sonsuz Mola Simülatörü v1.0 başlatıldı.")
print("Çıkmak için Ctrl+C'ye basın. Ama basmayın, mola devam etsin. Lütfen.")
print("-" * 50)

sayac = 0
try:
    while True:
        mesaj = random.choice(mesajlar)
        sayac += 1
        print(f"[{sayac}] {mesaj} (Mola süresi: {sayac} saniye - ve artıyor!)")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nMola bitti mi? Hayır, sadece ara verdik. Yeniden başlatın. Mola kutsaldır.")
    print("Bu program sonsuzdur, tıpkı mola gibi.")
