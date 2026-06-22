import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Deklarasi FUngsi anggota

def left_shoulder(x, a, b):
    if x <= a:
        return 1
    elif a < x < b:
        return (b - x) / (b - a)
    else:
        return 0


def right_shoulder(x, a, b):
    if x <= a:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    else:
        return 1


def triangle(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)


# Hitung Nilai

def hitung_mahasiswa(nilai):

    rendah = left_shoulder(nilai, 40, 60)
    sedang = triangle(nilai, 40, 60, 80)
    tinggi = right_shoulder(nilai, 60, 80)

    return {
        "Rendah": round(rendah, 3),
        "Sedang": round(sedang, 3),
        "Tinggi": round(tinggi, 3)
    }


def grafik_mahasiswa():

    x = np.linspace(0, 100, 500)

    rendah = [left_shoulder(i, 40, 60) for i in x]
    sedang = [triangle(i, 40, 60, 80) for i in x]
    tinggi = [right_shoulder(i, 60, 80) for i in x]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=rendah,
            mode="lines",
            name="Rendah"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=sedang,
            mode="lines",
            name="Sedang"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=tinggi,
            mode="lines",
            name="Tinggi"
        )
    )

    fig.update_layout(
        title="Grafik Fungsi Keanggotaan Nilai Ujian",
        xaxis_title="Nilai Ujian",
        yaxis_title="μ(x)"
    )

    return fig

# Hitung Beasiswa
def hitung_beasiswa(ipk):

    tidak_layak = left_shoulder(ipk, 1.5, 2.5)
    dipertimbangkan = triangle(ipk, 1.5, 2.5, 3.5)
    layak = right_shoulder(ipk, 2.5, 3.5)

    return {
        "Tidak Layak": round(tidak_layak, 3),
        "Dipertimbangkan": round(dipertimbangkan, 3),
        "Layak": round(layak, 3)
    }


def grafik_beasiswa():

    x = np.linspace(0, 4, 500)

    tidak_layak = [left_shoulder(i, 1.5, 2.5) for i in x]
    dipertimbangkan = [triangle(i, 1.5, 2.5, 3.5) for i in x]
    layak = [right_shoulder(i, 2.5, 3.5) for i in x]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=tidak_layak,
            mode="lines",
            name="Tidak Layak"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=dipertimbangkan,
            mode="lines",
            name="Dipertimbangkan"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=layak,
            mode="lines",
            name="Layak"
        )
    )

    fig.update_layout(
        title="Grafik Fungsi Keanggotaan IPK",
        xaxis_title="IPK",
        yaxis_title="μ(x)"
    )

    return fig


# ==========================
# STREAMLIT
# ==========================

st.set_page_config(
    page_title="Praktikum Logika Fuzzy",
    layout="wide"
)

st.title("Praktikum Logika Fuzzy")

menu = st.sidebar.selectbox(
    "Pilih Studi Kasus",
    [
        "Penilaian Mahasiswa",
        "Kelayakan Beasiswa"
    ]
)

# ==========================
# KASUS 1
# ==========================

if menu == "Penilaian Mahasiswa":

    st.header("Kasus 1 - Penilaian Mahasiswa")

    nilai = st.slider(
        "Masukkan Nilai Ujian",
        0,
        100,
        75
    )

    hasil = hitung_mahasiswa(nilai)

    st.subheader("Perhitungan Derajat Keanggotaan")

    st.table({
        "Kategori": list(hasil.keys()),
        "Nilai": list(hasil.values())
    })

    kategori = max(hasil, key=hasil.get)

    st.subheader("Interpretasi Hasil")

    st.success(
        f"Mahasiswa termasuk kategori: {kategori}"
    )

    st.subheader("Grafik Himpunan Fuzzy")

    st.plotly_chart(
        grafik_mahasiswa(),
        use_container_width=True
    )

# ==========================
# KASUS 2
# ==========================

else:

    st.header("Kasus 2 - Kelayakan Beasiswa")

    ipk = st.slider(
        "Masukkan IPK",
        0.0,
        4.0,
        3.0,
        0.01
    )

    hasil = hitung_beasiswa(ipk)

    st.subheader("Perhitungan Derajat Keanggotaan")

    st.table({
        "Kategori": list(hasil.keys()),
        "Nilai": list(hasil.values())
    })

    kategori = max(hasil, key=hasil.get)

    st.subheader("Interpretasi Hasil")

    st.success(
        f"Hasil kelayakan: {kategori}"
    )

    st.subheader("Grafik Himpunan Fuzzy")

    st.plotly_chart(
        grafik_beasiswa(),
        use_container_width=True
    )