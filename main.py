import unittest
import requests
from flask import jsonify, request
import pandas as pd

from app import create_app

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


# get data inegi
@app.route('/consulta', methods=['GET', 'POST'])
def request_inegi():
    data = request.get_json(force=True)
    buscar = data['buscar']
    clave_entidad = data['clave_entidad']
    if not clave_entidad:
        url = 'https://www.inegi.org.mx/app/api/denue/v1/consulta/buscarEntidad/todos/00/1/5000/9bdd2363-e5d9-b954-fd47-0372c0e5e05e'
    else:
        url = 'https://www.inegi.org.mx/app/api/denue/v1/consulta/buscarEntidad/todos/{}/1/5000/9bdd2363-e5d9-b954-fd47-0372c0e5e05e'.format(
            clave_entidad)
    respuesta = requests.get(url).json()
    df = pd.DataFrame(respuesta)
    df.columns = df.columns.str.lower()
    df.ubicacion = df.ubicacion.str.upper()

    df = df[['id', 'nombre', 'razon_social', 'clase_actividad', 'estrato', 'tipo_vialidad', 'calle', 'num_exterior', 'num_interior', 'colonia', 'cp', 'ubicacion',
             'telefono', 'correo_e', 'sitio_internet', 'tipo', 'longitud', 'latitud', 'tipo_corredor_industrial', 'nom_corredor_industrial', 'numero_local']]

    for busca in buscar:
        buscar = busca.upper()
        print(buscar)
        df = df.append(df[df.ubicacion.str.contains(buscar)],
                       ignore_index=True)
    return df.to_json(orient='index')


# Welcome message
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Message': 'Welcome to API REST Python myDenue'})


if __name__ == "__main__":
    app.run(debug=True)
