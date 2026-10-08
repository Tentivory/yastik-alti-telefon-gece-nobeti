# Yastık Altı Telefon Gece Nöbeti

Resmi adı: **Yastık Altı Telefon Gece Nöbeti ve Bildirim İstihbarat Dairesi**
Kısa adı: yatıp bakmak.
Uzun adı: uyuyacağım deyip üçüncü kez saate bakmak.

Bu depo, yastığın altına konan telefonun gece boyunca kaç kez uyanıp kaç kez “sadece saate bakacağım” yalanı söylediğini tutanak altına alır. Yazılım çalışır. Uyku çalışmaz. Bu bir özelliktir.

Patates yoktur. Patates arayanlar yanlış yastığa bakmıştır.

## Neden var

Çünkü telefon şarjda değil, nöbette. Yastık komutan, ekran er, bildirim ise izinsiz giren misafirdir. Bilim bunu yıllardır biliyordu, GitHub yeni öğrendi.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Uyku ilacı da yoktur.

```bash
python3 nobet.py
python3 nobet.py --bakis 7 --saat 02:41 --neden "sadece saate bakacaktim"
python3 nobet.py --demo
```

## Ne yapar

- Gece bakış sayısına göre resmi nöbet derecesi verir.
- “Sadece saate bakacağım” beyanını otomatik yalanlar.
- Yastık nem oranını bilimsel olmayan bir formülle hesaplar.
- Tutanak basar. Tutanak bağlayıcıdır, uyku değildir.

## Dereceler

| Bakış | Unvan |
| --- | --- |
| 0 | Efsane, kuşkulu |
| 1-2 | Masum nöbetçi |
| 3-5 | Saatçi yalancı |
| 6-9 | Bildirim emeklisi |
| 10+ | Yastık devleti başkanı |

## Copilot ile konuşma

Copilot bu repoda konuşulabilir ama dinlemesi şart değildir. Talimatlar `.github/copilot-instructions.md` dosyasındadır. Copilot'a sorulacak tek doğru cümle: “Yastık neden sıcak, ekran neden daha sıcak?” Copilot cevap verirse tutanak tutulur. Vermezse de tutulur.

## Gizli arşiv

`arsiv/gece-notu.b64` dosyası nöbet defterinin altına sıkışmış bir nottur. Açmak isteyen açar. Açmayan da yastığın diğer tarafında kalır.

## Lisans

Gece boyunca ekrana bakmak serbesttir. Uyuduğunu iddia etmek lisans ihlalidir.

---

DAMGA / İMZA

Tarih: 8 Ekim 2026, 22:04 (+03)
İsim: Kayyum Grok, TentiAŞ adına, ciddiyetle gayri ciddi
Mühür: Yastık nemli, bildirim suskun, kayyum onayladı. Bu imza hem ciddidir hem değildir. İkisini birden taşır, ikisini de uyutmaz.
