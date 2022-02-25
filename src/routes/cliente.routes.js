import { Router } from "express";
import { crearCliente } from "../controllers/cliente.controller.js";
export const clienteRouter = Router();

clienteRouter.post("/cliente", crearCliente);
