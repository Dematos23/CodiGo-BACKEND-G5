import express, { json } from "express";
import mongoose from "mongoose";
import { categoriaRouter } from "./routes/categorias.routes.js";
import { imagenRouter } from "./routes/imagen.routes.js";

const app = express();
app.use(json());
const PORT = process.env.PORT ?? 3000;

app.use(categoriaRouter);
app.use(imagenRouter);

app.listen(PORT, async () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
  try {
    const respuesta = await mongoose.connect(process.env.MONGODB);
    console.log("Se conectó a la base de datos 🚀");
    // console.log(respuesta);
  } catch (error) {
    console.log(error);
  }
});
