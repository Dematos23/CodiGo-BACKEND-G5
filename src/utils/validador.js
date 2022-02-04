import jwt from "jsonwebtoken";
import { prisma } from "../prisma.js"

export function verificarToken(token) {

    try {
        const payload = jwt.verify(token, process.env.JWT_SECRET);
        return payload;
    } catch (error) {
        return error;
    }

}

export async function validarUsuario(req, res, next) {

    if (!req.headers.authorization) {
        return res.status(401).json({
            message: "Se necesita una token para realizar esta solicitud",
        });
    }

    const token = req.headers.authorization.split(" ")[1]

    const resultado = verificarToken(token);

    if (resultado instanceof jwt.JsonWebTokenError) {
        return res.status(403).json({
            message: "La token es invalida, intente nuevamente",
            razon: resultado.message,
        });
    }

    console.log(resultado);
    const usuario = await prisma.usuario.findUnique({
        where: { id: resultado.id },
        select: { correo: true, id: true },
    })

    req.user = usuario;

    next();
}