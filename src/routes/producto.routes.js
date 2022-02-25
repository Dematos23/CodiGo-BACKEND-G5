import { Router } from "express";
import { crearProducto } from "../controllers/producto.controller.js";

export const productoRouter = Router();

productoRouter.route("/producto").post(crearProducto);
