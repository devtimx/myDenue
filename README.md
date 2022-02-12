# myDenue

Realizar lo siguiente utilizando servicios serveless y subirlo a un repositorio publico para su consulta.
Crear un servicio que proporcione la informacion de los negocios por localidades (Municipio/Delegación) del INEGI.
- Consultar la informacion del INEGI
- Proporcionar un endpoint donde poder consultar la informacion por uno o varios municipios o delegaciones
- Realizar fork del repositorio y solicitar pull request de la solucion
- Pruebas unitarias

Ejemplo de json a enviar:

- Para el parámetro buscar se enviá un arreglo con los parámetros de búsqueda, mediante un arreglo
- Para el parámetro de clave_entidad de enviá la clave de la entidad federativa qie abarcan del 01 al 31, si es enviado vació toma todas la entidades
- El parámetro page recibe el numero de pagina par listar lo resultados los cuales de muestran en bloques de 100 resultados

{
    "buscar":["parámetro1","parámetro1","parámetro3","..."],
    "clave_entidad":"20"
}

Librerías utilizadas
- api DENUE INEGI
- requests
- flask-testing
- pandas