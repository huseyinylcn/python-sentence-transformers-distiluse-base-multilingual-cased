# python-sentence-transformers-distiluse-base-multilingual-cased


Bu proje, kullanıcı verilerini vektör tabanlı arama ve sıralama işlemleri için optimize eden bir Python uygulamasıdır. SentenceTransformer kütüphanesi kullanılarak veri tabanındaki tüm veriler vektörleştirilir. Daha sonra, vektörleştirilen bu veriler Faiss kullanılarak sorgularda aranan kelimeye en yakın vektörler ile sıralanır. Projede, veri tabanındaki değişiklikleri takip edebilmek ve vektör dosyasını güncelleyebilmek için bir update fonksiyonu da eklenmiştir.

Bu proje örneğinde veriler MSSQL veritabanından çekilmiştir ve çekilen veriler bir DataFrame'e dönüştürülmüştür. MSSQL'e bağlanma kodu da projeye dahil edilmiştir. Siz bu kodu kendi ihtiyaçlarınıza göre uyarlamak isterseniz, verilerinizi farklı bir veritabanından veya kaynaktan çekebilir ve kök kod yapısını ihtiyacınıza göre değiştirebilirsiniz.


En son şunu da not etmek isterim: Eğer veritabanındaki kullanıcılarınızı isimlerine ve yeteneklerine göre girilen anahtar kelimeye göre sıralamak isterseniz, bence bu modellerle vakit kaybetmeyin. Üstelik Türkçe isimlerden anlam çıkarma konusunda diğer araçlara göre pek başarılı bulmadım. Yapmak istediğim, bir kullanıcı isim arattığında profilinde kayıtlı yeteneklere sahip olan veya ilişkili olan kullanıcıların öncelikli gelmesiydi, yani LinkedIn gibi, ama pek başarılı olamadım. Eğer bir uygulama yazıyorsanız ve buna benzer bir arama motoru geliştirmeye çalışıyorsanız, kendi modelinizi eğitin veya hazır araçlar kullanın. Örneğin, Elasticsearch veya OpenSearch kullanabilirsiniz. Dediğim gibi, belki de ben başarılı olamamışımdır. Siz bu tarz bir arama motoru geliştirirseniz mutlaka bana haber edin. 🫡
