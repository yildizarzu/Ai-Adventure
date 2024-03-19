""" 
### ARTIFICAL NEURAL NETWORK (ANN) /YAPAY SİNİR AĞLARI ###
    
    Biyolojik sinir ağlarını taklit eden bilgisayar programlarıdır.
    Yapay sinir ağları kısaca, örneklerle ilgili bilgiler toplamakta, genellemeler yapmakta ve daha sonra hiç görmediği örnekler ile karşılaştırılınca öğrendiği bilgileri kullanarak o örnekler hakkında karar verebilmektedir.

    YAPAY SİNİR AĞLARI İLE İLGİLİ GELİŞTİRİLEN MODELLER; 
        - Tek katmanlı algılayıcılar (TKA), 
        - Perceptron,
        - Adaline/ Madaline

        *Tek Katmanlı Algılayıcılar
            Sadece girdi ve çıktı katmanlarından oluşur. Çıktı doğrusal bir fonksiyondur 1 veya -1 değerini alır.
            Çıktı 1 ise 1.sınıfa, -1 ise 2. sınıfa kabul edilir.
        
        *Perceptron 
            Yapay Nöron olarakta kullanılabilir.
            Tek katmanlı sinir ağı modelidir. Eğitilebilecek tek bir yapay sinir hücresinden oluşmaktadır.
            Algılayıcı, ikili sınıflandırıcıların denetimli öğrenimi için bir algoritmadır.
            Girdinin belirli bir sınıfa ait olup olmadığını karar verir.
    
    AKTİVASYON FONKSİYONLARI

        İlgili URL: https://en.wikipedia.org/wiki/Activation_function

        *Sigmoid Fonksiyonu
            + 0 ile 1 arasında değer alır.
            + Belirlili % ile olasılık verir.
            + Genelde sınıflandırma problemlerimizde işe yarar.
            
        
        * Tanh ( Hiperbolik Tanjant) Fonksiyonu
            + -1 ile 1 arasında değer alır.
            + Negatif değerlerle daha geniş bir kapsaö sağlar ve genelde sınıflandırma operasyonlarında kullanılır.

        * ReLU (Rectified Linear Unit)
            + En çok kullanılan 
            + 0 ile sonsuz arasında değer alır.
            + Derin Öğrenmede çokça kullanılır.
        
        * Linear Fonksiyonlar
            + f(x)=x
            + Sonsuz değer alabilir fakat non-linear olması sebebiyle modellerde sorun çıkarabilir.

    REGRESYON
        - Bağımlı bir değişken ile bir veya daha fazla bağımsız değişken arasındaki ilişkiyi tahmin etmek için kullanılan bir dizi istatistiksel yaklaşımdır.
        - Çıktı Toplam veri setindeki ortalamya yakın olma eğilimi gösterebilir. 
        - Tahmin ve öngörü problemleri için regresyon kullanılır.
        - Faktörlerin nedenselliğini haritalamak, bağımlı ve bağımsız değişkenler arasındaki neden-sonuç ilişkisini çıkarmak için kullanılır.  
        - Y = a * x + b

    # TENSORFLOW => Makine Öğrenimi ve Derin Öğrenme modellerinin yanısıra "Sinir Ağlarının" oluşturulmasına olanak tanıyan araç ve kaynak koleksiyonundan oluşur.
        - CPU ve GPU platformalarının yanısıra TPU(Tensor İşleme Birimi) çalıştırıldığında "en iyi performansı" sağlar.
        - ML ve DL modellerinde "Pekiştirmeli Öğrenme" için kullanılır.
            ML modellerini doğrudan görselleştirebiliriz.
        - Esnek mimari ve çerçeve
        - Çeşitli hesaplama platformlarında çalışır.
        - Soyutlama yetenekleri
        - Derin Sinir Ağlarını yönetir.

