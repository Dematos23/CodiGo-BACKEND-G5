import { Router } from "express";
import { crearPreferencia } from "../controllers/pago.controller.js";

export const pagoRouter = Router();

pagoRouter.post("/preferencia", crearPreferencia);
