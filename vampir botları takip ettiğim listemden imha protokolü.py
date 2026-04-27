import time
from atproto import Client

# --- GİRİŞ BİLGİLERİ ---
HANDLE = "becaecosystem.bsky.social"
APP_PASSWORD = "2222-1111-0000-1111"

client = Client()

def nukleer_imha_protokolu():
    try:
        print("Sisteme giriş yapılıyor... 🔑")
        client.login(HANDLE, APP_PASSWORD)
        print(f"✅ Giriş BAŞARILI: @{HANDLE}")
        print("-" * 40)
        print("💀 NÜKLEER İMHA PROTOKOLÜ: TÜM TAKİPLER SİLİNİYOR... 💀")

        cursor = None
        toplam_imha = 0

        while True:
            # list_records kullanarak takip dökümünü doğrudan veritabanından alıyoruz
            # Bu yöntem, 'get_follows'un göremediği hayalet kayıtları yakalar.
            response = client.com.atproto.repo.list_records({
                'repo': client.me.did,
                'collection': 'app.bsky.graph.follow',
                'cursor': cursor,
                'limit': 100
            })

            if not response.records:
                break

            print(f"📡 {len(response.records)} hayalet kayıt tespit edildi. İmha ediliyor...")

            for record in response.records:
                try:
                    # Kaydı kökten siliyoruz
                    client.com.atproto.repo.delete_record({
                        'repo': client.me.did,
                        'collection': 'app.bsky.graph.follow',
                        'rkey': record.uri.split('/')[-1]
                    })
                    toplam_imha += 1
                    print(f"🔥 İMHA EDİLDİ: {record.uri.split('/')[-1]}")
                    time.sleep(0.5) # Nükleer modda daha hızlıyız
                except Exception as e:
                    print(f"❌ Kayıt atlandı: {e}")

            cursor = response.cursor
            if not cursor:
                break

        print("-" * 40)
        print(f"✅ NÜKLEER TEMİZLİK BİTTİ. Toplam {toplam_imha} virüs silindi.")
        print("Profilin artık tamamen steril! 🦾🔥")

    except Exception as e:
        print(f"❌ KRİTİK HATA: {e}")

if __name__ == "__main__":
    nukleer_imha_protokolu()