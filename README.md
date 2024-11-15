# python-sentence-transformers-distiluse-base-multilingual-cased


Bu proje, kullanıcı verilerini vektör tabanlı arama ve sıralama işlemleri için optimize eden bir Python uygulamasıdır. SentenceTransformer kütüphanesi kullanılarak veri tabanındaki tüm veriler vektörleştirilir. Daha sonra, vektörleştirilen bu veriler Faiss kullanılarak sorgularda aranan kelimeye en yakın vektörler ile sıralanır. Projede, veri tabanındaki değişiklikleri takip edebilmek ve vektör dosyasını güncelleyebilmek için bir update fonksiyonu da eklenmiştir.

Bu proje örneğinde veriler MSSQL veritabanından çekilmiştir ve çekilen veriler bir DataFrame'e dönüştürülmüştür. MSSQL'e bağlanma kodu da projeye dahil edilmiştir. Siz bu kodu kendi ihtiyaçlarınıza göre uyarlamak isterseniz, verilerinizi farklı bir veritabanından veya kaynaktan çekebilir ve kök kod yapısını ihtiyacınıza göre değiştirebilirsiniz.
