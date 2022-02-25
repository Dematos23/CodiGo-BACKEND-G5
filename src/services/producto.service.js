import { Producto } from "../models/producto.model.js";

export class ProductoService {
  static async crear(data) {
    try {
      const nuevoProducto = await Producto.create(data);
      return nuevoProducto;
    } catch (e) {
      return { message: e.message };
    }
  }
}
