import { Router } from "express";
import { crear } from "../controllers/categoria_producto.controller.js";

export const categoriaProductoRouter = Router();

categoriaProductoRouter.post("/categoria-producto", crear);
