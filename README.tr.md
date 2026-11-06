# HP ZBook Fury 15 G7 — OpenCore / macOS Sequoia

**Test edilen sistem:** i7-10850H, Intel UHD 630, 32 GB RAM, FHD 60 Hz ekran. **macOS:** 15.7.7 (24G720). **OpenCore:** 1.0.8 RELEASE. **SMBIOS:** MacBookPro16,2.

[EFI sürümünü indir](https://github.com/vurulkan/HP-ZBook-Fury-15-G7-Hackintosh/releases/latest) · [Ayrıntılı İngilizce dokümantasyon](README.md) · [Kurulum adımları](docs/SETUP.md)

Bu EFI, çalışan kişisel kurulumun kimlik bilgileri temizlenmiş kopyasıdır. Aynı modelin farklı GPU, panel, Wi-Fi kartı ve BIOS sürümleri vardır; hepsinde çalıştığı iddia edilmez.

## Kullanım

1. Release ZIP dosyasını ve `SHA256SUMS.txt` dosyasını indir; arşivi açmadan önce `shasum -a 256 -c SHA256SUMS.txt` ile kontrol et.
2. Config içindeki boş `SystemSerialNumber`, `MLB`, `SystemUUID` ve sıfırlanmış altı baytlık `ROM` alanlarını **kendi MacBookPro16,2 kimliğinle** doldur. GenSMBIOS kullanılabilir.
3. OpenCore **1.0.8** içindeki `ocvalidate` ile kontrol et.
4. Mevcut çalışan EFI’ni sakla ve önce USB üzerinden dene.
5. Wi-Fi için HeliPort’u macOS’a ayrıca kur; istersen Giriş Öğeleri’ne ekle.

## Durum

- Açılış, Intel grafik hızlandırma, parlaklık kaydırıcısı ve Fn+F3/F4 doğrulandı.
- Wi-Fi (itlwm + HeliPort), Bluetooth ve Fn ses tuşları çalışıyor.
- Pil bilgisi ve CPU güç yönetimi sürücüleri aktif.
- Güncelleme kontrolü RestrictEvents ile düzeltildi; **Sequoia 15.8.2 listeleniyor ama henüz yüklenip test edilmedi.**
- **Konum**, itlwm kartı Ethernet olarak sunduğu için çalışmıyor. Saat dilimini elle seçmek mümkün.
- macOS altında uzun CPU yükünde yaklaşık 25 W / 2,75 GHz gözlendi. Windows ile aynı benchmark yapılmadığından yüzde performans farkı verilmiyor. Bu sınırın nedeni çözülmüş değil.
- Uyku/uyanma, tüm USB portları, kamera, harici ekran, Thunderbolt, ses kaydı ve kulaklık girişi için eksiksiz fiziksel test yapılmadı.

## Önemli yapılandırma notları

Bu kopya mevcut kurulumun özel SIP ayarını (`FF0F0000`), `SecureBootModel=Disabled`, AMFIPass ve eski ağ bileşenlerini korur. Bunlar her sistemde uygulanması önerilen ayarlar değildir. Birden fazla EC/USBX SSDT ve iki USB haritası mevcut; sadeleştirme ayrıca değerlendirilmelidir.

Yayın paketinden seri numarası, MLB, UUID, ROM değeri, Bluetooth denetleyici durumu, kayıtlı Wi-Fi bilgileri, eski config, yedekler ve tanılama çıktıları çıkarıldı. Çalışan EFI değiştirilmedi.

Parlaklık yaması belirli bir DSDT’ye göre hazırlanmıştır. BIOS değişirse eşleşme yeniden incelenmelidir. Teknik açıklama ve kaynak kod [burada](docs/CONFIGURATION.md#hp-brightness-keys).
