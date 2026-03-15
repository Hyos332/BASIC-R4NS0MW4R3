# Proyecto Educativo de Cifrado de Archivos con Python

## Descripcion

En este repositorio documente un ejercicio de aprendizaje orientado a comprender conceptos basicos de cifrado simetrico, recorrido de archivos y recuperacion de informacion mediante Python. Utilice la libreria `cryptography` y su implementacion `Fernet` para aplicar cifrado y descifrado sobre archivos de prueba dentro de un entorno controlado.

Mi objetivo con este trabajo fue didactico: observar de forma practica como se genera una clave, como se procesa el contenido de un archivo en binario y como se puede revertir la operacion con la misma clave.

## Objetivos de aprendizaje

- Comprender el uso de cifrado simetrico con `Fernet`.
- Practicar lectura y escritura de archivos en modo binario.
- Recorrer directorios y filtrar archivos por extension.
- Entender la relacion entre proceso de cifrado, clave y recuperacion posterior.
- Analizar limites, riesgos y malas practicas en scripts que modifican archivos.

## Estructura del proyecto

- `ransomware.py`: script experimental que recorre una ruta configurada, toma archivos `.txt`, cifra su contenido y genera una version con extension `.locked`.
- `decryptor.py`: script complementario que intenta restaurar archivos `.locked` utilizando la clave correspondiente.
- `text.txt` y `text2.txt`: archivos simples de prueba para validar el flujo en un entorno local.

## Alcance tecnico

Con este proyecto quise demostrar, a nivel academico, los siguientes conceptos:

- Generacion de claves con `Fernet.generate_key()`.
- Cifrado y descifrado de datos binarios.
- Procesamiento automatizado de multiples archivos.
- Restauracion de archivos a partir de una clave valida.

No lo presento como una herramienta de produccion, seguridad ofensiva ni administracion real de archivos. El codigo actual esta pensado como prueba de concepto y presenta limitaciones deliberadas y riesgos tecnicos que deben analizarse antes de cualquier uso en datos propios.

## Limitaciones actuales

- Depende de rutas configuradas manualmente.
- Opera sobre extensiones concretas.
- Contiene manejo de errores demasiado amplio.
- Puede eliminar archivos originales durante el proceso.
- No incorpora protecciones para evitar ejecucion accidental sobre informacion importante.

Estas limitaciones forman parte del valor educativo del repositorio, porque me permiten mostrar por que un script de este tipo resulta fragil, riesgoso y no apto para uso real.

## Aviso legal y etico

Publique este repositorio exclusivamente con fines educativos y de analisis tecnico. No esta destinado a ser utilizado sobre sistemas, archivos o entornos de terceros. Cualquier ejecucion debe limitarse a archivos propios, entornos aislados y laboratorios controlados.

El uso no autorizado de software que altere, cifre o elimine informacion ajena puede ser ilegal y generar consecuencias civiles, penales y disciplinarias. Publicar este trabajo no implica autorizacion, recomendacion ni justificacion para usos indebidos.

## Enfoque recomendado de lectura

Si alguien revisa el proyecto con criterio tecnico, conviene observar:

- Como se genera y utiliza una clave simetrica.
- Como se transforma el contenido de un archivo antes y despues del cifrado.
- Que decisiones del codigo vuelven el flujo inseguro o poco robusto.
- Que diferencias existen entre una demostracion academica y una herramienta legitima para proteger archivos propios.

## Entorno utilizado

- Python 3
- Libreria `cryptography`
- Sistema de archivos local para pruebas controladas

## Nota final

Este proyecto debe entenderse como una practica de aprendizaje sobre cifrado de archivos y analisis de riesgos en automatizaciones destructivas. Para mi, su valor esta en estudiar como funciona internamente y en reconocer claramente por que este tipo de codigo no debe emplearse fuera de un contexto autorizado, aislado y academico.
