<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solusi SPNL - Newton Raphson</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f3f4f6;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 1100px;
            margin: auto;
            display: flex;
            gap: 20px;
        }

        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            flex: 1;
        }

        h2 {
            margin-top: 0;
        }

        label {
            font-weight: bold;
            margin-top: 10px;
            display: block;
        }

        input, textarea {
            width: 100%;
            padding: 10px;
            margin-top: 6px;
            margin-bottom: 10px;
            border-radius: 6px;
            border: 1px solid #ccc;
        }

        button {
            background: #2563eb;
            color: white;
            padding: 10px 15px;
            font-size: 15px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        button:hover {
            background: #1e4fd8;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            padding: 10px;
            text-align: center;
        }

        th {
            background: #e5e7eb;
        }
    </style>
</head>
<body>

    <h1 style="text-align:center;">Solusi SPNL dengan Metode Newton–Raphson</h1>

    <div class="container">

        <!-- Card Input -->
        <div class="card">
            <h2>Input Data</h2>

            <label>Fungsi f1(x,y):</label>
            <textarea id="f1" rows="2" placeholder="Misal: x*x + y*y - 25"></textarea>

            <label>Fungsi f2(x,y):</label>
            <textarea id="f2" rows="2" placeholder="Misal: x - y - 1"></textarea>

            <label>Tebakan Awal x₀:</label>
            <input type="number" id="x0" placeholder="Misal: 1.0">

            <label>Tebakan Awal y₀:</label>
            <input type="number" id="y0" placeholder="Misal: 1.0">

            <label>Jumlah Iterasi Maksimum:</label>
            <input type="number" id="iter" value="20">

            <label>Toleransi (ε):</label>
            <input type="number" id="eps" value="0.0001" step="0.0001">

            <button onclick="hitungNewton()">Hitung Newton–Raphson</button>
        </div>

        <!-- Card Output -->
        <div class="card">
            <h2>Hasil Perhitungan</h2>
            <div id="hasil"></div>

            <h2>Table Iterasi</h2>
            <table id="tabel">
                <thead>
                    <tr>
                        <th>Iterasi</th>
                        <th>x</th>
                        <th>y</th>
                        <th>Error</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </div>

    </div>

<script>
/*
    --- CATATAN ---
    Di bagian ini kamu bisa menambahkan perhitungan Newton Raphson.
    Saya bisa buatkan juga jika kamu ingin versi full dengan fungsi parse & Jacobian.
*/
function hitungNewton() {
    document.getElementById("hasil").innerHTML = "<i>Perhitungan belum diimplementasikan...</i>";
}
</script>

</body>
</html>
