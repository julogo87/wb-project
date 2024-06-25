from flask import Flask, jsonify, request, send_from_directory
import pandas as pd

app = Flask(__name__)

# Leer el archivo Excel
file_path = 'DIGITALIZACIÓN.xls (5 JUN).xls'
excel_data = pd.ExcelFile(file_path)

# Leer todas las hojas en un diccionario
data = {sheet: excel_data.parse(sheet).to_dict(orient='records') for sheet in excel_data.sheet_names}

@app.route('/api/data', methods=['GET'])
def get_data():
    sheet = request.args.get('sheet')
    if sheet in data:
        return jsonify(data[sheet])
    else:
        return jsonify({"error": "Sheet not found"}), 404

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
