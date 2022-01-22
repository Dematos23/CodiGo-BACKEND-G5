import {Router} from "express";
import {crearCategoria, listaCategoria} from '../controllers/categoria.controller.js';

export const categoriaRouter = Router();

categoriaRouter.route('/categoria').post(crearCategoria).get(listaCategoria);
