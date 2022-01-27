import {Router} from "express";
import {
    actualizarCategoria,
    buscarCategoria,
    crearCategoria, 
    listaCategoria,
} from '../controllers/categoria.controller.js';

export const categoriaRouter = Router();

categoriaRouter.route('/categoria').post(crearCategoria).get(listaCategoria);

categoriaRouter.get("/buscarCategoria", buscarCategoria);

categoriaRouter.route("/categoria/:id").put(actualizarCategoria)