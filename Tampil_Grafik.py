import os
import pandas as pd
import matplotlib.pyplot as plt

# Mendapatkan direktori dari skrip ini
output_folder = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(output_folder, "sink_databaru5.csv")

# Membaca file CSV
data = pd.read_csv(output_file)

# Menampilkan beberapa baris pertama dari data untuk memastikan data terbaca dengan benar
print(data.head())

# Menghitung tegangan rata-rata dan throughput rata-rata per ronde dan per node
average_data = data.groupby(['Round phase1', "Round phase2", 'Node ID']).agg({
    'Voltage': 'mean',
    'Throughput': 'mean'
}).reset_index()

# Menampilkan beberapa baris pertama dari data rata-rata untuk memastikan data terbaca dengan benar
print(average_data.head())

# Daftar warna
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

# Fungsi untuk membuat dan menyimpan grafik
def buat_grafik(data, x, y, xlabel, ylabel, title, filename, colors):
    plt.figure(figsize=(10, 6))
    node_ids = data['Node ID'].unique()
    for idx, node_id in enumerate(node_ids):
        subset = data[data['Node ID'] == node_id]
        color = colors[idx % len(colors)]  # Memastikan warna berulang jika node lebih banyak daripada warna
        plt.plot(subset[x], subset[y], marker='o', linestyle='-', label=f'Node {node_id}', color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    output_image_file = os.path.join(output_folder, filename)
    plt.savefig(output_image_file)
    plt.show()

# Membuat grafik tegangan rata-rata vs Ronde untuk masing-masing Node ID
buat_grafik(average_data, 'Round phase1', 'Voltage', 'Round phase2', 'Average Voltage', 'Grafik Round vs Average Voltage', 'grafik_round_vs_average_voltage.png', colors)

# Membuat grafik throughput rata-rata vs Ronde untuk masing-masing Node ID
buat_grafik(average_data, 'Round phase1', 'Throughput', 'Round phase2', 'Average Throughput', 'Grafik Round vs Average Throughput', 'grafik_round_vs_average_throughput.png', colors)
