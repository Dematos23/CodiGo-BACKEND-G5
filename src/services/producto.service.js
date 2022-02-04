import Prisma from "@prisma/client";
import { prisma } from "../prisma.js";

export class ProductoService {

    static async crearProducto(data) {

        try {
            const nuevoProducto = await prisma.producto.create({
                data: {
                    nombre: data.nombre,
                    precio: data.precio,
                    tipoProductoId: data.tipoProductoId,
                }
            });
            return { content: nuevoProducto };

        } catch (error) {

            if (error instanceof Prisma.Prisma.PrismaClientKnownRequestError) {
                return {
                    message: "Error al crear el producto",
                    content: error.message,
                };
            }
        }

    }
}