import express, {json} from "express";
import {categoriaRouter} from "./routes/categoria.routes.js";

const app = express();

const PORT = process.env.PORT ?? 3000;

app.use(json());

app.use(categoriaRouter);

app.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente 🚀 en el puerto ${PORT}`);
});