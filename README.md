# Chat Cliente-Servidor con Sockets y SQLite

## Descripción del Proyecto

Este proyecto consiste en la implementación de un sistema básico de comunicación cliente-servidor utilizando sockets en Python.

El servidor recibe mensajes enviados por uno o más clientes, los almacena en una base de datos SQLite y responde con una confirmación que incluye la fecha y hora de recepción.

El objetivo es aplicar conceptos fundamentales de redes, manejo de bases de datos y buenas prácticas de programación como la modularización y el manejo de errores.

---

## Objetivos

* Implementar comunicación cliente-servidor mediante sockets TCP/IP
* Almacenar mensajes en una base de datos SQLite
* Aplicar modularización mediante funciones
* Manejar errores básicos en la ejecución del servidor y cliente
* Documentar el código con comentarios explicativos

---

## Estructura del Proyecto

```
chat-sockets/
│
├── server.py      # Servidor que recibe y procesa los mensajes
├── client.py      # Cliente que envía mensajes al servidor
├── database.db    # Base de datos SQLite (se crea automáticamente)
```

---

## Tecnologías Utilizadas

* Python 3
* Módulo `socket`
* Módulo `sqlite3`
* Módulo `datetime`

---

## Funcionamiento del Sistema

### Servidor

* Escucha conexiones en `localhost:5000`
* Acepta conexiones de clientes
* Recibe mensajes enviados por el cliente
* Guarda cada mensaje en una base de datos SQLite con:

  * contenido
  * fecha y hora de envío
  * IP del cliente
* Responde al cliente con un mensaje de confirmación

---

### Cliente

* Se conecta al servidor en `localhost:5000`
* Permite enviar múltiples mensajes
* Muestra la respuesta del servidor
* Finaliza cuando el usuario escribe `"exit"`

---

## Instrucciones de Ejecución

### 1. Clonar o descargar el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>
cd chat-sockets
```

---

### 2. Ejecutar el servidor

```bash
python server.py
```

Debería aparecer:

```
Servidor escuchando en localhost:5000...
```

---

### 3. Ejecutar el cliente (en otra terminal)

```bash
python client.py
```

---

### 4. Enviar mensajes

Ejemplo:

```
Dejanos un mensaje ("exit" para salir): Hola
Servidor: Mensaje recibido: 2026-04-19 12:45:30
```

---

## Base de Datos

Se utiliza SQLite, que genera automáticamente el archivo `database.db`.

### Tabla: `mensajes`

| Campo       | Tipo    | Descripción              |
| ----------- | ------- | ------------------------ |
| id          | INTEGER | Identificador único      |
| contenido   | TEXT    | Mensaje enviado          |
| fecha_envio | TEXT    | Fecha y hora del mensaje |
| ip_cliente  | TEXT    | Dirección IP del cliente |

---

## Manejo de Errores

El sistema contempla:

* Error al iniciar el servidor (puerto ocupado)
* Error en la conexión del cliente
* Error al procesar mensajes
* Problemas de acceso a la base de datos

---

## Conceptos Aplicados

* Sockets TCP/IP
* Arquitectura cliente-servidor
* Bases de datos SQLite
* Codificación y decodificación de datos (`encode` / `decode`)
* Modularización del código
* Manejo de excepciones (`try / except`)

---

## Notas

* El servidor debe ejecutarse antes que el cliente
* El sistema funciona en entorno local (`localhost`)
* La base de datos se crea automáticamente al ejecutar el servidor

---

## Créditos

Documentación mantenida por:

**Gabycrem®**  
Trabajo práctico realizado como parte de la materia **Programación sobre Redes**.

- GitHub: [Gabycrem](https://github.com/Gabycrem)  
- LinkedIn: [Nazarena Macre](https://www.linkedin.com/in/macrenazarena/)  

---

<div align="center">
<code>Siempre construyendo, siempre aprendiendo. -- GABYCREM® </code>
</div>



