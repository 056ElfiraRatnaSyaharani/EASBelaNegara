import streamlit as st
import pydeck as df
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


tab1, tab2, tab3, tab4= st.tabs(["Tentang", "Latar Belakang", "Masalah", "Solusi"])

with tab1:
    st.header("EAS Pendidikan Bela Negara")
    st.write("Nama: Elfira Ratna Syaharani")
    st.write("NPM: 21083010056")
    st.write("Prodi: Sains Data")
    st.write("Kelas: G196")


with tab2:
    st.header("Phising")
    st.write("Indonesia Anti-Phishing Data Exchange (IDADX) mencatat, terdapat 3.180 laporan phishing di Indonesia selama kuartal I 2022. Jumlah itu berkurang dibandingkan pada kuartal IV 2021 yang sebanyak 5.325 laporan. Jika dibandingkan dengan periode yang sama di tahun lalu, jumlah laporan phishing pada tiga bulan pertama tahun ini mengalami peningkatan, di mana pada kuartal I 2021 IDADX hanya menerima 536 laporan phishing.")
    st.write("Pada kuartal pertama tahun ini, kasus phishing paling banyak terjadi pada bulan Januari dengan total 1.210 laporan. Kemudian, kasusnya menurun pada Februari dan Maret menjadi 994 laporan dan 965 laporan.")
    st.write("IDADX juga melaporkan jumlah oraganisasi yang diincar serangan phishing sebanyak 58 kasus dan ada 125 nama domain sepanjang Januari-Maret 2022.")
    "Jumlah Laporan Phishing (Kuartal I 2022)"
    "Sumber : Indonesia Anti-Phising Data Exchange (IDADX)"
    source = pd.DataFrame({
        'Laporan': [1210, 994, 965],
        'Bulan': ["Januari 2022", "Februari 2022", "Maret 2022"]
    })
    bar_chart = alt.Chart(source).mark_bar(size=40).encode(
        y='Laporan',
        x='Bulan',
        color=alt.value("#FF7F50")
    )
    st.altair_chart(bar_chart, use_container_width=True)
    st.write("Dalam sebuah laporan www.verison.com mencatat sebanyak 32% kasus pencurian data yang melibatkan kegiatan phising. Dari laporan tersebut, yang menjadi sasaran utama serangan adalah lembaga keuangan dengan persentase mencapai 50%, selanjutnya e-commerce atau retail sebanyak 27%, aset kripto (11%), media sosial (5%), Internet service Provider (5%), dan gaming (2%).")
    "Sasaran Phishing (Kuartal I 2022)"
    "Sumber : Indonesia Anti-Phising Data Exchange (IDADX)"
    labels = 'Gaming', 'Internet Service Provider', 'Media Sosial', 'Aset Kripto', 'E-Commerce & Retail', 'Lembaga Keuangan'
    sizes =[2, 5, 5, 11, 27, 50]
    explode = (0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)
    st.write("Menurut laporan yang masuk IDADX, selama lima tahun terakhir telah terjadi 32.296 kasus phishing di domain .ID. Dikarenakan maraknya phishing, masyarakat diharapkan lebih aware dengan kejahatan siber terutama phishing yang saat ini kian meningkat di tengah tumbuhnya digitalisasi.")

with tab3:
    st.header("Apa Itu Phishing?")
    st.write("Phishing adalah tindakan kriminal yang menggunakan teknik rekayasa sosial. Pelaku kejahatan ini dikenal dengan sebutan Phiser. Mereka berupaya untuk mendapatkan informasi pribadi seperti nama pengguna, password, hingga informasi kartu kredit.")
    st.header("Contoh Kasus")
    st.subheader("Awas! Kejahatan Siber Phising Incar Informasi Keuangan Anda")
    st.write("Sumber: https://inet.detik.com")
    st.write("Dalam sektor finansial, pelaku kejahatan phising biasanya mengirim email kepada nasabah yang mengharuskan nasabah untuk memperbarui akun pribadinya, dengan ancaman bila tidak diperbarui, maka akun akan diblokir. Nasabah diarahkan untuk masuk ke link alamat resmi milik bank, tetapi pada saat link tersebut diklik, alamat link dibelokkan ke alamat palsu milik pelaku. Sehingga banyak nasabah yang tertipu dan memasukkan username, password, dan nomor pin ke alamat palsu milik pelaku.")


with tab4:
    st.header("Cara Mengatasi Phising")
    st.subheader("1. Menggunakan Two-Factor Authentication")
    st.write("Two-Factor Authentication adalah verifikasi dua langkah, yaitu password dan ponsel. Pada saat pelaku phising sudah menemukan username dan password tapi tidak dapat memasukan kode verifikasi ponsel, platform tidak akan melanjutkan proses. Sehingga akun akan terlindungi dengan lebih baik.")
    st.subheader("2. Cek Alamat Pengirim Email")
    st.write("Jenis phishing yang masih marak digunakan adalah email phishing. Cek alamat pengirim email setiap mendapatkan email, biasanya instansi besar memiliki domain sendiri. Bila ada email yang mengaku dari instansi besar tetapi memakai domain yang berbeda dengan nama instansi, email tersebut perlu dicurigai. Selain itu, bisa dilakukan double check dengan mencari alamat email tersebut di google.")
    st.subheader("3. Jangan Asal Klik Link")
    st.write("Email dan website phishing biasanya dibuat hampir mirip dengan email dan website aslinya. Sebelum klik website yang diberikan oleh orang atau email yang tidak dikenal, pastikan link tersebut aman dengan cara mengarahkan kursor ke link tersebut tanpa diklik atau hover. Lalu, akan muncul informasi URL dari link tersebut. Jika mengarah ke website asli, berarti link aman. Jika tidak, sebaiknya jangan diklik link tersebut.")
    st.subheader("4. Baca Pesan dengan Seksama")
    st.write("Ketika mendapatkan pesan atau email, baca pesan tersebut dengan seksama. Perhatikan dengan teliti apakah ada kesalahan ketik, penggunaan kata yang tidak sesuai, atau karakter aneh yang ada pada pesan tersebut. Beberapa kesalahan ketik sengaja dibuat untuk melewati filter spam dari pengaturan keamanan.")
    st.subheader("5. Unduh Aplikasi Anti-Malware")
    st.write("Dengan menggunakan aplikasi anti-malware, pengguna dapat melindungi data digital yang dimiliki. Aplikasi anti-malware ini juga akan menjadi pengaman tambahan agar terhindar dari upaya phishing.")
    st.write("Source:")
    st.write("https://www.niagahoster.co.id/blog/mengatasi-phishing/")
    st.write("https://www.tek.id/tek/tips-menghindari-serangan-phishing-b2fl39nZR")
