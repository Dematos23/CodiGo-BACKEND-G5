import { Router } from "express";
import {
  crearCategoria,
  getCategoria,
  getCategorias,
  putCategoria,
} from "../controllers/categoria.controller.js";

export const categoriaRouter = Router();

categoriaRouter.route("/categoria").post(crearCategoria).get(getCategorias);

categoriaRouter.route("/categoria/:id").get(getCategoria).put(putCategoria);
