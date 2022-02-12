import { Router } from "express";
import Multer from "multer";
import { nanoid } from "nanoid";
import { subirImagen } from "../controllers/imagen.controller.js";

export const imagenRouter = Router();

const almacenamiento = Multer.diskStorage({
  destination: "src/media/",
  filename: (req, archivo, callback) => {
    const id = nanoid(5);
    const nombre = archivo.originalname;
    callback(null, id + nombre);
  },
});

const multerMiddleware = Multer({
  storage: almacenamiento,
  limits: { fileSize: 1 * 1024 * 1024 },
});

imagenRouter.post(
  "/subir-imagen",
  multerMiddleware.single("imagen"),
  subirImagen()
);
