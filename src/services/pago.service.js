import mercadopago from "mercadopago";
import { Cliente } from "../models/cliente.model.js";
import { Producto } from "../models/producto.model.js";

export class PagoService {
  static async generarPreferenciaDePago({ items, cliente }) {
    const metodosRespuesta = await mercadopago.payment_methods.listAll();
    const metodosDePago = Object.assign({}, metodosRespuesta.body);
    try {
      const clienteEncontrado = await Cliente.findById(cliente);

      const productosEncontrados = await Promise.all(
        items.map(async ({ id, cantidad }) => {
          const productoEncontrado = await Producto.findById(id);

          return { item: productoEncontrado, cantidad };
        })
      );
      const itemsMP = productosEncontrados.map(({ item, cantidad }) => ({
        id: item._id,
        title: item.nombre,
        quantity: cantidad,
        unit_price: +item.precio,
        currency_id: "PEN",
      }));

      const preferencia = await mercadopago.preferences.create({
        payer: {
          name: clienteEncontrado.nombre,
          surname: clienteEncontrado.apellido,
          address: {
            zip_code: clienteEncontrado.direccion.zip,
            street_name: clienteEncontrado.direccion.zip,
            street_number: clienteEncontrado.direccion.numero,
          },
          email: clienteEncontrado.correo,
        },
        payment_methods: metodosDePago,
        items: itemsMP,

        auto_return: "approved",

        back_urls: {
          success: "http://localhost:3000/exito",
          pending: "http://localhost:3000/pendiente",
          failure: "http://localhost:3000/fallo",
        },
      });
      console.log(metodosRespuesta.body);
      console.log(preferencia.body);
      return {
        resultado: preferencia,
      };
    } catch (error) {
      console.log(error);
    }
  }
}
